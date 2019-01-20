# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'xulpymoney/ui/wdgBanks.ui'
#
# Created by: PyQt5 UI code generator 5.12.dev1812231618
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_wdgBanks(object):
    def setupUi(self, wdgBanks):
        wdgBanks.setObjectName("wdgBanks")
        wdgBanks.resize(826, 591)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/xulpymoney/bank.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        wdgBanks.setWindowIcon(icon)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(wdgBanks)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lbl = QtWidgets.QLabel(wdgBanks)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl.setFont(font)
        self.lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl.setObjectName("lbl")
        self.verticalLayout_2.addWidget(self.lbl)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.chkActives = QtWidgets.QCheckBox(wdgBanks)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chkActives.sizePolicy().hasHeightForWidth())
        self.chkActives.setSizePolicy(sizePolicy)
        self.chkActives.setChecked(True)
        self.chkActives.setObjectName("chkActives")
        self.verticalLayout.addWidget(self.chkActives)
        self.line = QtWidgets.QFrame(wdgBanks)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.groupBox_3 = QtWidgets.QGroupBox(wdgBanks)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.tblEB = myQTableWidget(self.groupBox_3)
        self.tblEB.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tblEB.setAlternatingRowColors(True)
        self.tblEB.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tblEB.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tblEB.setObjectName("tblEB")
        self.tblEB.setColumnCount(3)
        self.tblEB.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblEB.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblEB.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblEB.setHorizontalHeaderItem(2, item)
        self.tblEB.verticalHeader().setVisible(False)
        self.horizontalLayout_4.addWidget(self.tblEB)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.groupBox_2 = QtWidgets.QGroupBox(wdgBanks)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tblAccounts = myQTableWidget(self.groupBox_2)
        self.tblAccounts.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tblAccounts.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tblAccounts.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tblAccounts.setObjectName("tblAccounts")
        self.tblAccounts.setColumnCount(3)
        self.tblAccounts.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblAccounts.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblAccounts.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblAccounts.setHorizontalHeaderItem(2, item)
        self.tblAccounts.verticalHeader().setVisible(False)
        self.horizontalLayout_2.addWidget(self.tblAccounts)
        self.horizontalLayout_3.addWidget(self.groupBox_2)
        self.groupBox = QtWidgets.QGroupBox(wdgBanks)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tblInvestments = myQTableWidget(self.groupBox)
        self.tblInvestments.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tblInvestments.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tblInvestments.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tblInvestments.setObjectName("tblInvestments")
        self.tblInvestments.setColumnCount(3)
        self.tblInvestments.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblInvestments.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblInvestments.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblInvestments.setHorizontalHeaderItem(2, item)
        self.tblInvestments.verticalHeader().setVisible(False)
        self.horizontalLayout.addWidget(self.tblInvestments)
        self.horizontalLayout_3.addWidget(self.groupBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.actionInvestmentReport = QtWidgets.QAction(wdgBanks)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/xulpymoney/report2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionInvestmentReport.setIcon(icon1)
        self.actionInvestmentReport.setObjectName("actionInvestmentReport")
        self.actionAccountReport = QtWidgets.QAction(wdgBanks)
        self.actionAccountReport.setIcon(icon1)
        self.actionAccountReport.setObjectName("actionAccountReport")
        self.actionBankAdd = QtWidgets.QAction(wdgBanks)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/xulpymoney/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBankAdd.setIcon(icon2)
        self.actionBankAdd.setObjectName("actionBankAdd")
        self.actionBankDelete = QtWidgets.QAction(wdgBanks)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/xulpymoney/button_cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBankDelete.setIcon(icon3)
        self.actionBankDelete.setObjectName("actionBankDelete")
        self.actionBankEdit = QtWidgets.QAction(wdgBanks)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/xulpymoney/editar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBankEdit.setIcon(icon4)
        self.actionBankEdit.setObjectName("actionBankEdit")
        self.actionActive = QtWidgets.QAction(wdgBanks)
        self.actionActive.setCheckable(True)
        self.actionActive.setObjectName("actionActive")

        self.retranslateUi(wdgBanks)
        QtCore.QMetaObject.connectSlotsByName(wdgBanks)

    def retranslateUi(self, wdgBanks):
        _translate = QtCore.QCoreApplication.translate
        self.lbl.setText(_translate("wdgBanks", "Banks list"))
        self.chkActives.setText(_translate("wdgBanks", "Show only active entities"))
        self.groupBox_3.setTitle(_translate("wdgBanks", "Banks"))
        item = self.tblEB.horizontalHeaderItem(0)
        item.setText(_translate("wdgBanks", "Banks"))
        item = self.tblEB.horizontalHeaderItem(1)
        item.setText(_translate("wdgBanks", "Active"))
        item = self.tblEB.horizontalHeaderItem(2)
        item.setText(_translate("wdgBanks", "Balance"))
        self.groupBox_2.setTitle(_translate("wdgBanks", "Accounts"))
        item = self.tblAccounts.horizontalHeaderItem(0)
        item.setText(_translate("wdgBanks", "Account"))
        item = self.tblAccounts.horizontalHeaderItem(1)
        item.setText(_translate("wdgBanks", "Active"))
        item = self.tblAccounts.horizontalHeaderItem(2)
        item.setText(_translate("wdgBanks", "Balance"))
        self.groupBox.setTitle(_translate("wdgBanks", "Investments"))
        item = self.tblInvestments.horizontalHeaderItem(0)
        item.setText(_translate("wdgBanks", "Investment"))
        item = self.tblInvestments.horizontalHeaderItem(1)
        item.setText(_translate("wdgBanks", "Active"))
        item = self.tblInvestments.horizontalHeaderItem(2)
        item.setText(_translate("wdgBanks", "Balance"))
        self.actionInvestmentReport.setText(_translate("wdgBanks", "Investment report"))
        self.actionInvestmentReport.setToolTip(_translate("wdgBanks", "Investment report"))
        self.actionAccountReport.setText(_translate("wdgBanks", "Account report"))
        self.actionAccountReport.setToolTip(_translate("wdgBanks", "Account report"))
        self.actionBankAdd.setText(_translate("wdgBanks", "New bank"))
        self.actionBankAdd.setToolTip(_translate("wdgBanks", "New bank"))
        self.actionBankDelete.setText(_translate("wdgBanks", "Delete bank"))
        self.actionBankDelete.setToolTip(_translate("wdgBanks", "Delete bank"))
        self.actionBankEdit.setText(_translate("wdgBanks", "Edit bank"))
        self.actionBankEdit.setToolTip(_translate("wdgBanks", "Edit bank"))
        self.actionActive.setText(_translate("wdgBanks", "Is it active?"))
        self.actionActive.setToolTip(_translate("wdgBanks", "Is it active?"))

from xulpymoney.ui.myqtablewidget import myQTableWidget
import xulpymoney.images.xulpymoney_rc
