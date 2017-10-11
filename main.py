import sys
from PyQt5.QtWidgets import QApplication
import main_window


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = main_window.MainWindow()
    window.show()

    sys.exit(app.exec_())