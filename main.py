from Camera import Camera
from ProgramThread import ProgramThread
from GUI import GUI
from PySide6.QtWidgets import QApplication
import sys

from Settings import Settings
   

app = QApplication(sys.argv)
settings = Settings()
settings.init(config_path='config/parameters.json')
t = ProgramThread()

window = GUI()
window.showMaximized()

t.image_ready_signal.connect(window.ui.image_widget.image_data_slot)
window.ui.button_start_video.toggled.connect(t.slot_enable_video)
window.ui.button_capture_frame.clicked.connect(t.slot_enable_processing)
window.ui.button_upload_image.clicked.connect(t.slot_load_image)
window.ui.button_start_draw.toggled.connect(t.slot_send_data)
t.robot_connection_state_changed.connect(window.slot_set_connection_state)
t.draw_finished.connect(window.slot_draw_finished)
t.camera_state_changed.connect(window.slot_set_camera_enabled)
t.progress_sending_updated.connect(window.ui.progress_sending.setValue)
t.progress_drawn_updated.connect(window.ui.progress_drawn.setValue)
t.start()
sys.exit(app.exec())