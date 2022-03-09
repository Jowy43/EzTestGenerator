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
        # por defecto se crean dos respuestas siempre
        self.ui.spinBox_numRes.setValue(2)
        # Pagina por defecto al iniciar la aplicación
        self.ui.pages_widget.setCurrentWidget(self.ui.pg_home)

        # Página por defecto al entrar en crear test
        self.ui.pages_test_create.setCurrentWidget(self.ui.pg_testname)

        ## Evento del botón del menu desplegable
        self.connect = self.ui.btn_toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 250, True))

        # Enlaces de botones del menu con sus páginas
        # Página 1
        self.ui.btn_menu_home.clicked.connect(lambda: self.ui.pages_widget.setCurrentWidget(self.ui.pg_home))
        # Página 2
        self.ui.btn_menu_home_2.clicked.connect(lambda: self.ui.pages_widget.setCurrentWidget(self.ui.pg_create))
        # Página 3
        self.ui.btn_menu_home_3.clicked.connect(lambda: self.ui.pages_widget.setCurrentWidget(self.ui.pg_list))
        # Enlaces para crear tests
        # Crear nombre del test

        self.ui.btn_crearTest.clicked.connect(lambda: Crear_Test(self.ui))
        self.ui.pages_Respuestas.setCurrentWidget(self.ui.page_Num_Res)
        self.show()


class Pregunta_actual:
    def __init__(self, ui: Ui_MainWindow, lastTestId: int):
        super(Pregunta_actual, self).__init__()
        self.ui = ui
        self.lastTestId = lastTestId
        self.numRes = self.ui.spinBox_numRes.value()
        self.lastPreId = self.crearPregunta(self.ui.textEdit_Enunciado.toPlainText(), self.numRes, self.lastTestId)
        self.ui.pages_Respuestas.setCurrentWidget(self.ui.page_Respuestas)

    def generarRespuestas(self, labelRespuesta: str):
        self.ui.label_respuesta.setText("Respuesta", labelRespuesta)
        self.ui.textEdit_respuesta.setText("")

    def crearPregunta(self, nombre: str, numRespuestas: int, idTest: int):
        if not nombre:
            self.ui.label_preguntaError.setText(
                "Ocurrio un error al crear la pregunta.\n Introduce unha pregunta válida.")
            QtCore.QTimer.singleShot(1500, lambda: self.ui.label_tituloTestError.setText(""))
        elif numRespuestas < 0:
            self.ui.label_preguntaError.setText(
                "Ocurrio un error al crear la pregunta.\n Introduce un número de respuestas válida.")
            QtCore.QTimer.singleShot(1500, lambda: self.ui.label_tituloTestError.setText(""))
        else:
            con = Conection.newConnection()
            cur = con.cursor()
            sql = "Insert into preguntas(nombrePregunta,idTest) VALUES('%s', '%s')" % (nombre, idTest)
            cur.execute(sql)
            con.commit()
            return cur.lastrowid


class Crear_Test:
    def __init__(self, ui: Ui_MainWindow):
        super(Crear_Test, self).__init__()
        self.ui = ui
        self.lastTestId = self.crearTest(self.ui.lineEdit_nombreTest.text())
        self.ui.pages_test_create.setCurrentWidget(self.ui.preguntas_test)
        self.ui.btn_crearRespuesta.clicked.connect(lambda: Pregunta_actual(self.ui, self.lastTestId))

    def crearTest(self, nombre: str):
        if not nombre:
            self.ui.label_tituloTestError.setText("Ocurrio un error al crear el test.\n Introduce un nombre válido.")
            QtCore.QTimer.singleShot(1500, lambda: self.ui.label_tituloTestError.setText(""))
        else:
            con = Conection.newConnection()
            cur = con.cursor()
            sql = "Insert into tests(nombreTest) VALUES('%s')" % nombre
            cur.execute(sql)
            con.commit()
            return cur.lastrowid


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
