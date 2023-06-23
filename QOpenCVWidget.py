from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QImage, QPainter
from cv2 import rotate
import numpy as np

class QOpenCVWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.image = QImage()
        self.rotation_type = None

    def image_data_slot(self, image_data):
        if self.rotation_type:
            image_data = rotate(image_data, self.rotation_type)
        #image_data = resize(image_data, width=self.size().width())
        self.image = self.get_qimage(image_data)
        if self.image.size() != self.size():
            self.setFixedSize(self.image.size())
        self.update()

    def get_qimage(self, image: np.ndarray):
        height, width, colors = image.shape
        bytesPerLine = 3 * width

        image = QImage(image.data, width, height,
                       bytesPerLine, QImage.Format.Format_RGB888)

        image = image.rgbSwapped()
        return image

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawImage(0, 0, self.image)


    def set_rotation_type(self, type):
        self.rotation_type = type

if __name__ == '__main__':
    import cv2
    import sys
    from Camera import Camera
    from PySide6.QtWidgets import QApplication, QMainWindow
    camera = Camera()
    frame = camera.get_frame()

    if isinstance(frame, type(None)):
        print('Failed to capture frame')
        exit(-1)
    
    app = QApplication(sys.argv)

    main_window = QMainWindow()
    main_window.setWindowTitle("Test window")
    main_window.setFixedSize(800, 800)
    main_widget = QOpenCVWidget()
    main_widget.set_rotation_type(cv2.ROTATE_90_COUNTERCLOCKWISE)
    main_window.setCentralWidget(main_widget)
    main_window.showMaximized()
    main_widget.image_data_slot(frame)

    main_window.show()
    exit(app.exec())