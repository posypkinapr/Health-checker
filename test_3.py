from PyQt5.QtWidgets import QLabel, QWidget, QPushButton, QHBoxLayout, QVBoxLayout

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
        self.timer_label3 = QLabel(constants.timer_3)
        self.timer_text3 = QLabel(constants.txt_timer_3)

        self.start_button3 = QPushButton(constants.button_1)

        self.next_button3 = QPushButton(constants.next_button_1)
        
        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.description)
        self.v_layout.addWidget(self.start_button)
        self.v_layout.addWidget(self.next_button)
        self.setLayout(self.v_layout)

    def set_appear(self):
        self.setWindowTitle(constants.title_3)
        x, y = constants.window_1_size
        self.resize(x, y)
        
    def connection(self):
        self.next_button.clicked.connect(self.next_click)

    def next_click(self):
        self.t_3 = results.Results()
        self.hide()

