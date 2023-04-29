from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QLabel, QVBoxLayout
from instr import *
from second_win import TestWin
app = QApplication([])

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
        
    def set_appear(self):
        self.move(win_x, win_y)
        self.setWindowTitle(title_txt)
        self.resize(win_width, win_height)

    def initUI(self):
        self.greet = QLabel(greet)
        self.instruction = QLabel(greet_instuction)
        self.button = QPushButton(fin_btn_txt)
        self.v_line = QVBoxLayout()
        self.v_line.addWidget(self.greet, alignment = Qt.AlignLeft)
        self.v_line.addWidget(self.instruction, alignment = Qt.AlignLeft)
        self.v_line.addWidget(self.button, alignment = Qt.AlignCenter)
        self.setLayout(self.v_line)

    def connects(self):
        self.button.clicked.connect(self.next_click)

    def next_click(self):
        self.hide()
        self.tw = TestWin()

mw = MainWin()
app.exec_()