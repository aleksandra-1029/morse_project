import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QFont


class Rules(QWidget):
    def __init__(self):
        super().__init__()

        self.title = QLabel(self)
        self.text = QLabel(self)

        self.initUI()

    def initUI(self):
        self.setGeometry(800, 100, 400, 340)
        self.setWindowTitle('Правила оформления запроса')
        self.setStyleSheet('background-color : #b5c6e0')

        self.title.setText('Правила оформления')
        self.title.move(70, 10)
        self.title.setFont(QFont('Century Gothic', 13))

        self.text.move(10, 50)
        self.text.setFont(QFont('Century Gothic', 8))
        self.text.setText('Переводчик:\n\n1. Текст на русском/английском должен быть \nоформлен '
                          'по обычным правилам.\n2. Текст на морзе должен быть \nофомлен по '
                          'следующим правилам:\n\tМежду символами одной буквы должен\n\t  быть'
                          ' 1 пробел\n\tМежду буквами одного слова \n\t  должно быть 3 пробела\n\t'
                          'Между словами должно быть 7 пробелов\n\n\n'
                          'Тренажёр:\n\n1. Лишних пробелов и знаков в вводе быть не должно')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Rules()
    ex.show()
    sys.exit(app.exec())
