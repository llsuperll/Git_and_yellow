from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
import sys
from random import randint


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)  # Загружаем дизайн
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_round(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_round(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        r = randint(1, 200)
        qp.drawEllipse(randint(1, 400 - r), randint(1, 400 - r), r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
