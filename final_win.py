from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout
from instr import *

class FinalWin(QWidget):
    def __init__(self, exp):
        super().__init__()
        self.exp = exp
        self.results()
        self.set_appear()
        self.initUI()
        self.show()

    def results(self):
        self.indexRuf = (4 * (self.exp.t1 + self.exp.t2 + self.exp.t3) - 200) / 10
        self.finalResult = ""
        usersAge = self.exp.age

        if 7 <= usersAge >= 8:
            if self.indexRuf >= 21:
                self.finalResult = txt_res1

            elif 17 <= self.indexRuf >= 20.9:
                self.finalResult = txt_res2

            elif 12 <= self.indexRuf >= 16.9:
                self.finalResult = txt_res3

            elif 6.5 <= self.indexRuf >= 11.9:
                self.finalResult = txt_res4

            elif self.indexRuf <= 6.4:
                self.finalResult = txt_res5

        if 9 <= usersAge >= 10:
            if self.indexRuf >= 19.5:
                self.finalResult = txt_res1

            elif 15.5 <= self.indexRuf >= 19.4:
                self.finalResult = txt_res2

            elif 10.5 <= self.indexRuf >= 15.4:
                self.finalResult = txt_res3

            elif 5 <= self.indexRuf >= 10.4:
                self.finalResult = txt_res4

            elif self.indexRuf <= 4.9:
                self.finalResult = txt_res5

        if 11 <= usersAge >= 12:
            if self.indexRuf >= 18:
                self.finalResult = txt_res1

            elif 14 <= self.indexRuf >= 17.9:
                self.finalResult = txt_res2

            elif 9 <= self.indexRuf >= 13.9:
                self.finalResult = txt_res3

            elif 3.5 <= self.indexRuf >= 8.9:
                self.finalResult = txt_res4

            elif self.indexRuf <= 3.4:
                self.finalResult = txt_res5

        if 13 <= usersAge >= 14:
            if self.indexRuf >= 16.5:
                self.finalResult = txt_res1

            elif 12.5 <= self.indexRuf >= 16.4:
                self.finalResult = txt_res2

            elif 7.5 <= self.indexRuf >= 12.4:
                self.finalResult = txt_res3

            elif 2 <= self.indexRuf >= 7.4:
                self.finalResult = txt_res4

            elif self.indexRuf <= 1.9:
                self.finalResult = txt_res5

        if usersAge >= 15:
            if self.indexRuf >= 15:
                self.finalResult = txt_res1

            elif 11 <= self.indexRuf >= 14.9:
                self.finalResult = txt_res2

            elif 6 <= self.indexRuf >= 10.9:
                self.finalResult = txt_res3

            elif 0.5 <= self.indexRuf >= 5.9:
                self.finalResult = txt_res4

            elif self.indexRuf <= 0.4:
                self.finalResult = txt_res5

    def set_appear(self):
        #Заголовок, место и размеры окна
        self.resize(win_width, win_height)
        self.setWindowTitle(title_txt)
        self.move(win_x, win_y)

    def initUI(self):
        #Создание главного лайаута, индекс Руфье, итог
        self.mainLayout = QVBoxLayout()
        self.indexLabel = QLabel(index + " " + str(self.indexRuf))
        self.resultLabel = QLabel(result + " " + self.finalResult)

        #Добавление виджетов на лайаут
        self.mainLayout.addWidget(self.indexLabel, alignment = Qt.AlignCenter)
        self.mainLayout.addWidget(self.resultLabel, alignment = Qt.AlignCenter)

        #Позиционирование главного лайаута на экране
        self.setLayout(self.mainLayout)
