import json

from PyQt5.QtGui import QFont, QIcon, QImage, QPalette, QBrush, QPixmap, QPen
from PyQt5.QtWidgets import (QPushButton, QMainWindow, QComboBox, QLabel, QLineEdit, QDialog, QMessageBox,
                             QStatusBar, QGridLayout, QSizePolicy)
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QSize

from PyQt5 import QtWidgets

import pickle
import random

from PyQt5.QtCore import (QPointF, QRectF, Qt)
from PyQt5.QtWidgets import (QApplication, QGraphicsView, QGraphicsScene, QGraphicsItem)
import sys


# Начальный экран
class WindowStart(QDialog):
    def __init__(self):
        super().__init__()
        self.state = 0
        # Название окна
        self.setWindowTitle("Крестики-олики")
        # Название окна, размеры
        self.title = "Крестики-олики"
        oImage = QImage("XO.png")
        sImage = oImage.scaled(QSize(689, 400))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

        # Иконка
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        vbox0 = QtWidgets.QVBoxLayout()

        # кнопки
        self.pushButton = QPushButton('Играть', self)
        self.pushButton.setFont(QtGui.QFont('Franklin Gothic Medium', 16))
        self.pushButton.setStyleSheet('background-color: rgb(192, 192, 192); color: rgb(0, 51, 51);')
        self.pushButton.setMinimumHeight(50)
        self.pushButton.setMinimumWidth(300)
        self.pushButton.clicked.connect(self.WindowEntry)
        self.pushButton.clicked.connect(self.Close)
        vbox0.addWidget(self.pushButton)

        self.pushButton = QPushButton('Сетевая игра', self)
        self.pushButton.setFont(QtGui.QFont('Franklin Gothic Medium', 16))
        self.pushButton.setStyleSheet('background-color: rgb(192, 192, 192); color: rgb(0, 51, 51);')
        self.pushButton.setMinimumHeight(50)
        self.pushButton.setMinimumWidth(300)
        vbox0.addWidget(self.pushButton)

        self.pushButton = QPushButton('Выход', self)
        self.pushButton.setFont(QtGui.QFont('Franklin Gothic Medium', 16))
        self.pushButton.setStyleSheet('background-color: rgb(192, 192, 192); color: rgb(0, 51, 51);')
        self.pushButton.setMinimumHeight(50)
        self.pushButton.setMinimumWidth(300)
        self.pushButton.clicked.connect(self.sys_exit)
        vbox0.addWidget(self.pushButton)

        self.setFixedSize(689, 400)
        vbox0.setAlignment(Qt.AlignCenter)
        vbox0.setSpacing(0)
        self.setLayout(vbox0)
        self.show()

    def WindowEntry(self):
        self.window = WindowEntry()
        self.window.show()

    def Close(self):
        self.hide()

    @staticmethod
    def sys_exit():
        sys.exit()


# Вход
class WindowEntry(QDialog):
    def __init__(self):
        super().__init__()
        # Название окна
        self.setWindowTitle("Крестики-олики")
        # Название окна, размеры
        self.title = "Крестики-олики"
        self.setFixedSize(400, 300)
        oImage = QImage("ground.png")
        sImage = oImage.scaled(QSize(689, 400))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)
        # Иконка
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

        hbox_1 = QtWidgets.QHBoxLayout()  # Введите имя
        hbox_2 = QtWidgets.QHBoxLayout()  # Поле ввода имени
        hbox_3 = QtWidgets.QHBoxLayout()  # Кнопка "Продолжить"

        vbox_1 = QtWidgets.QVBoxLayout()

        self.label_first = QLabel('Введите имя', self)
        self.label_first.setAlignment(Qt.AlignCenter)
        self.label_first.setFont(QtGui.QFont('Franklin Gothic Medium', 18))
        self.label_first.setStyleSheet('color: rgb(255, 255, 255);')
        hbox_1.addWidget(self.label_first)
        # Строка для ввода имени
        self.name = QLineEdit(self)
        self.name.resize(160, 100)
        self.name.setFont(QtGui.QFont('Franklin Gothic Medium', 17))
        hbox_2.addWidget(self.name)

        # кнопка
        self.pushButton = QPushButton("Продолжить", self)
        self.pushButton.resize(160, 100)
        self.pushButton.setFont(QtGui.QFont('Franklin Gothic Medium', 16))
        self.pushButton.setStyleSheet('background-color: rgb(192, 192, 192); color: rgb(0, 51, 51);')
        hbox_3.addWidget(self.pushButton)

        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.save_name)
        self.pushButton.clicked.connect(self.saved)
        self.pushButton.clicked.connect(self.Close)

        vbox_1.addLayout(hbox_1)
        vbox_1.addLayout(hbox_2)
        vbox_1.addLayout(hbox_3)

        vbox_1.setSpacing(100)
        self.setLayout(vbox_1)
        self.show()

    def save_name(self):
        name = self.name.text()
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(name, f, ensure_ascii=False, indent=4)

    def saved(self):
        with open('data.json', 'r', encoding='utf-8') as f:
            name = json.loads(f.read())
        with open("savegam", "rb") as f:
            num_strok_dict = pickle.load(f)
            if name in num_strok_dict:
                buttonReply = QMessageBox.question(self, 'PyQt5 message', "Хотите продолжить с сохраненного момента?",
                                                   QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if buttonReply == QMessageBox.Yes:
                    self.WindowDefault()
                else:
                    num_stolbets_dict = pickle.load(f)
                    count_pobeda_dict = pickle.load(f)
                    sign_of_user_dict = pickle.load(f)
                    sign_of_computer_dict = pickle.load(f)
                    button_list_dict = pickle.load(f)
                    win_size_dict = pickle.load(f)
                    first_dict = pickle.load(f)

                    del num_strok_dict[name]
                    del num_stolbets_dict[name]
                    del count_pobeda_dict[name]
                    del sign_of_user_dict[name]
                    del sign_of_computer_dict[name]
                    del button_list_dict[name]
                    del win_size_dict[name]
                    del first_dict[name]
                    with open("savegam", "wb") as f:
                        pickle.dump(num_strok_dict, f)
                        pickle.dump(num_stolbets_dict, f)
                        pickle.dump(count_pobeda_dict, f)
                        pickle.dump(sign_of_user_dict, f)
                        pickle.dump(sign_of_computer_dict, f)
                        pickle.dump(button_list_dict, f)
                        pickle.dump(win_size_dict, f)
                        pickle.dump(first_dict, f)
                    self.WindowMode()
            else:
                self.WindowMode()
                self.show()

    def WindowDefault(self):
        self.window = WindowDefault()
        self.window.show()

    def WindowMode(self):
        self.window = WindowMode()
        self.window.show()

    def Close(self):
        self.hide()


# Выбор режима игры
class WindowMode(QDialog):
    def __init__(self):
        super().__init__()
        self.state = 0
        # Название окна
        self.setWindowTitle("Крестки-олики")
        # Название окна, размеры
        self.title = "Крестки-олики"
        oImage = QImage("ground1.png")
        sImage = oImage.scaled(QSize(689, 400))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

        # Иконка
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

        grid = QGridLayout()

        self.label_first1 = QLabel('Выбор', self)
        self.label_first1.setStyleSheet('color: rgb(255, 255, 255);')
        self.label_first1.setFont(QtGui.QFont('Franklin Gothic Medium', 22))
        self.label_first1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.label_first1.setAlignment(Qt.AlignCenter)
        grid.addWidget(self.label_first1, 0, 2, alignment=Qt.AlignRight)

        self.label_first2 = QLabel('режима', self)
        self.label_first2.setStyleSheet('color: rgb(255, 255, 255);')
        self.label_first2.setFont(QtGui.QFont('Franklin Gothic Medium', 22))
        self.label_first2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.label_first2.setAlignment(Qt.AlignCenter)
        grid.addWidget(self.label_first2, 0, 3, alignment=Qt.AlignLeft)
        # кнопки
        self.pushButton = QPushButton(self)
        self.pushButton.setIcon(QIcon('графика.png'))
        self.pushButton.setIconSize(QSize(330, 330))
        self.pushButton.clicked.connect(self.save_2)
        self.pushButton.clicked.connect(self.save)
        self.pushButton.clicked.connect(self.WindowSettings)
        self.pushButton.clicked.connect(self.Close)
        self.pushButton.setFixedWidth(330)
        self.pushButton.setFixedHeight(316)
        grid.addWidget(self.pushButton, 1, 1, 1, 2)

        self.pushButton = QPushButton(self)
        self.pushButton.setIcon(QIcon('стандартный.png'))
        self.pushButton.setIconSize(QSize(330, 330))
        self.pushButton.clicked.connect(self.save_1)
        self.pushButton.clicked.connect(self.save)
        self.pushButton.clicked.connect(self.WindowSettings)
        self.pushButton.clicked.connect(self.Close)
        self.pushButton.setFixedWidth(330)
        self.pushButton.setFixedHeight(318)
        grid.addWidget(self.pushButton, 1, 3, 1, 4)

        self.setLayout(grid)

        self.setFixedSize(689, 400)
        self.show()
        # Открываем главное окно

    def save_1(self):
        self.state = 0

    def save_2(self):
        self.state = 1

    def save(self):
        state = self.state

        with open('data1.json', 'w', encoding='utf-8') as f:
            json.dump(state, f, ensure_ascii=False, indent=4)

    def WindowSettings(self):
        self.window = WindowSettings()
        self.window.show()

    def Close(self):
        self.hide()


# Окно настроек
class WindowSettings(QDialog):
    def __init__(self):
        super().__init__()
        global name
        with open('data.json', 'r', encoding='utf-8') as f:
            name = json.loads(f.read())
        with open('data1.json', 'r', encoding='utf-8') as f:
            state = json.loads(f.read())
        # Название окна
        self.setWindowTitle("Крестки-олики")
        self.num_strok = QComboBox(self)
        self.count_pobeda = QComboBox(self)
        self.num_stolbets = QComboBox(self)
        self.wind = QComboBox(self)

        # Название окна, размеры
        self.title = "Крестки-олики"
        self.setFixedSize(500, 335)
        oImage = QImage("ground.png")
        sImage = oImage.scaled(QSize(689, 400))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)
        # Иконка
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

        hbox00 = QtWidgets.QHBoxLayout()  # настройки
        hbox0 = QtWidgets.QHBoxLayout()  # расширение экрана и combobox
        hbox1 = QtWidgets.QHBoxLayout()  # кол-во строк и combobox
        hbox2 = QtWidgets.QHBoxLayout()  # кол-во столбцов и и combobox
        hbox3 = QtWidgets.QHBoxLayout()  # кол-во симв победы и и combobox
        hbox33 = QtWidgets.QHBoxLayout()  # кнопка

        vbox1 = QtWidgets.QVBoxLayout()

        # labels

        label0 = QLabel('Настройки', self)
        label0.setAlignment(Qt.AlignCenter)
        label0.setFont(QtGui.QFont('Franklin Gothic Medium', 17))
        label0.setStyleSheet('color: rgb(255, 255, 255);')
        hbox00.addWidget(label0)

        label2 = QLabel('Расширение экрана', self)
        label2.setFont(QtGui.QFont('Franklin Gothic Medium', 15))
        label2.setStyleSheet('color: rgb(255, 255, 255);')
        hbox0.addWidget(label2)

        label3 = QLabel('Количество строк', self)
        label3.setFont(QtGui.QFont('Franklin Gothic Medium', 15))
        label3.setStyleSheet('color: rgb(255, 255, 255);')
        hbox1.addWidget(label3)

        label4 = QLabel('Количество столбцов', self)
        label4.setFont(QtGui.QFont('Franklin Gothic Medium', 15))
        label4.setStyleSheet('color: rgb(255, 255, 255);')
        hbox2.addWidget(label4)

        label6 = QLabel('Количество символов для победы', self)
        label6.setFont(QtGui.QFont('Franklin Gothic Medium', 15))
        label6.setStyleSheet('color: rgb(255, 255, 255);')
        hbox3.addWidget(label6)

        # combobox
        # wind
        comboMass1 = [70, 100, 150]
        self.wind.setFont(QtGui.QFont('Franklin Gothic Medium', 10))
        self.wind.setMaximumHeight(23)
        self.wind.setMaximumWidth(80)
        hbox0.addWidget(self.wind)
        for i in comboMass1:
            i = str(i)
            self.wind.addItem(i)

        # num_strok
        comboMass = [3, 4, 5, 6]
        self.num_strok.setFont(QtGui.QFont('Franklin Gothic Medium', 10))
        self.num_strok.setMaximumHeight(23)
        self.num_strok.setMaximumWidth(80)
        hbox1.addWidget(self.num_strok)
        for i in comboMass:
            i = str(i)
            self.num_strok.addItem(i)

        # num_stolbets
        comboMass2 = [3, 4, 5, 6, 7, 8, 9, 10]
        self.num_stolbets.setFont(QtGui.QFont('Franklin Gothic Medium', 10))
        self.num_stolbets.setMaximumHeight(23)
        self.num_stolbets.setMaximumWidth(80)
        hbox2.addWidget(self.num_stolbets)
        for i in comboMass2:
            i = str(i)
            self.num_stolbets.addItem(i)

        # count_pobeda
        comboMass1 = [3, 4, 5, 6, 7]
        self.count_pobeda.setFont(QtGui.QFont('Franklin Gothic Medium', 10))
        self.count_pobeda.setMaximumHeight(23)
        self.count_pobeda.setMaximumWidth(80)
        hbox3.addWidget(self.count_pobeda)
        for i in comboMass1:
            i = str(i)
            self.count_pobeda.addItem(i)

        # Кнопка начала игры
        self.pushButton = QPushButton("Начать игру", self)
        self.pushButton.setGeometry(QtCore.QRect(110, 300, 101, 31))
        self.pushButton.setFont(QtGui.QFont('Franklin Gothic Medium', 14))
        self.pushButton.setStyleSheet('background-color: rgb(192, 192, 192); color: rgb(0, 51, 51);')
        self.pushButton.clicked.connect(self.save)
        if state == 0:
            self.pushButton.clicked.connect(self.WindowDefault)
        if state == 1:
            self.pushButton.clicked.connect(self.WindowGraphics)
        self.pushButton.clicked.connect(self.Close)
        hbox33.addWidget(self.pushButton)

        vbox1.addLayout(hbox00)
        vbox1.addLayout(hbox0)
        vbox1.addLayout(hbox1)
        vbox1.addLayout(hbox2)
        vbox1.addLayout(hbox3)
        vbox1.addLayout(hbox33)

        vbox1.setSpacing(30)
        vbox1.addStretch(1)
        self.setLayout(vbox1)
        self.show()

    # Сохраняем переменные и их значения в словарь
    def save(self):
        num_strok = self.num_strok.currentText()
        num_stolbets = self.num_stolbets.currentText()
        count_pobeda = self.count_pobeda.currentText()
        win_size = self.wind.currentText()

        with open("saveever", "rb") as f:
            num_strok_dict = pickle.load(f)
            num_stolbets_dict = pickle.load(f)
            count_pobeda_dict = pickle.load(f)
            win_size_dict = pickle.load(f)

        num_strok_dict.update({str(name): num_strok})
        num_stolbets_dict.update({str(name): num_stolbets})
        count_pobeda_dict.update({str(name): count_pobeda})
        win_size_dict.update({str(name): win_size})
        with open("saveever", "wb") as f:
            pickle.dump(num_strok_dict, f)
            pickle.dump(num_stolbets_dict, f)
            pickle.dump(count_pobeda_dict, f)
            pickle.dump(win_size_dict, f)

    # Открываем главное окно
    def WindowDefault(self):
        self.window = WindowDefault()
        self.window.show()

    def Close(self):
        self.hide()

    def WindowGraphics(self):
        self.window = WindowGraphics()
        self.window.show()


# Графика
class Graphics(QGraphicsItem):
    def __init__(self):
        super(Graphics, self).__init__()
        global name
        global num_strok
        global num_stolbets
        global count_pobeda
        global param_x
        global param_y
        global win_size
        with open('data.json', 'r', encoding='utf-8') as f:
            name = json.loads(f.read())
        with open("saveever", "rb") as f:
            num_strok_dict = pickle.load(f)
            if name in num_strok_dict:
                with open("saveever", "rb") as f:
                    num_strok_dict = pickle.load(f)
                    num_stolbets_dict = pickle.load(f)
                    count_pobeda_dict = pickle.load(f)
                    win_size_dict = pickle.load(f)
                    num_strok = num_strok_dict[str(name)]
                    num_stolbets = num_stolbets_dict[str(name)]
                    count_pobeda = count_pobeda_dict[str(name)]
                    win_size = win_size_dict[str(name)]

                    num_strok = int(num_strok)
                    num_stolbets = int(num_stolbets)
                    count_pobeda = int(count_pobeda)
                    win_size = int(win_size)
        param_x = win_size
        param_y = win_size
        self.board = [['' for j in range(num_stolbets)] for i in range(num_strok)]
        self.symbol_AI = 'O'
        self.symbol_Human = 'X'

    def reset(self):
        for y in range(num_strok):
            for x in range(num_stolbets):
                self.board[y][x] = ''

        self.update()

    def WindowStart(self):
        self.window = WindowStart()
        self.window.show()

    def select(self, x, y):
        k = 0
        if x < 0 or y < 0 or x >= num_stolbets or y >= num_strok:
            return
        if self.board[y][x] == '':
            self.board[y][x] = self.symbol_Human
            for j in range(num_strok):
                for i in range(num_stolbets):
                    if self.board[j][i] == '':
                        k = 1
                        break
        if k == 1:
            c = True
            while c:
                y = random.randint(0, num_strok - 1)
                x = random.randint(0, num_stolbets - 1)
                if self.board[y][x] == '':
                    self.board[y][x] = self.symbol_AI
                    c = False
                else:
                    continue

    def paint(self, painter, option, widget):  # рисуем при каждом нажатии мыши
        pen = QPen(Qt.lightGray, 2, Qt.SolidLine)
        painter.setPen(pen)
        # горизонтальные
        for j in range(0, win_size * num_strok + 1, win_size):
            painter.drawLine(0, j, win_size * num_stolbets, j)
            # вертикальные
        for i in range(0, win_size * num_stolbets + 1, win_size):
            painter.drawLine(i, 0, i, win_size * num_strok)
        for x in range(num_stolbets):
            for y in range(num_strok):
                if self.board[y][x] == self.symbol_Human:
                    pen = QPen(Qt.magenta, 2, Qt.SolidLine)
                    painter.setPen(pen)
                    painter.drawLine(x * param_x + 4, y * param_y + 4,
                                     int(param_x) - 4 + x * param_x,
                                     int(param_y) - 4 + y * param_y)
                    painter.drawLine(int(param_x) - 4 + x * param_x, y * param_y + 4,
                                     x * param_x + 4, int(param_y) - 4 + y * param_y)

                if self.who_wins('X'):
                    self.win()


                elif self.tie():
                    self.win_lose()

                if self.board[y][x] == self.symbol_AI:
                    pen = QPen(Qt.cyan, 2, Qt.SolidLine)
                    painter.setPen(pen)
                    painter.drawEllipse(
                        QPointF(int(param_x / 2) + x * param_x,
                                int(param_y / 2) + y * param_y),
                        int(param_x / 2) - 4, int(param_y / 2) - 4)
                if self.who_wins('O'):
                    self.lose()
                elif self.tie():
                    self.win_lose()

    def boundingRect(self):  # функция определяет внешние границы прямоугольника
        return QRectF(0, 0, win_size * num_stolbets,
                      win_size * num_strok)  # возвращает прямоугольник на плоскости

    def win(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowIcon(QtGui.QIcon('pic.png'))
        msg.setWindowTitle('Конец игры')
        msg.setText('Вы победили     ')
        msg.setFont(QtGui.QFont('Franklin Gothic Medium', 11))
        msg.setStyleSheet('background: rgb(144, 238, 144)')
        play = msg.addButton('Ок', QtWidgets.QMessageBox.AcceptRole)
        msg.setDefaultButton(play)
        msg.exec_()
        msg.deleteLater()
        if msg.clickedButton() is play:
            self.reset()

        self.show()

    def lose(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowIcon(QtGui.QIcon('pic.png'))
        msg.setWindowTitle('Конец игры')
        msg.setText('Вы проиграли     ')
        msg.setFont(QtGui.QFont('Franklin Gothic Medium', 11))
        msg.setStyleSheet('background: rgb(240, 128, 128)')
        play = msg.addButton('Ок', QtWidgets.QMessageBox.AcceptRole)
        msg.setDefaultButton(play)
        msg.exec_()
        msg.deleteLater()
        if msg.clickedButton() is play:
            self.reset()

        self.show()

    def win_lose(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowIcon(QtGui.QIcon('pic.png'))
        msg.setWindowTitle('Конец игры')
        msg.setText('Ничья     ')
        msg.setFont(QtGui.QFont('Franklin Gothic Medium', 11))
        msg.setStyleSheet('background: rgb(100, 149, 237)')
        play = msg.addButton('Ок', QtWidgets.QMessageBox.AcceptRole)
        msg.setDefaultButton(play)
        msg.exec_()
        msg.deleteLater()
        if msg.clickedButton() is play:
            self.reset()

        self.show()

    def mousePressEvent(self, event):
        pos = event.pos()
        self.select(int(pos.x() / param_x), int(pos.y() / param_y))
        self.update()
        super(Graphics, self).mousePressEvent(event)

    # проверка победы
    def who_wins(self, symbol):
        # проверка по столбцу
        for i in range(num_stolbets):
            win_mas = []
            count_symbol = 0
            for j in range(num_strok):
                if self.board[j][i] == symbol:
                    win_mas.append(self.board[j][i])
                    count_symbol += 1
                    if count_symbol == count_pobeda:
                        return True
                else:
                    count_symbol = 0

        # проверка по строке
        for j in range(num_strok):
            win_mas = []
            count_symbol = 0
            for i in range(num_stolbets):
                if self.board[j][i] == symbol:
                    win_mas.append(self.board[j][i])
                    count_symbol += 1
                    if count_symbol == count_pobeda:

                        return True
                else:
                    count_symbol = 0

        # главная диагональ
        win_mas = []
        win1_mas = []
        for line in range(num_strok - count_pobeda + 1):
            for k in range(num_stolbets - count_pobeda + 1):
                count_symbol1 = 0
                count_symbol2 = 0
                for j in range(num_strok - line):
                    if j + k == num_stolbets:
                        break
                    else:
                        if self.board[line + j][j + k] == symbol:
                            win_mas.append(self.board[line + j][j + k])
                            count_symbol1 += 1
                            if count_symbol1 == count_pobeda:
                                return True
                        else:
                            count_symbol1 = 0
                            win_mas = []
                        # побочная диагональ
                        if self.board[line + j][num_stolbets - j - k - 1] == symbol:
                            win1_mas.append(self.board[line + j][num_stolbets - j - k - 1])
                            count_symbol2 += 1
                            if count_symbol2 == count_pobeda:
                                return True
                        else:

                            count_symbol2 = 0
                            win1_mas = []
        return False

    # ничья
    def tie(self):
        count_symbol = 0
        count_tie = num_strok * num_stolbets
        for j in range(num_strok):
            for i in range(num_stolbets):
                if self.board[j][i] == 'X' or self.board[j][i] == 'O':
                    count_symbol += 1
                    if count_symbol == count_tie:
                        return True
        return False


class WindowGraphics(QGraphicsView):
    def __init__(self):
        super(WindowGraphics, self).__init__()
        scene = QGraphicsScene(self)
        self.tic_tac_toe = Graphics()

        scene.addItem(self.tic_tac_toe)
        scene.setSceneRect(0, 0, win_size * num_stolbets, win_size * num_strok)

        self.setFixedSize((win_size * num_stolbets + 100), (win_size * num_strok + 100))
        self.setBackgroundBrush(QBrush(QImage('ground.png')))
        self.setScene(scene)
        self.setCacheMode(QGraphicsView.CacheBackground)
        self.setWindowTitle("Крестики-олики")

        # Иконка
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

    def Close(self):
        self.hide()

    def keyPressEvent(self, event):
        key = event.key()  # ожидание нажатия клавиши на клавиатуре
        if key == Qt.Key_R:  # нажата клавиша R
            self.tic_tac_toe.reset()  # сброс ходов
        if key == Qt.Key_Escape:
            self.tic_tac_toe.WindowStart()
            self.Close()

        super(WindowGraphics, self).keyPressEvent(event)


# Основное окно
class WindowDefault(QMainWindow):
    def __init__(self):
        super().__init__()
        global name
        global num_strok
        global num_stolbets
        global count_pobeda
        global win_size
        global buttons_list
        global sign_of_user
        global sign_of_computer
        global first
        global button_list
        # Создаем массив кнопок и устанавливаем переменную, которая меняет ход чел-ка на ход комп-ра
        with open('data.json', 'r', encoding='utf-8') as f:
            name = json.loads(f.read())
        with open("savegam", "rb") as f:
            num_strok_dict = pickle.load(f)
            if name in num_strok_dict:
                # выгружаем переменные из словаря с сохраненными играми по имени
                with open("savegam", "rb") as f:
                    num_strok_dict = pickle.load(f)
                    num_stolbets_dict = pickle.load(f)
                    count_pobeda_dict = pickle.load(f)
                    sign_of_user_dict = pickle.load(f)
                    sign_of_computer_dict = pickle.load(f)
                    buttons_list_dict = pickle.load(f)
                    win_size_dict = pickle.load(f)
                    first_dict = pickle.load(f)
                    num_strok = num_strok_dict[str(name)]
                    num_stolbets = num_stolbets_dict[str(name)]
                    count_pobeda = count_pobeda_dict[str(name)]
                    sign_of_user = sign_of_user_dict[str(name)]
                    sign_of_computer = sign_of_computer_dict[str(name)]
                    buttons_list = buttons_list_dict[str(name)]
                    win_size = win_size_dict[str(name)]
                    first = first_dict[str(name)]

                self.turn = 0
                self.buttons_list = []

                # Название окна
                self.setWindowTitle("Крестики-олики")
                # Иконка
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("pic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.setWindowIcon(icon)

                # menu bar
                bar = self.menuBar()
                self.setMenuBar(bar)
                file_menu = bar.addMenu('Игра')
                new_action = QtWidgets.QAction('Новая игра', self)

                exit_action = QtWidgets.QAction('Выйти', self)
                file_menu.addAction(new_action)

                file_menu.addAction(exit_action)
                new_action.triggered.connect(self.new_game)

                exit_action.triggered.connect(self.exit)

                # status bar
                self.statusBar = QStatusBar()
                self.setStatusBar(self.statusBar)
                self.statusBar.showMessage('...')
                self.statusBar.setStyleSheet('background-color: pink')

                # Устанавливаем размер кнопок и окна
                self.cells_size = win_size
                self.setFixedSize(self.cells_size * num_stolbets, self.cells_size * num_strok + 80)
                self.label7 = QLabel('Идет игра', self)
                # кнопка новая игра
                self.pushButton = QPushButton(self)
                self.pushButton.setIcon(QIcon('replay.png'))
                self.pushButton.setIconSize(QSize(30, 30))
                self.pushButton.resize(40, 30)
                self.pushButton.move((self.cells_size * num_stolbets - self.cells_size),
                                     self.cells_size * num_strok + 25)
                self.pushButton.clicked.connect(self.new_game)
                self.change_size()

                # Вызываем основную функцию
                self.functions2()
                # Показываем все компоненты
                self.show()
            else:
                with open("saveever", "rb") as f:
                    num_strok_dict = pickle.load(f)
                    if name in num_strok_dict:
                        with open("saveever", "rb") as f:
                            num_strok_dict = pickle.load(f)
                            num_stolbets_dict = pickle.load(f)
                            count_pobeda_dict = pickle.load(f)
                            win_size_dict = pickle.load(f)
                            num_strok = num_strok_dict[str(name)]
                            num_stolbets = num_stolbets_dict[str(name)]
                            count_pobeda = count_pobeda_dict[str(name)]
                            win_size = win_size_dict[str(name)]

                            num_strok = int(num_strok)
                            num_stolbets = int(num_stolbets)
                            count_pobeda = int(count_pobeda)
                            win_size = int(win_size)

                self.buttons_list = []
                self.turn = 0
                # Название окна
                self.setWindowTitle("Крестики-олики")
                # Иконка
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("pic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.setWindowIcon(icon)

                # menu bar
                bar = self.menuBar()
                self.setMenuBar(bar)
                file_menu = bar.addMenu('Игра')
                new_action = QtWidgets.QAction('Новая игра', self)
                new_action.setStatusTip('Начать новую игру')
                new_action.triggered.connect(self.process)

                exit_action = QtWidgets.QAction('Выйти', self)
                exit_action.setStatusTip('Выйти из игры')
                exit_action.triggered.connect(self.process)
                file_menu.addAction(new_action)

                file_menu.addAction(exit_action)
                new_action.triggered.connect(self.new_game)


                exit_action.triggered.connect(self.exit)
                exit_action.triggered.connect(self.Close)

                # status bar
                self.statusBar = QStatusBar()
                self.setStatusBar(self.statusBar)
                self.statusBar.showMessage('...')
                self.statusBar.setStyleSheet('background-color: rgb(36, 58, 84)')

                # Устанавливаем размер кнопок и окна
                self.cells_size = win_size
                self.setFixedSize(self.cells_size * num_stolbets, self.cells_size * num_strok + 80)
                self.label7 = QLabel('Идет игра', self)
                # кнопка новая игра
                self.pushButton = QPushButton(self)
                self.pushButton.setIcon(QIcon('replay.png'))
                self.pushButton.setIconSize(QSize(30, 30))
                self.pushButton.resize(40, 30)
                self.pushButton.move((self.cells_size * num_stolbets - self.cells_size),
                                     self.cells_size * num_strok + 25)
                self.pushButton.clicked.connect(self.new_game)
                self.change_size()

                # Вызываем основную функцию
                self.functions()
                # Показываем все компоненты
                self.show()

    def Close(self):
        self.hide()

    def change_size(self):
        # смена шрифта и расположения QLabel в зависимости от размера окна
        if win_size == 70:
            self.label7.move((self.cells_size * num_stolbets // 2 + 20) - self.cells_size,
                             self.cells_size * num_strok + 25)
            self.label7.setFont(QtGui.QFont('Franklin Gothic Medium', 12))
            self.pushButton.move((self.cells_size * num_stolbets - self.cells_size + 10),
                                 self.cells_size * num_strok + 25)

        if win_size == 100:
            self.label7.move((self.cells_size * num_stolbets // 2) - (self.cells_size // 2),
                             self.cells_size * num_strok + 25)
            self.label7.setFont(QtGui.QFont('Franklin Gothic Medium', 13))
            self.pushButton.move((self.cells_size * num_stolbets - self.cells_size + 30),
                                 self.cells_size * num_strok + 25)

        if win_size == 150:
            self.label7.move(self.cells_size * num_stolbets // 2 - 50,
                             self.cells_size * num_strok + 25)
            self.label7.setFont(QtGui.QFont('Franklin Gothic Medium', 14))
            self.pushButton.move((self.cells_size * num_stolbets - self.cells_size + 60),
                                 self.cells_size * num_strok + 25)

    def process(self, state):
        if state:
            self.statusBar.show()
        else:
            self.statusBar.hide()

    # Основная функция
    def functions(self):
        # Создаем кнопки и добавляем их в массив
        for _ in range(num_strok):
            mas = []
            for _ in range(num_stolbets):
                mas.append((QPushButton(self)))
            self.buttons_list.append(mas)

        # Цикл, определяющий расположение кнопок
        y1 = 25
        side = self.cells_size
        x = 0
        y = 25
        j = 0
        i = 0
        for i in range(num_strok):
            self.buttons_list[i][j].setGeometry(QtCore.QRect(0, y, side, side))
            y += side
            for j in range(num_stolbets):
                self.buttons_list[i][j].setGeometry(QtCore.QRect(x, y1, side, side))
                x += side
                self.buttons_list[i][j].setFont(QFont(QFont('Franklin Gothic Medium', 17)))
                self.buttons_list[i][j].setStyleSheet('background: rgb(36, 58, 84);')
                self.buttons_list[i][j].clicked.connect(self.moves)

                if j == num_stolbets - 1:
                    x = 0
                    y1 += side
                else:
                    continue

        self.who_goes_first()

    # Основная функция
    def functions2(self):
        # Создаем кнопки и добавляем их в массив
        for _ in range(num_strok):
            mas = []
            for _ in range(num_stolbets):
                mas.append((QPushButton(self)))
            self.buttons_list.append(mas)

        k = 0
        for i in range(num_strok):
            for j in range(num_stolbets):
                self.buttons_list[i][j].setText(buttons_list[k])
                k += 1

        # Цикл, определяющий расположение кнопок
        y1 = 25
        side = self.cells_size
        x = 0
        y = 25
        j = 0
        i = 0
        for i in range(num_strok):
            self.buttons_list[i][j].setGeometry(QtCore.QRect(0, y, side, side))
            y += side
            for j in range(num_stolbets):
                self.buttons_list[i][j].setGeometry(QtCore.QRect(x, y1, side, side))
                x += side
                self.buttons_list[i][j].setFont(QFont(QFont('Franklin Gothic Medium', 17)))
                self.buttons_list[i][j].setStyleSheet('background: rgb(36, 58, 84);')
                self.buttons_list[i][j].clicked.connect(self.moves)

                if j == num_stolbets - 1:
                    x = 0
                    y1 += side
                else:
                    continue



    def new_game(self):
        for i in range(num_strok):
            for j in range(num_stolbets):
                self.buttons_list[i][j].setText('')
                self.buttons_list[i][j].setEnabled(True)
                self.buttons_list[i][j].setStyleSheet('background: rgb(36, 58, 84);')
                self.label7.setText('Идет игра')
                self.change_size()
                self.statusBar.show()
        self.who_goes_first()

    # Блокирует все кнопки по окончание игры
    def the_end(self):
        for i in range(num_strok):
            for j in range(num_stolbets):
                self.buttons_list[i][j].setEnabled(False)

    def moves(self):
        # Объединяет кнопки
        button = self.sender()
        # Блокирует кнопку
        button.setEnabled(False)

        # Ход чел-ка и комп-ра

        # Человек
        for i in range(num_strok):
            for j in range(num_stolbets):
                self.buttons_list[i][j].setStyleSheet('background: rgb(36, 58, 84);')
        if self.turn == 0:
            button.setText(sign_of_user)

            k = 0
            for i in range(num_strok):
                for j in range(num_stolbets):
                    if self.buttons_list[i][j].text() == 'X' or self.buttons_list[i][j].text() == 'O':
                        k += 1
            if k != num_strok * num_stolbets:
                if not self.who_wins(sign_of_user):
                    self.turn = 1
            else:
                if not self.who_wins(sign_of_user):
                    self.tie()

        # Компьютер
        if self.turn == 1:
            if button.text() == sign_of_user:
                button.setStyleSheet('background: rgb(36, 58, 84); color: cyan;')
            c = True
            while c:
                i = random.randint(0, num_strok - 1)
                j = random.randint(0, num_stolbets - 1)
                if self.buttons_list[i][j].text() == '':
                    button = self.buttons_list[i][j]
                    button.setEnabled(False)
                    button.setText(sign_of_computer)

                    button.setStyleSheet('background: rgb(36, 58, 84); color: magenta;')
                    self.turn = 0
                    c = False
                else:
                    continue
            if not self.who_wins(sign_of_computer):
                self.tie()

    def who_goes_first(self):
        global sign_of_user
        global sign_of_computer
        global first
        sign_of_user = ''
        sign_of_computer = ''
        """Выбор первого хода, 0 - человек, 1 -компьютер"""
        first = random.randint(0, 1)
        if first == 0:
            sign_of_user = 'X'
            sign_of_computer = 'O'
        else:
            sign_of_user = 'O'
            sign_of_computer = 'X'
            self.buttons_list[1][1].setText('X')
            self.buttons_list[1][1].setStyleSheet('background: rgb(36, 58, 84); color: magenta;')
            self.buttons_list[1][1].setEnabled(False)

    def exit(self):
        buttonReply = QMessageBox.question(self, 'PyQt5 message', "Сохранить игру?",
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            self.save()
            self.WindowStart()
        else:
            self.WindowStart()
        self.show()

    def WindowStart(self):
        self.window = WindowStart()
        self.window.show()

    @staticmethod
    def sys_exit():
        sys.exit()

    def save(self):
        buttons_list = []
        for i in range(num_strok):
            for j in range(num_stolbets):
                buttons_list.append(self.buttons_list[i][j].text())
        with open("savegam", "rb") as f:
            num_strok_dict = pickle.load(f)
            num_stolbets_dict = pickle.load(f)
            count_pobeda_dict = pickle.load(f)
            sign_of_user_dict = pickle.load(f)
            sign_of_computer_dict = pickle.load(f)
            buttons_list_dict = pickle.load(f)
            win_size_dict = pickle.load(f)
            first_dict = pickle.load(f)

        num_strok_dict.update({str(name): num_strok})
        num_stolbets_dict.update({str(name): num_stolbets})
        count_pobeda_dict.update({str(name): count_pobeda})
        sign_of_user_dict.update({str(name): sign_of_user})
        sign_of_computer_dict.update({str(name): sign_of_computer})
        buttons_list_dict.update({str(name): buttons_list})
        win_size_dict.update({str(name): win_size})
        first_dict.update({str(name): first})
        with open("savegam", "wb") as f:
            pickle.dump(num_strok_dict, f)
            pickle.dump(num_stolbets_dict, f)
            pickle.dump(count_pobeda_dict, f)
            pickle.dump(sign_of_user_dict, f)
            pickle.dump(sign_of_computer_dict, f)
            pickle.dump(buttons_list_dict, f)
            pickle.dump(win_size_dict, f)
            pickle.dump(first_dict, f)

    # проверка победы
    def who_wins(self, symbol):
        # проверка по столбцу
        for j in range(num_stolbets):
            win_mas = []
            count_symbol = 0
            for i in range(num_strok):
                if self.buttons_list[i][j].text() == symbol:
                    win_mas.append(self.buttons_list[i][j])
                    count_symbol += 1
                    if count_symbol == count_pobeda:
                        self.label7.setText(symbol)
                        self.label7.setFont(QtGui.QFont('Franklin Gothic Medium', 13))
                        self.label7.move((self.cells_size * int(num_stolbets) // 2),
                                         self.cells_size * int(num_strok) + 25)
                        for n in win_mas:
                            n.setStyleSheet('background: rgb(255, 164, 32); color: black;')
                        self.the_end()

                        return True

                else:
                    count_symbol = 0

        # проверка по строке
        for i in range(num_strok):
            win_mas = []
            count_symbol = 0
            for j in range(num_stolbets):
                if self.buttons_list[i][j].text() == symbol:
                    win_mas.append(self.buttons_list[i][j])
                    count_symbol += 1
                    if count_symbol == count_pobeda:

                        self.label7.setText(symbol)
                        self.label7.setFont(QtGui.QFont('Franklin Gothic Medium', 13))
                        self.label7.move((self.cells_size * int(num_stolbets) // 2),
                                         self.cells_size * int(num_strok) + 25)
                        for n in win_mas:
                            n.setStyleSheet('background: rgb(255, 164, 32); color: black;')
                        self.the_end()
                        return True
                else:
                    count_symbol = 0

        # главная диагональ
        win_mas = []
        win1_mas = []
        for line in range(num_strok - count_pobeda + 1):
            for k in range(num_stolbets - count_pobeda + 1):
                count_symbol1 = 0
                count_symbol2 = 0
                for i in range(num_strok - line):
                    if i + k == num_stolbets:
                        break
                    else:
                        if self.buttons_list[line + i][i + k].text() == symbol:
                            win_mas.append(self.buttons_list[line + i][i + k])
                            count_symbol1 += 1
                            if count_symbol1 == count_pobeda:
                                self.label7.setText(symbol)
                                self.label7.setFont(QtGui.QFont('Franklin Gothic Medium', 13))
                                self.label7.move((self.cells_size * int(num_stolbets) // 2),
                                                 self.cells_size * int(num_strok) + 25)
                                for n in win_mas:
                                    n.setStyleSheet('background: rgb(255, 164, 32); color: black;')
                                self.the_end()
                                return True
                        else:
                            count_symbol1 = 0
                            win_mas = []
                        # побочная диагональ

                        if self.buttons_list[line + i][num_stolbets - i - k - 1].text() == symbol:
                            win1_mas.append(self.buttons_list[line + i][num_stolbets - i - k - 1])
                            count_symbol2 += 1
                            if count_symbol2 == count_pobeda:
                                self.label7.setText(symbol)
                                self.label7.setFont(QtGui.QFont('Franklin Gothic Medium', 13))
                                self.label7.move((self.cells_size * int(num_stolbets) // 2),
                                                 self.cells_size * int(num_strok) + 25)
                                for n in win1_mas:
                                    n.setStyleSheet('background: rgb(255, 164, 32); color: black;')
                                self.the_end()
                                return True
                        else:
                            count_symbol2 = 0
                            win1_mas = []
        return False

    # ничья
    def tie(self):
        count_symbol = 0
        count_tie = num_strok * num_stolbets
        for i in range(num_strok):
            for j in range(num_stolbets):
                if self.buttons_list[i][j].text() == 'X' or self.buttons_list[i][j].text() == 'O':
                    count_symbol += 1
                    if count_symbol == count_tie:
                        self.label7.setText('Ничья')
                        self.label7.setFont(QtGui.QFont('Franklin Gothic Medium', 13))
                        self.label7.move((self.cells_size * int(num_stolbets) // 2 - (self.cells_size // 2)),
                                         self.cells_size * int(num_strok) + 25)
                        self.the_end()
                        return True
        return False


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WindowStart()
    sys.exit(app.exec())
