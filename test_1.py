import typing
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QHBoxLayout, QVBoxLayout
import constants
class Test1(QWidget):
    def __init__(self):
        super().__init__()
        self.init_Ui()
        self.set_appear()
        self.show()
    def init_Ui(self):
        self.description = QLabel(constants.description_1)
        self.start_button = QPushButton(constants.button_1)
        self.next_button = QPushButton(constants.next_button_1)
        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.description)
        self.v_layout.addWidget(self.start_button)
        self.v_layout.addWidget(self.next_button)
        self.setLayout(self.v_layout)
    def set_appear(self):
        self.setWindowTitle(constants.title_1)
        x, y =constants.window_1_size
        self.resize(x, y)

