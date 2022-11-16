import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QButtonGroup, QTextBrowser
from PyQt5.QtGui import QFont
import sqlite3

con = sqlite3.connect('morse_dictionary.db')
cur = con.cursor()


class Numbers(QWidget):

    def __init__(self):
        super().__init__()

        self.btn_1 = QPushButton('1', self)
        self.btn_2 = QPushButton('2', self)
        self.btn_3 = QPushButton('3', self)
        self.btn_4 = QPushButton('4', self)
        self.btn_5 = QPushButton('5', self)
        self.btn_6 = QPushButton('6', self)
        self.btn_7 = QPushButton('7', self)
        self.btn_8 = QPushButton('8', self)
        self.btn_9 = QPushButton('9', self)
        self.btn_0 = QPushButton('0', self)
        self.sw = QTextBrowser(self)
        self.num_btn_gr = QButtonGroup(self)

        self.initUI()

    def initUI(self):
        self.setGeometry(800, 100, 285, 240)
        self.setWindowTitle('Цифры')
        self.setStyleSheet("background-color : #b5c6e0")

        self.btn_1.resize(40, 40)
        self.btn_1.move(10, 10)
        self.btn_1.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")
        self.btn_1.setCheckable(True)

        self.btn_2.resize(40, 40)
        self.btn_2.move(55, 10)
        self.btn_2.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")
        self.btn_2.setCheckable(True)

        self.btn_3.resize(40, 40)
        self.btn_3.move(10, 55)
        self.btn_3.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")
        self.btn_3.setCheckable(True)

        self.btn_4.resize(40, 40)
        self.btn_4.move(55, 55)
        self.btn_4.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")
        self.btn_4.setCheckable(True)

        self.btn_5.resize(40, 40)
        self.btn_5.move(10, 100)
        self.btn_5.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")
        self.btn_5.setCheckable(True)

        self.btn_6.resize(40, 40)
        self.btn_6.move(55, 100)
        self.btn_6.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")
        self.btn_6.setCheckable(True)

        self.btn_7.resize(40, 40)
        self.btn_7.move(10, 145)
        self.btn_7.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")
        self.btn_7.setCheckable(True)

        self.btn_8.resize(40, 40)
        self.btn_8.move(55, 145)
        self.btn_8.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")
        self.btn_8.setCheckable(True)

        self.btn_9.resize(40, 40)
        self.btn_9.move(10, 190)
        self.btn_9.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")
        self.btn_9.setCheckable(True)

        self.btn_0.resize(40, 40)
        self.btn_0.move(55, 190)
        self.btn_0.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")
        self.btn_0.setCheckable(True)

        self.sw.move(100, 10)
        self.sw.resize(175, 175)
        self.sw.setStyleSheet("background-color : #f5f7f; color : #4c5461")
        self.sw.setFont(QFont('Courier New', 26))

        self.num_btn_gr.setExclusive(True)
        self.num_btn_gr.addButton(self.btn_1)
        self.num_btn_gr.addButton(self.btn_2)
        self.num_btn_gr.addButton(self.btn_3)
        self.num_btn_gr.addButton(self.btn_4)
        self.num_btn_gr.addButton(self.btn_5)
        self.num_btn_gr.addButton(self.btn_6)
        self.num_btn_gr.addButton(self.btn_7)
        self.num_btn_gr.addButton(self.btn_8)
        self.num_btn_gr.addButton(self.btn_9)
        self.num_btn_gr.addButton(self.btn_0)

        self.num_btn_gr.buttonClicked.connect(self.num_btn_clicked)

    def num_btn_clicked(self):
        what_btn_clicked = self.num_btn_gr.checkedButton().text()
        m = list(cur.execute(
            f"""SELECT morse_num FROM numbers WHERE number == '{what_btn_clicked}'"""))[0][0]
        self.sw.setText(f'{what_btn_clicked}\n{m}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Numbers()
    ex.show()
    sys.exit(app.exec())
