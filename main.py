import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
import random


class Focus(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.paint)
        self.setWindowTitle('репозитории вроде норм а вроде и нет')
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        a = random.randrange(0, 200)
        b = random.randrange(0, 500)
        c = random.randrange(0, 500)
        qp.setBrush(QColor(random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)))
        qp.drawEllipse(b, c, a, a)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Focus()
    ex.show()
    sys.exit(app.exec_())
