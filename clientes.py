# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'clientes.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 234)
        self.label_cantidad_clientes = QLabel(Dialog)
        self.label_cantidad_clientes.setObjectName(u"label_cantidad_clientes")
        self.label_cantidad_clientes.setGeometry(QRect(120, 200, 47, 16))
        self.btn_actualizar_aguas_cordobesas = QPushButton(Dialog)
        self.btn_actualizar_aguas_cordobesas.setObjectName(u"btn_actualizar_aguas_cordobesas")
        self.btn_actualizar_aguas_cordobesas.setGeometry(QRect(10, 70, 261, 31))
        self.btn_actualizar_agua_todos = QPushButton(Dialog)
        self.btn_actualizar_agua_todos.setObjectName(u"btn_actualizar_agua_todos")
        self.btn_actualizar_agua_todos.setGeometry(QRect(10, 150, 261, 31))
        self.label_txt_seleccione_cliente = QLabel(Dialog)
        self.label_txt_seleccione_cliente.setObjectName(u"label_txt_seleccione_cliente")
        self.label_txt_seleccione_cliente.setGeometry(QRect(10, 10, 131, 16))
        self.btn_exit = QPushButton(Dialog)
        self.btn_exit.setObjectName(u"btn_exit")
        self.btn_exit.setGeometry(QRect(300, 110, 75, 31))
        self.btn_exit.setStyleSheet(u"background-color: red;\n"
"color: white;\n"
"font: 75 10pt \"Arial\";")
        self.cb_seleccionar_cliente = QComboBox(Dialog)
        self.cb_seleccionar_cliente.addItem("")
        self.cb_seleccionar_cliente.setObjectName(u"cb_seleccionar_cliente")
        self.cb_seleccionar_cliente.setGeometry(QRect(10, 30, 371, 22))
        self.le_periodo_a_buscar = QLineEdit(Dialog)
        self.le_periodo_a_buscar.setObjectName(u"le_periodo_a_buscar")
        self.le_periodo_a_buscar.setGeometry(QRect(10, 110, 261, 31))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 200, 111, 16))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_cantidad_clientes.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.btn_actualizar_aguas_cordobesas.setText(QCoreApplication.translate("Dialog", u"Actualizar Aguas Cordobesas al Cliente Actual", None))
        self.btn_actualizar_agua_todos.setText(QCoreApplication.translate("Dialog", u"Actualizar Aguas Cordobesas a Todos los Clientes", None))
        self.label_txt_seleccione_cliente.setText(QCoreApplication.translate("Dialog", u"Seleccione el cliente:", None))
        self.btn_exit.setText(QCoreApplication.translate("Dialog", u"Salir", None))
        self.cb_seleccionar_cliente.setItemText(0, QCoreApplication.translate("Dialog", u"Sin Selecci\u00f3n", None))

        self.le_periodo_a_buscar.setPlaceholderText(QCoreApplication.translate("Dialog", u"Periodo a Buscar", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Cantidad de Clientes:", None))
    # retranslateUi

