from PyQt5.QtWidgets import QLabel, QWidget, QPushButton, QHBoxLayout, QVBoxLayout
import constants
import test_3

class Description3(QWidget):
    def __init__(self):
        super().__init__()
        self.init_Ui()
        self.set_appear()
        self.show()
        self.connection()

    def init_Ui(self):
        self.description = QLabel(constants.description_3)
        self.next_button = QPushButton(constants.next_button_1)
        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.description)
        self.v_layout.addWidget(self.next_button)
        self.setLayout(self.v_layout)

    def set_appear(self):
        self.setWindowTitle(constants.d_title_3)
        x, y = constants.window_1_size
        self.resize(x, y)

    def connection(self):
        self.next_button.clicked.connect(self.next_click)

    def next_click(self):
        self.t_3 = test_3.Test3()
        self.hide()