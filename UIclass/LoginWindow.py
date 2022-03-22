import bcrypt
from PyQt5 import QtCore, QtWidgets

from UIclass.Conection import Conection
from UI.loginWindow import Ui_LoginWindow
from UIclass.RegisterWindow import RegisterWindow
from UIclass.mainWindow import MainWindow
from UIclass import var


class LoginWindow(QtWidgets.QMainWindow):
    """Genera una ventana de login"""

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.pushButton_logIn.clicked.connect(
            lambda: Login(self.ui.lineEdit_name.text(), self.ui.lineEdit_password.text(), self.ui, self))
        self.ui.pushButton.clicked.connect(self.lanzarRegister)

    def lanzarRegister(self):
        self.main = RegisterWindow()
        self.main.show()
        self.close()


class Login():
    """Controla el estado del login de usuario"""

    def __init__(self, name, passwd, ui: Ui_LoginWindow, loginWin: LoginWindow):
        self.loginWin = loginWin
        self.ui = ui
        self.user: int
        if self.check_login(name, passwd):
            self.main = MainWindow(self.user)
            var.mainWin = self.main
            self.loginWin.close()

        else:
            self.ui.label_aviso.setText("Nombre o contraseña incorrectos")
            QtCore.QTimer.singleShot(1500, lambda: self.ui.label_aviso.setText(""))

    def check_login(self, name: str, password: str):
        """Comprueba si el usuario existe o no"""
        name = name.lower()
        if not name and not password:
            return False
        con = Conection.newConnection()
        cur = con.cursor()
        sql = "SELECT * from cuentas where Name = '%s' and Password = '%s'" % (name, password)
        cur.execute(sql)
        result = cur.fetchall()
        if cur.rowcount > 0:
            if name == result[0][1]:
                if password == result[0][2]:
                    self.user = result[0][0]
                    return True
            else:
                return False
        else:
            return False
