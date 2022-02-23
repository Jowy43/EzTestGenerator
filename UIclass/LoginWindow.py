import bcrypt
from PyQt5 import QtCore, QtWidgets

from UI.loginWindow import Ui_MainWindow
from UIclass.Conection import Conection
from UIclass.mainWindow import MainWindow


class LoginWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.pushButton_logIn.clicked.connect(
            lambda: Login(self.ui.lineEdit_name.text(), self.ui.lineEdit_password.text(), self))


class Login():
    def __init__(self, name, passwd, ui):
        if Login.check_login(name, passwd):
            ui.main = MainWindow()
            ui.main.show()
            ui.close()
        else:
            ui.label_aviso.setText("Nombre o contraseña incorrectos")
            QtCore.QTimer.singleShot(1500, lambda: ui.label_aviso.setText(""))

    @staticmethod
    def check_login(name, password):
        if not name and not password:
            return False
        con = Conection.newConnection()
        cur = con.cursor()
        sql = "SELECT * from cuentas where Name = %s and Password = %s"
        val = (name, password)
        cur.execute(sql, val)
        result = cur.fetchall()
        if cur.rowcount > 0:
            if [x[0] for x in result][0] == name:
                if [x[1] for x in result][0] == password:
                    return True
            else:
                return False
        else:
            return False
