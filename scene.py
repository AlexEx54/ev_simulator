import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QThread
import workers


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.__worker = workers.Worker()
        self.__thread = QThread()

        self.__worker.moveToThread(self.__thread)
        self.__thread.started.connect(self.__worker.do_task)
        self.__thread.start()

    def paintEvent(self, paintEvent):
        print("paint event")



if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MainWindow()
    w.setWindowTitle('ev_simulator')
    w.resize(1000, 700)
    w.setStyleSheet("background-color: black");
    w.show()

    sys.exit(app.exec_())