# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'seleccionar_access.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(292, 272)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btn_elegir_archivo_access = QPushButton(self.centralwidget)
        self.btn_elegir_archivo_access.setObjectName(u"btn_elegir_archivo_access")
        self.btn_elegir_archivo_access.setGeometry(QRect(50, 90, 191, 31))
        self.btn_exit = QPushButton(self.centralwidget)
        self.btn_exit.setObjectName(u"btn_exit")
        self.btn_exit.setGeometry(QRect(110, 170, 75, 31))
        self.btn_exit.setStyleSheet(u"background-color: red;\n"
"color: white;\n"
"font: 75 10pt \"Arial\";")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(False)
        self.pushButton.setGeometry(QRect(110, 130, 75, 31))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_elegir_archivo_access.setText(QCoreApplication.translate("MainWindow", u"Elegir Archivo Access", None))
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Continuar", None))
    # retranslateUi

