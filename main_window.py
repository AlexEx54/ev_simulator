from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QThread, QObject, pyqtSlot
import time


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('ev_simulator')
        self.resize(1000, 700)
        self.setStyleSheet("background-color: black");

        self.__updater = Updater(self)
        self.__updater.Start()


    def paintEvent(self, paintEvent):
        print("drawing scene")


class Updater(QObject):
    def __init__(self, widget_to_update):
        super().__init__()
        self.__widget = widget_to_update
        self.__thread = QThread()
        self.moveToThread(self.__thread)
        self.__thread.started.connect(self.__DoTask)

    def Start(self):
        self.__thread.start()


    @pyqtSlot()
    def __DoTask(self):
        while True:
            self.__widget.update()
            time.sleep(0.1)
