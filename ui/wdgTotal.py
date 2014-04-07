from PyQt4.QtCore import *
from PyQt4.QtGui import *
from libxulpymoney import *
from libxulpymoney import *
from matplotlib.finance import *

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar

from matplotlib.dates import *
from Ui_wdgTotal import *
import calendar,  datetime

# Matplotlib Figure object
from matplotlib.figure import Figure
class canvasTotal(FigureCanvas):
    def __init__(self, cfg, parent):
        self.cfg=cfg
        self.fig = Figure()
        FigureCanvas.__init__(self, self.fig)
        FigureCanvas.setSizePolicy(self,QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.ax = self.fig.add_subplot(111)
        self.labels=[]
        self.plot_main=None
        self.plot_zero=None
        
    
    def price(self, x): 
        return self.cfg.localcurrency.string(x)
        
    def mydraw(self, cfg, data, zero):
        self.ax.clear()

        (dates, total)=zip(*data)
        (datesz, zero)=zip(*zero)
        if len(dates)<36:
            self.ax.xaxis.set_minor_locator(MonthLocator())
            self.ax.xaxis.set_major_locator(MonthLocator())
            self.ax.xaxis.set_major_formatter( DateFormatter('%Y-%m'))   
        elif len(dates)>=36:
            self.ax.xaxis.set_minor_locator(YearLocator())
            self.ax.xaxis.set_major_locator(YearLocator())    
            self.ax.xaxis.set_major_formatter( DateFormatter('%Y'))                   
        self.ax.autoscale_view()
        
        # format the coords message box
        self.ax.fmt_xdata = DateFormatter('%Y-%m-%d')
        self.ax.fmt_ydata = self.price
        self.ax.grid(True)
        self.fig.autofmt_xdate()
        self.plot_main, =self.ax.plot_date(dates, total, '-')
        self.plot_zero, =self.ax.plot_date(datesz, zero, '-')
        self.showLegend()
        self.draw()
        
    def showLegend(self):
        """Alterna mostrando y desmostrando legend, empieza con s´i"""
        self.makeLegend()
                
        if self.ax.legend_==None:
            (plots, labels)=zip(*self.labels)
            self.ax.legend(plots, labels, "upper left")
        else:
            self.ax.legend_=None

    def mouseReleaseEvent(self,  event):
        self.showLegend()
        self.draw()
    
    def makeLegend(self):
        if len(self.labels)==0:
            self.labels.append((self.plot_main, self.trUtf8("Total assets")))
            self.labels.append((self.plot_zero,self.trUtf8("Zero risk assets")))

class wdgTotal(QWidget, Ui_wdgTotal):
    def __init__(self, cfg,  parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.cfg=cfg
#        self.pathGraphTotal=os.environ['HOME']+"/.xulpymoney/graphTotal.png"
        self.progress = QProgressDialog(self.tr("Rellenando los datos del informe"), self.tr("Cancelar"), 0,0)
        self.progress.setModal(True)
        self.progress.setWindowTitle(self.trUtf8("Calculando datos..."))
        self.progress.setMinimumDuration(0)        
        self.sumpopup=[]
        for i in range(0, 13):
            self.sumpopup.append(0)

        fechainicio=Patrimonio(self.cfg).primera_fecha_con_datos_usuario()         

        self.cfg.data.load_inactives()
        if fechainicio==None: #Base de datos vacía
            self.tab.setEnabled(False)
            return
        
        self.table.settings(None,  self.cfg)
        
        self.wyData.initiate(fechainicio.year, datetime.date.today().year, datetime.date.today().year)
        QObject.connect(self.wyData, SIGNAL("changed"), self.on_wyData_changed)
        self.wyChart.initiate(fechainicio.year, datetime.date.today().year, datetime.date.today().year)
        self.wyChart.label.setText(self.trUtf8("Data from selected year"))
        QObject.connect(self.wyChart, SIGNAL("changed"), self.on_wyChart_changed)


        self.canvas=canvasTotal(self.cfg,  self)
        self.ntb = NavigationToolbar(self.canvas, self)
        
        self.tabGraphTotal.addWidget(self.canvas)
        self.tabGraphTotal.addWidget(self.ntb)
        self.on_tab_currentChanged(0)

        
    def load_data(self, cur, curms):        
        self.table.clearContents()
        inicio=datetime.datetime.now()     
#        cmbanos=int(self.cmbYears.currentText())
        sumgastos=0
        sumdividendos=0
        sumingresos=0        
        sumconsolidado=0
        (sumdiferencia, sumsaldoaccionescostecero)=(0, 0)
        
        totallastmonth=Patrimonio(self.cfg).saldo_total(self.cfg.data.inversiones_all(),  datetime.date(self.wyData.year-1, 12, 31))#Mes de 12 31 año anteriro
        self.lblPreviousYear.setText(self.trUtf8("Balance at {0}-12-31: {1}".format(self.wyData.year-1, self.cfg.localcurrency.string(totallastmonth))))
        inicioano=totallastmonth

        for i in range(12): 
            gastos=Patrimonio(self.cfg).saldo_por_tipo_operacion( self.wyData.year,i+1,1)#La facturación de tarjeta dentro esta por el union
            dividendos=Inversion(self.cfg).dividendos_neto(  self.wyData.year, i+1)
            ingresos=Patrimonio(self.cfg).saldo_por_tipo_operacion(  self.wyData.year,i+1,2)-dividendos #Se quitan los dividendos que luego se suman
            
#            consolidado=InversionOperacionHistorica(self.cfg).consolidado_total_mensual(cur, self.wyData.year,i+1)
            consolidado=Patrimonio(self.cfg).consolidado_neto(self.cfg.data.inversiones_all(), self.wyData.year, i+1)
            gi=ingresos+dividendos+consolidado+gastos
            self.sumpopup[i]=consolidado+dividendos
            
            sumgastos=sumgastos+gastos
            sumdividendos=sumdividendos+dividendos
            sumingresos=sumingresos+ingresos
            sumconsolidado=sumconsolidado+consolidado
            sumgi=sumgastos+sumdividendos+sumingresos+sumconsolidado

            if  datetime.date.today()<datetime.date(self.wyData.year, i+1, 1):
                cuentas=0
                inversiones=0
                total=0
                diferencia=0
                tpc=0
            else:
                fecha=datetime.date (self.wyData.year, i+1, calendar.monthrange(self.wyData.year, i+1)[1])#Último día de mes.
                cuentas=Patrimonio(self.cfg).saldo_todas_cuentas( fecha)
                inversiones=Patrimonio(self.cfg).saldo_todas_inversiones(self.cfg.data.inversiones_all(),  fecha)
                total=cuentas+inversiones
                diferencia=total-totallastmonth
                sumdiferencia=sumdiferencia+diferencia
                totallastmonth=total
                if inicioano==0:
                    tpc=None
                else:
                    tpc=100*(total-inicioano)/inicioano    
            
            self.table.setItem(0, i, self.cfg.localcurrency.qtablewidgetitem(ingresos))
            self.table.setItem(1, i, self.cfg.localcurrency.qtablewidgetitem(consolidado))
            self.table.setItem(2, i, self.cfg.localcurrency.qtablewidgetitem(dividendos))
            self.table.setItem(3, i, self.cfg.localcurrency.qtablewidgetitem(gastos))
            self.table.setItem(4, i, self.cfg.localcurrency.qtablewidgetitem(gi))
            self.table.setItem(6, i, self.cfg.localcurrency.qtablewidgetitem(cuentas))
            self.table.setItem(7, i, self.cfg.localcurrency.qtablewidgetitem(inversiones))
            self.table.setItem(8, i, self.cfg.localcurrency.qtablewidgetitem(total))
            self.table.setItem(9, i, self.cfg.localcurrency.qtablewidgetitem(diferencia))
            self.table.setItem(11, i, qtpc(tpc))
        self.table.setItem(0, 12, self.cfg.localcurrency.qtablewidgetitem(sumingresos))
        self.table.setItem(1, 12, self.cfg.localcurrency.qtablewidgetitem(sumconsolidado))
        self.table.setItem(2, 12, self.cfg.localcurrency.qtablewidgetitem(sumdividendos))
        self.table.setItem(3, 12, self.cfg.localcurrency.qtablewidgetitem(sumgastos))
        self.table.setItem(4, 12, self.cfg.localcurrency.qtablewidgetitem(sumgi))      
        self.sumpopup[12]=sumconsolidado+sumdividendos
        self.table.setItem(9, 12, self.cfg.localcurrency.qtablewidgetitem(sumdiferencia))    
        if inicioano==0:
            self.table.setItem(11, 12, qtpc(None))     
        else:
            self.table.setItem(11, 12, qtpc(sumdiferencia*100/inicioano))       
        
        self.table.setCurrentCell(6, datetime.date.today().month-1)

        final=datetime.datetime.now()          
        print ("wdgTotal > load_data: {0}".format(final-inicio))


    def load_graphic(self, cur, curms):          
        inicio=datetime.datetime.now()  
        data=[]#date,valor
        zero=[]#date, valor zero

        years=datetime.date.today().year-self.wyChart.year
        months=datetime.date.today().month+1
        self.progress.reset()
        self.progress.setMinimum(0)
        self.progress.setMaximum(12*years+months+years+1)
        self.progress.setValue(1)     
        self.progress.forceShow()
        self.progress.setValue(0)        
        for year in range(self.wyChart.year, datetime.date.today().year+1):
            for month in range(1, 14):
                if self.progress.wasCanceled():
                    break;
                else:
                    self.progress.setValue(self.progress.value()+1)          
                if month==13:
                    date=datetime.date(year, 12, 31)
                else:
                    date=datetime.date(year, month, 1)-datetime.timedelta(days=1)
                if date.month==datetime.date.today().month and date.year==datetime.date.today().year:
                    date=datetime.date.today()
                if date.month>datetime.date.today().month and date.year>=datetime.date.today().year:
                    break
                data.append( (date,Patrimonio(self.cfg).saldo_total(self.cfg.data.inversiones_all(), date)) )
                zero.append( (date,Patrimonio(self.cfg).patrimonio_riesgo_cero(self.cfg.data.inversiones_all(), date) ))
        self.canvas.mydraw(self.cfg, data, zero)
        print ("wdgTotal > load_graphic: {0}".format(datetime.datetime.now()-inicio))

    def on_wyData_changed(self):
        con=self.cfg.connect_xulpymoney()
        cur = con.cursor()        
        mq=self.cfg.connect_mystocks()
        curms=mq.cursor()        
        self.load_data(cur, curms) 
        cur.close()     
        self.cfg.disconnect_xulpymoney(con)       
        curms.close()
        self.cfg.disconnect_mystocks(mq)        
        
    def on_wyChart_changed(self):
        con=self.cfg.connect_xulpymoney()
        cur = con.cursor()        
        mq=self.cfg.connect_mystocks()
        curms=mq.cursor()        
        self.load_graphic(cur, curms)
        cur.close()     
        self.cfg.disconnect_xulpymoney(con)       
        curms.close()
        self.cfg.disconnect_mystocks(mq)        
        

    def on_tab_currentChanged(self, index):
        if index==0:#datos
            self.on_wyData_changed()
        elif index==1: #grafico
            self.on_wyChart_changed()
            
        
    def on_table_cellDoubleClicked(self, row, column):
        if row in (1, 2):
            m=QMessageBox()
            message=self.trUtf8("La suma de consolidado y dividendos  de este mes es {0}. En el año su valor asciende a {1}".format(self.cfg.localcurrency.string(self.sumpopup[column]), self.cfg.localcurrency.string(self.sumpopup[12])))

            m.setText(message)
            m.exec_()             
