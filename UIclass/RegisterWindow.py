from PyQt5 import QtWidgets, QtCore

from UI.registerWindow import Ui_RegisterWindow
from UIclass.Conection import Conection


class RegisterWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_RegisterWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.pushButton_logIn.clicked.connect(
            lambda: self.createUser(self.ui.lineEdit_name.text(), self.ui.lineEdit_password.text()))

    def createUser(self, name: str, passwd: str):
        if not name and not passwd:
            self.ui.label_aviso.setText("El nombre o la contraseña son invalidos")
            QtCore.QTimer.singleShot(1500, lambda: self.ui.label_aviso.setText(""))
            return None
        else:
            con = Conection.newConnection()
            cur = con.cursor()
            sql = "INSERT INTO cuentas (Name, Password) VALUES ('%s', '%s')" % (name, passwd)
            print(sql)
            cur.execute(sql)
            con.commit()
            self.ui.label_aviso.setText("Usuario creado, tiene que ejecutar la aplicación de nuevo para logearse")
            QtCore.QTimer.singleShot(1500, lambda: self.ui.label_aviso.setText(""))
            self.close()
