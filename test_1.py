from PyQt5.QtCore import QTimer, QTime
from PyQt5.QtWidgets import QLabel, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLineEdit

import constants
import description_2


class Test1(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.set_appear()
        self.show()
        self.connection()

    def init_ui(self):
        self.timer_label1 = QLabel(constants.timer)
        self.timer_text1 = QLabel(constants.txt_timer_1)

        self.pulse_count = QLineEdit()
        self.pulse_count.setEnabled(False)

        self.start_button1 = QPushButton(constants.button_1)

        self.next_button1 = QPushButton(constants.next_button1)
        self.next_button1.setEnabled(False)

        self.h_layout = QHBoxLayout()
        self.v_layout = QVBoxLayout()

        self.h_layout.addWidget(self.timer_label1)
        self.h_layout.addWidget(self.timer_text1)

        self.v_layout.addLayout(self.h_layout)
        self.v_layout.addWidget(self.pulse_count)
        self.v_layout.addSpacing(40)
        self.v_layout.addWidget(self.start_button1)
        self.v_layout.addWidget(self.next_button1)
        self.setLayout(self.v_layout)

    def timer_test_1(self):
        global time_1
        time_1 = QTime(0, 0, 15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer_event_1)
        self.timer.start(1000)

    def timer_event_1(self):
        global time_1
        time_1 = time_1.addSecs(-1)
        self.timer_text1.setText(time_1.toString('hh:mm:ss'))

        if time_1.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()
            self.pulse_count.setEnabled(True)
            self.next_button1.setEnabled(True)

    def set_appear(self):
        self.setWindowTitle(constants.title_1)
        x, y = constants.window_1_size
        self.resize(x, y)

    # def return_count(self):
    #     count_pulse = self.pulse_count.text()
    #     return count_pulse

    def connection(self):
        self.next_button1.clicked.connect(self.next_click)
        self.start_button1.clicked.connect(self.timer_test_1)

    def next_click(self):
        file = open('results.txt', 'w')
        file.write(self.pulse_count.text() + '\n')
        file.close()
        self.d_2 = description_2.Description2()
        self.hide()
