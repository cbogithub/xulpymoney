# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/wdgInvestments.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_wdgInvestments(object):
    def setupUi(self, wdgInvestments):
        wdgInvestments.setObjectName("wdgInvestments")
        wdgInvestments.resize(754, 525)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(wdgInvestments)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl = QtWidgets.QLabel(wdgInvestments)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl.setFont(font)
        self.lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl.setObjectName("lbl")
        self.verticalLayout.addWidget(self.lbl)
        self.chkInactivas = QtWidgets.QCheckBox(wdgInvestments)
        self.chkInactivas.setObjectName("chkInactivas")
        self.verticalLayout.addWidget(self.chkInactivas)
        self.tblInvestments = myQTableWidget(wdgInvestments)
        self.tblInvestments.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tblInvestments.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblInvestments.setAlternatingRowColors(True)
        self.tblInvestments.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tblInvestments.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tblInvestments.setObjectName("tblInvestments")
        self.tblInvestments.setColumnCount(9)
        self.tblInvestments.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblInvestments.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblInvestments.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblInvestments.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblInvestments.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblInvestments.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblInvestments.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblInvestments.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblInvestments.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblInvestments.setHorizontalHeaderItem(8, item)
        self.tblInvestments.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tblInvestments)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.wdgIBM = QtWidgets.QWidget(wdgInvestments)
        self.wdgIBM.setObjectName("wdgIBM")
        self.verticalLayout_2.addWidget(self.wdgIBM)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.lblTotal = QtWidgets.QLabel(wdgInvestments)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lblTotal.setFont(font)
        self.lblTotal.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTotal.setWordWrap(True)
        self.lblTotal.setObjectName("lblTotal")
        self.verticalLayout_3.addWidget(self.lblTotal)
        self.actionInvestmentAdd = QtWidgets.QAction(wdgInvestments)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/xulpymoney/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionInvestmentAdd.setIcon(icon)
        self.actionInvestmentAdd.setObjectName("actionInvestmentAdd")
        self.actionInvestmentReport = QtWidgets.QAction(wdgInvestments)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/xulpymoney/bundle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionInvestmentReport.setIcon(icon1)
        self.actionInvestmentReport.setObjectName("actionInvestmentReport")
        self.actionSortTPCDiario = QtWidgets.QAction(wdgInvestments)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/xulpmoney/document-preview.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSortTPCDiario.setIcon(icon2)
        self.actionSortTPCDiario.setObjectName("actionSortTPCDiario")
        self.actionSortTPCVenta = QtWidgets.QAction(wdgInvestments)
        self.actionSortTPCVenta.setIcon(icon2)
        self.actionSortTPCVenta.setObjectName("actionSortTPCVenta")
        self.actionSortTPC = QtWidgets.QAction(wdgInvestments)
        self.actionSortTPC.setIcon(icon2)
        self.actionSortTPC.setObjectName("actionSortTPC")
        self.actionSortName = QtWidgets.QAction(wdgInvestments)
        self.actionSortName.setIcon(icon2)
        self.actionSortName.setObjectName("actionSortName")
        self.actionSortHour = QtWidgets.QAction(wdgInvestments)
        self.actionSortHour.setIcon(icon2)
        self.actionSortHour.setObjectName("actionSortHour")
        self.actionActive = QtWidgets.QAction(wdgInvestments)
        self.actionActive.setObjectName("actionActive")
        self.actionProduct = QtWidgets.QAction(wdgInvestments)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/xulpymoney/books.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionProduct.setIcon(icon3)
        self.actionProduct.setObjectName("actionProduct")
        self.actionProductPrice = QtWidgets.QAction(wdgInvestments)
        self.actionProductPrice.setIcon(icon)
        self.actionProductPrice.setObjectName("actionProductPrice")
        self.actionInvestmentDelete = QtWidgets.QAction(wdgInvestments)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/xulpymoney/list-remove.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionInvestmentDelete.setIcon(icon4)
        self.actionInvestmentDelete.setObjectName("actionInvestmentDelete")
        self.actionProductPriceLastRemove = QtWidgets.QAction(wdgInvestments)
        self.actionProductPriceLastRemove.setIcon(icon4)
        self.actionProductPriceLastRemove.setObjectName("actionProductPriceLastRemove")
        self.actionSameProduct = QtWidgets.QAction(wdgInvestments)
        self.actionSameProduct.setIcon(icon1)
        self.actionSameProduct.setObjectName("actionSameProduct")
        self.actionSameProductFIFO = QtWidgets.QAction(wdgInvestments)
        self.actionSameProductFIFO.setIcon(icon1)
        self.actionSameProductFIFO.setObjectName("actionSameProductFIFO")

        self.retranslateUi(wdgInvestments)
        QtCore.QMetaObject.connectSlotsByName(wdgInvestments)

    def retranslateUi(self, wdgInvestments):
        _translate = QtCore.QCoreApplication.translate
        self.lbl.setText(_translate("wdgInvestments", "Investments list"))
        self.chkInactivas.setText(_translate("wdgInvestments", "Show inactive investments"))
        item = self.tblInvestments.horizontalHeaderItem(0)
        item.setText(_translate("wdgInvestments", "Investment"))
        item = self.tblInvestments.horizontalHeaderItem(1)
        item.setText(_translate("wdgInvestments", "Last datetime"))
        item = self.tblInvestments.horizontalHeaderItem(2)
        item.setText(_translate("wdgInvestments", "Last value"))
        item = self.tblInvestments.horizontalHeaderItem(3)
        item.setText(_translate("wdgInvestments", "Daily difference"))
        item = self.tblInvestments.horizontalHeaderItem(4)
        item.setText(_translate("wdgInvestments", "% Intraday"))
        item = self.tblInvestments.horizontalHeaderItem(5)
        item.setText(_translate("wdgInvestments", "Balance"))
        item = self.tblInvestments.horizontalHeaderItem(6)
        item.setText(_translate("wdgInvestments", "Pending"))
        item = self.tblInvestments.horizontalHeaderItem(7)
        item.setText(_translate("wdgInvestments", "% Invested"))
        item = self.tblInvestments.horizontalHeaderItem(8)
        item.setText(_translate("wdgInvestments", "% Selling point"))
        self.actionInvestmentAdd.setText(_translate("wdgInvestments", "New investment"))
        self.actionInvestmentAdd.setToolTip(_translate("wdgInvestments", "New investment"))
        self.actionInvestmentReport.setText(_translate("wdgInvestments", "Investment report"))
        self.actionInvestmentReport.setToolTip(_translate("wdgInvestments", "Investment report"))
        self.actionSortTPCDiario.setText(_translate("wdgInvestments", "% Daily"))
        self.actionSortTPCDiario.setToolTip(_translate("wdgInvestments", "% Daily"))
        self.actionSortTPCVenta.setText(_translate("wdgInvestments", "% Selling point"))
        self.actionSortTPCVenta.setToolTip(_translate("wdgInvestments", "% Selling point"))
        self.actionSortTPC.setText(_translate("wdgInvestments", "% Invested"))
        self.actionSortTPC.setToolTip(_translate("wdgInvestments", "% Invested"))
        self.actionSortName.setText(_translate("wdgInvestments", "Name"))
        self.actionSortName.setToolTip(_translate("wdgInvestments", "Name"))
        self.actionSortHour.setText(_translate("wdgInvestments", "Time"))
        self.actionSortHour.setToolTip(_translate("wdgInvestments", "Time"))
        self.actionActive.setText(_translate("wdgInvestments", "Is it active?"))
        self.actionActive.setToolTip(_translate("wdgInvestments", "Is it active?"))
        self.actionProduct.setText(_translate("wdgInvestments", "Product report"))
        self.actionProduct.setToolTip(_translate("wdgInvestments", "Product report"))
        self.actionProductPrice.setText(_translate("wdgInvestments", "Add product price"))
        self.actionProductPrice.setToolTip(_translate("wdgInvestments", "Add product price"))
        self.actionInvestmentDelete.setText(_translate("wdgInvestments", "Delete investment"))
        self.actionInvestmentDelete.setToolTip(_translate("wdgInvestments", "Delete investment"))
        self.actionProductPriceLastRemove.setText(_translate("wdgInvestments", "Remove last product price"))
        self.actionProductPriceLastRemove.setToolTip(_translate("wdgInvestments", "Remove last product price"))
        self.actionSameProduct.setText(_translate("wdgInvestments", "Same product Investments merging current operations"))
        self.actionSameProduct.setToolTip(_translate("wdgInvestments", "Same product Investments merging current operations"))
        self.actionSameProductFIFO.setText(_translate("wdgInvestments", "Same product Investments merging operations"))
        self.actionSameProductFIFO.setToolTip(_translate("wdgInvestments", "Same product Investments merging operations"))

from myqtablewidget import myQTableWidget
import xulpymoney_rc
