# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'xulpymoney/ui/frmSplitManual.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_frmSplitManual(object):
    def setupUi(self, frmSplitManual):
        frmSplitManual.setObjectName("frmSplitManual")
        frmSplitManual.resize(872, 477)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/xulpymoney/study.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        frmSplitManual.setWindowIcon(icon)
        frmSplitManual.setSizeGripEnabled(True)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(frmSplitManual)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(frmSplitManual)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.wdgDtStart = wdgDatetime(frmSplitManual)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wdgDtStart.sizePolicy().hasHeightForWidth())
        self.wdgDtStart.setSizePolicy(sizePolicy)
        self.wdgDtStart.setObjectName("wdgDtStart")
        self.horizontalLayout_3.addWidget(self.wdgDtStart)
        self.line = QtWidgets.QFrame(frmSplitManual)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_3.addWidget(self.line)
        self.wdgDtEnd = wdgDatetime(frmSplitManual)
        self.wdgDtEnd.setObjectName("wdgDtEnd")
        self.horizontalLayout_3.addWidget(self.wdgDtEnd)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(frmSplitManual)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.txtInitial = myQLineEdit(frmSplitManual)
        self.txtInitial.setAlignment(QtCore.Qt.AlignCenter)
        self.txtInitial.setObjectName("txtInitial")
        self.verticalLayout.addWidget(self.txtInitial)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(frmSplitManual)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.txtFinal = myQLineEdit(frmSplitManual)
        self.txtFinal.setAlignment(QtCore.Qt.AlignCenter)
        self.txtFinal.setObjectName("txtFinal")
        self.verticalLayout_2.addWidget(self.txtFinal)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.lblExample = QtWidgets.QLabel(frmSplitManual)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblExample.setFont(font)
        self.lblExample.setAlignment(QtCore.Qt.AlignCenter)
        self.lblExample.setWordWrap(True)
        self.lblExample.setObjectName("lblExample")
        self.verticalLayout_3.addWidget(self.lblExample)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.buttonbox = QtWidgets.QDialogButtonBox(frmSplitManual)
        self.buttonbox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonbox.setCenterButtons(True)
        self.buttonbox.setObjectName("buttonbox")
        self.horizontalLayout_2.addWidget(self.buttonbox)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)

        self.retranslateUi(frmSplitManual)
        QtCore.QMetaObject.connectSlotsByName(frmSplitManual)

    def retranslateUi(self, frmSplitManual):
        _translate = QtCore.QCoreApplication.translate
        frmSplitManual.setWindowTitle(_translate("frmSplitManual", "Split / Contrasplit relation"))
        self.label.setText(_translate("frmSplitManual", "Manual Split / Contrasplit to adjust split directly on prices (Not recomended)"))
        self.label_2.setText(_translate("frmSplitManual", "Current Shares"))
        self.txtInitial.setText(_translate("frmSplitManual", "1"))
        self.label_3.setText(_translate("frmSplitManual", "Final Shares"))
        self.txtFinal.setText(_translate("frmSplitManual", "10"))


from xulpymoney.ui.myqlineedit import myQLineEdit
from xulpymoney.ui.wdgDatetime import wdgDatetime
import xulpymoney.images.xulpymoney_rc
