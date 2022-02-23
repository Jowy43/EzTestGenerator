import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                           QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from UI.mainWindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ## Evento del botón del menu desplegable
        self.ui.btn_toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 250, True))

        #Páginas
           # Página 1
        self.ui.btn_menu_home.clicked.connect(lambda: self.ui.pages_widget.setCurrentWidget(self.ui.pg_home))

        # Página 2
        self.ui.btn_menu_home_2.clicked.connect(lambda: self.ui.pages_widget.setCurrentWidget(self.ui.pg_create))

        # Página 3
        self.ui.btn_menu_home_3.clicked.connect(lambda: self.ui.pages_widget.setCurrentWidget(self.ui.pg_list))

        self.show()


class UIFunctions(MainWindow):

    def toggleMenu(self, maxWidth, enable):
        if enable:

            # GET WIDTH
            width = self.ui.frame_left_menu.width()
            maxExtend = maxWidth
            standard = 70

            # SET MAX WIDTH
            if width == 70:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.frame_left_menu, b"minimumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()
