## -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
#from apoyo import *
from core import *
from Ui_wdgInformeHistorico import *

class wdgInformeHistorico(QWidget, Ui_wdgInformeHistorico):
    def __init__(self, cfg,  parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.cfg=cfg
        self.tblEstudio.settings("wdgInformeHistorico",  self.cfg.inifile)
        self.tblDividendos.settings("wdgInformeHistorico",  self.cfg.inifile)
        self.tblInversiones.settings("wdgInformeHistorico",  self.cfg.inifile)
        self.tblAdded.settings("wdgInformeHistorico",  self.cfg.inifile)
        
        self.totalDividendosNetos=0
        self.totalDividendosBrutos=0
        self.totalDividendosRetenciones=0
        
        con=self.cfg.connect_xulpymoney()
        cur = con.cursor()     
        mq=self.cfg.connect_myquotes()
        curmq=mq.cursor()        
        anoinicio=Patrimonio().primera_fecha_con_datos_usuario(cur).year       

        ran=datetime.date.today().year-anoinicio+1
        for i in range(ran):
            self.cmbYears.addItem(str(anoinicio+i))
        self.cmbYears.setCurrentIndex(datetime.date.today().year-anoinicio)

        self.ano=int(self.cmbYears.currentText())
        self.load(cur, curmq)
        cur.close()     
        self.cfg.disconnect_xulpymoney(con)       
        curmq.close()
        self.cfg.disconnect_myquotes(mq)        
        self.tab.setCurrentIndex(0)


    def load(self, cur, curmq):
        inicio=datetime.datetime.now()
        self.load_dividendos(cur)
        self.load_historicas(cur)
        self.load_added(cur, curmq)
        self.load_rendimientos(cur, curmq)
        print("wdgInformeHistorico > load: {0}".format(datetime.datetime.now()-inicio))
        
    def load_added(self, cur, curmq):
        operaciones=[]
        for i in self.cfg.inversiones.arr:
            for o in i.op.arr:
                if o.tipooperacion.id==6 and o.datetime.year==int(self.cmbYears.currentText()):
                    operaciones.append(o)    
        operaciones=sorted(operaciones, key=lambda o: o.datetime,  reverse=False)                         
                    
        self.tblAdded.setRowCount(len(operaciones)+1)
        sumsaldo=0        
        for i,  o in enumerate(operaciones):
            valor=Quote().init__from_query(curmq, o.inversion.mq, o.datetime).quote
            if valor==None:
                print("wdgInformeHistorico > load_added: {0} en {1} da nulo".format(o.inversion.mq.id, o.datetime))
                valor=0
            saldo=valor*o.acciones
            sumsaldo=sumsaldo+saldo
            self.tblAdded.setItem(i, 0, qdatetime(o.datetime))
            self.tblAdded.setItem(i, 1, QTableWidgetItem(o.inversion.name))
            self.tblAdded.setItem(i, 2, QTableWidgetItem(self.cfg.tiposoperaciones(6).name))
            self.tblAdded.setItem(i, 3, qright(str(o.acciones)))
            self.tblAdded.setItem(i, 4, self.cfg.localcurrency.qtablewidgetitem(saldo))
        self.tblAdded.setItem(len(operaciones), 3, QTableWidgetItem(("TOTAL")))
        self.tblAdded.setItem(len(operaciones), 4, self.cfg.localcurrency.qtablewidgetitem(sumsaldo))
   
    def load_dividendos(self, cur):
        self.totalDividendosNetos=0
        self.totalDividendosBrutos=0
        self.totalDividendosRetenciones=0
        sql="select * from dividendos where date_part('year',fecha)="+str(self.ano) + " order by fecha"
        cur.execute(sql); 
        dividendos=[]
        for row in  cur:
            dividendos.append(Dividendo().init__db_row(row, self.cfg.inversiones.inversion(row['id_inversiones']), None,  None))#Creación incompleta por no ser necesario con None
        self.tblDividendos.clearContents()
        self.tblDividendos.setRowCount(len(dividendos)+1)
        for i, d in enumerate(dividendos):
            self.totalDividendosNetos=self.totalDividendosNetos+d.neto_antes_impuestos()
            self.totalDividendosBrutos=self.totalDividendosBrutos+d.bruto
            self.totalDividendosRetenciones=self.totalDividendosRetenciones+d.retencion
            self.tblDividendos.setItem(i, 0,QTableWidgetItem(str(d.fecha)))
            self.tblDividendos.setItem(i, 1,QTableWidgetItem(d.inversion.name))
            self.tblDividendos.setItem(i, 2,QTableWidgetItem(d.inversion.cuenta.eb.name))
            self.tblDividendos.setItem(i, 3,self.cfg.localcurrency.qtablewidgetitem(d.neto_antes_impuestos()))
        self.tblDividendos.setItem(len(dividendos), 2,QTableWidgetItem(("TOTAL")))
        self.tblDividendos.setItem(len(dividendos), 3,self.cfg.localcurrency.qtablewidgetitem(self.totalDividendosNetos))
        self.tblDividendos.setCurrentCell(len(dividendos), 3)

    def load_historicas(self, cur):
        operaciones=[]
        for i in self.cfg.inversiones.arr:
            for o in i.op_historica.arr:
                if o.fecha_venta.year==int(self.cmbYears.currentText()) and o.tipooperacion.id in (5, 8):#Venta y traspaso fondos inversion
                    operaciones.append(o)
        operaciones=sorted(operaciones, key=lambda o: o.fecha_venta,  reverse=False)      
        (self.totalBruto, self.totalComisiones, self.totalImpuestos, self.totalNeto)=myqtablewidget_loads_SetInversionOperacionHistorica(self.tblInversiones, operaciones)



    def load_rendimientos(self, cur, curmq ):
        inicio=datetime.date(self.ano-1, 12, 31)
        cur.execute("select sum(importe) as suma from opercuentas where id_conceptos=59 and date_part('year',fecha)="+str(self.ano))
        sumcomisioncustodia=cur.fetchone()[0]        
        if sumcomisioncustodia==None:
            sumcomisioncustodia=0
            
        saldototal=Patrimonio().saldo_total(self.cfg, cur, curmq,  datetime.date.today());
        saldototalinicio=Patrimonio().saldo_total(self.cfg, cur, curmq, inicio)
        if self.totalBruto>0:
            impxplus=-self.totalBruto*config.taxcapitalappreciation
        else:            
            impxplus=0
        
        beneficiosin=self.totalBruto+self.totalComisiones+sumcomisioncustodia+self.totalDividendosBrutos
        beneficiopag=self.totalBruto+impxplus+self.totalImpuestos+self.totalComisiones+sumcomisioncustodia+self.totalDividendosNetos
        
        if saldototalinicio==0:
            tpcneto=None
            tpcimpxplus=None
            tpcplus=None
            tpcdividendosbrutos=None
            tpcdividendosnetos=None
            tpcsumcomision=None
            tpcsumcustodia=None
            tpcsumimpuestos=None
            tpcretenciondividendos=None
        else:
            tpcneto=self.totalNeto*100/saldototalinicio
            tpcimpxplus=impxplus*100/saldototalinicio
            tpcplus=self.totalBruto*100/saldototalinicio
            tpcdividendosbrutos=self.totalDividendosBrutos*100/saldototalinicio
            tpcdividendosnetos=self.totalDividendosNetos*100/saldototalinicio
            tpcsumcomision=self.totalComisiones*100/saldototalinicio
            tpcsumcustodia=sumcomisioncustodia*100/saldototalinicio
            tpcsumimpuestos=self.totalImpuestos*100/saldototalinicio
            tpcretenciondividendos=self.totalDividendosRetenciones*100/saldototalinicio

        self.tblEstudio.horizontalHeaderItem(1).setText(("% TAE desde "+str(inicio)))
        self.lblSaldo.setText(self.tr("Saldo a {0}, {1}".format(str(inicio), self.cfg.localcurrency.string(saldototalinicio))))

        self.tblEstudio.setItem(0, 0,self.cfg.localcurrency.qtablewidgetitem(self.totalBruto))       
        self.tblEstudio.setItem(0, 1,qtpc(tpcplus))            

        self.tblEstudio.setItem(1, 0,self.cfg.localcurrency.qtablewidgetitem(self.totalComisiones))       
        self.tblEstudio.setItem(1, 1,qtpc(tpcsumcomision))     

        self.tblEstudio.setItem(2, 0,self.cfg.localcurrency.qtablewidgetitem(self.totalImpuestos))       
        self.tblEstudio.setItem(2, 1,qtpc(tpcsumimpuestos))    
        
        self.tblEstudio.setItem(3, 0,self.cfg.localcurrency.qtablewidgetitem(self.totalNeto))    #Lo que sale en total y patrimonio   
        self.tblEstudio.setItem(3, 1,qtpc(tpcneto))      

        self.tblEstudio.setItem(5, 0,self.cfg.localcurrency.qtablewidgetitem(self.totalDividendosBrutos))       
        self.tblEstudio.setItem(5, 1,qtpc(tpcdividendosbrutos))     
        
        self.tblEstudio.setItem(6, 0,self.cfg.localcurrency.qtablewidgetitem(self.totalDividendosRetenciones))       
        self.tblEstudio.setItem(6, 1,qtpc(tpcretenciondividendos))            

        self.tblEstudio.setItem(7, 0,self.cfg.localcurrency.qtablewidgetitem(self.totalDividendosNetos))       
        self.tblEstudio.setItem(7, 1,qtpc(tpcdividendosnetos))                
        
        self.tblEstudio.setItem(9, 0,self.cfg.localcurrency.qtablewidgetitem(sumcomisioncustodia))       
        self.tblEstudio.setItem(9, 1,qtpc(tpcsumcustodia))      

        self.tblEstudio.setItem(11, 0,self.cfg.localcurrency.qtablewidgetitem(impxplus))     
        self.tblEstudio.setItem(11, 1, qtpc(tpcimpxplus))


        self.tblEstudio.setItem(13, 0,self.cfg.localcurrency.qtablewidgetitem(beneficiosin))       
        try:
            self.tblEstudio.setItem(13, 1,qtpc((beneficiosin)*100/saldototalinicio))            
        except:
            self.tblEstudio.setItem(13, 1,qtpc(None))     

        self.tblEstudio.setItem(14, 0,self.cfg.localcurrency.qtablewidgetitem(beneficiopag))       
        try:
            self.tblEstudio.setItem(14, 1,qtpc((beneficiopag)*100/saldototalinicio))            
        except:
            self.tblEstudio.setItem(14,  1,qtpc(None))     

        self.tblEstudio.setItem(16, 0,self.cfg.localcurrency.qtablewidgetitem(saldototal))       
        try:
            self.tblEstudio.setItem(16, 1,qtpc((saldototal-saldototalinicio)*100/saldototalinicio))            
        except:
            self.tblEstudio.setItem(16, 1,qtpc(None))     


    def on_cmd_pressed(self):
        con=self.cfg.connect_xulpymoney()
        cur = con.cursor()     
        mq=self.cfg.connect_myquotes()
        curmq=mq.cursor()                
        self.load(cur, curmq)
        cur.close()     
        self.cfg.disconnect_xulpymoney(con)       
        curmq.close()
        self.cfg.disconnect_myquotes(mq)       

    @QtCore.pyqtSlot(str) 
    def on_cmbYears_currentIndexChanged(self, text):
        self.ano=int(text)