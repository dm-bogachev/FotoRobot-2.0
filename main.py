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
t.robot_connection_state_changed.connect(window.slot_set_connection_state)
t.start()
sys.exit(app.exec())