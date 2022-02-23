from PySide2 import QtCore
from PySide2.QtGui import (QColor)
from PySide2.QtWidgets import *

from UI.loading import Ui_SplashScreen
from UIclass.LoginWindow import LoginWindow

counter = 0


class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        # Sombras
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)
        # Timer
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(35)

        QtCore.QTimer.singleShot(1500, lambda: self.ui.label_loading.setText("<strong>loading</strong> database"))
        QtCore.QTimer.singleShot(1500, lambda: self.ui.label_loading.setText("<strong>loading</strong> user interface"))

        self.show()

    def progress(self):
        global counter
        self.ui.progressBar.setValue(counter)
        if counter > 100:
            self.timer.stop()
            self.main = LoginWindow()
            self.close()
            self.main.show()
        counter += 10
