import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtGui import QFont
from rule_window import Rules
from translator import Translator
from training import Training
from middle_window import MiddleWindow


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.rw = Rules()
        self.translatew = Translator()
        self.trainw = Training()
        self.mw = MiddleWindow()

        self.btn_rules = QPushButton('Правила оформления запросов', self)
        self.btn_train = QPushButton('Тренажёр', self)
        self.btn_dict = QPushButton('Словарь', self)
        self.btn_translate = QPushButton('Переводчик', self)
        self.title_label = QLabel('Азбука Морзе', self)

        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 700, 500)
        self.setWindowTitle('Азбука Морзе')
        self.setStyleSheet("background-color : #b5c6e0")

        self.btn_rules.resize(230, 40)
        self.btn_rules.move(20, 435)
        self.btn_rules.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")
        self.btn_rules.setFont(QFont('Century Gothic', 7))

        self.btn_train.resize(180, 40)
        self.btn_train.move(260, 200)
        self.btn_train.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")
        self.btn_train.setFont(QFont('Century Gothic', 12))

        self.btn_dict.resize(150, 40)
        self.btn_dict.move(275, 150)
        self.btn_dict.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")
        self.btn_dict.setFont(QFont('Century Gothic', 12))

        self.btn_translate.resize(200, 40)
        self.btn_translate.move(250, 250)
        self.btn_translate.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")
        self.btn_translate.setFont(QFont('Century Gothic', 12))

        self.title_label.resize(300, 50)
        self.title_label.move(210, 40)
        self.title_label.setStyleSheet("color : #4c5461")
        self.title_label.setFont(QFont('Courier New', 24))

        self.btn_rules.clicked.connect(self.rules_button_pressed)
        self.btn_translate.clicked.connect(self.translate_button_pressed)
        self.btn_train.clicked.connect(self.training_button_pressed)
        self.btn_dict.clicked.connect(self.dict_button_pressed)

    def rules_button_pressed(self):
        self.rw.show()

    def translate_button_pressed(self):
        self.translatew.show()

    def training_button_pressed(self):
        self.trainw.show()

    def dict_button_pressed(self):
        self.mw.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
