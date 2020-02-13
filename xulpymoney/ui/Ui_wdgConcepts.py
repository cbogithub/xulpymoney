# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'xulpymoney/ui/wdgConcepts.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_wdgConcepts(object):
    def setupUi(self, wdgConcepts):
        wdgConcepts.setObjectName("wdgConcepts")
        wdgConcepts.resize(754, 525)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/xulpymoney/books.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        wdgConcepts.setWindowIcon(icon)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(wdgConcepts)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lblTotal = QtWidgets.QLabel(wdgConcepts)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblTotal.setFont(font)
        self.lblTotal.setText("")
        self.lblTotal.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTotal.setObjectName("lblTotal")
        self.horizontalLayout_4.addWidget(self.lblTotal)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl = QtWidgets.QLabel(wdgConcepts)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl.setFont(font)
        self.lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl.setObjectName("lbl")
        self.verticalLayout.addWidget(self.lbl)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.wdgYM = wdgYearMonth(wdgConcepts)
        self.wdgYM.setObjectName("wdgYM")
        self.horizontalLayout_3.addWidget(self.wdgYM)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.tab = QtWidgets.QTabWidget(wdgConcepts)
        self.tab.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tab.setTabsClosable(True)
        self.tab.setObjectName("tab")
        self.tabExpenses = QtWidgets.QWidget()
        self.tabExpenses.setObjectName("tabExpenses")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tabExpenses)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.layExpenses = QtWidgets.QHBoxLayout()
        self.layExpenses.setObjectName("layExpenses")
        self.mqtwExpenses = myQTableWidget(self.tabExpenses)
        self.mqtwExpenses.setObjectName("mqtwExpenses")
        self.layExpenses.addWidget(self.mqtwExpenses)
        self.verticalLayout_3.addLayout(self.layExpenses)
        self.tab.addTab(self.tabExpenses, "")
        self.tabIncomes = QtWidgets.QWidget()
        self.tabIncomes.setObjectName("tabIncomes")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tabIncomes)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.layIncomes = QtWidgets.QHBoxLayout()
        self.layIncomes.setObjectName("layIncomes")
        self.mqtwIncomes = myQTableWidget(self.tabIncomes)
        self.mqtwIncomes.setObjectName("mqtwIncomes")
        self.layIncomes.addWidget(self.mqtwIncomes)
        self.verticalLayout_2.addLayout(self.layIncomes)
        self.tab.addTab(self.tabIncomes, "")
        self.verticalLayout.addWidget(self.tab)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.actionHistoricalReport = QtWidgets.QAction(wdgConcepts)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/xulpymoney/history.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHistoricalReport.setIcon(icon1)
        self.actionHistoricalReport.setObjectName("actionHistoricalReport")

        self.retranslateUi(wdgConcepts)
        self.tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(wdgConcepts)

    def retranslateUi(self, wdgConcepts):
        _translate = QtCore.QCoreApplication.translate
        self.lbl.setText(_translate("wdgConcepts", "Concepts report"))
        self.tab.setTabText(self.tab.indexOf(self.tabExpenses), _translate("wdgConcepts", "Expenses"))
        self.tab.setTabText(self.tab.indexOf(self.tabIncomes), _translate("wdgConcepts", "Incomes"))
        self.actionHistoricalReport.setText(_translate("wdgConcepts", "Historical report"))
        self.actionHistoricalReport.setToolTip(_translate("wdgConcepts", "Historical report"))
from xulpymoney.ui.myqtablewidget import myQTableWidget
from xulpymoney.ui.wdgYearMonth import wdgYearMonth
import xulpymoney.images.xulpymoney_rc
