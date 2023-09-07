import typing
from PyQt5 import QtCore
from PyQt5.QtCore import QTime, QTimer
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QHBoxLayout, QVBoxLayout
import constants
import description_3
class Test2(QWidget):
    def __init__(self):
        super().__init__()
        self.init_Ui()
        self.set_appear()
        self.connection()
        self.show()
    def init_Ui(self):
        self.description = QLabel(constants.timer_1)
        self.start_button = QPushButton(constants.button_1)
        self.next_button = QPushButton(constants.next_button_1)
        self.next_button.setEnabled(False)
        self.v_layout = QVBoxLayout()
        self.text_timer_2 = QLabel(constants.txt_timer_2)
        self.v_layout.addWidget(self.text_timer_2)
        self.v_layout.addWidget(self.description)
        self.v_layout.addWidget(self.start_button)
        self.v_layout.addWidget(self.next_button)
        self.setLayout(self.v_layout)
    def timer_test_2(self):
        global time_2
        time_2 = QTime(0, 0, 45)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer_event_2)
        self.timer.start(1000)
    def timer_event_2(self):
        global time_2
        time_2= time_2.addSecs(-1)
        self.text_timer_2.setText(time_2.toString('hh:mm:ss'))
        if time_2.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()
            self.next_button.setEnabled(True)
    def set_appear(self):
        self.setWindowTitle(constants.title_2)
        x, y =constants.window_1_size
        self.resize(x, y)
    def connection(self):
        self.next_button.clicked.connect(self.next_click)
        self.start_button.clicked.connect(self.timer_test_2)
    def next_click(self):
        self.t_2 = description_3.Description3()
        self.hide()

