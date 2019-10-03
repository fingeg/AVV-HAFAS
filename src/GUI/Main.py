from PyQt4 import QtCore, QtGui

class BusStop:
    """Draw a bus stop"""

    def __init__(self, parent, network, code):
        self.parent = parent
        self.network = network
        self.code = code
        self.stop = network.stops[code]
        self.x, self.y = self.getCoordinates()

    def getCoordinates(self):
        x = int(1300 / (self.network.field[0][1] - self.network.field[0][0]) * (self.stop.x - self.network.field[0][0]))
        y = int(700 / (self.network.field[1][1] - self.network.field[1][0]) * (self.stop.y - self.network.field[1][0]))
        return x, y

    def draw(self):
        color = QtGui.QColor(250, 0, 0)
        painter = QtGui.QPainter(self.parent.image)
        painter.setPen(QtGui.QPen(color, 4, QtCore.Qt.SolidLine, QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin))

        point = QtCore.QPoint(self.x, self.y)
        painter.drawPoint(point)

        self.parent.modified = True
        self.parent.update()
        painter.end()

        print('draw point at %d %d' % (self.x, self.y))

class MainPanel(QtGui.QWidget):
    """Control the GUI"""

    def __init__(self, parent, network, height, width):
        super(MainPanel, self).__init__(parent)

        self.parent = parent
        self.network = network
        self.modified = False
        self.imageSize = QtCore.QSize(width, height)
        self.image = QtGui.QImage(self.imageSize, QtGui.QImage.Format_RGB32)
        self.image.fill(QtGui.qRgb(50, 50, 50))

        self.stops = []
        i = 0
        for stop in self.network.stops.keys():
            i += 1
            self.stops.append(BusStop(self, network, stop))
            if i > 20:
                pass

        self.paintStops()

    def filterStop(self, stop):
        stop = self.network.stops[stop.code]
        return True

    def paintStops(self):
        for stop in self.stops:
            if self.filterStop(stop):
                stop.draw()

    def paintEvent(self, event):
        """Paint the image, with all the rails and switches."""
        painter = QtGui.QPainter(self)
        painter.drawImage(event.rect(), self.image)

    def resizeEvent(self, event):
        self.resizeImage(self.image, event.size())
        super(MainPanel, self).resizeEvent(event)

    def resizeImage(self, image, newSize, paintAlways=False):
        if image.size() == newSize and not paintAlways:
            return

        # Create a new image with new size and re-draw the rail network
        self.image = QtGui.QImage(newSize, QtGui.QImage.Format_RGB32)
        self.image.fill(QtGui.qRgb(30, 30, 30))

        self.paintStops()

class MainWindow(QtGui.QMainWindow):
    def __init__(self, network):
        super(MainWindow, self).__init__()

        height = 700
        width = 1300

        self.mainPanel = MainPanel(self, network, height, width)

        self.setCentralWidget(self.mainPanel)
        self.setWindowTitle("AVV-HAFAS Visualisation")
        self.setGeometry(0, 30, width, height)

class GUI:
    def __init__(self, network):
        self.app = QtGui.QApplication([])
        self.window = MainWindow(network)
        self.window.show()

    def run(self):
        status = self.app.exec_()
        print("GUI finished with status %d" % status)
