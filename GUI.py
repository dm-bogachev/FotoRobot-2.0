from PySide6.QtWidgets import QWidget
from Settings import Settings
from ui_main_window import Ui_window_form
from Settings import Settings


class GUI(QWidget):
    __CONNECTION_STATE_CONNECTED_TEXT = "ROBOT IS CONNECTED"
    __CONNECTION_STATE_CONNECTED_STYLE = (
        "border-radius: 10px;\nbackground-color: rgb(0, 255, 0);\n\n\n"
    )
    __CONNECTION_STATE_DISCONNECTED_TEXT = "ROBOT IS NOT CONNECTED"
    __CONNECTION_STATE_DISCONNECTED_STYLE = (
        "border-radius: 10px;\nbackground-color: rgb(255, 0, 0);\n\n\n"
    )
    __CAMERA_STATE_CONNECTED_TEXT = "CAMERA IS ACTIVE"
    __CAMERA_STATE_DISCONNECTED_TEXT = "CAMERA IS NOT ACTIVE"

    def __init__(self):
        super().__init__()
        self.ui = Ui_window_form()
        self.ui.setupUi(self)
        self.__init_content()
        self.__pressed_coordinates = (0, 0)
        self.button_draw_was_enabled = False
        self.allow_button_draw_enable = False

    def __button_start_video_clicked(self):
        if self.ui.button_start_video.isChecked():
            self.ui.button_capture_frame.setEnabled(True)
            self.ui.button_upload_image.setEnabled(False)
            self.button_draw_was_enabled = False
            self.ui.button_start_draw.setEnabled(False)
        else:
            self.ui.button_capture_frame.setEnabled(False)
            self.ui.button_upload_image.setEnabled(True)

    def __button_capture_frame_clicked(self):
        self.ui.button_start_video.setEnabled(True)
        self.ui.button_start_video.setChecked(False)
        self.ui.button_capture_frame.setEnabled(False)
        self.ui.button_upload_image.setEnabled(True)
        self.button_draw_was_enabled = True
        if self.allow_button_draw_enable: 
            self.ui.button_start_draw.setEnabled(True)

    def __button_upload_frame_clicked(self):
        self.button_draw_was_enabled = True
        if self.allow_button_draw_enable: 
            self.ui.button_start_draw.setEnabled(True)

    def __button_start_draw_clicked(self):
        if self.ui.button_start_draw.isChecked():
            self.ui.button_capture_frame.setEnabled(False)
            self.ui.button_start_video.setEnabled(False)
            self.ui.button_upload_image.setEnabled(False)
            self.ui.progress_sending.setValue(0)
            self.ui.progress_sending.setVisible(True)
            self.ui.label_progress.setVisible(True)
            self.ui.progress_drawn.setValue(0)
            self.ui.progress_drawn.setVisible(True)
            self.ui.label_drawn.setVisible(True)
        else:
            self.ui.button_capture_frame.setEnabled(False)
            self.ui.button_start_video.setEnabled(True)
            self.ui.button_upload_image.setEnabled(True)
            self.ui.progress_sending.setValue(0)
            self.ui.progress_sending.setVisible(False)
            self.ui.label_progress.setVisible(False)
            self.ui.progress_drawn.setValue(0)
            self.ui.progress_drawn.setVisible(False)
            self.ui.label_drawn.setVisible(False)

    def slot_draw_finished(self):
        if self.ui.button_start_draw.isChecked():
            self.ui.button_start_draw.click()

    def slot_set_connection_state(self, state):
        if state:
            self.allow_button_draw_enable = True
            self.ui.label_connection_state.setText(
                self.__CONNECTION_STATE_CONNECTED_TEXT
            )
            self.ui.label_connection_state_lamp.setStyleSheet(
                self.__CONNECTION_STATE_CONNECTED_STYLE
            )
            if self.button_draw_was_enabled: self.ui.button_start_draw.setEnabled(True)
        else:
            self.allow_button_draw_enable = False
            self.ui.label_connection_state.setText(
                self.__CONNECTION_STATE_DISCONNECTED_TEXT
            )
            self.ui.label_connection_state_lamp.setStyleSheet(
                self.__CONNECTION_STATE_DISCONNECTED_STYLE
            )
            self.ui.button_start_draw.setEnabled(False)


    def slot_set_camera_enabled(self, state):
        if state:
            self.ui.button_start_video.setEnabled(True)
            self.ui.label_camera_state.setText(self.__CAMERA_STATE_CONNECTED_TEXT)
            self.ui.label_camera_state_lamp.setStyleSheet(
                self.__CONNECTION_STATE_CONNECTED_STYLE
            )
        else:
            self.ui.button_start_video.click()
            self.ui.button_start_video.setEnabled(False)
            self.ui.label_camera_state.setText(self.__CAMERA_STATE_DISCONNECTED_TEXT)
            self.ui.label_camera_state_lamp.setStyleSheet(
                self.__CONNECTION_STATE_DISCONNECTED_STYLE
            )

    def __init_content(self):
        self.settings = Settings()
        self.ui.progress_sending.setVisible(False)
        self.ui.label_progress.setVisible(False)
        self.ui.progress_drawn.setVisible(False)
        self.ui.label_drawn.setVisible(False)

        def mousePressEvent(QMouseEvent):
            self.__pressed_coordinates = QMouseEvent.pos()
            print(QMouseEvent.pos())

        def mouseMoveEvent(QMouseEvent):
            __new_coordinates = QMouseEvent.pos()
            delta = __new_coordinates - self.__pressed_coordinates
            self.__pressed_coordinates = __new_coordinates
            self.settings.roi_rect[0] = self.settings.roi_rect[0] + delta.x()
            self.settings.roi_rect[1] = self.settings.roi_rect[1] + delta.y()
            print(delta)

        self.ui.image_widget.mousePressEvent = mousePressEvent
        self.ui.image_widget.mouseMoveEvent = mouseMoveEvent

        self.__load_settings()
        self.ui.button_start_video.clicked.connect(self.__button_start_video_clicked)
        self.ui.button_capture_frame.clicked.connect(
            self.__button_capture_frame_clicked
        )
        self.ui.button_upload_image.clicked.connect(self.__button_upload_frame_clicked)
        self.ui.button_start_draw.clicked.connect(self.__button_start_draw_clicked)

        self.ui.slider_roi_width.valueChanged.connect(self.__update_settings)
        self.ui.button_show_filled_contours.clicked.connect(self.__update_settings)

        self.ui.slider_roi_height.valueChanged.connect(self.__update_settings)
        self.ui.slider_canny_parameter_1.valueChanged.connect(self.__update_settings)
        self.ui.slider_canny_parameter_2.valueChanged.connect(self.__update_settings)
        self.ui.slider_approximation.valueChanged.connect(self.__update_settings)
        self.ui.slider_minimal_contour.valueChanged.connect(self.__update_settings)
        self.ui.combo_blur_level.currentIndexChanged.connect(self.__update_settings)
        self.ui.line_paper_width.textChanged.connect(self.__update_settings)
        self.ui.line_paper_height.textChanged.connect(self.__update_settings)
        #
        self.ui.check_background_segmentation.stateChanged.connect(
            self.__update_settings
        )
        self.ui.slider_background_segmentation_value.valueChanged.connect(
            self.__update_settings
        )

    def __load_settings(self):
        self.ui.slider_roi_width.setValue(self.settings.roi_rect[2])
        self.ui.slider_roi_height.setValue(self.settings.roi_rect[3])
        self.ui.combo_blur_level.setCurrentText(str(self.settings.blur_value))
        self.ui.slider_canny_parameter_1.setValue(self.settings.canny_threshold[0])
        self.ui.slider_canny_parameter_2.setValue(self.settings.canny_threshold[1])
        self.ui.slider_minimal_contour.setValue(self.settings.minimal_contour_length)
        self.ui.slider_approximation.setValue(self.settings.approximation_epsilon)
        self.ui.line_paper_width.setText(str(self.settings.paper_size[0]))
        self.ui.line_paper_height.setText(str(self.settings.paper_size[1]))
        self.ui.button_show_filled_contours.setChecked(self.settings.appearance_filled)
        self.ui.line_paper_width.setText(str(self.settings.paper_size[1]))
        self.ui.line_paper_height.setText(str(self.settings.paper_size[0]))
        #
        self.ui.check_background_segmentation.setChecked(
            self.settings.background_segmentation_state
        )
        self.ui.slider_background_segmentation_value.setValue(
            self.settings.background_segmentation_value
        )

    def __update_settings(self):
        self.settings.roi_rect[2] = self.ui.slider_roi_width.value()
        self.settings.roi_rect[3] = self.ui.slider_roi_height.value()
        self.settings.blur_value = int(self.ui.combo_blur_level.currentText())
        self.settings.canny_threshold = (
            self.ui.slider_canny_parameter_1.value(),
            self.ui.slider_canny_parameter_2.value(),
        )
        self.settings.minimal_contour_length = self.ui.slider_minimal_contour.value()
        self.settings.approximation_epsilon = self.ui.slider_approximation.value()
        self.settings.paper_size = (
            int(self.ui.line_paper_width.text()),
            int(self.ui.line_paper_height.text()),
        )
        self.settings.appearance_filled = (
            self.ui.button_show_filled_contours.isChecked()
        )
        #
        self.settings.background_segmentation_state = (
            self.ui.check_background_segmentation.isChecked()
        )
        self.settings.background_segmentation_value = (
            self.ui.slider_background_segmentation_value.value()
        )
        #
        self.settings.save_settings()


if __name__ == "__main__":
    import sys
    from Camera import Camera
    from PySide6.QtWidgets import QApplication

    def test():
        frame = camera.get_frame()
        window.ui.image_widget.image_data_slot(frame)

    camera = Camera()

    app = QApplication(sys.argv)
    window = GUI()
    window.ui.button_capture_frame.clicked.connect(test)
    sys.exit(app.exec())
