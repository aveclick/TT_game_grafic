import pickle
import sys
import json

from PyQt5.QtGui import QFont, QColor, QIcon
from PyQt5.QtWidgets import (QApplication, QPushButton, QMainWindow, QComboBox, QLabel, QLineEdit, QDialog, QSlider, )
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt, QSize
import random


# Основное окно
class Window2(QMainWindow):
    def __init__(self):
        super().__init__()

        # Создаем массив кнопок и устанавливаем переменную, которая меняет ход чел-ка на ход комп-ра
        self.buttons_list = []
        self.turn = 0
        global name
        global num_strok
        global num_stolbets
        global count_pobeda

        # Название окна
        self.setWindowTitle("Крестики-олики")

        # Переменные из словарей (задаются в окне настроек)
        # Имя из словаря имен, которое связано с переменными

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

        # Устанавливаем размер кнопок и окна
        self.cells_size = win_size
        self.setFixedSize(self.cells_size * num_stolbets, self.cells_size * num_strok + 40)

        self.label7 = QLabel('Идет игра', self)
        self.label7.move((self.cells_size * num_stolbets // 2) - (self.cells_size // 2),
                         self.cells_size * num_strok + 5)

        self.label7.setFont(QtGui.QFont('Comic Sans MS', 12))

        # кнопка новая игра
        self.pushButton = QPushButton(self)
        self.pushButton.setIcon(QIcon('replay.png'))
        self.pushButton.setIconSize(QSize(30, 30))
        self.pushButton.move((self.cells_size * num_stolbets - self.cells_size + 30),
                             self.cells_size * num_strok + 5)
        self.pushButton.setFont(QtGui.QFont('Comic Sans MS', 11))
        self.pushButton.setObjectName("pushButton")
        """self.pushButton.clicked.connect(self.save)
        self.pushButton.clicked.connect(self.Window2)"""

        # Вызываем основную функцию
        self.functions()
        # Показываем все компоненты
        self.show()

    # Основная функция
    def functions(self):

        # Создаем кнопки и добавляем их в массив
        for _ in range(num_strok):
            mas = []
            for _ in range(num_stolbets):
                mas.append((QPushButton(self)))
            self.buttons_list.append(mas)

        # Цикл, определяющий расположение кнопок
        y1 = 0
        side = self.cells_size
        x = 0
        y = 0
        j = 0
        i = 0
        for i in range(num_strok):
            self.buttons_list[i][j].setGeometry(QtCore.QRect(0, y, side, side))
            y += side
            for j in range(num_stolbets):
                self.buttons_list[i][j].setGeometry(QtCore.QRect(x, y1, side, side))
                x += side
                self.buttons_list[i][j].setFont(QFont(QFont('Times', 17)))
                self.buttons_list[i][j].clicked.connect(self.moves)

                if j == num_stolbets - 1:
                    x = 0
                    y1 += side
                else:
                    continue

        self.who_goes_first()

    # Блокирует все кнопки по оконччанию игры
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
                self.buttons_list[i][j].setStyleSheet('background: rgb(255, 255, 255);')
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
                button.setStyleSheet('background: rgb(204, 153, 255); color: black;')
            c = True
            while c:
                i = random.randint(0, num_strok - 1)
                j = random.randint(0, num_stolbets - 1)
                if self.buttons_list[i][j].text() == '':
                    button = self.buttons_list[i][j]
                    button.setEnabled(False)
                    button.setText(sign_of_computer)
                    button.setStyleSheet('background: rgb(204, 255, 255); color: black;')
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
            print('Поздравляю, Вы ходите первым!')
            sign_of_user = 'X'
            sign_of_computer = 'O'
        else:
            print('Первым выпал шанс ходить компьютеру')
            sign_of_user = 'O'
            sign_of_computer = 'X'
            self.buttons_list[1][1].setText('X')
            self.buttons_list[1][1].setStyleSheet('background: rgb(204, 255, 255); color: black;')
            self.buttons_list[1][1].setEnabled(False)

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
                        self.label7.move((self.cells_size * int(num_stolbets) // 2),
                                         self.cells_size * int(num_strok) + 5)
                        for n in win_mas:
                            n.setStyleSheet('background: rgb(0, 255, 0); color: black;')
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
                        self.label7.move((self.cells_size * int(num_stolbets) // 2),
                                         self.cells_size * int(num_strok) + 5)
                        for n in win_mas:
                            n.setStyleSheet('background: rgb(0, 255, 0); color: black;')
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
                                self.label7.move((self.cells_size * int(num_stolbets) // 2),
                                                 self.cells_size * int(num_strok) + 5)
                                for n in win_mas:
                                    n.setStyleSheet('background: rgb(0, 255, 0); color: black;')
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
                                self.label7.move((self.cells_size * int(num_stolbets) // 2),
                                                 self.cells_size * int(num_strok) + 5)
                                for n in win1_mas:
                                    n.setStyleSheet('background: rgb(0, 255, 0); color: black;')
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
                        self.label7.move((self.cells_size * int(num_stolbets) // 2 - (self.cells_size // 2)),
                                         self.cells_size * int(num_strok) + 5)
                        self.the_end()
                        return True
        return False


# Окно настроек
class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.num_strok = QComboBox(self)
        self.count_pobeda = QComboBox(self)
        self.num_stolbets = QComboBox(self)
        self.name = QLineEdit(self)
        self.wind = QComboBox(self)

        self.components()

        # Название окна, размеры
        self.title = "Настройки"
        self.setFixedSize(341, 341)
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Background, QColor('#CCFFFF'))
        self.setPalette(palette)
        # Иконка
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

        # Кнопка начала игры
        self.pushButton = QPushButton("Начать игру", self)
        self.pushButton.setGeometry(QtCore.QRect(110, 300, 101, 31))
        self.pushButton.setFont(QtGui.QFont('Comic Sans MS', 11))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.save)
        self.pushButton.clicked.connect(self.Window2)
        self.show()

    def changeValue(self, value):
        print(value)

    def components(self):
        global name
        global num_strok
        global num_stolbets
        global count_pobeda

        # Строка для ввода имени
        self.name.setGeometry(110, 60, 195, 31)
        self.name.setFont(QtGui.QFont('Comic Sans MS', 10))

        # combobox
        # wind
        comboMass1 = [50, 100, 150]
        self.wind.setGeometry(170, 110, 131, 21)
        self.wind.setFont(QtGui.QFont('Comic Sans MS', 10))
        for i in comboMass1:
            i = str(i)
            self.wind.addItem(i)

        # num_strok
        comboMass = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        self.num_strok.setGeometry(170, 160, 131, 21)
        self.num_strok.setFont(QtGui.QFont('Comic Sans MS', 10))
        for i in comboMass:
            i = str(i)
            self.num_strok.addItem(i)

        # num_stolbets
        self.num_stolbets.setGeometry(170, 210, 131, 21)
        self.num_stolbets.setFont(QtGui.QFont('Comic Sans MS', 10))
        for i in comboMass:
            i = str(i)
            self.num_stolbets.addItem(i)

        # count_pobeda
        comboMass1 = [3, 4, 5, 6, 7]
        self.count_pobeda.setGeometry(250, 260, 51, 21)
        self.count_pobeda.setFont(QtGui.QFont('Comic Sans MS', 10))
        for i in comboMass1:
            i = str(i)
            self.count_pobeda.addItem(i)

        # labels
        label1 = QLabel('Введите имя', self)
        label1.setGeometry(10, 60, 91, 31)
        label1.setFont(QtGui.QFont('Comic Sans MS', 10))

        label2 = QLabel('Расширение экрана', self)
        label2.setGeometry(10, 110, 121, 21)
        label2.setFont(QtGui.QFont('Comic Sans MS', 10))

        label3 = QLabel('Количество строк', self)
        label3.setGeometry(10, 160, 151, 21)
        label3.setFont(QtGui.QFont('Comic Sans MS', 10))

        label4 = QLabel('Количество столбцов', self)
        label4.setGeometry(10, 200, 231, 41)
        label4.setFont(QtGui.QFont('Comic Sans MS', 10))

        label5 = QLabel('Настройки', self)
        label5.setGeometry(120, 20, 111, 21)
        label5.setFont(QtGui.QFont('Comic Sans MS', 11))

        label6 = QLabel('Количество символов для победы', self)
        label6.setGeometry(10, 240, 311, 61)
        label6.setFont(QtGui.QFont('Comic Sans MS', 10))

    # Сохраняем переменные и их значения в словарь
    def save(self):
        global name
        name = self.name.text()
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

        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(name, f, ensure_ascii=False, indent=4)

    # Открываем главное окно
    def Window2(self):
        self.window = Window2()
        self.window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())
