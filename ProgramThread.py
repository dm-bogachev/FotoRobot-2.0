import random
import cv2
import numpy as np
from Camera import Camera
from PySide6 import QtCore
import debugpy


from Robot import Robot
from Settings import Settings


class ProgramThread(QtCore.QThread):
    image_ready_signal = QtCore.Signal(np.ndarray)
    robot_connection_state_changed = QtCore.Signal(bool)
    camera_state_changed = QtCore.Signal(bool)

    def slot_enable_video(self, state):
        self.__video_enabled = state
        self.__processing_enabled = False

    def slot_enable_processing(self):
        self.__video_enabled = False
        self.__processing_enabled = True

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
        while True:
            captured_frame = None
            # Emit connection state
            self.robot_connection_state_changed.emit(self.robot.is_connected)
            self.camera_state_changed.emit(self.camera.is_active)

            if self.__video_enabled:
                frame = self.camera.get_frame()
                if not isinstance(frame, type(None)):
                    frame = cv2.rectangle(frame, self.settings.roi_rect, (255, 0, 0), 2)
                    self.image_ready_signal.emit(frame)
                    x,y,h,w = self.settings.roi_rect
                    self.__image_loaded = False
            elif self.__processing_enabled:
                captured_frame = frame.copy()
                if not self.__image_loaded:
                    roi = captured_frame[y:y+w, x:x+h]
                else:
                    roi = captured_frame
                roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
                roi = cv2.medianBlur(roi, self.settings.blur_value)
                
                roi = cv2.cvtColor(roi, cv2.COLOR_GRAY2BGR)
                self.image_ready_signal.emit(roi)
            else:
                self.msleep(100)



