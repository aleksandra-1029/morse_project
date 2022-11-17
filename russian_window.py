import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QButtonGroup, QTextBrowser
from PyQt5.QtGui import QFont
import sqlite3

con = sqlite3.connect('morse_dictionary.db')
cur = con.cursor()


class RusAlphabet(QWidget):
    def __init__(self):
        super().__init__()

        self.btn_a = QPushButton('а', self)
        self.btn_b = QPushButton('б', self)
        self.btn_v = QPushButton('в', self)
        self.btn_g = QPushButton('г', self)
        self.btn_d = QPushButton('д', self)
        self.btn_e = QPushButton('е', self)
        self.btn_e2 = QPushButton('ё', self)
        self.btn_zh = QPushButton('ж', self)
        self.btn_z = QPushButton('з', self)
        self.btn_i = QPushButton('и', self)
        self.btn_j = QPushButton('й', self)
        self.btn_k = QPushButton('к', self)
        self.btn_l = QPushButton('л', self)
        self.btn_m = QPushButton('м', self)
        self.btn_n = QPushButton('н', self)
        self.btn_o = QPushButton('о', self)
        self.btn_p = QPushButton('п', self)
        self.btn_r = QPushButton('р', self)
        self.btn_s = QPushButton('с', self)
        self.btn_t = QPushButton('т', self)
        self.btn_u = QPushButton('у', self)
        self.btn_f = QPushButton('ф', self)
        self.btn_h = QPushButton('х', self)
        self.btn_c = QPushButton('ц', self)
        self.btn_ch = QPushButton('ч', self)
        self.btn_sh = QPushButton('ш', self)
        self.btn_sch = QPushButton('щ', self)
        self.btn_x = QPushButton('ъ', self)
        self.btn_y = QPushButton('ы', self)
        self.btn_q = QPushButton('ь', self)
        self.btn_ie = QPushButton('э', self)
        self.btn_iu = QPushButton('ю', self)
        self.btn_ia = QPushButton('я', self)
        self.sw = QTextBrowser(self)
        self.rus_btn_gr = QButtonGroup(self)

        self.initUI()

    def initUI(self):
        self.setGeometry(800, 100, 350, 350)
        self.setWindowTitle('Русский алфавит')
        self.setStyleSheet("background-color : #b5c6e0")

        self.btn_a.resize(40, 40)
        self.btn_a.move(10, 10)
        self.btn_a.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")
        self.btn_a.setCheckable(True)

        self.btn_b.resize(40, 40)
        self.btn_b.move(55, 10)
        self.btn_b.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")
        self.btn_b.setCheckable(True)

        self.btn_v.resize(40, 40)
        self.btn_v.move(100, 10)
        self.btn_v.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")
        self.btn_v.setCheckable(True)

        self.btn_g.resize(40, 40)
        self.btn_g.move(145, 10)
        self.btn_g.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")
        self.btn_g.setCheckable(True)

        self.btn_d.resize(40, 40)
        self.btn_d.move(190, 10)
        self.btn_d.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")
        self.btn_d.setCheckable(True)

        self.btn_e.resize(40, 40)
        self.btn_e.move(235, 10)
        self.btn_e.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")
        self.btn_e.setCheckable(True)

        self.btn_e2.resize(40, 40)
        self.btn_e2.move(280, 10)
        self.btn_e2.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")
        self.btn_e2.setCheckable(True)

        self.btn_zh.resize(40, 40)
        self.btn_zh.move(10, 55)
        self.btn_zh.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")
        self.btn_zh.setCheckable(True)

        self.btn_z.resize(40, 40)
        self.btn_z.move(55, 55)
        self.btn_z.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")
        self.btn_z.setCheckable(True)

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
        self.btn_m.move(280, 55)
        self.btn_m.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")
        self.btn_m.setCheckable(True)

        self.btn_n.resize(40, 40)
        self.btn_n.move(10, 100)
        self.btn_n.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")
        self.btn_n.setCheckable(True)

        self.btn_o.resize(40, 40)
        self.btn_o.move(55, 100)
        self.btn_o.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")
        self.btn_o.setCheckable(True)

        self.btn_p.resize(40, 40)
        self.btn_p.move(100, 100)
        self.btn_p.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")
        self.btn_p.setCheckable(True)

        self.btn_r.resize(40, 40)
        self.btn_r.move(145, 100)
        self.btn_r.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")
        self.btn_r.setCheckable(True)

        self.btn_s.resize(40, 40)
        self.btn_s.move(190, 100)
        self.btn_s.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")
        self.btn_s.setCheckable(True)

        self.btn_t.resize(40, 40)
        self.btn_t.move(235, 100)
        self.btn_t.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")
        self.btn_t.setCheckable(True)

        self.btn_u.resize(40, 40)
        self.btn_u.move(280, 100)
        self.btn_u.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")
        self.btn_u.setCheckable(True)

        self.btn_f.resize(40, 40)
        self.btn_f.move(10, 145)
        self.btn_f.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")
        self.btn_f.setCheckable(True)

        self.btn_h.resize(40, 40)
        self.btn_h.move(55, 145)
        self.btn_h.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")
        self.btn_h.setCheckable(True)

        self.btn_c.resize(40, 40)
        self.btn_c.move(100, 145)
        self.btn_c.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")
        self.btn_c.setCheckable(True)

        self.btn_ch.resize(40, 40)
        self.btn_ch.move(10, 190)
        self.btn_ch.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")
        self.btn_ch.setCheckable(True)

        self.btn_sh.resize(40, 40)
        self.btn_sh.move(55, 190)
        self.btn_sh.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")
        self.btn_sh.setCheckable(True)

        self.btn_sch.resize(40, 40)
        self.btn_sch.move(100, 190)
        self.btn_sch.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")
        self.btn_sch.setCheckable(True)

        self.btn_x.resize(40, 40)
        self.btn_x.move(10, 235)
        self.btn_x.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")
        self.btn_x.setCheckable(True)

        self.btn_y.resize(40, 40)
        self.btn_y.move(55, 235)
        self.btn_y.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")
        self.btn_y.setCheckable(True)

        self.btn_q.resize(40, 40)
        self.btn_q.move(100, 235)
        self.btn_q.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")
        self.btn_q.setCheckable(True)

        self.btn_ie.resize(40, 40)
        self.btn_ie.move(10, 280)
        self.btn_ie.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")
        self.btn_ie.setCheckable(True)

        self.btn_iu.resize(40, 40)
        self.btn_iu.move(55, 280)
        self.btn_iu.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")
        self.btn_iu.setCheckable(True)

        self.btn_ia.resize(40, 40)
        self.btn_ia.move(100, 280)
        self.btn_ia.setStyleSheet("background-color : #ebf1f5; color : #6f7b8c")
        self.btn_ia.setCheckable(True)

        self.sw.move(145, 145)
        self.sw.resize(175, 175)
        self.sw.setStyleSheet("background-color : #f5f7f")
        self.sw.setFont(QFont('Courier New', 15))

        self.rus_btn_gr.setExclusive(True)
        self.rus_btn_gr.addButton(self.btn_a)
        self.rus_btn_gr.addButton(self.btn_b)
        self.rus_btn_gr.addButton(self.btn_v)
        self.rus_btn_gr.addButton(self.btn_g)
        self.rus_btn_gr.addButton(self.btn_d)
        self.rus_btn_gr.addButton(self.btn_e)
        self.rus_btn_gr.addButton(self.btn_e2)
        self.rus_btn_gr.addButton(self.btn_zh)
        self.rus_btn_gr.addButton(self.btn_z)
        self.rus_btn_gr.addButton(self.btn_i)
        self.rus_btn_gr.addButton(self.btn_j)
        self.rus_btn_gr.addButton(self.btn_k)
        self.rus_btn_gr.addButton(self.btn_l)
        self.rus_btn_gr.addButton(self.btn_m)
        self.rus_btn_gr.addButton(self.btn_n)
        self.rus_btn_gr.addButton(self.btn_o)
        self.rus_btn_gr.addButton(self.btn_p)
        self.rus_btn_gr.addButton(self.btn_r)
        self.rus_btn_gr.addButton(self.btn_s)
        self.rus_btn_gr.addButton(self.btn_t)
        self.rus_btn_gr.addButton(self.btn_u)
        self.rus_btn_gr.addButton(self.btn_f)
        self.rus_btn_gr.addButton(self.btn_h)
        self.rus_btn_gr.addButton(self.btn_c)
        self.rus_btn_gr.addButton(self.btn_ch)
        self.rus_btn_gr.addButton(self.btn_sh)
        self.rus_btn_gr.addButton(self.btn_sch)
        self.rus_btn_gr.addButton(self.btn_x)
        self.rus_btn_gr.addButton(self.btn_y)
        self.rus_btn_gr.addButton(self.btn_q)
        self.rus_btn_gr.addButton(self.btn_ie)
        self.rus_btn_gr.addButton(self.btn_iu)
        self.rus_btn_gr.addButton(self.btn_ia)

        self.rus_btn_gr.buttonClicked.connect(self.rus_btn_clicked)

    def rus_btn_clicked(self):
        what_btn_clicked = self.rus_btn_gr.checkedButton().text()
        m = \
            list(cur.execute(
                f"""SELECT morse_letter FROM russian WHERE rus_letter == '{what_btn_clicked}'"""))[
                0][0]
        self.sw.setText(f'{what_btn_clicked}\n{m}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RusAlphabet()
    ex.show()
    sys.exit(app.exec())
