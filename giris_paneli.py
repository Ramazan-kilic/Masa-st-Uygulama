# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'giris_paneli.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class login_Screen(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(50, 140, 721, 281))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.txt_ka = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txt_ka.setObjectName("txt_ka")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txt_ka)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.txt_sfr = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txt_sfr.setObjectName("txt_sfr")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txt_sfr)
        self.btn_giris = QtWidgets.QPushButton(self.formLayoutWidget)
        self.btn_giris.setObjectName("btn_giris")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.btn_giris)
        self.btn_kayitol = QtWidgets.QPushButton(self.formLayoutWidget)
        self.btn_kayitol.setObjectName("btn_kayitol")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.btn_kayitol)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(310, 60, 194, 36))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Kullanıcı Adı:"))
        self.label_2.setText(_translate("MainWindow", "Şifre:"))
        self.btn_giris.setText(_translate("MainWindow", "Giriş"))
        self.btn_kayitol.setText(_translate("MainWindow", "Kayıt Ol"))
        self.label_3.setText(_translate("MainWindow", "GİRİŞ PANELİ"))