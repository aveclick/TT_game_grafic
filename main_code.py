import pickle
import sys
import json

from PyQt5.QtGui import QFont, QColor, QIcon
from PyQt5.QtWidgets import (QApplication, QPushButton, QMainWindow, QComboBox, QLabel, QLineEdit, QDialog, QMessageBox)
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt, QSize
import random
from PyQt5 import QtWidgets

# Основное окно
class Window2(QMainWindow):
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
                    button_list_dict = pickle.load(f)
                    win_size_dict = pickle.load(f)
                    first_dict = pickle.load(f)
                    num_strok = num_strok_dict[str(name)]
                    num_stolbets = num_stolbets_dict[str(name)]
                    count_pobeda = count_pobeda_dict[str(name)]
                    sign_of_user = sign_of_user_dict[str(name)]
                    sign_of_computer = sign_of_computer_dict[str(name)]
                    button_list = button_list_dict[str(name)]
                    win_size = win_size_dict[str(name)]
                    first = first_dict[str(name)]

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
                save_action = QtWidgets.QAction('Сохранить', self)
                exit_action = QtWidgets.QAction('Выйти', self)
                file_menu.addAction(new_action)
                file_menu.addAction(save_action)
                file_menu.addAction(exit_action)
                new_action.triggered.connect(self.new_game)
                save_action.triggered.connect(self.save)
                exit_action.triggered.connect(self.exit)
                # Устанавливаем размер кнопок и окна
                self.cells_size = win_size
                self.setFixedSize(self.cells_size * num_stolbets, self.cells_size * num_strok + 60)
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
                save_action = QtWidgets.QAction('Сохранить', self)
                exit_action = QtWidgets.QAction('Выйти', self)
                file_menu.addAction(new_action)
                file_menu.addAction(save_action)
                file_menu.addAction(exit_action)
                new_action.triggered.connect(self.new_game)
                save_action.triggered.connect(self.save)
                exit_action.triggered.connect(self.exit)
                # Устанавливаем размер кнопок и окна
                self.cells_size = win_size
                self.setFixedSize(self.cells_size * num_stolbets, self.cells_size * num_strok + 60)
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

    def change_size(self):
        # смена шрифта и расположения QLabel в зависимости от размера окна
        if win_size == 50:
            self.label7.move((self.cells_size * num_stolbets // 2) - self.cells_size,
                             self.cells_size * num_strok + 25)
            self.label7.setFont(QtGui.QFont('Comic Sans MS', 10))

        if win_size == 100:
            self.label7.move((self.cells_size * num_stolbets // 2) - (self.cells_size // 2),
                             self.cells_size * num_strok + 25)
            self.label7.setFont(QtGui.QFont('Comic Sans MS', 12))
            self.pushButton.move((self.cells_size * num_stolbets - self.cells_size + 30),
                                 self.cells_size * num_strok + 25)

        if win_size == 150:
            self.label7.move(self.cells_size * num_stolbets // 2 - 50,
                             self.cells_size * num_strok + 25)
            self.label7.setFont(QtGui.QFont('Comic Sans MS', 14))

    # Основная функция
    def functions(self):

        # Создаем кнопки и добавляем их в массив
        for _ in range(num_strok):
            mas = []
            for _ in range(num_stolbets):
                mas.append((QPushButton(self)))
            self.buttons_list.append(mas)

        # Цикл, определяющий расположение кнопок
        y1 = 20
        side = self.cells_size
        x = 0
        y = 20
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
                self.buttons_list[i][j].setText(button_list[k])
                k += 1

            # Цикл, определяющий расположение кнопок
        y1 = 20
        side = self.cells_size
        x = 0
        y = 20
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

    def new_game(self):
        for i in range(num_strok):
            for j in range(num_stolbets):
                self.buttons_list[i][j].setText('')
                self.buttons_list[i][j].setEnabled(True)
                self.buttons_list[i][j].setStyleSheet('background: rgb(255, 255, 255);')
                self.label7.setText('Идет игра')
                self.change_size()
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
            sign_of_user = 'X'
            sign_of_computer = 'O'
        else:
            sign_of_user = 'O'
            sign_of_computer = 'X'
            self.buttons_list[1][1].setText('X')
            self.buttons_list[1][1].setStyleSheet('background: rgb(204, 255, 255); color: black;')
            self.buttons_list[1][1].setEnabled(False)

    def exit(self):
        buttonReply = QMessageBox.question(self, 'PyQt5 message', "Вы уверены, что хотите выйти?",
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            sys.exit()
        else:
            pass
        self.show()

    def save(self):
        buttons_list = []
        for i in range(num_strok):
            for j in range(num_stolbets):
                buttons_list.append(self.buttons_list[i][j].text())
        print(buttons_list)
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
                        self.label7.setFont(QtGui.QFont('Comic Sans MS', 13))
                        self.label7.move((self.cells_size * int(num_stolbets) // 2),
                                         self.cells_size * int(num_strok) + 25)
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
                        self.label7.setFont(QtGui.QFont('Comic Sans MS', 13))
                        self.label7.move((self.cells_size * int(num_stolbets) // 2),
                                         self.cells_size * int(num_strok) + 25)
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
                                self.label7.setFont(QtGui.QFont('Comic Sans MS', 13))
                                self.label7.move((self.cells_size * int(num_stolbets) // 2),
                                                 self.cells_size * int(num_strok) + 25)
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
                                self.label7.setFont(QtGui.QFont('Comic Sans MS', 13))
                                self.label7.move((self.cells_size * int(num_stolbets) // 2),
                                                 self.cells_size * int(num_strok) + 25)
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
                        self.label7.setFont(QtGui.QFont('Comic Sans MS', 13))
                        self.label7.move((self.cells_size * int(num_stolbets) // 2 - (self.cells_size // 2)),
                                         self.cells_size * int(num_strok) + 25)
                        self.the_end()
                        return True
        return False


# Окно настроек
class Window(QDialog):
    def __init__(self):
        super().__init__()
        global name
        with open('data.json', 'r', encoding='utf-8') as f:
            name = json.loads(f.read())
        # Название окна
        self.setWindowTitle("Настройки")
        self.num_strok = QComboBox(self)
        self.count_pobeda = QComboBox(self)
        self.num_stolbets = QComboBox(self)
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
        self.pushButton.clicked.connect(self.Close)
        self.show()

    def components(self):

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
    def Window2(self):
        self.window = Window2()
        self.window.show()

    def Close(self):
        self.hide()

# Главное меню
class Window3(QDialog):
    def __init__(self):
        super().__init__()
        # Название окна
        self.setWindowTitle("Главное меню")
        # Название окна, размеры
        self.title = "Главное меню"
        self.setFixedSize(341, 341)
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Background, QColor('#D8BFD8'))
        self.setPalette(palette)
        # Иконка
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

        self.label_first = QLabel('Начать игру', self)
        self.label_first.move(120, 70)
        self.label_first.setFont(QtGui.QFont('Comic Sans MS', 13))

        # кнопки
        self.pushButton = QPushButton("Графический режим", self)
        self.pushButton.setGeometry(QtCore.QRect(10, 120, 101, 31))
        self.pushButton.resize(160, 31)
        self.pushButton.setFont(QtGui.QFont('Comic Sans MS', 11))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.Window)
        self.pushButton.clicked.connect(self.Close)


        self.pushButton = QPushButton("Стандартный режим", self)
        self.pushButton.setGeometry(QtCore.QRect(170, 120, 101, 31))
        self.pushButton.resize(160, 31)
        self.pushButton.setFont(QtGui.QFont('Comic Sans MS', 11))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.Window)
        self.pushButton.clicked.connect(self.Close)
        self.show()
        # Открываем главное окно

    def Window(self):
        self.window = Window()
        self.window.show()

    def Close(self):
        self.hide()

class Window4(QDialog):
    def __init__(self):
        super().__init__()
        # Название окна
        self.setWindowTitle("Главное меню")
        # Название окна, размеры
        self.title = "Главное меню"
        self.setFixedSize(341, 341)
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Background, QColor('#D8BFD8'))
        self.setPalette(palette)
        # Иконка
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

        self.label_first = QLabel('Введите имя', self)
        self.label_first.move(10, 65)
        self.label_first.setFont(QtGui.QFont('Comic Sans MS', 11))
        # Строка для ввода имени
        self.name = QLineEdit(self)
        self.name.setGeometry(110, 60, 195, 31)
        self.name.setFont(QtGui.QFont('Comic Sans MS', 10))
        # кнопки
        self.pushButton = QPushButton("Продолжить", self)
        self.pushButton.setGeometry(QtCore.QRect(10, 120, 101, 31))
        self.pushButton.resize(160, 31)
        self.pushButton.setFont(QtGui.QFont('Comic Sans MS', 11))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.save_name)
        self.pushButton.clicked.connect(self.saved)
        self.pushButton.clicked.connect(self.Close)
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
                    self.Window2()
                else:
                    num_stolbets_dict = pickle.load(f)
                    count_pobeda_dict = pickle.load(f)
                    up_me_dict = pickle.load(f)
                    sign_of_user_dict = pickle.load(f)
                    sign_of_computer_dict = pickle.load(f)
                    button_list_dict = pickle.load(f)
                    first_dict = pickle.load(f)

                    del num_strok_dict[name]
                    del num_stolbets_dict[name]
                    del count_pobeda_dict[name]
                    del up_me_dict[name]
                    del sign_of_user_dict[name]
                    del sign_of_computer_dict[name]
                    del button_list_dict[name]
                    del first_dict[name]
                    with open("savegam", "wb") as f:
                        pickle.dump(num_strok_dict, f)
                        pickle.dump(num_stolbets_dict, f)
                        pickle.dump(count_pobeda_dict, f)
                        pickle.dump(up_me_dict, f)
                        pickle.dump(sign_of_user_dict, f)
                        pickle.dump(sign_of_computer_dict, f)
                        pickle.dump(button_list_dict, f)
                        pickle.dump(first_dict, f)
                    self.Window()
            else:
                self.Window()
                self.show()

    def Window2(self):
        self.window = Window2()
        self.window.show()

    def Window(self):
        self.window = Window()
        self.window.show()

    def Close(self):
        self.hide()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window4()
    sys.exit(app.exec())
