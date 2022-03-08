import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                           QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from UI.mainWindow import Ui_MainWindow
from UIclass.Conection import Conection


class MainWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Pagina por defecto al iniciar la aplicación
        self.ui.pages_widget.setCurrentWidget(self.ui.pg_home)

        # Página por defecto al entrar en crear test
        self.ui.pages_test_create.setCurrentWidget(self.ui.pg_testname)

        ## Evento del botón del menu desplegable
        self.ui.btn_toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 250, True))

        # Enlaces de botones del menu con sus páginas
        # Página 1
        self.ui.btn_menu_home.clicked.connect(lambda: self.ui.pages_widget.setCurrentWidget(self.ui.pg_home))
        # Página 2
        self.ui.btn_menu_home_2.clicked.connect(lambda: self.ui.pages_widget.setCurrentWidget(self.ui.pg_create))
        # Página 3
        self.ui.btn_menu_home_3.clicked.connect(lambda: self.ui.pages_widget.setCurrentWidget(self.ui.pg_list))

        # Enlaces para crear tests
        # Crear nombre del test

        self.ui.btn_crearTest.clicked.connect(lambda: CrearTest(self.ui))

        self.show()


class CrearTest():
    def __init__(self, ui):
        super(CrearTest, self).__init__()
        self.ui = ui
        self.lastid = self.crearTest(self.ui.lineEdit_nombreTest.text())

    def crearTest(self, nombre: str):
        if not nombre:
            self.ui.label_tituloTestError.setText("Ocurrio un error al crear el test.\n Introduce un nombre válido.")
            QtCore.QTimer.singleShot(1500, lambda: self.ui.label_tituloTestError.setText(""))
        else:
            con = Conection.newConnection()
            cur = con.cursor()
            sql = "Insert into tests(nombre) VALUES('%s')" % nombre
            cur.execute(sql)
            con.commit()
            return cur.lastrowid

    def crearPregunta(self, nombre: str):
        if not nombre:
            self.ui.label_tituloTestError.setText("Ocurrio un error al crear el test.\n Introduce un nombre válido.")
            QtCore.QTimer.singleShot(1500, lambda: self.ui.label_tituloTestError.setText(""))
        else:
            con = Conection.newConnection()
            cur = con.cursor()
            sql = "Insert into preguntas(nombre"


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
