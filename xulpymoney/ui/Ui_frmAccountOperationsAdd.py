# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'xulpymoney/ui/frmAccountOperationsAdd.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_frmAccountOperationsAdd(object):
    def setupUi(self, frmAccountOperationsAdd):
        frmAccountOperationsAdd.setObjectName("frmAccountOperationsAdd")
        frmAccountOperationsAdd.setWindowModality(QtCore.Qt.WindowModal)
        frmAccountOperationsAdd.resize(566, 286)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/xulpymoney/document-edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        frmAccountOperationsAdd.setWindowIcon(icon)
        frmAccountOperationsAdd.setModal(True)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(frmAccountOperationsAdd)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblTitulo = QtWidgets.QLabel(frmAccountOperationsAdd)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lblTitulo.setFont(font)
        self.lblTitulo.setStyleSheet("color: rgb(0, 128, 0);")
        self.lblTitulo.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTitulo.setObjectName("lblTitulo")
        self.verticalLayout.addWidget(self.lblTitulo)
        self.wdgDT = wdgDatetime(frmAccountOperationsAdd)
        self.wdgDT.setObjectName("wdgDT")
        self.verticalLayout.addWidget(self.wdgDT)
        self.groupBox = QtWidgets.QGroupBox(frmAccountOperationsAdd)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.radAccounts = QtWidgets.QRadioButton(self.groupBox)
        self.radAccounts.setObjectName("radAccounts")
        self.horizontalLayout_5.addWidget(self.radAccounts)
        self.cmbAccounts = QtWidgets.QComboBox(self.groupBox)
        self.cmbAccounts.setObjectName("cmbAccounts")
        self.horizontalLayout_5.addWidget(self.cmbAccounts)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.radCreditCards = QtWidgets.QRadioButton(self.groupBox)
        self.radCreditCards.setObjectName("radCreditCards")
        self.horizontalLayout_6.addWidget(self.radCreditCards)
        self.cmbCreditCards = QtWidgets.QComboBox(self.groupBox)
        self.cmbCreditCards.setObjectName("cmbCreditCards")
        self.horizontalLayout_6.addWidget(self.cmbCreditCards)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.verticalLayout.addWidget(self.groupBox)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(frmAccountOperationsAdd)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.cmbConcepts = QtWidgets.QComboBox(frmAccountOperationsAdd)
        self.cmbConcepts.setObjectName("cmbConcepts")
        self.horizontalLayout_3.addWidget(self.cmbConcepts)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(frmAccountOperationsAdd)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.txtImporte = myQLineEdit(frmAccountOperationsAdd)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtImporte.sizePolicy().hasHeightForWidth())
        self.txtImporte.setSizePolicy(sizePolicy)
        self.txtImporte.setObjectName("txtImporte")
        self.horizontalLayout.addWidget(self.txtImporte)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(frmAccountOperationsAdd)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.txtComentario = QtWidgets.QLineEdit(frmAccountOperationsAdd)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtComentario.sizePolicy().hasHeightForWidth())
        self.txtComentario.setSizePolicy(sizePolicy)
        self.txtComentario.setObjectName("txtComentario")
        self.horizontalLayout_4.addWidget(self.txtComentario)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.cmd = QtWidgets.QPushButton(frmAccountOperationsAdd)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/xulpymoney/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cmd.setIcon(icon1)
        self.cmd.setObjectName("cmd")
        self.verticalLayout.addWidget(self.cmd)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(frmAccountOperationsAdd)
        self.radAccounts.toggled['bool'].connect(self.cmbCreditCards.setDisabled)
        self.radCreditCards.toggled['bool'].connect(self.cmbAccounts.setDisabled)
        QtCore.QMetaObject.connectSlotsByName(frmAccountOperationsAdd)

    def retranslateUi(self, frmAccountOperationsAdd):
        _translate = QtCore.QCoreApplication.translate
        frmAccountOperationsAdd.setWindowTitle(_translate("frmAccountOperationsAdd", "New account operation"))
        self.radAccounts.setText(_translate("frmAccountOperationsAdd", "Se&lect an account"))
        self.radCreditCards.setText(_translate("frmAccountOperationsAdd", "Selec&t a credit card"))
        self.label_2.setText(_translate("frmAccountOperationsAdd", "Select a concept"))
        self.label_3.setText(_translate("frmAccountOperationsAdd", "Add an amount"))
        self.label_4.setText(_translate("frmAccountOperationsAdd", "Add a comment"))
        self.cmd.setText(_translate("frmAccountOperationsAdd", "Save"))
from xulpymoney.ui.myqlineedit import myQLineEdit
from xulpymoney.ui.wdgDatetime import wdgDatetime
import xulpymoney.images.xulpymoney_rc
