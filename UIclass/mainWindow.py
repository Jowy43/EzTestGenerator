from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                           QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

import UIclass.var
import pdf.pdf
from pdf.Examen import Examen
from pdf.Preguntas import Preguntas
from UI.mainWindow import Ui_MainWindow
from UIclass.Conection import Conection


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)

        self.user = 2

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
        self.ui.btn_menu_home_3.clicked.connect(lambda: ListarTests(self.ui, self.user))
        self.ui.btn_crearTest.clicked.connect(lambda: Crear_Test(self.ui, self.user))
        self.show()


class ListarTests:
    def __init__(self, ui: Ui_MainWindow, user: int):
        super(ListarTests, self).__init__()
        self.ui = ui
        all = ListarTests.allTestUsuario(user)
        for x in all:
            self.ui.listWidgetTests.addItem(str(x[0]) + "-" + str(x[1]))
        self.ui.listWidgetTests.itemDoubleClicked.connect(lambda: self.getItem())

    def getItem(self):
        id = self.ui.listWidgetTests.currentItem().text().split("-")[0]
        titulo = self.ui.listWidgetTests.currentItem().text().split("-")[1]
        resul = self.allPreguntasTest(id)
        lpreguntas = []
        for x in resul:
            lpreguntas.append(Preguntas(str(x[1]), str(x[3]), str(x[4])))
        Examen(lpreguntas, titulo)

    def allPreguntasTest(self, id: int):
        con = Conection.newConnection()

        cur = con.cursor()
        sql = "select * from preguntas where idTest = '%s'" % id
        cur.execute(sql)
        result = cur.fetchall()
        return result

    def allTestUsuario(user: int):
        con = Conection.newConnection()

        cur = con.cursor()
        sql = "select * from tests te where te.idCuenta = '%s'" % user
        cur.execute(sql)
        result = cur.fetchall()
        return result


class PreguntaActual():
    def __init__(self, ui: Ui_MainWindow, IdTest: int, user: int):
        super(PreguntaActual, self).__init__()
        self.ui = ui
        self.IdTest = IdTest
        self.preguntaId = None

        self.ui.btn_siguientePregunta.clicked.connect(
            lambda: Crear_pregunta(self.ui, self.IdTest))
        self.ui.btn_finalizarTest.clicked.connect(lambda: Finalizar_Test(self.ui, self.IdTest))


class Finalizar_Test():
    def __init__(self, ui: Ui_MainWindow, idTest: int):
        super(Finalizar_Test, self).__init__()
        self.ui = ui
        self.IdTest = idTest
        Crear_pregunta.crearPregunta(self, self.ui, self.ui.textEdit_Enunciado.toPlainText(), self.IdTest,
                                     self.ui.textEdit_resA.toPlainText(),
                                     self.ui.textEdit_resB.toPlainText(), self.ui.checkBox_resA,
                                     self.ui.checkBox_resB)
        self.ui.pages_test_create.setCurrentWidget(self.ui.pg_testname)
        self.ui.label_numeroPregunta.setText("Pregunta número 1")
        self.ui.textEdit_Enunciado.setText("")
        self.ui.textEdit_resA.setText("")
        self.ui.textEdit_resB.setText("")
        self.ui.checkBox_resA.setChecked(False)
        self.ui.checkBox_resB.setChecked(False)
        self.ventana: MainWindow = UIclass.var.mainWin
        self.ventana.close()
        UIclass.var.mainWin = MainWindow()


class Crear_pregunta():
    def __init__(self, ui: Ui_MainWindow, idTest: int):
        super(Crear_pregunta, self).__init__()
        self.ui = ui
        self.IdTest = idTest
        self.lastPreguntaId = Crear_pregunta.crearPregunta(self, self.ui, self.ui.textEdit_Enunciado.toPlainText(),
                                                           self.IdTest,
                                                           self.ui.textEdit_resA.toPlainText(),
                                                           self.ui.textEdit_resB.toPlainText(), self.ui.checkBox_resA,
                                                           self.ui.checkBox_resB)
        if self.lastPreguntaId is not None:
            self.cont = 1
            self.siguientePregunta()

    def siguientePregunta(self):
        self.cont += 1
        self.ui.label_numeroPregunta.setText("Pregunta número " + str(self.cont))
        self.ui.textEdit_Enunciado.setText("")
        self.ui.textEdit_resA.setText("")
        self.ui.textEdit_resB.setText("")
        self.ui.checkBox_resA.setChecked(False)
        self.ui.checkBox_resB.setChecked(False)

    @staticmethod
    def crearPregunta(objeto: object, ui: Ui_MainWindow, nombre: str, idTest: int, respuestaA: str, respuestaB: str,
                      checkBox_resA: bool,
                      checkBox_resB: bool):
        if not nombre:
            ui.label_preguntaError.setText(
                "Ocurrio un error al crear la pregunta.\n Introduce unha pregunta válida.")
            QtCore.QTimer.singleShot(1500, lambda: ui.label_tituloTestError.setText(""))
        elif not respuestaA and not respuestaB:
            ui.label_preguntaError.setText(
                "Ocurrio un error al crear la pregunta.\n Introduce respuestas válidas.")
            QtCore.QTimer.singleShot(1500, lambda: ui.label_tituloTestError.setText(""))
        else:
            con = Conection.newConnection()
            cur = con.cursor()
            correcta = 0
            if checkBox_resA:
                correcta = 1
            elif checkBox_resB:
                correcta = 2
            sql = "Insert into preguntas(nombrePregunta,idTest,respuestaA,respuestaB,correcta) VALUES('%s', '%s', '%s', '%s', '%s')" % (
                nombre, idTest, respuestaA, respuestaB, correcta)
            cur.execute(sql)
            con.commit()
            print(sql)
            return cur.lastrowid


# Clase para crear los test e insertarlos en la base de datos
class Crear_Test:
    def __init__(self, ui: Ui_MainWindow, user: str):
        super(Crear_Test, self).__init__()
        self.ui = ui
        self.lastTestId = self.crearTest(self.ui.lineEdit_nombreTest.text(), user)
        if self.lastTestId is not None:
            self.ui.pages_test_create.setCurrentWidget(self.ui.preguntas_test)
            PreguntaActual(self.ui, self.lastTestId, user)

    def crearTest(self, nombre: str, user: str):
        if not nombre:
            self.ui.label_tituloTestError.setText(
                "Ocurrio un error al crear el test.\n Introduce un nombre válido.")
            QtCore.QTimer.singleShot(1500, lambda: self.ui.label_tituloTestError.setText(""))
        else:
            con = Conection.newConnection()
            cur = con.cursor()
            sql = "Insert into tests(nombreTest,idCuenta) VALUES('%s','%s')" % (nombre, user)
            cur.execute(sql)
            con.commit()
            self.ui.lineEdit_nombreTest.setText("")
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
