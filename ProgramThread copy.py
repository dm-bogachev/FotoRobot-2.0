import random
import cv2
import numpy as np
from Camera import Camera
from PySide6 import QtCore

from Robot import Robot


class ProgramThread(QtCore.QObject):
    image_ready_signal = QtCore.Signal(np.ndarray)
    robot_connection_state_changed = QtCore.Signal(bool)
    # processed_image_signal = QtCore.pyqtSignal(np.ndarray)
    # score_data = QtCore.pyqtSignal(str)

    def slot_enable_video(self, state):
        self.video_enabled = state

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__once = True       
        self.timer = QtCore.QBasicTimer()
        self.timer.start(0, self)

        self.video_enabled = False
        

    def timerEvent(self, event):
        if (event.timerId() != self.timer.timerId()):
            return
        if self.__once:
            self.robot = Robot(config_path='config/parameters.json') 
            self.robot.start()
            self.camera = Camera(config_path='config/parameters.json')   
            self.__once = False
        # Emit connection
        if self.robot.is_connected:
            self.robot_connection_state_changed.emit(True)
        else:
            self.robot_connection_state_changed.emit(False)
        frame = self.camera.get_frame()
        if self.video_enabled:
            self.image_ready_signal.emit(frame)

    def __del__(self):
        self.timer.stop()


if __name__ == '__main__':
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

    #self.game.oid.connect(self.oiw.image_data_slot)