from PyQt5.QtCore import QObject, pyqtSlot
import time


class Worker(QObject):

    @pyqtSlot()
    def do_task(self):
        while True:
            print("Doing background task")
            time.sleep(1)
