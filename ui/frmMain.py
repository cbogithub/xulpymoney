from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
from Ui_frmMain import *
from frmAbout import *
from libxulpymoney import *
from frmAccess import *
from wdgTotal import *
from wdgDividendsReport import *
from wdgInvestmentClasses import *
from wdgJointReport import *
from wdgAPR import *
from wdgAccounts import *
from wdgBanks import *
from wdgConcepts import *
from wdgCalculator import *
from wdgIndexRange import *
from wdgInvestments import *
from wdgInvestmentsOperations import *
from frmAuxiliarTables import *
from frmTransfer import *
from frmSettings import *
from frmHelp import *
from wdgProducts import *
from source_yahoohistorical import WorkerYahooHistorical

class frmMain(QMainWindow, Ui_frmMain):
    """Clase principal del programa"""
    def __init__(self, mem, parent = 0,  flags = False):
        QMainWindow.__init__(self, None)
        self.setupUi(self)
        self.showMaximized()
        self.setWindowTitle(self.trUtf8("Xulpymoney 2010-{0} ©".format(version[:4])))
        
        self.mem=mem
        self.sqlvacio="select * from products where id=-999999"
        
        self.w=QWidget()       
        
#        access2=frmAccess(self.mem, 1, self)
#        access2.exec_()
#        self.retranslateUi(self)
#        if access2.result()==QDialog.Rejected:
#            self.on_actionExit_activated()
#            sys.exit(1)

        access=frmAccess(self.mem, 2, self)
        access.exec_()
        self.retranslateUi(self)
        
        if access.result()==QDialog.Rejected:
            self.on_actionExit_activated()
            sys.exit(1)

        
        self.mem.actualizar_memoria() ##CARGA TODOS LOS DATOS Y LOS VINCULA       
        
        
        print ("Protecting products needed in xulpymoney")
        cur=self.mem.con.cursor()
        cur.execute("select distinct(mystocksid) from inversiones;")
        ids2protect=[]
        for row in cur:
            ids2protect.append(row[0])
        if len(ids2protect)>0:
            Product(self.mem).changeDeletable(  ids2protect,  False)
        self.mem.con.commit()
        
#        self.mem.data.load_inactives()
#        print ("==========================================")
#        Maintenance(self.mem).show_investments_status(datetime.date(2007, 2, 28))
#        print ("==========================================")
#        Maintenance(self.mem).show_investments_status(datetime.date(2007, 3, 30))
#        print ("==========================================")
#        Maintenance(self.mem).show_investments_status(datetime.date(2007, 4, 30))
#        print ("==========================================")

        
    @QtCore.pyqtSlot()  
    def on_actionExit_activated(self):
        self.mem.__del__()
        print ("App correctly closed")
        self.close()
        
    @pyqtSignature("")
    def on_actionAbout_activated(self):
        fr=frmAbout(self.mem, self, "frmabout")
        fr.open()

    @QtCore.pyqtSlot()  
    def on_actionBanks_activated(self):
        self.w.close()
        self.w=wdgBanks(self.mem)
                
        self.layout.addWidget(self.w)
        self.w.show()
        
    @QtCore.pyqtSlot()  
    def on_actionCalculator_activated(self):
        d=QDialog(self)        
        d.setFixedSize(670, 670)
        d.setWindowTitle(self.trUtf8("Investment calculator"))
        w=wdgCalculator(self.mem)
        lay = QVBoxLayout(d)
        lay.addWidget(w)
        d.show()
    @QtCore.pyqtSlot()  
    def on_actionConcepts_activated(self):
        self.w.close()
        self.w=wdgConcepts(self.mem)
                
        self.layout.addWidget(self.w)
        self.w.show()
        
    @QtCore.pyqtSlot()  
    def on_actionAccounts_activated(self):
        self.w.close()
        self.w=wdgAccounts(self.mem)
                
        self.layout.addWidget(self.w)
        self.w.show()
    
    @QtCore.pyqtSlot()  
    def on_actionMemory_activated(self):        
        self.mem.data.reload()
        
        
    @QtCore.pyqtSlot()  
    def on_actionDividendsReport_activated(self):
        self.w.close()
        self.w=wdgDividendsReport(self.mem)
                
        self.layout.addWidget(self.w)
        self.w.show()
        
    @QtCore.pyqtSlot()  
    def on_actionInvestmentsClasses_activated(self):
        self.w.close()
        self.w=wdgInvestmentClasses(self.mem)
                
        self.layout.addWidget(self.w)
        self.w.show()

    @QtCore.pyqtSlot()  
    def on_actionJointReport_activated(self):
        self.w.close()
        self.w=wdgJointReport(self.mem)
                
        self.layout.addWidget(self.w)
        self.w.show()        
            
    @QtCore.pyqtSlot()  
    def on_actionTotalReport_activated(self):
        self.w.close()
        self.w=wdgTotal(self.mem)
                
        self.layout.addWidget(self.w)
        self.w.show()

    @QtCore.pyqtSlot()  
    def on_actionReportAPR_activated(self):
        self.w.close()
        self.w=wdgAPR(self.mem)
              
        self.layout.addWidget(self.w)
        self.w.show()
        
    @QtCore.pyqtSlot()  
    def on_actionHelp_activated(self):
        w=frmHelp(self.mem)
        w.exec_()
    @QtCore.pyqtSlot()  
    def on_actionIndexRange_activated(self):
        self.w.close()
        self.w=wdgIndexRange(self.mem)
                
        self.layout.addWidget(self.w)
        self.w.show()

    @QtCore.pyqtSlot()  
    def on_actionInvestments_activated(self):
        self.w.close()
        self.w=wdgInvestments(self.mem)
               
        self.layout.addWidget(self.w)
        self.w.show()
        
    @QtCore.pyqtSlot()  
    def on_actionInvestmentsOperations_activated(self):
        self.w.close()
        self.w=wdgInvestmentsOperations(self.mem)
        self.layout.addWidget(self.w)
        self.w.show()

    @QtCore.pyqtSlot()  
    def on_actionAuxiliarTables_activated(self):
        w=frmAuxiliarTables(self.mem)
        w.exec_()
        
    @QtCore.pyqtSlot()  
    def on_actionSettings_activated(self):
        w=frmSettings(self.mem, self)
        w.exec_()
        self.retranslateUi(self)

    @QtCore.pyqtSlot()  
    def on_actionTransfer_activated(self):
        w=frmTransfer(self.mem)
        w.exec_()
        self.on_actionAccounts_activated()

#    def closeEvent(self,  event):
#        self.on_actionExit_activated()
################################
                
    @QtCore.pyqtSlot()  
    def on_actionCAC40_activated(self):
        self.w.close()
        self.w=wdgProducts(self.mem,  "select * from products where agrupations like '%|CAC|%' order by name,id")

        self.layout.addWidget(self.w)
        self.w.show()                
    @QtCore.pyqtSlot()  
    def on_actionActive_activated(self):
        self.w.close()
        self.w=wdgProducts(self.mem,  "select * from products where active=true order by name")

        self.layout.addWidget(self.w)
        self.w.show()
    
    @QtCore.pyqtSlot()  
    def on_actionCurrenciesAll_activated(self):
        self.w.close()
        self.w=wdgProducts(self.mem,  "select * from products where type=6 order by name,id")

        self.layout.addWidget(self.w)
        self.w.show()
    @QtCore.pyqtSlot()  
    def on_actionDividends_activated(self):
        """Shows products with current year estimations_dps and with quotes in current year"""
        self.w.close()
        self.w=wdgProducts(self.mem, "select * from products where id in (select id from estimations_dps where year=date_part('year',now()) and estimation is not null) and id in (select distinct(id) from quotes where date_part('year', datetime)=date_part('year',now()));")
#        self.w=wdgProducts(self.mem,  "select * from products where id in (select distinct(quotes.id) from quotes, estimations_dps where quotes.id=estimations_dps.id and year={0}  and estimation is not null );".format(datetime.date.today().year))
        
        self.layout.addWidget(self.w)
        self.w.on_actionSortDividend_activated()
        self.w.show()

    @QtCore.pyqtSlot()  
    def on_actionExport_activated(self):
        os.popen("pg_dump -U postgres -t quotes mystocks | sed -e 's:quotes:export:' | gzip > "+os.environ['HOME']+"/.mystocks/dump-%s.txt.gz" % str(datetime.date.today()))
        m=QMessageBox()
        m.setText(QApplication.translate("Core","Se ha exportado con éxito la tabla quotes"))
        m.exec_()      

    @QtCore.pyqtSlot()  
    def on_actionImport_activated(self):
        filename=(QFileDialog.getOpenFileName(self, self.tr("Selecciona el fichero a importar"), os.environ['HOME']+ "/.mystocks/", "Gzipped text (*.txt.gz)"))
        inicio=datetime.datetime.now()
        con=self.mem.connect_xulpymoney()
        cur = con.cursor()
        print ("Importando la tabla export")
        os.popen("zcat " + filename  + " | psql -U postgres mystocks")
        cur.execute("insert into quotes(select * from export where code||date::text in (select code||date::text from export except select code||date::text from quotes));") #solo los que faltan no los modificados que sería select * en los dos lados
        con.commit()
        estado=cur.statusmessage
        print ("Borrando la tabla export y sus índices")
        cur.execute("drop table export;")
        con.commit()        
        cur.execute("DROP INDEX index_export_unik;")
        con.commit()
        cur.execute("DROP INDEX index_export_unik2;")
        con.commit()
        cur.close()
        self.mem.disconnect_xulpymoneyd(con)      
        fin=datetime.datetime.now()
        
        m=QMessageBox()
        m.setText("Ha tardado %s y ha salido con mensaje de estado %s" % (str(fin-inicio),  estado))
        m.exec_()            


        
    @QtCore.pyqtSlot()  
    def on_actionNasdaq100_activated(self):
        self.w.close()
        self.w=wdgProducts(self.mem,  "select * from products where agrupations like '%|NASDAQ100|%' order by name,id")

        self.layout.addWidget(self.w)
        self.w.show()
            
    @QtCore.pyqtSlot()  
    def on_actionISINDuplicado_activated(self):
        self.w.close()
        cur=self.mem.con.cursor()
        #ßaca los isin duplicados buscando distintct isin, bolsa con mas de dos registros
        cur.execute("select isin, id_bolsas, count(*) as num from products  where isin!='' group by isin, id_bolsas having count(*)>1 order by num desc;")
        isins=set([])
        for row in cur:
            isins.add(row['isin'] )
        if len(isins)>0:
            self.w=wdgProducts(self.mem,  "select * from products where isin in ("+list2string(list(isins))+") order by isin, id_bolsas")
        else:
            self.w=wdgProducts(self.mem, self.sqlvacio)

        self.layout.addWidget(self.w)
        self.w.show()
        
    @QtCore.pyqtSlot()  
    def on_actionMC_activated(self):
        self.w.close()
        self.w=wdgProducts(self.mem, "select * from products where agrupations like '%|MERCADOCONTINUO|%' order by name,id")

        self.layout.addWidget(self.w)
        self.w.show()
        

    @QtCore.pyqtSlot()  
    def on_actionETFAll_activated(self):
        self.w.close()
        self.w=wdgProducts(self.mem,  "select * from products where type=4 order by name, id")

        self.layout.addWidget(self.w)
        self.w.show()
        
    @QtCore.pyqtSlot()  
    def on_actionEurostoxx50_activated(self):
        self.w.close()
        self.w=wdgProducts(self.mem,  "select * from products where agrupations like '%|EUROSTOXX|%' order by name,id")

        self.layout.addWidget(self.w)
        self.w.show()
        

    @QtCore.pyqtSlot()  
    def on_actionFavorites_activated(self):
        favoritos=self.mem.config.get_list("wdgProducts",  "favoritos")
        if len(favoritos)==0:
            m=QMessageBox()
            m.setIcon(QMessageBox.Information)
            m.setText(self.trUtf8("No se ha seleccionado ningún favorito"))
            m.exec_()     
            return
        self.w.close()
        self.w=wdgProducts(self.mem,  "select * from products where id in ("+str(favoritos)[1:-1]+") order by name, id")

        self.layout.addWidget(self.w)
        self.w.show()

    @QtCore.pyqtSlot()  
    def on_actionSharesAll_activated(self):
        self.w.close()
        self.w=wdgProducts(self.mem,  "select * from products where type=1 order by name, id")

        self.layout.addWidget(self.w)
        self.w.show()          
    @QtCore.pyqtSlot()  
    def on_actionWarrantsAll_activated(self):
        self.w.close()
        self.w=wdgProducts(self.mem,  "select * from products where type=5 order by name, id")

        self.layout.addWidget(self.w)
        self.w.show()          
        
    @QtCore.pyqtSlot()  
    def on_actionWarrantsCall_activated(self):
        self.w.close()
        self.w=wdgProducts(self.mem,  "select * from products where type=5 and pci='c' order by name, id")

        self.layout.addWidget(self.w)
        self.w.show()              
    @QtCore.pyqtSlot()  
    def on_actionWarrantsPut_activated(self):
        self.w.close()
        self.w=wdgProducts(self.mem,  "select * from products where type=5 and pci='p' order by name, id")

        self.layout.addWidget(self.w)
        self.w.show()              
    @QtCore.pyqtSlot()  
    def on_actionWarrantsInline_activated(self):
        self.w.close()
        self.w=wdgProducts(self.mem,  "select * from products where type=5 and pci='i' order by name, id")

        self.layout.addWidget(self.w)
        self.w.show()      
    @QtCore.pyqtSlot()  
    def on_actionFundsAll_activated(self):
        self.w.close()
        self.w=wdgProducts(self.mem,  "select * from products where type=2 order by name, id")

        self.layout.addWidget(self.w)
        self.w.show()                        

    @QtCore.pyqtSlot()  
    def on_actionBondsPublic_activated(self):
        self.w.close()
        self.w=wdgProducts(self.mem,  "select * from products where type=7 order by name, id")

        self.layout.addWidget(self.w)
        self.w.show()                        

    @QtCore.pyqtSlot()  
    def on_actionBondsPrivate_activated(self):
        self.w.close()
        self.w=wdgProducts(self.mem,  "select * from products where type=9 order by name, id")

        self.layout.addWidget(self.w)
        self.w.show()

    @QtCore.pyqtSlot()  
    def on_actionPurgeAll_activated(self):
        """Purga todas las quotes de todas inversión. """
        products=[]
        curms=self.mem.con.cursor()
        curms.execute("select * from products where id in ( select distinct( id) from quotes) order by name;")
        for row in curms:
            products.append(Product(self.mem).init__db_row(row))
        curms.close()
               
        
        pd= QProgressDialog(QApplication.translate("Core","Purging innecesary data from all products"), QApplication.translate("Core","Cancel"), 0,len(products))
        pd.setModal(True)
        pd.setWindowTitle(QApplication.translate("Core","Purging quotes from all products"))
        pd.setMinimumDuration(0)          
        counter=0      
        
        for i, inv in enumerate(products):
            pd.setValue(i)
            pd.setLabelText(QApplication.translate("Core","Purging quotes from {0}.\nTotal purged in global process: {1}".format(inv.name,  counter)))
            pd.update()
            QApplication.processEvents()
            if pd.wasCanceled():
                self.mem.con.rollback()
                return
            pd.update()
            QApplication.processEvents()
            pd.update()            
            inv.result.all.load_from_db(inv)
            invcounter=inv.result.all.purge(progress=True)
            if invcounter==None:#Pulsado cancelar
                self.mem.con.rollback()
                break
            else:
                counter=counter+invcounter
                self.mem.con.commit()
        
        m=QMessageBox()
        m.setIcon(QMessageBox.Information)
        m.setText(self.trUtf8("{0} quotes have been purged from {1} products".format(counter, len(products))))
        m.exec_()    
        
    @QtCore.pyqtSlot()  
    def on_actionBondsAll_activated(self):
        self.w.close()
        self.w=wdgProducts(self.mem,  "select * from products where type in (7,9) order by name, id")

        self.layout.addWidget(self.w)
        self.w.show()

        

    @QtCore.pyqtSlot()  
    def on_actionIbex35_activated(self):
        self.w.close()
        self.w=wdgProducts(self.mem,  "select  * from products where agrupations like '%|IBEX|%' order by name,id")
        self.layout.addWidget(self.w)
        self.w.show()        

    @QtCore.pyqtSlot()  
    def on_actionLATIBEX_activated(self):
        self.w.close()
        self.w=wdgProducts(self.mem,  "select  * from products where agrupations like '%|LATIBEX|%' order by name,id")
        self.layout.addWidget(self.w)
        self.w.show()
        
    @QtCore.pyqtSlot()  
    def on_actionIndexesAll_activated(self):
        self.w.close()
        self.w=wdgProducts(self.mem,  "select  * from products where type=3 order by id_bolsas,name")
        self.layout.addWidget(self.w)
        self.w.show()        
                
    @QtCore.pyqtSlot()  
    def on_actionSP500_activated(self):
        self.w.close()
        self.w=wdgProducts(self.mem,  "select * from products where agrupations like '%|SP500|%' order by name,id")

        self.layout.addWidget(self.w)
        self.w.show()
    
    @QtCore.pyqtSlot()  
    def on_actionInvestmentsDesaparecidas_activated(self):
        self.w.close()
        self.w=wdgProducts(self.mem,  "select * from products where obsolete=true order by name,id")

        self.layout.addWidget(self.w)
        self.w.show()
                
    @QtCore.pyqtSlot()  
    def on_actionInvestmentsSinActualizar_activated(self):
        self.w.close()
        self.w=wdgProducts(self.mem,  "select * from products where id in( select id  from quotes group by id having last(datetime::date)<now()::date-60)")

        self.layout.addWidget(self.w)
        self.w.show()       
    
    @QtCore.pyqtSlot()  
    def on_actionInvestmentsSinActualizarHistoricos_activated(self):
        self.w.close()
        self.w=wdgProducts(self.mem, "select * from products where id in (select id from quotes  group by id having date_part('microsecond',last(datetime))=4 and last(datetime)<now()-interval '60 days' );")

        self.layout.addWidget(self.w)
        self.w.show()            
        
    @QtCore.pyqtSlot()  
    def on_actionInvestmentsManual_activated(self):
        self.w.close()
        self.w=wdgProducts(self.mem,  "select * from products where id<0 order by name, id ")

        self.layout.addWidget(self.w)
        self.w.show()
        
    @QtCore.pyqtSlot()  
    def on_actionInvestmentsSinISIN_activated(self):
        self.w.close()
        self.w=wdgProducts(self.mem,  "select * from products  where isin is null or isin ='' order by name,id")

        self.layout.addWidget(self.w)
        self.w.show()


    @QtCore.pyqtSlot()  
    def on_actionInvestmentsSinNombre_activated(self):
        self.w.close()
        self.w=wdgProducts(self.mem,  "select * from products  where name is null or name='' order by name,id")

        self.layout.addWidget(self.w)
        self.w.show()

        
    @QtCore.pyqtSlot()  
    def on_actionTablasAuxiliares_activated(self):
        w=frmAuxiliarTables(self.mem)
        w.tblTipos_reload()
        w.exec_()

                
    @QtCore.pyqtSlot()  
    def on_actionXetra_activated(self):
        self.w.close()
        self.w=wdgProducts(self.mem,  "select * from products where agrupations like '%|DAX|%' order by name,id")

        self.layout.addWidget(self.w)
        self.w.show()        
        
    @QtCore.pyqtSlot()  
    def on_actionSearch_activated(self):
        self.w.close()
        self.w=wdgProducts(self.mem,  self.sqlvacio)

        self.layout.addWidget(self.w)
        self.w.show()
        

    @QtCore.pyqtSlot()  
    def on_actionPriceUpdates_activated(self):  
        w=WorkerYahooHistorical(self.mem)
        w.start()           
