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



if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MainWindow()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('ev_simulator')
    w.show()

    sys.exit(app.exec_())