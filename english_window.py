import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QButtonGroup, QTextBrowser
from PyQt5.QtGui import QFont
import sqlite3

con = sqlite3.connect('morze_dictionary.db')
cur = con.cursor()


class EngAlphabet(QWidget):
    def __init__(self):
        super().__init__()

        self.btn_a = QPushButton('a', self)
        self.btn_b = QPushButton('b', self)
        self.btn_c = QPushButton('c', self)
        self.btn_d = QPushButton('d', self)
        self.btn_e = QPushButton('e', self)
        self.btn_f = QPushButton('f', self)
        self.btn_g = QPushButton('g', self)
        self.btn_h = QPushButton('h', self)
        self.btn_i = QPushButton('i', self)
        self.btn_j = QPushButton('j', self)
        self.btn_k = QPushButton('k', self)
        self.btn_l = QPushButton('l', self)
        self.btn_m = QPushButton('m', self)
        self.btn_n = QPushButton('n', self)
        self.btn_o = QPushButton('o', self)
        self.btn_p = QPushButton('p', self)
        self.btn_q = QPushButton('q', self)
        self.btn_r = QPushButton('r', self)
        self.btn_s = QPushButton('s', self)
        self.btn_t = QPushButton('t', self)
        self.btn_u = QPushButton('u', self)
        self.btn_v = QPushButton('v', self)
        self.btn_w = QPushButton('w', self)
        self.btn_x = QPushButton('x', self)
        self.btn_y = QPushButton('y', self)
        self.btn_z = QPushButton('z', self)
        self.sw = QTextBrowser(self)
        self.eng_btn_gr = QButtonGroup(self)

        self.initUI()

    def initUI(self):
        self.setGeometry(800, 100, 285, 330)
        self.setWindowTitle('Английский алфавит')
        self.setStyleSheet("background-color : #b5c6e0")

        self.btn_a.resize(40, 40)
        self.btn_a.move(10, 10)
        self.btn_a.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")
        self.btn_a.setCheckable(True)

        self.btn_b.resize(40, 40)
        self.btn_b.move(55, 10)
        self.btn_b.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")
        self.btn_b.setCheckable(True)

        self.btn_c.resize(40, 40)
        self.btn_c.move(100, 10)
        self.btn_c.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")
        self.btn_c.setCheckable(True)

        self.btn_d.resize(40, 40)
        self.btn_d.move(145, 10)
        self.btn_d.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")
        self.btn_d.setCheckable(True)

        self.btn_e.resize(40, 40)
        self.btn_e.move(190, 10)
        self.btn_e.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")
        self.btn_e.setCheckable(True)

        self.btn_f.resize(40, 40)
        self.btn_f.move(235, 10)
        self.btn_f.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")
        self.btn_f.setCheckable(True)

        self.btn_g.resize(40, 40)
        self.btn_g.move(10, 55)
        self.btn_g.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")
        self.btn_g.setCheckable(True)

        self.btn_h.resize(40, 40)
        self.btn_h.move(55, 55)
        self.btn_h.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")
        self.btn_h.setCheckable(True)

        self.btn_i.resize(40, 40)
        self.btn_i.move(100, 55)
        self.btn_i.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")
        self.btn_i.setCheckable(True)

        self.btn_j.resize(40, 40)
        self.btn_j.move(145, 55)
        self.btn_j.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")
        self.btn_j.setCheckable(True)

        self.btn_k.resize(40, 40)
        self.btn_k.move(190, 55)
        self.btn_k.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")
        self.btn_k.setCheckable(True)

        self.btn_l.resize(40, 40)
        self.btn_l.move(235, 55)
        self.btn_l.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")
        self.btn_l.setCheckable(True)

        self.btn_m.resize(40, 40)
        self.btn_m.move(10, 100)
        self.btn_m.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")
        self.btn_m.setCheckable(True)

        self.btn_n.resize(40, 40)
        self.btn_n.move(55, 100)
        self.btn_n.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")
        self.btn_n.setCheckable(True)

        self.btn_o.resize(40, 40)
        self.btn_o.move(100, 100)
        self.btn_o.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")
        self.btn_o.setCheckable(True)

        self.btn_p.resize(40, 40)
        self.btn_p.move(145, 100)
        self.btn_p.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")
        self.btn_p.setCheckable(True)

        self.btn_q.resize(40, 40)
        self.btn_q.move(190, 100)
        self.btn_q.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")
        self.btn_q.setCheckable(True)

        self.btn_r.resize(40, 40)
        self.btn_r.move(235, 100)
        self.btn_r.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")
        self.btn_r.setCheckable(True)

        self.btn_s.resize(40, 40)
        self.btn_s.move(10, 145)
        self.btn_s.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")
        self.btn_s.setCheckable(True)

        self.btn_t.resize(40, 40)
        self.btn_t.move(55, 145)
        self.btn_t.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")
        self.btn_t.setCheckable(True)

        self.btn_u.resize(40, 40)
        self.btn_u.move(10, 190)
        self.btn_u.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")
        self.btn_u.setCheckable(True)

        self.btn_v.resize(40, 40)
        self.btn_v.move(55, 190)
        self.btn_v.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")
        self.btn_v.setCheckable(True)

        self.btn_w.resize(40, 40)
        self.btn_w.move(10, 235)
        self.btn_w.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")
        self.btn_w.setCheckable(True)

        self.btn_x.resize(40, 40)
        self.btn_x.move(55, 235)
        self.btn_x.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")
        self.btn_x.setCheckable(True)

        self.btn_y.resize(40, 40)
        self.btn_y.move(10, 280)
        self.btn_y.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")
        self.btn_y.setCheckable(True)

        self.btn_z.resize(40, 40)
        self.btn_z.move(55, 280)
        self.btn_z.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")
        self.btn_z.setCheckable(True)

        self.sw.move(100, 145)
        self.sw.resize(175, 175)
        self.sw.setStyleSheet("background-color : #f5f7f; color : #4c5461")
        self.sw.setFont(QFont('Courier New', 26))

        self.eng_btn_gr.setExclusive(True)
        self.eng_btn_gr.addButton(self.btn_a)
        self.eng_btn_gr.addButton(self.btn_b)
        self.eng_btn_gr.addButton(self.btn_c)
        self.eng_btn_gr.addButton(self.btn_d)
        self.eng_btn_gr.addButton(self.btn_e)
        self.eng_btn_gr.addButton(self.btn_f)
        self.eng_btn_gr.addButton(self.btn_g)
        self.eng_btn_gr.addButton(self.btn_h)
        self.eng_btn_gr.addButton(self.btn_i)
        self.eng_btn_gr.addButton(self.btn_j)
        self.eng_btn_gr.addButton(self.btn_k)
        self.eng_btn_gr.addButton(self.btn_l)
        self.eng_btn_gr.addButton(self.btn_m)
        self.eng_btn_gr.addButton(self.btn_n)
        self.eng_btn_gr.addButton(self.btn_o)
        self.eng_btn_gr.addButton(self.btn_p)
        self.eng_btn_gr.addButton(self.btn_q)
        self.eng_btn_gr.addButton(self.btn_r)
        self.eng_btn_gr.addButton(self.btn_s)
        self.eng_btn_gr.addButton(self.btn_t)
        self.eng_btn_gr.addButton(self.btn_u)
        self.eng_btn_gr.addButton(self.btn_v)
        self.eng_btn_gr.addButton(self.btn_w)
        self.eng_btn_gr.addButton(self.btn_x)
        self.eng_btn_gr.addButton(self.btn_y)
        self.eng_btn_gr.addButton(self.btn_z)

        self.eng_btn_gr.buttonClicked.connect(self.eng_btn_clicked)

    def eng_btn_clicked(self):
        what_btn_clicked = self.eng_btn_gr.checkedButton().text()
        m = list(cur.execute(
            f"""SELECT morze_letter FROM english WHERE eng_letter == '{what_btn_clicked}'"""))[0][0]
        self.sw.setText(f'{what_btn_clicked}\n{m}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = EngAlphabet()
    ex.show()
    sys.exit(app.exec())
