# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowxSxHzw.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QCheckBox, QComboBox,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QScrollArea, QSizePolicy, QSlider,
    QSpacerItem, QToolButton, QVBoxLayout, QWidget)

from QOpenCVWidget import QOpenCVWidget

class Ui_window_form(object):
    def setupUi(self, window_form):
        if not window_form.objectName():
            window_form.setObjectName(u"window_form")
        window_form.setEnabled(True)
        window_form.resize(1022, 810)
        self.main_layout = QHBoxLayout(window_form)
        self.main_layout.setObjectName(u"main_layout")
        self.control_layout = QVBoxLayout()
        self.control_layout.setObjectName(u"control_layout")
        self.button_start_video = QToolButton(window_form)
        self.button_start_video.setObjectName(u"button_start_video")
        self.button_start_video.setEnabled(False)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_start_video.sizePolicy().hasHeightForWidth())
        self.button_start_video.setSizePolicy(sizePolicy)
        self.button_start_video.setMinimumSize(QSize(96, 96))
        self.button_start_video.setMaximumSize(QSize(96, 96))
        self.button_start_video.setFocusPolicy(Qt.NoFocus)
        self.button_start_video.setStyleSheet(u"QToolButton {border: 0px solid;}")
        icon = QIcon()
        icon.addFile(u"files/icons8-video-camera-96.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u"files/icons8-cancel-96.png", QSize(), QIcon.Normal, QIcon.On)
        self.button_start_video.setIcon(icon)
        self.button_start_video.setIconSize(QSize(96, 96))
        self.button_start_video.setCheckable(True)
        self.button_start_video.setAutoRaise(True)

        self.control_layout.addWidget(self.button_start_video)

        self.button_capture_frame = QToolButton(window_form)
        self.button_capture_frame.setObjectName(u"button_capture_frame")
        self.button_capture_frame.setEnabled(False)
        sizePolicy.setHeightForWidth(self.button_capture_frame.sizePolicy().hasHeightForWidth())
        self.button_capture_frame.setSizePolicy(sizePolicy)
        self.button_capture_frame.setMinimumSize(QSize(96, 96))
        self.button_capture_frame.setMaximumSize(QSize(96, 96))
        self.button_capture_frame.setFocusPolicy(Qt.NoFocus)
        self.button_capture_frame.setStyleSheet(u"QToolButton {border: 0px solid;}")
        icon1 = QIcon()
        icon1.addFile(u"files/icons8-aperture-96.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_capture_frame.setIcon(icon1)
        self.button_capture_frame.setIconSize(QSize(96, 96))
        self.button_capture_frame.setAutoRaise(True)

        self.control_layout.addWidget(self.button_capture_frame)

        self.button_upload_image = QToolButton(window_form)
        self.button_upload_image.setObjectName(u"button_upload_image")
        sizePolicy.setHeightForWidth(self.button_upload_image.sizePolicy().hasHeightForWidth())
        self.button_upload_image.setSizePolicy(sizePolicy)
        self.button_upload_image.setMinimumSize(QSize(96, 96))
        self.button_upload_image.setMaximumSize(QSize(96, 96))
        self.button_upload_image.setFocusPolicy(Qt.NoFocus)
        self.button_upload_image.setStyleSheet(u"QToolButton {border: 0px solid;}")
        icon2 = QIcon()
        icon2.addFile(u"files/icons8-upload-96.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_upload_image.setIcon(icon2)
        self.button_upload_image.setIconSize(QSize(96, 96))
        self.button_upload_image.setAutoRaise(True)

        self.control_layout.addWidget(self.button_upload_image)

        self.button_start_draw = QToolButton(window_form)
        self.button_start_draw.setObjectName(u"button_start_draw")
        self.button_start_draw.setEnabled(False)
        sizePolicy.setHeightForWidth(self.button_start_draw.sizePolicy().hasHeightForWidth())
        self.button_start_draw.setSizePolicy(sizePolicy)
        self.button_start_draw.setMinimumSize(QSize(96, 96))
        self.button_start_draw.setMaximumSize(QSize(96, 96))
        self.button_start_draw.setFocusPolicy(Qt.NoFocus)
        self.button_start_draw.setStyleSheet(u"QToolButton {border: 0px solid;}")
        icon3 = QIcon()
        icon3.addFile(u"files/icons8-paint-96.png", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u"files/icons8-cancel-96.png", QSize(), QIcon.Normal, QIcon.On)
        self.button_start_draw.setIcon(icon3)
        self.button_start_draw.setIconSize(QSize(96, 96))
        self.button_start_draw.setCheckable(True)
        self.button_start_draw.setChecked(False)
        self.button_start_draw.setAutoRaise(True)

        self.control_layout.addWidget(self.button_start_draw)

        self.control_layout_vertical_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.control_layout.addItem(self.control_layout_vertical_spacer)

        self.button_show_filled_contours = QToolButton(window_form)
        self.button_show_filled_contours.setObjectName(u"button_show_filled_contours")
        self.button_show_filled_contours.setStyleSheet(u"QToolButton {border: 0px solid;}")
        icon4 = QIcon()
        icon4.addFile(u"files/icons8-360-degrees-96.png", QSize(), QIcon.Normal, QIcon.Off)
        icon4.addFile(u"files/icons8-0-degrees-96.png", QSize(), QIcon.Normal, QIcon.On)
        self.button_show_filled_contours.setIcon(icon4)
        self.button_show_filled_contours.setIconSize(QSize(96, 96))
        self.button_show_filled_contours.setCheckable(True)
        self.button_show_filled_contours.setAutoRaise(True)

        self.control_layout.addWidget(self.button_show_filled_contours)

        self.control_layout_vertical_spacer2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.control_layout.addItem(self.control_layout_vertical_spacer2)


        self.main_layout.addLayout(self.control_layout)

        self.image_scroll_area = QScrollArea(window_form)
        self.image_scroll_area.setObjectName(u"image_scroll_area")
        self.image_scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.image_scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.image_scroll_area.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.image_scroll_area.setWidgetResizable(True)
        self.image_scroll_area_content = QWidget()
        self.image_scroll_area_content.setObjectName(u"image_scroll_area_content")
        self.image_scroll_area_content.setGeometry(QRect(0, 0, 618, 773))
        self.horizontalLayout = QHBoxLayout(self.image_scroll_area_content)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.image_widget = QOpenCVWidget(self.image_scroll_area_content)
        self.image_widget.setObjectName(u"image_widget")
        self.image_widget.setEnabled(True)
        self.image_widget.setMinimumSize(QSize(600, 400))

        self.horizontalLayout.addWidget(self.image_widget)

        self.image_scroll_area.setWidget(self.image_scroll_area_content)

        self.main_layout.addWidget(self.image_scroll_area)

        self.parameters_layout = QVBoxLayout()
        self.parameters_layout.setObjectName(u"parameters_layout")
        self.connection_state_group = QGroupBox(window_form)
        self.connection_state_group.setObjectName(u"connection_state_group")
        self.connection_state_group.setMinimumSize(QSize(300, 0))
        self.connection_state_group.setMaximumSize(QSize(300, 16777215))
        self.gridLayout_6 = QGridLayout(self.connection_state_group)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.horizontalSpacer = QSpacerItem(404, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer, 1, 3, 1, 1)

        self.label_camera_state_lamp = QLabel(self.connection_state_group)
        self.label_camera_state_lamp.setObjectName(u"label_camera_state_lamp")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_camera_state_lamp.sizePolicy().hasHeightForWidth())
        self.label_camera_state_lamp.setSizePolicy(sizePolicy1)
        self.label_camera_state_lamp.setMinimumSize(QSize(20, 20))
        self.label_camera_state_lamp.setMaximumSize(QSize(20, 20))
        self.label_camera_state_lamp.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(255, 0, 0);\n"
"\n"
"\n"
"")

        self.gridLayout_6.addWidget(self.label_camera_state_lamp, 0, 0, 1, 1)

        self.label_connection_state_lamp = QLabel(self.connection_state_group)
        self.label_connection_state_lamp.setObjectName(u"label_connection_state_lamp")
        sizePolicy1.setHeightForWidth(self.label_connection_state_lamp.sizePolicy().hasHeightForWidth())
        self.label_connection_state_lamp.setSizePolicy(sizePolicy1)
        self.label_connection_state_lamp.setMinimumSize(QSize(20, 20))
        self.label_connection_state_lamp.setMaximumSize(QSize(20, 20))
        self.label_connection_state_lamp.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(255, 0, 0);\n"
"\n"
"\n"
"")

        self.gridLayout_6.addWidget(self.label_connection_state_lamp, 1, 0, 1, 1)

        self.label_camera_state = QLabel(self.connection_state_group)
        self.label_camera_state.setObjectName(u"label_camera_state")

        self.gridLayout_6.addWidget(self.label_camera_state, 0, 1, 1, 1)

        self.label_connection_state = QLabel(self.connection_state_group)
        self.label_connection_state.setObjectName(u"label_connection_state")

        self.gridLayout_6.addWidget(self.label_connection_state, 1, 1, 1, 1)


        self.parameters_layout.addWidget(self.connection_state_group)

        self.roi_parameters_group = QGroupBox(window_form)
        self.roi_parameters_group.setObjectName(u"roi_parameters_group")
        self.roi_parameters_group.setMaximumSize(QSize(300, 16777215))
        self.gridLayout = QGridLayout(self.roi_parameters_group)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_roi_width = QLabel(self.roi_parameters_group)
        self.label_roi_width.setObjectName(u"label_roi_width")

        self.gridLayout.addWidget(self.label_roi_width, 0, 0, 1, 1)

        self.label_roi_width_value = QLabel(self.roi_parameters_group)
        self.label_roi_width_value.setObjectName(u"label_roi_width_value")
        self.label_roi_width_value.setMinimumSize(QSize(30, 0))
        self.label_roi_width_value.setMaximumSize(QSize(30, 16777215))

        self.gridLayout.addWidget(self.label_roi_width_value, 1, 1, 1, 1)

        self.slider_roi_height = QSlider(self.roi_parameters_group)
        self.slider_roi_height.setObjectName(u"slider_roi_height")
        self.slider_roi_height.setMinimum(100)
        self.slider_roi_height.setMaximum(1024)
        self.slider_roi_height.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.slider_roi_height, 3, 0, 1, 1)

        self.slider_roi_width = QSlider(self.roi_parameters_group)
        self.slider_roi_width.setObjectName(u"slider_roi_width")
        self.slider_roi_width.setMinimum(100)
        self.slider_roi_width.setMaximum(1024)
        self.slider_roi_width.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.slider_roi_width, 1, 0, 1, 1)

        self.label_roi_height_value = QLabel(self.roi_parameters_group)
        self.label_roi_height_value.setObjectName(u"label_roi_height_value")
        self.label_roi_height_value.setMinimumSize(QSize(30, 0))
        self.label_roi_height_value.setMaximumSize(QSize(30, 16777215))

        self.gridLayout.addWidget(self.label_roi_height_value, 3, 1, 1, 1)

        self.label_roi_height = QLabel(self.roi_parameters_group)
        self.label_roi_height.setObjectName(u"label_roi_height")

        self.gridLayout.addWidget(self.label_roi_height, 2, 0, 1, 1)


        self.parameters_layout.addWidget(self.roi_parameters_group)

        self.background_segmentation_group = QGroupBox(window_form)
        self.background_segmentation_group.setObjectName(u"background_segmentation_group")
        self.background_segmentation_group.setMinimumSize(QSize(300, 0))
        self.background_segmentation_group.setMaximumSize(QSize(300, 16777215))
        self.gridLayout_7 = QGridLayout(self.background_segmentation_group)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.slider_background_segmentation_value = QSlider(self.background_segmentation_group)
        self.slider_background_segmentation_value.setObjectName(u"slider_background_segmentation_value")
        self.slider_background_segmentation_value.setMinimum(1)
        self.slider_background_segmentation_value.setMaximum(100)
        self.slider_background_segmentation_value.setOrientation(Qt.Horizontal)

        self.gridLayout_7.addWidget(self.slider_background_segmentation_value, 0, 1, 1, 1)

        self.check_background_segmentation = QCheckBox(self.background_segmentation_group)
        self.check_background_segmentation.setObjectName(u"check_background_segmentation")

        self.gridLayout_7.addWidget(self.check_background_segmentation, 0, 0, 1, 1)

        self.label_background_segmentation = QLabel(self.background_segmentation_group)
        self.label_background_segmentation.setObjectName(u"label_background_segmentation")
        self.label_background_segmentation.setMinimumSize(QSize(30, 0))
        self.label_background_segmentation.setMaximumSize(QSize(30, 16777215))

        self.gridLayout_7.addWidget(self.label_background_segmentation, 0, 2, 1, 1)


        self.parameters_layout.addWidget(self.background_segmentation_group)

        self.image_processing_parameters_group = QGroupBox(window_form)
        self.image_processing_parameters_group.setObjectName(u"image_processing_parameters_group")
        self.image_processing_parameters_group.setMaximumSize(QSize(300, 16777215))
        self.gridLayout_2 = QGridLayout(self.image_processing_parameters_group)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_blur_label = QLabel(self.image_processing_parameters_group)
        self.label_blur_label.setObjectName(u"label_blur_label")

        self.gridLayout_2.addWidget(self.label_blur_label, 0, 1, 1, 1)

        self.canny_parameters_group = QGroupBox(self.image_processing_parameters_group)
        self.canny_parameters_group.setObjectName(u"canny_parameters_group")
        self.gridLayout_3 = QGridLayout(self.canny_parameters_group)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_canny_parameter_1 = QLabel(self.canny_parameters_group)
        self.label_canny_parameter_1.setObjectName(u"label_canny_parameter_1")

        self.gridLayout_3.addWidget(self.label_canny_parameter_1, 0, 0, 1, 1)

        self.slider_canny_parameter_2 = QSlider(self.canny_parameters_group)
        self.slider_canny_parameter_2.setObjectName(u"slider_canny_parameter_2")
        self.slider_canny_parameter_2.setMinimum(1)
        self.slider_canny_parameter_2.setMaximum(512)
        self.slider_canny_parameter_2.setOrientation(Qt.Horizontal)

        self.gridLayout_3.addWidget(self.slider_canny_parameter_2, 3, 0, 1, 1)

        self.label_canny_parameter_2_value = QLabel(self.canny_parameters_group)
        self.label_canny_parameter_2_value.setObjectName(u"label_canny_parameter_2_value")
        self.label_canny_parameter_2_value.setMinimumSize(QSize(30, 0))
        self.label_canny_parameter_2_value.setMaximumSize(QSize(30, 16777215))

        self.gridLayout_3.addWidget(self.label_canny_parameter_2_value, 3, 2, 1, 1)

        self.label_canny_parameter_2 = QLabel(self.canny_parameters_group)
        self.label_canny_parameter_2.setObjectName(u"label_canny_parameter_2")

        self.gridLayout_3.addWidget(self.label_canny_parameter_2, 2, 0, 1, 1)

        self.slider_canny_parameter_1 = QSlider(self.canny_parameters_group)
        self.slider_canny_parameter_1.setObjectName(u"slider_canny_parameter_1")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.slider_canny_parameter_1.sizePolicy().hasHeightForWidth())
        self.slider_canny_parameter_1.setSizePolicy(sizePolicy2)
        self.slider_canny_parameter_1.setMinimum(1)
        self.slider_canny_parameter_1.setMaximum(512)
        self.slider_canny_parameter_1.setOrientation(Qt.Horizontal)

        self.gridLayout_3.addWidget(self.slider_canny_parameter_1, 1, 0, 1, 1)

        self.label_canny_parameter_1_value = QLabel(self.canny_parameters_group)
        self.label_canny_parameter_1_value.setObjectName(u"label_canny_parameter_1_value")
        self.label_canny_parameter_1_value.setMinimumSize(QSize(30, 0))
        self.label_canny_parameter_1_value.setMaximumSize(QSize(30, 16777215))

        self.gridLayout_3.addWidget(self.label_canny_parameter_1_value, 1, 2, 1, 1)


        self.gridLayout_2.addWidget(self.canny_parameters_group, 2, 1, 1, 2)

        self.contour_parameters_group = QGroupBox(self.image_processing_parameters_group)
        self.contour_parameters_group.setObjectName(u"contour_parameters_group")
        self.gridLayout_4 = QGridLayout(self.contour_parameters_group)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_approximation_value = QLabel(self.contour_parameters_group)
        self.label_approximation_value.setObjectName(u"label_approximation_value")
        self.label_approximation_value.setMinimumSize(QSize(30, 0))
        self.label_approximation_value.setMaximumSize(QSize(30, 16777215))

        self.gridLayout_4.addWidget(self.label_approximation_value, 3, 1, 1, 1)

        self.label_approximation = QLabel(self.contour_parameters_group)
        self.label_approximation.setObjectName(u"label_approximation")

        self.gridLayout_4.addWidget(self.label_approximation, 2, 0, 1, 1)

        self.label_minimal_contour = QLabel(self.contour_parameters_group)
        self.label_minimal_contour.setObjectName(u"label_minimal_contour")

        self.gridLayout_4.addWidget(self.label_minimal_contour, 0, 0, 1, 1)

        self.slider_approximation = QSlider(self.contour_parameters_group)
        self.slider_approximation.setObjectName(u"slider_approximation")
        self.slider_approximation.setMinimum(1)
        self.slider_approximation.setMaximum(500)
        self.slider_approximation.setOrientation(Qt.Horizontal)

        self.gridLayout_4.addWidget(self.slider_approximation, 3, 0, 1, 1)

        self.slider_minimal_contour = QSlider(self.contour_parameters_group)
        self.slider_minimal_contour.setObjectName(u"slider_minimal_contour")
        self.slider_minimal_contour.setMinimum(0)
        self.slider_minimal_contour.setMaximum(500)
        self.slider_minimal_contour.setOrientation(Qt.Horizontal)

        self.gridLayout_4.addWidget(self.slider_minimal_contour, 1, 0, 1, 1)

        self.label_minimal_contour_value = QLabel(self.contour_parameters_group)
        self.label_minimal_contour_value.setObjectName(u"label_minimal_contour_value")
        self.label_minimal_contour_value.setMinimumSize(QSize(30, 0))
        self.label_minimal_contour_value.setMaximumSize(QSize(30, 16777215))

        self.gridLayout_4.addWidget(self.label_minimal_contour_value, 1, 1, 1, 1)


        self.gridLayout_2.addWidget(self.contour_parameters_group, 3, 1, 1, 1)

        self.combo_blur_level = QComboBox(self.image_processing_parameters_group)
        self.combo_blur_level.addItem("")
        self.combo_blur_level.addItem("")
        self.combo_blur_level.addItem("")
        self.combo_blur_level.addItem("")
        self.combo_blur_level.addItem("")
        self.combo_blur_level.addItem("")
        self.combo_blur_level.addItem("")
        self.combo_blur_level.addItem("")
        self.combo_blur_level.addItem("")
        self.combo_blur_level.setObjectName(u"combo_blur_level")
        self.combo_blur_level.setMinimumSize(QSize(60, 0))
        self.combo_blur_level.setMaximumSize(QSize(60, 16777215))
        self.combo_blur_level.setEditable(False)

        self.gridLayout_2.addWidget(self.combo_blur_level, 1, 1, 1, 1)


        self.parameters_layout.addWidget(self.image_processing_parameters_group)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.parameters_layout.addItem(self.verticalSpacer_2)

        self.paper_parameters_group = QGroupBox(window_form)
        self.paper_parameters_group.setObjectName(u"paper_parameters_group")
        self.paper_parameters_group.setMinimumSize(QSize(300, 0))
        self.paper_parameters_group.setMaximumSize(QSize(300, 16777215))
        self.gridLayout_5 = QGridLayout(self.paper_parameters_group)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_paper_height = QLabel(self.paper_parameters_group)
        self.label_paper_height.setObjectName(u"label_paper_height")

        self.gridLayout_5.addWidget(self.label_paper_height, 1, 0, 1, 1)

        self.line_paper_height = QLineEdit(self.paper_parameters_group)
        self.line_paper_height.setObjectName(u"line_paper_height")
        self.line_paper_height.setMinimumSize(QSize(40, 0))
        self.line_paper_height.setMaximumSize(QSize(40, 16777215))
        self.line_paper_height.setFrame(True)
        self.line_paper_height.setEchoMode(QLineEdit.Normal)
        self.line_paper_height.setCursorPosition(0)

        self.gridLayout_5.addWidget(self.line_paper_height, 1, 1, 1, 1)

        self.line_paper_width = QLineEdit(self.paper_parameters_group)
        self.line_paper_width.setObjectName(u"line_paper_width")
        self.line_paper_width.setMinimumSize(QSize(40, 0))
        self.line_paper_width.setMaximumSize(QSize(40, 16777215))
        self.line_paper_width.setCursorPosition(0)

        self.gridLayout_5.addWidget(self.line_paper_width, 0, 1, 1, 1)

        self.label_paper_width = QLabel(self.paper_parameters_group)
        self.label_paper_width.setObjectName(u"label_paper_width")

        self.gridLayout_5.addWidget(self.label_paper_width, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)


        self.parameters_layout.addWidget(self.paper_parameters_group)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.parameters_layout.addItem(self.verticalSpacer)


        self.main_layout.addLayout(self.parameters_layout)


        self.retranslateUi(window_form)
        self.slider_roi_width.valueChanged.connect(self.label_roi_width_value.setNum)
        self.slider_roi_height.valueChanged.connect(self.label_roi_height_value.setNum)
        self.slider_canny_parameter_1.valueChanged.connect(self.label_canny_parameter_1_value.setNum)
        self.slider_canny_parameter_2.valueChanged.connect(self.label_canny_parameter_2_value.setNum)
        self.slider_minimal_contour.valueChanged.connect(self.label_minimal_contour_value.setNum)
        self.slider_approximation.valueChanged.connect(self.label_approximation_value.setNum)
        self.slider_background_segmentation_value.valueChanged.connect(self.label_background_segmentation.setNum)

        QMetaObject.connectSlotsByName(window_form)
    # setupUi

    def retranslateUi(self, window_form):
        window_form.setWindowTitle(QCoreApplication.translate("window_form", u"FotoRobot", None))
        self.button_start_video.setText("")
        self.button_capture_frame.setText("")
        self.button_upload_image.setText("")
        self.button_start_draw.setText("")
        self.button_show_filled_contours.setText("")
        self.connection_state_group.setTitle(QCoreApplication.translate("window_form", u"State", None))
        self.label_camera_state_lamp.setText("")
        self.label_connection_state_lamp.setText("")
        self.label_camera_state.setText(QCoreApplication.translate("window_form", u"CAMERA IS OFF", None))
        self.label_connection_state.setText(QCoreApplication.translate("window_form", u"ROBOT IS NOT CONNECTED", None))
        self.roi_parameters_group.setTitle(QCoreApplication.translate("window_form", u"ROI Parameters", None))
        self.label_roi_width.setText(QCoreApplication.translate("window_form", u"ROI Width", None))
        self.label_roi_width_value.setText(QCoreApplication.translate("window_form", u"0", None))
        self.label_roi_height_value.setText(QCoreApplication.translate("window_form", u"0", None))
        self.label_roi_height.setText(QCoreApplication.translate("window_form", u"ROI Height", None))
        self.background_segmentation_group.setTitle(QCoreApplication.translate("window_form", u"Background segmentation", None))
        self.check_background_segmentation.setText(QCoreApplication.translate("window_form", u"Activate", None))
        self.label_background_segmentation.setText(QCoreApplication.translate("window_form", u"0", None))
        self.image_processing_parameters_group.setTitle(QCoreApplication.translate("window_form", u"Processing parameters", None))
        self.label_blur_label.setText(QCoreApplication.translate("window_form", u"Blur value", None))
        self.canny_parameters_group.setTitle(QCoreApplication.translate("window_form", u"Canny parameters", None))
        self.label_canny_parameter_1.setText(QCoreApplication.translate("window_form", u"Canny parameter 1", None))
        self.label_canny_parameter_2_value.setText(QCoreApplication.translate("window_form", u"0", None))
        self.label_canny_parameter_2.setText(QCoreApplication.translate("window_form", u"Canny parameter 2", None))
        self.label_canny_parameter_1_value.setText(QCoreApplication.translate("window_form", u"0", None))
        self.contour_parameters_group.setTitle(QCoreApplication.translate("window_form", u"Contour parameters", None))
        self.label_approximation_value.setText(QCoreApplication.translate("window_form", u"0", None))
        self.label_approximation.setText(QCoreApplication.translate("window_form", u"Approximation epsilon", None))
        self.label_minimal_contour.setText(QCoreApplication.translate("window_form", u"Minimal contour length", None))
        self.label_minimal_contour_value.setText(QCoreApplication.translate("window_form", u"0", None))
        self.combo_blur_level.setItemText(0, QCoreApplication.translate("window_form", u"1", None))
        self.combo_blur_level.setItemText(1, QCoreApplication.translate("window_form", u"3", None))
        self.combo_blur_level.setItemText(2, QCoreApplication.translate("window_form", u"5", None))
        self.combo_blur_level.setItemText(3, QCoreApplication.translate("window_form", u"7", None))
        self.combo_blur_level.setItemText(4, QCoreApplication.translate("window_form", u"9", None))
        self.combo_blur_level.setItemText(5, QCoreApplication.translate("window_form", u"11", None))
        self.combo_blur_level.setItemText(6, QCoreApplication.translate("window_form", u"13", None))
        self.combo_blur_level.setItemText(7, QCoreApplication.translate("window_form", u"15", None))
        self.combo_blur_level.setItemText(8, QCoreApplication.translate("window_form", u"17", None))

        self.paper_parameters_group.setTitle(QCoreApplication.translate("window_form", u"Paper parameters", None))
        self.label_paper_height.setText(QCoreApplication.translate("window_form", u"Paper height", None))
        self.line_paper_height.setInputMask(QCoreApplication.translate("window_form", u"0000", None))
        self.line_paper_height.setText(QCoreApplication.translate("window_form", u"297", None))
        self.line_paper_width.setInputMask(QCoreApplication.translate("window_form", u"0000", None))
        self.line_paper_width.setText(QCoreApplication.translate("window_form", u"210", None))
        self.label_paper_width.setText(QCoreApplication.translate("window_form", u"Paper width", None))
    # retranslateUi

