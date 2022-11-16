# Запустите программу create_database перед запуском проекта для создания необхадимой базы данных

import sys
from PyQt5.QtWidgets import QApplication

from main_window import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
