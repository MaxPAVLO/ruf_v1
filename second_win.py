from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout
from instr import *
app = QApplication([])

class TestWin(QWidget):
    def set_appear(self):
        #Заголовок, место и размеры окна
        self.setWindowTitle("Тест Руфье")
        self.move(0, 0)

    def initUI(self):
        #Имя пользователя
        self.SurNameLabel = QLabel(surname)
        self.SurNameInput = QLineEdit()

        #Возраст пользователя
        self.userYearsLabel = QLabel(years)
        self.userYearsInput = QLineEdit()

        #Первая часть теста
        self.instructionFirstLabel = QLabel(InstructionFirst)
        self.firstButton = QPushButton(FirstButtonText)
        self.firstTaskInput = QLineEdit()

        #Вторая часть теста
        self.instructionSecondLabel = QLabel(InstructionSecond)
        self.secondButton = QPushButton(SecondBttonText)

        #Третья часть теста
        self.instructionThirdLabel = QLabel(InstructionThird)
        self.thirdButton = QPushButton(ThirdButtonText)
        self.thirdTaskInput1 = QLineEdit()
        self.thirdTaskInput2 - QLineEdit()

        self.sendButton = QPushButton()

        #Главный лайаут
        self.mainLayout = QHBoxLayout()

        #Первый лайаут
        self.firstLayout = QVBoxLayout()

        #Второй лайаут
        self.secondLayout = QVBoxLayout()

        #Добавление второстепенных лайаутов на главный
        self.mainLayout.addLayout(self.firstLayout)
        self.mainLayout.addLayout(self.secondLayout)

        #Добавление виджетов на первый лайаут

        self.firstLayout.addWidget(self.SurNameLabel, alignment = Qt.AlignLeft)
        self.firstLayout.addWidget(self.SurNameInput, alignment = Qt.AlignLeft)

        self.firstLayout.addWidget(self.userYearsLabel, alignment = Qt.AlignLeft)
        self.firstLayout.addWidget(self.userYearsInput, alignment = Qt.AlignLeft)

        self.firstLayout.addWidget(self.instructionFirstLabel, alignment = Qt.AlignLeft)
        self.firstLayout.addWidget(self.firstButton, alignment = Qt.AlignLeft)
        self.firstLayout.addWidget(self.firstTaskInput, alignment = Qt.AlignLeft)

        self.firstLayout.addWidget(self.instructionSecondLabel, alignment = Qt.AlignLeft)
        self.firstLayout.addWidget(self.secondButton, alignment = Qt.AlignLeft)

        self.firstLayout.addWidget(self.instructionThirdLabel, alignment = Qt.AlignLeft)
        self.firstLayout.addWidget(self.thirdButton, alignment = Qt.AlignLeft)
        self.firstLayout.addWidget(self.thirdTaskInput1, alignment = Qt.AlignLeft)
        self.firstLayout.addWidget(self.thirdTaskInput2, alignment = Qt.AlignLeft)

        self.firstLayout.addWidget(self.sendButton, alignment = Qt.AlignCenter)

        #Создание таймера
        self.timer = QLabel(timerText)

        #Добавление виджетов на второй лайаут
        self.secondLayout.addWidget(self.timer, alignment = Qt.AlignCenter)


    def connects(self):
        self.sendButton.clicked.connect(self.next_click)

    def next_click(self):
        self.hide()
        self.fw = FinalWin() 

    def __init__(self):
        super().__init__()
        self.set_apper()
        self.initUI()
        self.connects()
        self.show()

app.exec_()