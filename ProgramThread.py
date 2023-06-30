import copy
from datetime import datetime
import os
import cv2
import numpy as np
from Camera import Camera
from PySide6 import QtCore
from PySide6.QtWidgets import QFileDialog, QWidget
from PySide6.QtGui import QImage
import debugpy

from cvzone.SelfiSegmentationModule import SelfiSegmentation

from Robot import Robot
from Settings import Settings


class ProgramThread(QtCore.QThread):
    __COLOR_GREEN = (0, 255, 0)
    __COLOR_RED = (0, 0, 255)

    image_ready_signal = QtCore.Signal(np.ndarray)
    robot_connection_state_changed = QtCore.Signal(bool)
    camera_state_changed = QtCore.Signal(bool)
    draw_finished = QtCore.Signal()
    progress_sending_updated = QtCore.Signal(float)
    progress_drawn_updated = QtCore.Signal(float)

    def slot_enable_video(self, state):
        self.__video_enabled = state
        self.__processing_enabled = False
        self.__transmission_enabled = False

    def slot_enable_processing(self):
        self.__video_enabled = False
        self.__processing_enabled = True
        self.__transmission_enabled = False

    def slot_load_image(self):
        file_filter = "Image (*.jpg *.jpeg *.png);"
        file_path = QFileDialog.getOpenFileName(
            QWidget(), "Select image", os.getcwd(), file_filter
        )
        # Dirty hack
        self.temp_qimage = QImage()
        self.temp_qimage.load(file_path[0])
        self.temp_qimage.save("_.jpg")
        self.working_frame = cv2.imread("_.jpg")
        self.__processing_enabled = True
        self.__image_loaded = True

    def slot_send_data(self, state):
        if state:
            self.__video_enabled = False
            self.__processing_enabled = False
            self.__transmission_enabled = True
        else:
            self.__transmission_enabled = False
            self.robot.stop_required = True
            

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__image_loaded = False

        self.__video_enabled = False
        self.__processing_enabled = False
        self.__transmission_enabled = False

    def __video_processing(self):
        self.captured_frame = self.camera.get_frame()
        if not isinstance(self.captured_frame, type(None)):
            if self.settings.background_segmentation_state:
                self.captured_frame = cv2.medianBlur(
                    self.captured_frame, self.settings.blur_value
                )
                self.captured_frame = self.segmentor.removeBG(
                    self.captured_frame,
                    (255, 255, 255),
                    threshold=self.settings.background_segmentation_value / 100,
                )
            x, y, h, w = self.__check_roi(self.settings.roi_rect)
            self.captured_frame = cv2.rectangle(
                # self.captured_frame, (x-1, y-1, h+2, w+2), self.__COLOR_GREEN, 1
                self.captured_frame, (x, y, h, w), self.__COLOR_GREEN, 1
            )
            self.image_ready_signal.emit(self.captured_frame)
            self.__image_loaded = False

    def __check_roi(self, roi):
        x, y, h, w = roi
        if x < 0: 
            h = h + x
            x = 0
        if y < 0: 
            w = w + y
            y = 0
        if x + h > self.captured_frame.shape[1]: h = self.captured_frame.shape[1] - x
        if y + w > self.captured_frame.shape[0]: w = self.captured_frame.shape[0] - y

        return (x, y, h, w)

    def __frame_processing(self):
        if not self.__image_loaded:
            self.working_frame = self.captured_frame.copy()
            x, y, h, w = self.__check_roi(self.settings.roi_rect)
            roi = self.working_frame[y+1 : y + w-1, x+1 : x + h-1]
        else:
            roi = self.working_frame
            if self.settings.background_segmentation_state:
                roi = self.segmentor.removeBG(
                    roi,
                    (255, 255, 255),
                    threshold=self.settings.background_segmentation_value / 100,
                )
        roi = cv2.flip(roi, -1)
        if roi.shape[1] > roi.shape[0]:
            roi = cv2.rotate(roi, cv2.ROTATE_90_CLOCKWISE)
        self.image_for_save = roi.copy()
        roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        roi = cv2.medianBlur(roi, self.settings.blur_value)
        edges = cv2.Canny(
            roi,
            self.settings.canny_threshold[0],
            self.settings.canny_threshold[1],
        )
        contours, hierarchy = cv2.findContours(
            edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_TC89_KCOS
        )
        if not self.settings.appearance_filled:
            roi = np.zeros(roi.shape, roi.dtype)
            roi.fill(255)
        roi = cv2.cvtColor(roi, cv2.COLOR_GRAY2BGR)
        self.actual_contours = []
        for contour in contours:
            if cv2.arcLength(contour, False) > self.settings.minimal_contour_length:
                epsilon = (
                    self.settings.approximation_epsilon / 100
                )
                approximations = cv2.approxPolyDP(contour, epsilon, False)
                self.actual_contours.append(approximations)
                cv2.drawContours(
                    roi,
                    [approximations],
                    0,
                    color=self.__COLOR_RED,
                    thickness=1,
                    lineType=cv2.LINE_AA,
                )
        roi = cv2.flip(roi, -1)
        self.image_ready_signal.emit(roi)

    def __scale_contours(self):
        contours = copy.deepcopy(self.actual_contours)
        # Width/Height
        if not self.__image_loaded:
            frm = (self.settings.roi_rect[3], self.settings.roi_rect[2])
        else:
            frm = self.working_frame.shape
        to = self.settings.paper_size
        scale_factor = to[1]/frm[0]
        for i, contour in enumerate(contours):
            for j, point in enumerate(contour):
                contours[i][j] = contours[i][j]*scale_factor
        self.scaled_contours = contours

    def __prepare_data(self):
        transmission_data = []
        for contour in self.scaled_contours:
            transmission_data.append([contour[0][0][0], contour[0][0][1], 1])
            for point in contour:
                transmission_data.append([point[0][0], point[0][1], 0])
            _last = transmission_data[-1].copy()
            _last[2] = 1
            transmission_data.append(_last)

        return transmission_data

    def __save_image(self):
        if not os.path.exists("drawn"):
            os.makedirs("drawn")
        cv2.imwrite('drawn/' + datetime.now().strftime("%d_%m_%Y_%H_%M_%S") + '.jpg', self.image_for_save)

    def __data_transmission(self):
        self.progress_sending_updated.emit(0)
        self.__save_image()
        self.__scale_contours()
        data = self.__prepare_data()
        self.robot.send(data)
        while self.robot.is_sending:
            print(self.robot.drawn_percentage)
            self.progress_sending_updated.emit(self.robot.sent_percentage)
            self.progress_drawn_updated.emit(self.robot.drawn_percentage)
        self.progress_sending_updated.emit(0)
        self.progress_drawn_updated.emit(0)
        self.draw_finished.emit()
        self.__transmission_enabled = False

    def run(self):
        debugpy.debug_this_thread()
        self.robot = Robot(config_path="config/parameters.json")
        self.camera = Camera(config_path="config/parameters.json")
        self.settings = Settings(config_path="config/parameters.json")
        self.robot.start()
        self.segmentor = SelfiSegmentation()
        self.working_frame = None

        while True:
            # Emit connection state
            self.robot_connection_state_changed.emit(self.robot.is_connected)
            self.camera_state_changed.emit(self.camera.is_active)

            if self.__video_enabled:
                self.__video_processing()
            elif self.__processing_enabled:
                self.__frame_processing()
            elif self.__transmission_enabled:
                self.__data_transmission()
            else:
                self.msleep(10)
            # if self.robot.is_connected:
            #     self.robot.send('wait')
            #     _ = self.robot.receive()
