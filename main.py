from PyQt5 import Qt
from random import randint
import sys
from Ui import Ui_MainWindow


class MyWidget(Qt.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.plot)

    def plot(self):
        self.scene = Qt.QGraphicsScene()

        self.graphics_view = Qt.QGraphicsView()
        self.graphics_view.setScene(self.scene)

        self.setCentralWidget(self.graphics_view)
        diameter = randint(0, 300)
        rect = Qt.QRectF(0, 0, diameter, diameter)
        colorlist = [Qt.Qt.yellow, Qt.Qt.red, Qt.Qt.blue, Qt.Qt.green, Qt.Qt.black, Qt.Qt.gray, Qt.Qt.darkCyan]
        color = colorlist[randint(0,6)]

        self.scene.addEllipse(rect, Qt.QPen(color), Qt.QBrush(color))


if __name__ == '__main__':
    app = Qt.QApplication([])
    mw = MyWidget()
    mw.show()
    app.exec()