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

    def slot_enable_video(self, state):
        self.__video_enabled = state
        self.__processing_enabled = False


    def slot_enable_processing(self):
        self.__video_enabled = False
        self.__processing_enabled = True

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__run_once = True
        
        self.__video_enabled = False
        self.__processing_enabled = False

    def run(self):
        debugpy.debug_this_thread()
        self.robot = Robot(config_path="config/parameters.json")
        self.camera = Camera(config_path="config/parameters.json")
        self.settings = Settings(config_path="config/parameters.json")
        
        self.robot.start()
        while True:
            # Emit connection state
            if self.robot.is_connected:
                self.robot_connection_state_changed.emit(True)
            else:
                self.robot_connection_state_changed.emit(False)
            
            if self.__video_enabled:
                frame = self.camera.get_frame()
                frame = cv2.rectangle(frame, self.settings.roi_rect, (255, 0, 0), 2)
                self.image_ready_signal.emit(frame)
            elif self.__processing_enabled:
                captured_frame = frame.copy()
                captured_frame = captured_frame[self.settings.roi_rect[0]:self.settings.roi_rect[0] + self.settings.roi_rect[3], self.settings.roi_rect[1]:self.settings.roi_rect[1] + self.settings.roi_rect[2]]
                captured_frame = cv2.cvtColor(captured_frame, cv2.COLOR_BGR2GRAY)
                captured_frame = cv2.medianBlur(captured_frame, self.settings.blur_value)
                
                captured_frame = cv2.cvtColor(captured_frame, cv2.COLOR_GRAY2BGR)
                self.image_ready_signal.emit(captured_frame)
            else:
                self.msleep(100)


    # def timerEvent(self, event):
    #     if (event.timerId() != self.timer.timerId()):
    #         return
    #     if self.__once:
    #         self.robot = Robot(config_path='config/parameters.json')
    #         self.robot.start()
    #         self.camera = Camera(config_path='config/parameters.json')
    #         self.__once = False
    #     # Emit connection
    #     if self.robot.is_connected:
    #         self.robot_connection_state_changed.emit(True)
    #     else:
    #         self.robot_connection_state_changed.emit(False)
    #     frame = self.camera.get_frame()
    #     if self.video_enabled:
    #         self.image_ready_signal.emit(frame)

    # def __del__(self):
    #     self.timer.stop()


if __name__ == "__main__":
    import sys
    from PySide6 import QtWidgets, QtGui

    # from ImageWidget import ImageWidget

    # app = QtWidgets.QApplication(sys.argv)
    # main_window = QtWidgets.QMainWindow()
    # main_window.setWindowTitle("КЁРЛИНГ ВЕРСИИ ОДИН ТОЧКА НОЛЬ")
    # main_window.showMaximized()
    # main_widget = ImageWidget()
    # main_window.setCentralWidget(main_widget)
    # main_window.showMaximized()
    # game = GameThread()
    # game.original_image_signal.connect(main_widget.image_data_slot)
    # sys.exit(app.exec())

    # self.game.oid.connect(self.oiw.image_data_slot)
