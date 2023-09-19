from PyQt5.QtWidgets import QLabel, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLineEdit

from PyQt5.QtCore import QTime, QTimer

import constants
import results


class Test3(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.set_appear()
        self.connection()
        self.show()

    def init_ui(self):
        self.timer_label3 = QLabel(constants.timer)
        self.timer_text3 = QLabel(constants.txt_timer_3)

        self.pulse_count = QLineEdit()
        self.pulse_count.setEnabled(False)

        self.start_button3 = QPushButton(constants.button_1)

        self.next_button3 = QPushButton(constants.next_button1)
        self.next_button3.setEnabled(False)

        self.h_layout = QHBoxLayout()
        self.v_layout = QVBoxLayout()

        self.h_layout.addWidget(self.timer_label3)
        self.h_layout.addWidget(self.timer_text3)

        self.v_layout.addLayout(self.h_layout)
        self.v_layout.addWidget(self.pulse_count)
        self.v_layout.addSpacing(40)
        self.v_layout.addWidget(self.start_button3)
        self.v_layout.addWidget(self.next_button3)
        self.setLayout(self.v_layout)

    def timer_test_3(self):
        global time_3
        time_3 = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer_event_3)
        self.timer.start(1000)

    def timer_event_3(self):
        global time_3
        time_3 = time_3.addSecs(-1)
        self.timer_text3.setText(time_3.toString('hh:mm:ss'))

        if 15 <= int(time_3.toString('hh:mm:ss')[6:8]) <= 45:
            self.timer_text3.setStyleSheet('color: rgb(255,0,0)')

        else:
            self.timer_text3.setStyleSheet('color: rgb(0,255,0)')

        if time_3.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()
            self.pulse_count.setEnabled(True)
            self.next_button3.setEnabled(True)

    def set_appear(self):
        self.setWindowTitle(constants.title_3)
        x, y = constants.window_1_size
        self.resize(x, y)

    # @classmethod
    # def return_count(self):
    #     count_pulse = self.pulse_count.text()
    #     return count_pulse

    def connection(self):
        self.next_button3.clicked.connect(self.next_click)
        self.start_button3.clicked.connect(self.timer_test_3)

    def next_click(self):
        file = open('results.txt', 'a')
        file.write(self.pulse_count.text())
        file.close()
        self.r = results.Results()
        self.hide()
