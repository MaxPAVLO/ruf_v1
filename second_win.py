from PyQt5.QtCore import Qt, QTime, QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QFont
from instr import *
from final_win import FinalWin

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def set_appear(self):
        #Заголовок, место и размеры окна
        self.resize(win_width, win_height)
        self.setWindowTitle(title_txt)
        self.move(win_x, win_y)

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
        self.thirdTaskInput2 = QLineEdit()

        self.sendButton = QPushButton(sendButtonText)

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
        self.timer.setFont(QFont("Times", 36, QFont.Bold))

        #Добавление виджетов на второй лайаут
        self.secondLayout.addWidget(self.timer, alignment = Qt.AlignCenter)

        #Позиционирование главного лайаута на экране
        self.setLayout(self.mainLayout)

    def connects(self):
        self.sendButton.clicked.connect(self.next_click)
        self.firstButton.clicked.connect(self.timerTest1)
        self.secondButton.clicked.connect(self.timerTest2)
        self.thirdButton.clicked.connect(self.timerTest3)

    def timerTest1(self):
        global Time
        Time = QTime(0, 0, 15)
        self.Timer = QTimer()
        self.Timer.timeout.connect(self.timer1Event)
        self.Timer.start(1000)

    def timerTest2(self):
        global Time
        Time = QTime(0, 0, 30)
        self.timer.setText("30")
        self.Timer.timeout.connect(self.timer2Event)
        self.Timer.start(1500)

    def timerTest3(self):
        global Time
        Time = QTime(0, 1, 0)
        self.Timer.timeout.connect(self.timer3Event)

    def timer1Event(self):
        global Time
        Time = Time.addSecs(-1)
        self.timer.setText(Time.toString("hh:mm:ss"))

        if Time.toString("hh:mm:ss") == "00:00:00":
            self.Timer.stop()

    def timer2Event(self):
        global Time
        Time = Time.addSecs(-1)
        self.timer.setText(Time.toString("00:00:00")[6:])

        if Time.toString("hh:mm:ss")[6:] == "00":
            self.Timer.stop()

    def timer3Event(self):
        pass

    def next_click(self):
        self.hide()
        self.fw = FinalWin()
