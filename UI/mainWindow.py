from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                           QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 500)
        MainWindow.setMinimumSize(QSize(1000, 500))
        MainWindow.setStyleSheet("background-color: rgb(45, 45, 45);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Top_Bar = QtWidgets.QFrame(self.centralwidget)
        self.Top_Bar.setMaximumSize(QtCore.QSize(50000, 40))
        self.Top_Bar.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.Top_Bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Top_Bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Top_Bar.setObjectName("Top_Bar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Top_Bar)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_toggle = QtWidgets.QFrame(self.Top_Bar)
        self.frame_toggle.setMaximumSize(QtCore.QSize(70, 40))
        self.frame_toggle.setStyleSheet("")
        self.frame_toggle.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_toggle.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_toggle.setObjectName("frame_toggle")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_toggle)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btn_toggle = QtWidgets.QPushButton(self.frame_toggle)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_toggle.sizePolicy().hasHeightForWidth())
        self.btn_toggle.setSizePolicy(sizePolicy)
        self.btn_toggle.setStyleSheet("background-image: url(:/newPrefix/menu.png);\n"
                                      "background-position: center;\n"
                                      "background-repeat: no-reperat;\n"
                                      "border: none;\n"
                                      "background-color: rgb(27, 29, 35);")
        self.btn_toggle.setText("")
        self.btn_toggle.setObjectName("btn_toggle")
        self.verticalLayout_2.addWidget(self.btn_toggle)
        self.horizontalLayout.addWidget(self.frame_toggle)
        self.frame_top = QtWidgets.QFrame(self.Top_Bar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_top.sizePolicy().hasHeightForWidth())
        self.frame_top.setSizePolicy(sizePolicy)
        self.frame_top.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top.setObjectName("frame_top")
        self.horizontalLayout.addWidget(self.frame_top)
        self.verticalLayout.addWidget(self.Top_Bar)
        self.Content = QtWidgets.QFrame(self.centralwidget)
        self.Content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Content.setObjectName("Content")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Content)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_left_menu = QtWidgets.QFrame(self.Content)
        self.frame_left_menu.setMinimumSize(QtCore.QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QtCore.QSize(70, 16777215))
        self.frame_left_menu.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.frame_left_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_left_menu.setObjectName("frame_left_menu")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_top_menus = QtWidgets.QFrame(self.frame_left_menu)
        self.frame_top_menus.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top_menus.setObjectName("frame_top_menus")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.btn_menu_home = QtWidgets.QPushButton(self.frame_top_menus)
        self.btn_menu_home.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_menu_home.setStyleSheet("QPushButton{\n"
                                         "    color:rgb(255, 255, 255);\n"
                                         "    background-color: rgb(35, 35, 35);\n"
                                         "    border: 0px solid;\n"
                                         "    background-image: url(:/newPrefix/home.png);\n"
                                         "    background-repeat: no-reperat;\n"
                                         "    border: none;\n"
                                         "    background-position: center;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover{\n"
                                         "    background-color: rgb(255, 204, 0);\n"
                                         "}")
        self.btn_menu_home.setText("")
        self.btn_menu_home.setObjectName("btn_menu_home")
        self.verticalLayout_4.addWidget(self.btn_menu_home)
        self.btn_menu_home_2 = QtWidgets.QPushButton(self.frame_top_menus)
        self.btn_menu_home_2.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_menu_home_2.setStyleSheet("QPushButton{\n"
                                           "    color:rgb(255, 255, 255);\n"
                                           "    background-color: rgb(35, 35, 35);\n"
                                           "    border: 0px solid;\n"
                                           "    background-image: url(:/newPrefix/create.png);\n"
                                           "    background-repeat: no-reperat;\n"
                                           "    border: none;\n"
                                           "    background-position: center;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:hover{\n"
                                           "        \n"
                                           "    background-color: rgb(255, 204, 0);\n"
                                           "}")
        self.btn_menu_home_2.setText("")
        self.btn_menu_home_2.setObjectName("btn_menu_home_2")
        self.verticalLayout_4.addWidget(self.btn_menu_home_2)
        self.btn_menu_home_3 = QtWidgets.QPushButton(self.frame_top_menus)
        self.btn_menu_home_3.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_menu_home_3.setStyleSheet("QPushButton{\n"
                                           "    color:rgb(255, 255, 255);\n"
                                           "    background-color: rgb(35, 35, 35);\n"
                                           "    \n"
                                           "    background-image: url(:/newPrefix/testList.png);\n"
                                           "    background-repeat: no-reperat;\n"
                                           "    border: none;\n"
                                           "    background-position: center;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:hover{\n"
                                           "        \n"
                                           "    background-color: rgb(255, 204, 0);\n"
                                           "}")
        self.btn_menu_home_3.setText("")
        self.btn_menu_home_3.setObjectName("btn_menu_home_3")
        self.verticalLayout_4.addWidget(self.btn_menu_home_3)
        self.verticalLayout_3.addWidget(self.frame_top_menus, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout_2.addWidget(self.frame_left_menu)
        self.frame_pages = QtWidgets.QFrame(self.Content)
        self.frame_pages.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_pages.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_pages.setObjectName("frame_pages")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.pages_widget = QtWidgets.QStackedWidget(self.frame_pages)
        self.pages_widget.setObjectName("pages_widget")
        self.pg_home = QtWidgets.QWidget()
        self.pg_home.setObjectName("pg_home")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.pg_home)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame = QtWidgets.QFrame(self.pg_home)
        self.frame.setMaximumSize(QtCore.QSize(700, 350))
        self.frame.setStyleSheet("QFrame{\n"
                                 "    background-color: rgb(56, 58, 89 );\n"
                                 "    color:rgb(220,    220, 220);\n"
                                 "    border-radius:10px;\n"
                                 "}\n"
                                 "\n"
                                 "")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(90)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgb(255, 204, 0);")
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_6.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(23)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:rgb(98,114,164);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_6.addWidget(self.label_2)
        self.horizontalLayout_3.addWidget(self.frame)
        self.pages_widget.addWidget(self.pg_home)
        self.pg_create = QtWidgets.QWidget()
        self.pg_create.setObjectName("pg_create")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.pg_create)
        self.verticalLayout_8.setContentsMargins(6, 10, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.pages_test_create = QtWidgets.QStackedWidget(self.pg_create)
        self.pages_test_create.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.pages_test_create.setObjectName("pages_test_create")
        self.pg_testname = QtWidgets.QWidget()
        self.pg_testname.setObjectName("pg_testname")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.pg_testname)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_2 = QtWidgets.QFrame(self.pg_testname)
        self.frame_2.setMaximumSize(QtCore.QSize(300, 300))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setLineWidth(1)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_TituloTest = QtWidgets.QLabel(self.frame_2)
        self.label_TituloTest.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_TituloTest.setFont(font)
        self.label_TituloTest.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_TituloTest.setAlignment(QtCore.Qt.AlignCenter)
        self.label_TituloTest.setObjectName("label_TituloTest")
        self.verticalLayout_9.addWidget(self.label_TituloTest)
        spacerItem = QtWidgets.QSpacerItem(20, 33, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_9.addItem(spacerItem)
        self.lineEdit_nombreTest = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_nombreTest.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_nombreTest.setStyleSheet("QLineEdit {\n"
                                               "    \n"
                                               "    color: rgb(255, 255, 255);\n"
                                               "    background-color: rgb(33, 37, 43);\n"
                                               "    border-radius: 5px;\n"
                                               "    border: 2px solid rgb(33, 37, 43);\n"
                                               "    padding-left: 10px;\n"
                                               "    selection-color: rgb(255, 255, 255);\n"
                                               "    selection-background-color: rgb(255, 121, 198);\n"
                                               "}\n"
                                               "QLineEdit:hover {\n"
                                               "    border: 2px solid rgb(64, 71, 88);\n"
                                               "}\n"
                                               "QLineEdit:focus {\n"
                                               "    border: 2px solid rgb(91, 101, 124);\n"
                                               "}")
        self.lineEdit_nombreTest.setText("")
        self.lineEdit_nombreTest.setObjectName("lineEdit_nombreTest")
        self.verticalLayout_9.addWidget(self.lineEdit_nombreTest)
        self.label_tituloTestError = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_tituloTestError.sizePolicy().hasHeightForWidth())
        self.label_tituloTestError.setSizePolicy(sizePolicy)
        self.label_tituloTestError.setMaximumSize(QtCore.QSize(5000, 25))
        self.label_tituloTestError.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_tituloTestError.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_tituloTestError.setLineWidth(1)
        self.label_tituloTestError.setText("")
        self.label_tituloTestError.setScaledContents(False)
        self.label_tituloTestError.setAlignment(QtCore.Qt.AlignCenter)
        self.label_tituloTestError.setObjectName("label_tituloTestError")
        self.verticalLayout_9.addWidget(self.label_tituloTestError)
        spacerItem1 = QtWidgets.QSpacerItem(20, 21, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_9.addItem(spacerItem1)
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.btn_crearTest = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_crearTest.sizePolicy().hasHeightForWidth())
        self.btn_crearTest.setSizePolicy(sizePolicy)
        self.btn_crearTest.setMaximumSize(QtCore.QSize(150, 30))
        self.btn_crearTest.setStyleSheet("QPushButton {\n"
                                         "    \n"
                                         "    color: rgb(255, 255, 255);\n"
                                         "    border: 2px solid rgb(52, 59, 72);\n"
                                         "    border-radius: 5px;    \n"
                                         "    background-color: rgb(52, 59, 72);\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "    background-color: rgb(57, 65, 80);\n"
                                         "    border: 2px solid rgb(61, 70, 86);\n"
                                         "}\n"
                                         "QPushButton:pressed {    \n"
                                         "    background-color: rgb(35, 40, 49);\n"
                                         "    border: 2px solid rgb(43, 50, 61);\n"
                                         "}")
        self.btn_crearTest.setObjectName("btn_crearTest")
        self.horizontalLayout_5.addWidget(self.btn_crearTest)
        self.verticalLayout_9.addWidget(self.frame_3)
        self.horizontalLayout_4.addWidget(self.frame_2)
        self.pages_test_create.addWidget(self.pg_testname)
        self.preguntas_test = QtWidgets.QWidget()
        self.preguntas_test.setObjectName("preguntas_test")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.preguntas_test)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frame_4 = QtWidgets.QFrame(self.preguntas_test)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_numeroPregunta = QtWidgets.QLabel(self.frame_4)
        self.label_numeroPregunta.setGeometry(QtCore.QRect(380, 10, 101, 51))
        self.label_numeroPregunta.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_numeroPregunta.setObjectName("label_numeroPregunta")
        self.textEdit_Enunciado = QtWidgets.QTextEdit(self.frame_4)
        self.textEdit_Enunciado.setGeometry(QtCore.QRect(180, 90, 501, 31))
        self.textEdit_Enunciado.setStyleSheet("color: rgb(255, 255, 255);")
        self.textEdit_Enunciado.setObjectName("textEdit_Enunciado")
        self.label_Enunciado = QtWidgets.QLabel(self.frame_4)
        self.label_Enunciado.setGeometry(QtCore.QRect(90, 90, 71, 31))
        self.label_Enunciado.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_Enunciado.setObjectName("label_Enunciado")
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setGeometry(QtCore.QRect(170, 130, 511, 231))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setMaximumSize(QtCore.QSize(600, 300))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.frame_6 = QtWidgets.QFrame(self.frame_5)
        self.frame_6.setMaximumSize(QtCore.QSize(16777215, 54))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_resA = QtWidgets.QLabel(self.frame_6)
        self.label_resA.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_resA.setObjectName("label_resA")
        self.horizontalLayout_7.addWidget(self.label_resA)
        self.textEdit_resA = QtWidgets.QTextEdit(self.frame_6)
        self.textEdit_resA.setStyleSheet("color: rgb(255, 255, 255);")
        self.textEdit_resA.setObjectName("textEdit_resA")
        self.horizontalLayout_7.addWidget(self.textEdit_resA)
        self.checkBox_resA = QtWidgets.QCheckBox(self.frame_6)
        self.checkBox_resA.setStyleSheet("color: rgb(255, 255, 255);")
        self.checkBox_resA.setObjectName("checkBox_resA")
        self.horizontalLayout_7.addWidget(self.checkBox_resA)
        self.verticalLayout_10.addWidget(self.frame_6)
        self.frame_7 = QtWidgets.QFrame(self.frame_5)
        self.frame_7.setMaximumSize(QtCore.QSize(16777215, 54))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_resB = QtWidgets.QLabel(self.frame_7)
        self.label_resB.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_resB.setObjectName("label_resB")
        self.horizontalLayout_8.addWidget(self.label_resB)
        self.textEdit_resB = QtWidgets.QTextEdit(self.frame_7)
        self.textEdit_resB.setStyleSheet("color: rgb(255, 255, 255);")
        self.textEdit_resB.setObjectName("textEdit_resB")
        self.horizontalLayout_8.addWidget(self.textEdit_resB)
        self.checkBox_resB = QtWidgets.QCheckBox(self.frame_7)
        self.checkBox_resB.setStyleSheet("color: rgb(255, 255, 255);")
        self.checkBox_resB.setObjectName("checkBox_resB")
        self.horizontalLayout_8.addWidget(self.checkBox_resB)
        self.verticalLayout_10.addWidget(self.frame_7)
        self.label_preguntaError = QtWidgets.QLabel(self.frame_5)
        self.label_preguntaError.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_preguntaError.setText("")
        self.label_preguntaError.setAlignment(QtCore.Qt.AlignCenter)
        self.label_preguntaError.setObjectName("label_preguntaError")
        self.verticalLayout_10.addWidget(self.label_preguntaError)
        self.frame_8 = QtWidgets.QFrame(self.frame_5)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.btn_siguientePregunta = QtWidgets.QPushButton(self.frame_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_siguientePregunta.sizePolicy().hasHeightForWidth())
        self.btn_siguientePregunta.setSizePolicy(sizePolicy)
        self.btn_siguientePregunta.setMaximumSize(QtCore.QSize(150, 30))
        self.btn_siguientePregunta.setStyleSheet("QPushButton {\n"
                                                 "    \n"
                                                 "    color: rgb(255, 255, 255);\n"
                                                 "    border: 2px solid rgb(52, 59, 72);\n"
                                                 "    border-radius: 5px;    \n"
                                                 "    background-color: rgb(52, 59, 72);\n"
                                                 "}\n"
                                                 "QPushButton:hover {\n"
                                                 "    background-color: rgb(57, 65, 80);\n"
                                                 "    border: 2px solid rgb(61, 70, 86);\n"
                                                 "}\n"
                                                 "QPushButton:pressed {    \n"
                                                 "    background-color: rgb(35, 40, 49);\n"
                                                 "    border: 2px solid rgb(43, 50, 61);\n"
                                                 "}")
        self.btn_siguientePregunta.setObjectName("btn_siguientePregunta")
        self.horizontalLayout_9.addWidget(self.btn_siguientePregunta)
        self.btn_finalizarTest = QtWidgets.QPushButton(self.frame_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_finalizarTest.sizePolicy().hasHeightForWidth())
        self.btn_finalizarTest.setSizePolicy(sizePolicy)
        self.btn_finalizarTest.setMaximumSize(QtCore.QSize(150, 30))
        self.btn_finalizarTest.setStyleSheet("QPushButton {\n"
                                             "    \n"
                                             "    color: rgb(255, 255, 255);\n"
                                             "    border: 2px solid rgb(52, 59, 72);\n"
                                             "    border-radius: 5px;    \n"
                                             "    background-color: rgb(52, 59, 72);\n"
                                             "}\n"
                                             "QPushButton:hover {\n"
                                             "    background-color: rgb(57, 65, 80);\n"
                                             "    border: 2px solid rgb(61, 70, 86);\n"
                                             "}\n"
                                             "QPushButton:pressed {    \n"
                                             "    background-color: rgb(35, 40, 49);\n"
                                             "    border: 2px solid rgb(43, 50, 61);\n"
                                             "}")
        self.btn_finalizarTest.setObjectName("btn_finalizarTest")
        self.horizontalLayout_9.addWidget(self.btn_finalizarTest)
        self.verticalLayout_10.addWidget(self.frame_8)
        self.horizontalLayout_6.addWidget(self.frame_4)
        self.pages_test_create.addWidget(self.preguntas_test)
        self.verticalLayout_8.addWidget(self.pages_test_create)
        self.pages_widget.addWidget(self.pg_create)
        self.pg_list = QtWidgets.QWidget()
        self.pg_list.setObjectName("pg_list")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.pg_list)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(1)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_TituloTest_2 = QtWidgets.QLabel(self.pg_list)
        self.label_TituloTest_2.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_TituloTest_2.setFont(font)
        self.label_TituloTest_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_TituloTest_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_TituloTest_2.setObjectName("label_TituloTest_2")
        self.verticalLayout_7.addWidget(self.label_TituloTest_2)
        self.listWidgetTests = QtWidgets.QListWidget(self.pg_list)
        self.listWidgetTests.setStyleSheet("color: rgb(255, 255, 255);")
        self.listWidgetTests.setObjectName("listWidgetTests")
        self.verticalLayout_7.addWidget(self.listWidgetTests)
        self.pages_widget.addWidget(self.pg_list)
        self.verticalLayout_5.addWidget(self.pages_widget)
        self.horizontalLayout_2.addWidget(self.frame_pages)
        self.verticalLayout.addWidget(self.Content)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pages_widget.setCurrentIndex(2)
        self.pages_test_create.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "EzTests"))
        self.label_2.setText(_translate("MainWindow", "Genera Test de manera sencilla"))
        self.label_TituloTest.setText(_translate("MainWindow", "Titulo"))
        self.lineEdit_nombreTest.setPlaceholderText(_translate("MainWindow", "Nombre del Test"))
        self.btn_crearTest.setText(_translate("MainWindow", "Crear Test"))
        self.label_numeroPregunta.setText(_translate("MainWindow", "Pregunta numero 1"))
        self.textEdit_Enunciado.setPlaceholderText(_translate("MainWindow", "Enunciado de la pregunta"))
        self.label_Enunciado.setText(_translate("MainWindow", "Pregunta:"))
        self.label_resA.setText(_translate("MainWindow", "Respuesta A:"))
        self.textEdit_resA.setPlaceholderText(_translate("MainWindow", "Texto de la respuesta"))
        self.checkBox_resA.setText(_translate("MainWindow", "Correcta?"))
        self.label_resB.setText(_translate("MainWindow", "Respuesta B:"))
        self.textEdit_resB.setPlaceholderText(_translate("MainWindow", "Texto de la respuesta"))
        self.checkBox_resB.setText(_translate("MainWindow", "Correcta?"))
        self.btn_siguientePregunta.setText(_translate("MainWindow", "Siguiente pregunta"))
        self.btn_finalizarTest.setText(_translate("MainWindow", "Finalizar Test"))
        self.label_TituloTest_2.setText(_translate("MainWindow", "Lista de Test"))


from images import create_rc
from images import home_rc
from images import menu_rc
from images import testList_rc
