import sys

from PySide2.QtWidgets import *

from UIclass.mainWindow import MainWindow

if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    sys.exit(app.exec_())
