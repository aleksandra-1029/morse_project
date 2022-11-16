import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from russian_window import RusAlphabet
from english_window import EngAlphabet
from number_window import Numbers
from sym_window import Symbols


class MiddleWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.btn_rus = QPushButton('Русский алфавит', self)
        self.btn_eng = QPushButton('Английский алфавит', self)
        self.btn_num = QPushButton('Цифры', self)
        self.btn_sym = QPushButton('Символы', self)

        self.rw = RusAlphabet()
        self.ew = EngAlphabet()
        self.sw = Symbols()
        self.nw = Numbers()

        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 180, 170)
        self.setWindowTitle('Выбор окна словаря')
        self.setStyleSheet("background-color : #b5c6e0")

        self.btn_rus.resize(160, 30)
        self.btn_rus.move(10, 10)
        self.btn_rus.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")

        self.btn_eng.resize(160, 30)
        self.btn_eng.move(10, 50)
        self.btn_eng.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")

        self.btn_num.resize(160, 30)
        self.btn_num.move(10, 90)
        self.btn_num.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")

        self.btn_sym.resize(160, 30)
        self.btn_sym.move(10, 130)
        self.btn_sym.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")

        self.btn_rus.clicked.connect(self.rus_dictionary)
        self.btn_eng.clicked.connect(self.eng_dictionary)
        self.btn_num.clicked.connect(self.num_dictionary)
        self.btn_sym.clicked.connect(self.sym_dictionary)

    def rus_dictionary(self):
        self.rw.show()

    def eng_dictionary(self):
        self.ew.show()

    def num_dictionary(self):
        self.nw.show()

    def sym_dictionary(self):
        self.sw.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MiddleWindow()
    ex.show()
    sys.exit(app.exec())
