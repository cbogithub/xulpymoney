# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'xulpymoney/ui/wdgCalculator.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_wdgCalculator(object):
    def setupUi(self, wdgCalculator):
        wdgCalculator.setObjectName("wdgCalculator")
        wdgCalculator.resize(1066, 852)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(wdgCalculator)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl = QtWidgets.QLabel(wdgCalculator)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl.setFont(font)
        self.lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl.setObjectName("lbl")
        self.verticalLayout.addWidget(self.lbl)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.label_7 = QtWidgets.QLabel(wdgCalculator)
        self.label_7.setMaximumSize(QtCore.QSize(64, 64))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap(":/xulpymoney/kcalc.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.groupBox = QtWidgets.QGroupBox(wdgCalculator)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.cmbProducts = QtWidgets.QComboBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbProducts.sizePolicy().hasHeightForWidth())
        self.cmbProducts.setSizePolicy(sizePolicy)
        self.cmbProducts.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.cmbProducts.setObjectName("cmbProducts")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.cmbProducts)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.cmbPrice = QtWidgets.QComboBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbPrice.sizePolicy().hasHeightForWidth())
        self.cmbPrice.setSizePolicy(sizePolicy)
        self.cmbPrice.setObjectName("cmbPrice")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.cmbPrice)
        self.txtProductPrice = myQLineEdit(self.groupBox)
        self.txtProductPrice.setEnabled(True)
        self.txtProductPrice.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txtProductPrice.setReadOnly(True)
        self.txtProductPrice.setObjectName("txtProductPrice")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txtProductPrice)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.spnProductPriceVariation = QtWidgets.QDoubleSpinBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spnProductPriceVariation.sizePolicy().hasHeightForWidth())
        self.spnProductPriceVariation.setSizePolicy(sizePolicy)
        self.spnProductPriceVariation.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spnProductPriceVariation.setMinimum(-99.99)
        self.spnProductPriceVariation.setObjectName("spnProductPriceVariation")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.spnProductPriceVariation)
        self.lblLeveraged = QtWidgets.QLabel(self.groupBox)
        self.lblLeveraged.setObjectName("lblLeveraged")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.lblLeveraged)
        self.txtLeveraged = myQLineEdit(self.groupBox)
        self.txtLeveraged.setEnabled(True)
        self.txtLeveraged.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txtLeveraged.setReadOnly(True)
        self.txtLeveraged.setObjectName("txtLeveraged")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.txtLeveraged)
        self.lblFinalPrice = QtWidgets.QLabel(self.groupBox)
        self.lblFinalPrice.setObjectName("lblFinalPrice")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.lblFinalPrice)
        self.txtFinalPrice = myQLineEdit(self.groupBox)
        self.txtFinalPrice.setEnabled(True)
        self.txtFinalPrice.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txtFinalPrice.setObjectName("txtFinalPrice")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.txtFinalPrice)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.cmbInvestments = QtWidgets.QComboBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbInvestments.sizePolicy().hasHeightForWidth())
        self.cmbInvestments.setSizePolicy(sizePolicy)
        self.cmbInvestments.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.cmbInvestments.setObjectName("cmbInvestments")
        self.horizontalLayout_6.addWidget(self.cmbInvestments)
        self.chkWithoutShares = QtWidgets.QCheckBox(self.groupBox)
        self.chkWithoutShares.setObjectName("chkWithoutShares")
        self.horizontalLayout_6.addWidget(self.chkWithoutShares)
        self.formLayout_2.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_6)
        self.horizontalLayout_3.addLayout(self.formLayout_2)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(wdgCalculator)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.lblAmount = QtWidgets.QLabel(self.groupBox_2)
        self.lblAmount.setObjectName("lblAmount")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblAmount)
        self.txtAmount = myQLineEdit(self.groupBox_2)
        self.txtAmount.setEnabled(True)
        self.txtAmount.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txtAmount.setObjectName("txtAmount")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txtAmount)
        self.lblShares = QtWidgets.QLabel(self.groupBox_2)
        self.lblShares.setObjectName("lblShares")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lblShares)
        self.txtShares = myQLineEdit(self.groupBox_2)
        self.txtShares.setEnabled(True)
        self.txtShares.setText("")
        self.txtShares.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txtShares.setReadOnly(True)
        self.txtShares.setObjectName("txtShares")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txtShares)
        self.horizontalLayout_2.addLayout(self.formLayout)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.cmdGraph = QtWidgets.QPushButton(wdgCalculator)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/xulpymoney/report.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cmdGraph.setIcon(icon)
        self.cmdGraph.setObjectName("cmdGraph")
        self.horizontalLayout_5.addWidget(self.cmdGraph)
        self.line = QtWidgets.QFrame(wdgCalculator)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_5.addWidget(self.line)
        self.cmdOrder = QtWidgets.QPushButton(wdgCalculator)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/xulpymoney/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cmdOrder.setIcon(icon1)
        self.cmdOrder.setObjectName("cmdOrder")
        self.horizontalLayout_5.addWidget(self.cmdOrder)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.groupBox_3 = QtWidgets.QGroupBox(wdgCalculator)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.mqtw = mqtw(self.groupBox_3)
        self.mqtw.setObjectName("mqtw")
        self.horizontalLayout.addWidget(self.mqtw)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.horizontalLayout_8.addLayout(self.verticalLayout)

        self.retranslateUi(wdgCalculator)
        QtCore.QMetaObject.connectSlotsByName(wdgCalculator)

    def retranslateUi(self, wdgCalculator):
        _translate = QtCore.QCoreApplication.translate
        self.lbl.setText(_translate("wdgCalculator", "Investment calculator"))
        self.groupBox.setTitle(_translate("wdgCalculator", "Product settings"))
        self.label_3.setText(_translate("wdgCalculator", "Select a product"))
        self.label.setText(_translate("wdgCalculator", "Select your personal investment"))
        self.label_2.setText(_translate("wdgCalculator", "Variation from current price"))
        self.spnProductPriceVariation.setSuffix(_translate("wdgCalculator", " %"))
        self.lblLeveraged.setText(_translate("wdgCalculator", "Leveraged product"))
        self.txtLeveraged.setText(_translate("wdgCalculator", "1"))
        self.lblFinalPrice.setText(_translate("wdgCalculator", "Final price"))
        self.chkWithoutShares.setText(_translate("wdgCalculator", "Without shares"))
        self.groupBox_2.setTitle(_translate("wdgCalculator", "Shares calc"))
        self.lblAmount.setText(_translate("wdgCalculator", "Amount to invest"))
        self.lblShares.setText(_translate("wdgCalculator", "Shares"))
        self.cmdGraph.setText(_translate("wdgCalculator", "Show purchase graph"))
        self.cmdOrder.setText(_translate("wdgCalculator", "Add order annotation"))
        self.groupBox_3.setTitle(_translate("wdgCalculator", "Calc estimations"))
from xulpymoney.ui.myqlineedit import myQLineEdit
from xulpymoney.ui.myqtablewidget import mqtw
import xulpymoney.images.xulpymoney_rc
