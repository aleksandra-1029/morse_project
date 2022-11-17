import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QTextBrowser, QTextEdit, \
    QComboBox
from PyQt5.QtGui import QFont
import sqlite3

con = sqlite3.connect('morse_dictionary.db')
cur = con.cursor()


class Translator(QWidget):
    def __init__(self):
        super().__init__()

        self.mnumbers, self.msymbols, self.mrussian, self.menglish = list(), list(), list(), list()
        self.copy = QTextBrowser(self)
        for a in list(cur.execute("""SELECT morse_num FROM numbers""")):
            self.mnumbers.append(a[0])
        for a in list(cur.execute("""SELECT morse_sym FROM symbols""")):
            self.msymbols.append(a[0])
        for a in list(cur.execute("""SELECT morse_letter FROM russian""")):
            self.mrussian.append(a[0])
        for a in list(cur.execute("""SELECT morse_letter FROM english""")):
            self.menglish.append(a[0])

        self.input = QTextEdit(self)
        self.output = QTextBrowser(self)
        self.run_btn = QPushButton('перевести', self)
        self.chose_lang1 = QComboBox(self)
        self.chose_lang2 = QComboBox(self)
        self.text1 = QLabel('Изначальный язык:', self)
        self.text2 = QLabel('На какой язык:', self)
        self.text3 = QLabel('Введите текст:', self)
        self.text4 = QLabel('Перевод:', self)

        self.initUI()

    def initUI(self):
        self.setGeometry(800, 100, 800, 600)
        self.setWindowTitle('Переводчик')
        self.setStyleSheet("background-color : #b5c6e0")

        self.text1.move(10, 10)
        self.chose_lang1.resize(100, 20)
        self.chose_lang1.move(150, 10)
        self.chose_lang1.addItem('русский')
        self.chose_lang1.addItem('английский')
        self.chose_lang1.addItem('морзе')

        self.text2.move(10, 50)
        self.chose_lang2.resize(100, 20)
        self.chose_lang2.move(150, 50)
        self.chose_lang2.addItem('русский')
        self.chose_lang2.addItem('английский')
        self.chose_lang2.addItem('морзе')

        self.run_btn.move(280, 10)
        self.run_btn.resize(100, 60)
        self.run_btn.setStyleSheet("background-color : #ebf1f5; color : #4c5461")
        self.run_btn.setFont(QFont('Century Gothic', 9))

        self.text3.move(10, 100)
        self.input.move(120, 100)
        self.input.resize(450, 200)
        self.input.setStyleSheet("background-color : #ebf1f5; color : #4c5461")
        self.input.setFont(QFont('Century Gothic', 8))

        self.text4.move(10, 350)
        self.output.move(120, 350)
        self.output.resize(450, 200)
        self.output.setStyleSheet("background-color : #ebf1f5; color : #4c5461")
        self.output.setFont(QFont('Century Gothic', 8))

        self.copy.move(120, 560)
        self.copy.resize(250, 30)
        self.copy.setText('Символы для копирования: -  •')

        self.run_btn.clicked.connect(self.translate_function)

    def translate_function(self):
        language1 = self.chose_lang1.currentText()
        language2 = self.chose_lang2.currentText()
        if language1 == language2:
            self.output.setText(self.input.toPlainText())
        elif {language1, language2} == {'русский', 'английский'}:
            self.output.setText('Неправильно выбраны языки перевода!')
        else:
            res = ''
            is_ok = True
            if language1 == 'морзе':
                for line in self.input.toPlainText().splitlines():
                    if is_ok:
                        for word in line.split('       '):
                            if is_ok:
                                for letter in word.split('   '):
                                    print(letter)
                                    if letter in self.mnumbers:
                                        res += str(list(cur.execute(f"""SELECT number FROM numbers 
                                        WHERE morse_num == '{letter}'"""))[0][0])
                                    elif letter in self.msymbols:
                                        res += str(list(cur.execute(f"""SELECT symbol FROM symbols 
                                        WHERE morse_sym == '{letter}'"""))[0][0])
                                    elif language2 == 'русский' and letter in self.mrussian:
                                        res += str(list(cur.execute(f"""SELECT rus_letter FROM 
                                        russian WHERE morse_letter == '{letter}'"""))[0][0])
                                    elif language2 == 'английский' and letter in self.menglish:
                                        res += str(list(cur.execute(f"""SELECT eng_letter FROM 
                                        english WHERE morse_letter == '{letter}'"""))[0][0])
                                    else:
                                        self.output.setText('Ввод содержит некорректные символы!')
                                        is_ok = False
                                        break
                                res += ' '
                    res += '\n'
            else:
                res = ''
                for line in self.input.toPlainText().splitlines():
                    if is_ok:
                        for word in line.split():
                            if is_ok:
                                for letter in word:
                                    if letter in '1234567890':
                                        res += list(cur.execute(f"""SELECT morse_num 
                                        FROM numbers WHERE number == '{letter}'"""))[0][0]
                                    elif letter in '.,:;"-+=!?()':
                                        res += list(cur.execute(f"""SELECT morse_sym FROM 
                                        symbols WHERE symbol == '{letter}'"""))[0][0]
                                    elif language1 == 'русский' and letter.lower() in 'аб' \
                                                                                      'вгдеёжз' \
                                                                                      'ийклмнопр' \
                                                                                      'стуфхцчшщъ' \
                                                                                      'ыьэюя':
                                        res += list(cur.execute(f"""SELECT morse_letter FROM 
                                        russian WHERE rus_letter == '{letter}'"""))[0][0]
                                    elif language1 == 'английский' and letter in 'abcdefghigklmnop' \
                                                                                 'qrstuvwxyz':
                                        res += list(cur.execute(f"""SELECT morse_letter FROM 
                                        english WHERE eng_letter == '{letter}'"""))[0][0]
                                    else:
                                        is_ok = False
                                        self.output.setText('Ввод содержит некорректные символы!')
                                        break
                                    res += '   '
                                res += '       '
                        res += '\n'
            if is_ok:
                self.output.setText(res)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Translator()
    ex.show()
    sys.exit(app.exec())
