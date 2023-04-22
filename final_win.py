from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout
from instr import *

class FinalWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.show()

    def set_appear(self):
        #Заголовок, место и размеры окна
        self.resize(win_width, win_height)
        self.setWindowTitle("Тест Руфье")
        self.move(win_x, win_y)

    def initUI(self):
        #Создание главного лайаута, индекс Руфье, итог
        self.mainLayout = QVBoxLayout()
        self.indexLabel = QLabel(index)
        self.resultLabel = QLabel(result)

        #Добавление виджетов на лайаут
        self.mainLayout.addWidget(self.indexLabel, alignment = Qt.AlignCenter)
        self.mainLayout.addWidget(self.resultLabel, alignment = Qt.AlignCenter)

        #Позиционирование главного лайаута на экране
        self.setLayout(self.mainLayout)
