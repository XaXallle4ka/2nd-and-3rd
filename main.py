from PyQt5 import Qt
from random import randint
import sys
from PyQt5 import uic


class MyWidget(Qt.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui',self)

        self.pushButton.clicked.connect(self.plot)

    def plot(self):
        self.scene = Qt.QGraphicsScene()

        self.graphics_view = Qt.QGraphicsView()
        self.graphics_view.setScene(self.scene)

        self.setCentralWidget(self.graphics_view)
        diameter = randint(0, 300)
        rect = Qt.QRectF(0, 0, diameter, diameter)
        color = Qt.Qt.yellow

        self.scene.addEllipse(rect, Qt.QPen(color), Qt.QBrush(color))


if __name__ == '__main__':
    app = Qt.QApplication([])
    mw = MyWidget()
    mw.show()
    app.exec()