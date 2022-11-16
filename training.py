import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QTextEdit, QTextBrowser, \
    QComboBox
from PyQt5.QtGui import QFont
import sqlite3
import random

con = sqlite3.connect('morze_dictionary.db')
cur = con.cursor()


class Training(QWidget):
    def __init__(self):
        super().__init__()

        self.btn_generate = QPushButton('сгенерировать', self)
        self.btn_check = QPushButton('проверить', self)
        self.type = QComboBox(self)
        self.sym1 = QLabel(self)
        self.sym2 = QLabel(self)
        self.sym3 = QLabel(self)
        self.ans1 = QTextEdit(self)
        self.ans2 = QTextEdit(self)
        self.ans3 = QTextEdit(self)
        self.copy = QTextBrowser(self)

        self.initUI()

    def initUI(self):
        self.setGeometry(800, 100, 280, 270)
        self.setWindowTitle('Тренажёр')
        self.setStyleSheet("background-color : #b5c6e0")

        self.type.move(10, 10)
        self.type.resize(150, 25)
        self.type.addItem('русский')
        self.type.addItem('английский')
        self.type.addItem('символы')
        self.type.addItem('цифры')

        self.btn_generate.move(170, 10)
        self.btn_generate.resize(100, 25)
        self.btn_generate.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")

        self.btn_check.move(150, 200)
        self.btn_check.resize(100, 25)
        self.btn_check.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")

        self.sym1.move(20, 50)
        self.sym1.resize(40, 40)
        self.sym1.setFont(QFont('Century Gothic', 10))

        self.sym2.move(20, 100)
        self.sym2.resize(40, 40)
        self.sym2.setFont(QFont('Century Gothic', 10))

        self.sym3.move(20, 150)
        self.sym3.resize(40, 40)
        self.sym3.setFont(QFont('Century Gothic', 10))

        self.ans1.move(100, 50)
        self.ans1.resize(150, 40)
        self.ans1.setStyleSheet("background-color : white")

        self.ans2.move(100, 100)
        self.ans2.resize(150, 40)
        self.ans2.setStyleSheet("background-color : white")

        self.ans3.move(100, 150)
        self.ans3.resize(150, 40)
        self.ans3.setStyleSheet("background-color : white")

        self.copy.move(10, 230)
        self.copy.resize(250, 30)
        self.copy.setText('Символы для копирования: -  •')

        self.btn_generate.clicked.connect(self.generate)
        self.btn_check.clicked.connect(self.check)

    def generate(self):
        language = self.type.currentText()
        self.ans1.setText('')
        self.ans1.setStyleSheet("background-color : white")
        self.ans2.setText('')
        self.ans2.setStyleSheet("background-color : white")
        self.ans3.setText('')
        self.ans3.setStyleSheet("background-color : white")
        rus = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й',
               'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
               'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю',
               'я']
        eng = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
               'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        sym = ['.', ',', '"', ';', ':', '=', '+', '-', '!', '?', '(', ')']
        num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        if language == 'русский':
            self.sym1.setText(random.choice(rus))
            self.sym2.setText(random.choice(rus))
            self.sym3.setText(random.choice(rus))

        elif language == 'английский':
            self.sym1.setText(random.choice(eng))
            self.sym2.setText(random.choice(eng))
            self.sym3.setText(random.choice(eng))

        elif language == 'символы':
            self.sym1.setText(random.choice(sym))
            self.sym2.setText(random.choice(sym))
            self.sym3.setText(random.choice(sym))
        else:
            self.sym1.setText(random.choice(num))
            self.sym2.setText(random.choice(num))
            self.sym3.setText(random.choice(num))

    def check(self):
        language = self.type.currentText()
        if language == 'русский':
            rans1 = list(cur.execute(
                f"""SELECT morze_letter FROM russian WHERE rus_letter == '{self.sym1.text()}'"""))[
                0][0]
            rans2 = list(cur.execute(
                f"""SELECT morze_letter FROM russian WHERE rus_letter == '{self.sym2.text()}'"""))[
                0][0]
            rans3 = list(cur.execute(
                f"""SELECT morze_letter FROM russian WHERE rus_letter == '{self.sym3.text()}'"""))[
                0][0]

        elif language == 'английский':
            rans1 = list(cur.execute(
                f"""SELECT morze_letter FROM english WHERE eng_letter == '{self.sym1.text()}'"""))[
                0][0]
            rans2 = list(cur.execute(
                f"""SELECT morze_letter FROM english WHERE eng_letter == '{self.sym2.text()}'"""))[
                0][0]
            rans3 = list(cur.execute(
                f"""SELECT morze_letter FROM english WHERE eng_letter == '{self.sym3.text()}'"""))[
                0][0]

        elif language == 'символы':
            rans1 = list(cur.execute(
                f"""SELECT morze_sym FROM symbols WHERE symbol == '{self.sym1.text()}'"""))[0][0]
            rans2 = list(cur.execute(
                f"""SELECT morze_sym FROM symbols WHERE symbol == '{self.sym2.text()}'"""))[0][0]
            rans3 = list(cur.execute(
                f"""SELECT morze_sym FROM symbols WHERE symbol == '{self.sym3.text()}'"""))[0][0]

        else:
            rans1 = list(cur.execute(
                f"""SELECT morze_num FROM numbers WHERE number == '{self.sym1.text()}'"""))[0][0]
            rans2 = list(cur.execute(
                f"""SELECT morze_num FROM numbers WHERE number == '{self.sym2.text()}'"""))[0][0]
            rans3 = list(cur.execute(
                f"""SELECT morze_num FROM numbers WHERE number == '{self.sym3.text()}'"""))[0][0]

        if rans1 == self.ans1.toPlainText():
            self.ans1.setStyleSheet("background-color : #99c480")
        else:
            self.ans1.setStyleSheet("background-color : #a86262")

        if rans2 == self.ans2.toPlainText():
            self.ans2.setStyleSheet("background-color : #99c480")
        else:
            self.ans2.setStyleSheet("background-color : #a86262")

        if rans3 == self.ans3.toPlainText():
            self.ans3.setStyleSheet("background-color : #99c480")
        else:
            self.ans3.setStyleSheet("background-color : #a86262")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Training()
    ex.show()
    sys.exit(app.exec())
