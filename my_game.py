from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QLabel, QVBoxLayout
from instr import *
class main_win(QWidget):
    def __init__(self):
        def set_appear(self):
            main_win.move(win_x, win_y)
            main_win.setWindowTitle(title_txt)
            main_win.resize(win_width, win_height)
            main_win.show()
        def initUI(self):
            greet = QLabel('Hello')
            instruction = QLabel('Что то  на казахском')
            button = QPushButton('Готов начать тест')
            button.text()
            v_line = QVBoxLayout()
            v_line.addWidget(greet, alignment = Qt.AlignLeft)
            v_line.addWidget(instruction, alignment = Qt.AlignLeft)
            v_line.addWidget(button, alignment = Qt.AlignCenter)
            main_win.setLayout(v_line)
        def connects(self):
            self.button.clicked.connect(self.next_click)
        def next_click(self):
            self.hide()
            self.sw = second_win()
        def show(self):
            pass
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
app = QApplication([])
main_win = QWidget()
app.exec_()
