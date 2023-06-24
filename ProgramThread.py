import os
import cv2
import numpy as np
from Camera import Camera
from PySide6 import QtCore
from PySide6.QtWidgets import QFileDialog, QWidget
from PySide6.QtGui import QImage
import debugpy


from Robot import Robot
from Settings import Settings


class ProgramThread(QtCore.QThread):

    __COLOR_GREEN = (0, 255, 0)
    __COLOR_RED = (0, 0, 255)

    image_ready_signal = QtCore.Signal(np.ndarray)
    robot_connection_state_changed = QtCore.Signal(bool)
    camera_state_changed = QtCore.Signal(bool)

    def slot_enable_video(self, state):
        self.__video_enabled = state
        self.__processing_enabled = False

    def slot_enable_processing(self):
        self.__video_enabled = False
        self.__processing_enabled = True

    def slot_load_image(self):
        file_filter = 'Image (*.jpg *.jpeg *.png);'
        file_path = QFileDialog.getOpenFileName(QWidget(), "Select image", os.getcwd(), file_filter)
        # Dirty hack
        self.temp_qimage = QImage()
        self.temp_qimage.load(file_path[0])
        self.temp_qimage.save('_.jpg')
        self.working_frame = cv2.imread('_.jpg')
        self.__processing_enabled = True
        self.__image_loaded = True
        a = 0

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__image_loaded = False
        
        self.__video_enabled = False
        self.__processing_enabled = False

    def run(self):
        debugpy.debug_this_thread()
        self.robot = Robot(config_path="config/parameters.json")
        self.camera = Camera(config_path="config/parameters.json")
        self.settings = Settings(config_path="config/parameters.json")
        self.robot.start()
        self.working_frame = None

        while True:
            # Emit connection state
            self.robot_connection_state_changed.emit(self.robot.is_connected)
            self.camera_state_changed.emit(self.camera.is_active)

            if self.__video_enabled:
                captured_frame = self.camera.get_frame()
                if not isinstance(captured_frame, type(None)):
                    captured_frame = cv2.rectangle(captured_frame, self.settings.roi_rect, self.__COLOR_GREEN, 1)
                    self.image_ready_signal.emit(captured_frame)
                    x,y,h,w = self.settings.roi_rect
                    self.__image_loaded = False
            elif self.__processing_enabled:
                if not self.__image_loaded:
                    self.working_frame = captured_frame.copy()
                    roi = self.working_frame[y:y+w, x:x+h]
                else:
                    roi = self.working_frame
                roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
                roi = cv2.medianBlur(roi, self.settings.blur_value)
                edges = cv2.Canny(roi, self.settings.canny_threshold[0], self.settings.canny_threshold[1])
                contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_TC89_KCOS)
                #contours = cv2.approxPolyDP(contours, self.settings.approximation_epsilon, False)
                if not self.settings.appearance_filled:
                    roi = np.zeros(roi.shape, roi.dtype)
                    roi.fill(255)
                roi = cv2.cvtColor(roi, cv2.COLOR_GRAY2BGR)
                for contour in contours:
                    if cv2.arcLength(contour, False) > self.settings.minimal_contour_length:
                        epsilon = self.settings.approximation_epsilon/100# * cv2.arcLength(contour, True)
                        approximations = cv2.approxPolyDP(contour, epsilon, False)
                        cv2.drawContours(roi, [approximations], 0, color=self.__COLOR_RED, thickness=1, lineType=cv2.LINE_AA)

                self.image_ready_signal.emit(roi)
            else:
                self.msleep(100)



