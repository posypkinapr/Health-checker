from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QFont

import constants
import description_1

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.set_appear()
        self.show()
        self.connection()

    def init_ui(self):
        font = QFont()
        font.setBold(True)
        self.greetings = QLabel(constants.greetings)
        self.greetings.setFont(font)

        self.description = QLabel(constants.description)

        self.start = QPushButton(constants.start_text)

        self.h_layout_1 = QHBoxLayout()
        self.h_layout_2 = QHBoxLayout()
        self.h_layout_3 = QHBoxLayout()
        self.v_layout = QVBoxLayout()

        self.h_layout_1.addWidget(self.greetings)
        self.h_layout_2.addWidget(self.description)
        self.h_layout_3.addWidget(self.start)

        self.v_layout.addLayout(self.h_layout_1)
        self.v_layout.addLayout(self.h_layout_2)
        self.v_layout.addLayout(self.h_layout_3)
        self.setLayout(self.v_layout)

    def set_appear(self):
        self.setWindowTitle(constants.title)
        x, y = constants.window_1_size
        self.resize(x, y) 
    
    def connection(self):
        self.start.clicked.connect(self.next_click)

    def next_click(self):
        self.d_1 = description_1.Description1()
        self.hide()
        
app = QApplication([])
main_w = MainWindow()    
app.exec_()