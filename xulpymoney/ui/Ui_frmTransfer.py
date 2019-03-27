# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'xulpymoney/ui/frmTransfer.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_frmTransfer(object):
    def setupUi(self, frmTransfer):
        frmTransfer.setObjectName("frmTransfer")
        frmTransfer.setWindowModality(QtCore.Qt.WindowModal)
        frmTransfer.resize(612, 246)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/xulpymoney/transfer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        frmTransfer.setWindowIcon(icon)
        frmTransfer.setModal(True)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(frmTransfer)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblTitulo = QtWidgets.QLabel(frmTransfer)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lblTitulo.setFont(font)
        self.lblTitulo.setStyleSheet("color: rgb(0, 128, 0);")
        self.lblTitulo.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTitulo.setObjectName("lblTitulo")
        self.verticalLayout.addWidget(self.lblTitulo)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.wdgDT = wdgDatetime(frmTransfer)
        self.wdgDT.setObjectName("wdgDT")
        self.horizontalLayout_2.addWidget(self.wdgDT)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(frmTransfer)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.cmbOrigen = QtWidgets.QComboBox(frmTransfer)
        self.cmbOrigen.setObjectName("cmbOrigen")
        self.horizontalLayout_3.addWidget(self.cmbOrigen)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(frmTransfer)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.cmbDestino = QtWidgets.QComboBox(frmTransfer)
        self.cmbDestino.setObjectName("cmbDestino")
        self.horizontalLayout_5.addWidget(self.cmbDestino)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(frmTransfer)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.txtImporte = myQLineEdit(frmTransfer)
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
        self.label_4 = QtWidgets.QLabel(frmTransfer)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.txtComision = myQLineEdit(frmTransfer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtComision.sizePolicy().hasHeightForWidth())
        self.txtComision.setSizePolicy(sizePolicy)
        self.txtComision.setObjectName("txtComision")
        self.horizontalLayout_4.addWidget(self.txtComision)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.cmd = QtWidgets.QPushButton(frmTransfer)
        self.cmd.setIcon(icon)
        self.cmd.setObjectName("cmd")
        self.verticalLayout.addWidget(self.cmd)
        self.horizontalLayout_6.addLayout(self.verticalLayout)

        self.retranslateUi(frmTransfer)
        QtCore.QMetaObject.connectSlotsByName(frmTransfer)

    def retranslateUi(self, frmTransfer):
        _translate = QtCore.QCoreApplication.translate
        frmTransfer.setWindowTitle(_translate("frmTransfer", "Account transfer"))
        self.lblTitulo.setText(_translate("frmTransfer", "Transfer"))
        self.label_2.setText(_translate("frmTransfer", "Select origin account"))
        self.label_5.setText(_translate("frmTransfer", "Select destiny account"))
        self.label_3.setText(_translate("frmTransfer", "Amount"))
        self.txtImporte.setToolTip(_translate("frmTransfer", "Amount must be positive"))
        self.txtImporte.setText(_translate("frmTransfer", "0"))
        self.label_4.setText(_translate("frmTransfer", "Comission"))
        self.txtComision.setToolTip(_translate("frmTransfer", "Amount must be positive"))
        self.txtComision.setText(_translate("frmTransfer", "0"))
        self.cmd.setText(_translate("frmTransfer", "Transfer"))


from xulpymoney.ui.myqlineedit import myQLineEdit
from xulpymoney.ui.wdgDatetime import wdgDatetime
import xulpymoney.images.xulpymoney_rc
