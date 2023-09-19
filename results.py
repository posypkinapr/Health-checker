from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QHBoxLayout, QVBoxLayout
import constants
import sys


class Results(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.set_appear()
        self.show()
        self.connection()

    def init_ui(self):
        v = []
        file = open('results.txt', 'r')
        for line in file:
            v.append(int(line))

        result = ((v[0] + v[1] + v[2]) - 200) / 10

        if 0.1 <= result <= 5:
            comment = 'работоспобность вашего сердца на высшем уровне!!!'

        elif 5 < result <= 10:
            comment = 'жить будете!)'

        elif 10 < result <= 15:
            comment = 'еще поживете!('

        else:
            comment = 'вам осталось жить 2 часа :)'

        self.result_widget = QLabel(comment)
        self.description = QLabel(constants.description_r)
        self.next_button = QPushButton(constants.end_button)
        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.description)
        self.v_layout.addWidget(self.result_widget)
        self.v_layout.addWidget(self.next_button)
        self.setLayout(self.v_layout)

    def set_appear(self):
        self.setWindowTitle(constants.title_r)
        x, y = constants.window_1_size
        self.resize(x, y)

    def connection(self):
        self.next_button.clicked.connect(self.next_click)

    def next_click(self):
        self.hide()
        sys.exit()
