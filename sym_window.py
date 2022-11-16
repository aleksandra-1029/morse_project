import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTextBrowser, QButtonGroup
from PyQt5.QtGui import QFont
import sqlite3

con = sqlite3.connect('morse_dictionary.db')
cur = con.cursor()


class Symbols(QWidget):
    def __init__(self):
        super().__init__()

        self.btn1 = QPushButton('.', self)
        self.btn2 = QPushButton(',', self)
        self.btn3 = QPushButton('!', self)
        self.btn4 = QPushButton('(', self)
        self.btn5 = QPushButton(')', self)
        self.btn6 = QPushButton(':', self)
        self.btn7 = QPushButton('?', self)
        self.btn8 = QPushButton('=', self)
        self.btn9 = QPushButton('+', self)
        self.btn10 = QPushButton('-', self)
        self.btn11 = QPushButton(';', self)
        self.btn12 = QPushButton('"', self)
        self.sw = QTextBrowser(self)
        self.sym_btn_gr = QButtonGroup(self)

        self.initUI()

    def initUI(self):
        self.setGeometry(800, 100, 285, 240)
        self.setWindowTitle('Символы')
        self.setStyleSheet("background-color : #b5c6e0")

        self.btn1.resize(40, 40)
        self.btn1.move(10, 10)
        self.btn1.setStyleSheet(
            "background-color : #ebf1f5; color : #6f7b8c")
        self.btn1.setCheckable(True)

        self.btn2.resize(40, 40)
        self.btn2.move(55, 10)
        self.btn2.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")
        self.btn2.setCheckable(True)

        self.btn3.resize(40, 40)
        self.btn3.move(100, 10)
        self.btn3.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")
        self.btn3.setCheckable(True)

        self.btn4.resize(40, 40)
        self.btn4.move(145, 10)
        self.btn4.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")
        self.btn4.setCheckable(True)

        self.btn5.resize(40, 40)
        self.btn5.move(190, 10)
        self.btn5.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")
        self.btn5.setCheckable(True)

        self.btn6.resize(40, 40)
        self.btn6.move(235, 10)
        self.btn6.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")
        self.btn6.setCheckable(True)

        self.btn7.resize(40, 40)
        self.btn7.move(10, 55)
        self.btn7.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")
        self.btn7.setCheckable(True)

        self.btn8.resize(40, 40)
        self.btn8.move(55, 55)
        self.btn8.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")
        self.btn8.setCheckable(True)

        self.btn9.resize(40, 40)
        self.btn9.move(10, 100)
        self.btn9.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")
        self.btn9.setCheckable(True)

        self.btn10.resize(40, 40)
        self.btn10.move(55, 100)
        self.btn10.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")
        self.btn10.setCheckable(True)

        self.btn11.resize(40, 40)
        self.btn11.move(10, 145)
        self.btn11.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")
        self.btn11.setCheckable(True)

        self.btn12.resize(40, 40)
        self.btn12.move(55, 145)
        self.btn12.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")
        self.btn12.setCheckable(True)

        self.sw.move(100, 55)
        self.sw.resize(175, 175)
        self.sw.setStyleSheet("background-color : #f5f7f; color : #4c5461")
        self.sw.setFont(QFont('Courier New', 23))

        self.sym_btn_gr.setExclusive(True)
        self.sym_btn_gr.addButton(self.btn1)
        self.sym_btn_gr.addButton(self.btn2)
        self.sym_btn_gr.addButton(self.btn3)
        self.sym_btn_gr.addButton(self.btn4)
        self.sym_btn_gr.addButton(self.btn5)
        self.sym_btn_gr.addButton(self.btn6)
        self.sym_btn_gr.addButton(self.btn7)
        self.sym_btn_gr.addButton(self.btn8)
        self.sym_btn_gr.addButton(self.btn9)
        self.sym_btn_gr.addButton(self.btn10)
        self.sym_btn_gr.addButton(self.btn11)
        self.sym_btn_gr.addButton(self.btn12)

        self.sym_btn_gr.buttonClicked.connect(
            self.sym_btn_clicked)

    def sym_btn_clicked(self):
        what_btn_clicked = self.sym_btn_gr.checkedButton().text()
        m = \
            list(cur.execute(
                f"""SELECT morse_sym FROM symbols WHERE symbol == '{what_btn_clicked}'"""))[0][0]
        self.sw.setText(f'{what_btn_clicked}\n{m}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Symbols()
    ex.show()
    sys.exit(app.exec())
