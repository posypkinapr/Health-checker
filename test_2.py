from PyQt5.QtCore import QTime, QTimer
from PyQt5.QtWidgets import QLabel, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLineEdit

import constants
import description_3


class Test2(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.set_appear()
        self.connection()
        self.show()

    def init_ui(self):
        self.timer_label2 = QLabel(constants.timer)
        self.timer_text2 = QLabel(constants.txt_timer_2)

        self.pulse_count = QLineEdit()
        self.pulse_count.setEnabled(False)

        self.start_button2 = QPushButton(constants.button_1)

        self.next_button2 = QPushButton(constants.next_button1)
        self.next_button2.setEnabled(False)

        self.h_layout = QHBoxLayout()
        self.v_layout = QVBoxLayout()

        self.h_layout.addWidget(self.timer_label2)
        self.h_layout.addWidget(self.timer_text2)

        self.v_layout.addLayout(self.h_layout)
        self.v_layout.addWidget(self.pulse_count)
        self.v_layout.addSpacing(40)
        self.v_layout.addWidget(self.start_button2)
        self.v_layout.addWidget(self.next_button2)
        self.setLayout(self.v_layout)

    def timer_test_2(self):
        global time_2
        time_2 = QTime(0, 0, 45)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer_event_2)
        self.timer.start(1000)

    def timer_event_2(self):
        global time_2

        time_2 = time_2.addSecs(-1)
        self.timer_text2.setText(time_2.toString('hh:mm:ss'))

        if time_2.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()
            self.pulse_count.setEnabled(True)
            self.next_button2.setEnabled(True)

    def set_appear(self):
        self.setWindowTitle(constants.title_2)
        x, y = constants.window_1_size
        self.resize(x, y)

    # def return_count(self):
    #     count_pulse = self.pulse_count.text()
    #     return count_pulse

    def connection(self):
        self.next_button2.clicked.connect(self.next_click)
        self.start_button2.clicked.connect(self.timer_test_2)

    def next_click(self):
        file = open('results.txt', 'a')
        file.write(self.pulse_count.text() + '\n')
        file.close()
        self.d_3 = description_3.Description3()
        self.hide()
