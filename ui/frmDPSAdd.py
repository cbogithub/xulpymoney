from libxulpymoney import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Ui_frmDPSAdd import *

class frmDPSAdd(QDialog, Ui_frmDPSAdd):
    def __init__(self, cfg,  investment,   parent=None):
        """type="dps or "eps" """
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.cfg=cfg
        self.investment=investment
        self.dps=None
        self.lbl.setText(self.trUtf8("New DPS"))

    def on_cmd_released(self):
        self.dps=DPS(self.cfg, self.investment).init__create(self.calendar.selectedDate().toPyDate(), self.txtGross.decimal())
        self.dps.save()
        self.cfg.conms.commit()      
        self.investment.dps.arr.append(self.dps)
        self.accept()