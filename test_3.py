import typing
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QHBoxLayout, QVBoxLayout
import constants
import results
class Test3(QWidget):
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
        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.description)
        self.v_layout.addWidget(self.start_button)
        self.v_layout.addWidget(self.next_button)
        self.setLayout(self.v_layout)
    def set_appear(self):
        self.setWindowTitle(constants.title_3)
        x, y =constants.window_1_size
        self.resize(x, y)
    def connection(self):
        self.next_button.clicked.connect(self.next_click)
    def next_click(self):
        self.t_3 = results.Results()
        self.hide()

