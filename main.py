import sys

from PySide2.QtWidgets import *

from UIclass.mainWindow import MainWindow
import UIclass

if __name__ == "__main__":
    app = QApplication()
    UIclass.var.mainWin = MainWindow()
    sys.exit(app.exec_())
