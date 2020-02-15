from PyQt5.QtCore import QObject, QTime, QCoreApplication, QEventLoop
from datetime import datetime, date
from logging import debug
from officegenerator import ODT
from os import makedirs
from xulpymoney.casts import lor_remove_columns, list_remove_positions
from xulpymoney.datetime_functions import days2string
from xulpymoney.version import __version__
from xulpymoney.objects.assets import  Assets
from xulpymoney.objects.annualtarget import  AnnualTarget
from xulpymoney.objects.money import Money
from xulpymoney.objects.percentage import  Percentage
from xulpymoney.package_resources import package_filename


class AssetsReport(ODT, QObject):
    def __init__(self, mem, filename):
        ODT.__init__(self, filename, package_filename("xulpymoney", "templates/AssetsReport.odt"))
        QObject.__init__(self)
        self.mem=mem
        self.datetime=datetime.now()
        self.dir='/tmp/AssetsReport-{}'.format(datetime.now())
        makedirs(self.dir, exist_ok=True)
        
    def generate(self):
        self.setMetadata( self.tr("Assets report"),  self.tr("This is an automatic generated report from Xulpymoney"), "Xulpymoney-{}".format(__version__))
        self.variables()
        self.cover()
        self.body()
        self.save()   
        
    def variables(self):
        self.vTotalLastYear=Assets(self.mem).saldo_total(self.mem.data.investments,  date(date.today().year-1, 12, 31))
        self.vTotal=Assets(self.mem).saldo_total(self.mem.data.investments,  date.today())

    def cover(self):
        self.search_and_replace("__TITLE__", self.tr("Assets Report"), type_="P")
        self.search_and_replace("__SUBTITLE__", self.tr("Generated by Xulpymoney-{}".format(__version__)), type_="P")
        self.search_and_replace("__DATETIME__", str(self.datetime), type_="P")
        self.pageBreak()
        
    def body(self):
        c=self.mem.localcurrency.string
        # About
        self.header(self.tr("About Xulpymoney"), 1)
        
        # Assets
        self.header(self.tr("Assets"), 1)
        self.simpleParagraph(self.tr("Total assets of the user are {}.").format(self.vTotal))
        if self.vTotalLastYear.isZero()==False:
            moreorless=self.tr("more")
            if (self.vTotal-self.vTotalLastYear).isLTZero():
                moreorless=self.tr("less")
            self.simpleParagraph(self.tr("It's a {} {} of the total assets at the end of the last year.").format(Percentage(self.vTotal-self.vTotalLastYear, self.vTotalLastYear), moreorless))
        
        # Assets by bank
        self.header(self.tr("Assets by bank"), 2)
        data=[]
        self.mem.data.banks_active().order_by_name()
        sumbalances=Money(self.mem, 0, self.mem.localcurrency)
        for bank in self.mem.data.banks_active().arr:
            balance=bank.balance(self.mem.data.accounts_active(), self.mem.data.investments_active())
            sumbalances=sumbalances+balance
            data.append((bank.name, balance))
        self.table( [self.tr("Bank"), self.tr("Balance")], data, [4, 3], 9)       
        self.simpleParagraph(self.tr("Sum of all bank balances is {}").format(sumbalances))
        
        self.pageBreak(True)
        # Assests current year
        self.header(self.tr("Assets current year evolution"), 2)
        
        #wdgTotal
        from xulpymoney.ui.wdgTotal import TotalYear
        setData=TotalYear(self.mem, date.today().year)
        columns=[]
        columns.append([self.tr("Incomes"), self.tr("Gains"), self.tr("Dividends"), self.tr("Expenses"), self.tr("I+G+D-E"), "",  self.tr("Accounts"), self.tr("Investments"), self.tr("Total"),"",  self.tr("Monthly difference"), "",  self.tr("% current year")])
        self.simpleParagraph(self.tr("Assets Balance at {0}-12-31 is {1}".format(setData.year-1, setData.total_last_year)))
        for i, m in enumerate(setData.arr):
            if m.year<date.today().year or (m.year==date.today().year and m.month<=date.today().month):
                columns.append([m.incomes(), m.gains(), m.dividends(), m.expenses(), m.i_d_g_e(), "", m.total_accounts(), m.total_investments(), m.total(),"", setData.difference_with_previous_month(m),"",  setData.assets_percentage_in_month(m.month)])
            else:
                columns.append(["","","","","","","","","", "", "", "", ""])
        columns.append([setData.incomes(), setData.gains(), setData.dividends(), setData.expenses(), setData.i_d_g_e(), "", "", "", "", "", setData.difference_with_previous_year(), "", setData.assets_percentage_in_month(12)]) 
        data=zip(*columns)
        debug("Porcentage {}".format(setData.assets_percentage_in_month(12).__class__.__name__))
        self.table(   [self.tr("Concept"), self.tr("January"),  self.tr("February"), self.tr("March"), self.tr("April"), self.tr("May"), self.tr("June"), self.tr("July"), self.tr("August"), self.tr("September"), self.tr("October"), self.tr("November"), self.tr("December"), self.tr("Total")], 
                            data, [2.5]+[1.8]*13, 6)
                
        ## Target
        target=AnnualTarget(self.mem).init__from_db(date.today().year)
        self.simpleParagraph(self.tr("The investment system has established a {} year target.").format(target.percentage)+" " +
                self.tr("With this target you will gain {} at the end of the year.").format(c(target.annual_balance())) +" " +
                self.tr("Up to date you have got  {} (gains + dividends) what represents a {} of the target.").format(setData.dividends()+setData.gains(), Percentage(setData.gains()+setData.dividends(), target.annual_balance())))
        self.pageBreak(True)
        
        ### Assets evolution graphic
        self.header(self.tr("Assets graphical evolution"), 2)
        
        self.mem.frmMain.on_actionTotalReport_triggered()
        self.mem.frmMain.w.load_graphic(animations=False)
        self.mem.frmMain.w.tab.setCurrentIndex(1)
        savefile="{}/wdgTotal.png".format(self.dir)
        self.mem.frmMain.w.view.save(savefile)
        self.addImage(savefile, savefile)
        self.illustration([savefile, ], 25, 13, savefile)
        self.pageBreak()
        
        
        ## Accounts
        self.header(self.tr("Current Accounts"), 1)
        data=[]
        self.mem.data.accounts_active().order_by_name()
        for account in self.mem.data.accounts_active().arr:
            data.append((account.name, account.eb.name, account.balance()))
        self.table( [self.tr("Account"), self.tr("Bank"),  self.tr("Balance")], data, [6, 6, 3], 9)       
        
        self.simpleParagraph(self.tr("Sum of all account balances is {}").format(self.mem.data.accounts_active().balance()))

        
        self.pageBreak(True)
        
        ## Investments
        self.header(self.tr("Current investments"), 1)
        
        self.header(self.tr("Investments list"), 2)
        self.simpleParagraph(self.tr("Next list is sorted by the distance in percent to the selling point."))
        self.mem.frmMain.on_actionInvestments_triggered()
        self.table( 
            list_remove_positions(self.mem.frmMain.w.mqtwInvestments.listHorizontalHeaders(), [1, 2, 3, 4]), 
            lor_remove_columns(self.mem.frmMain.w.mqtwInvestments.data, [1, 2, 3, 4]), 
            [13,  3, 3, 3, 3],  8)       
        
        suminvertido=self.mem.data.investments_active().invested()
        sumpendiente=self.mem.data.investments_active().pendiente()
        if suminvertido.isZero()==False:
            self.simpleParagraph(self.tr("Sum of all invested assets is {}.").format(suminvertido))
            self.simpleParagraph(self.tr("Investment gains (positive minus negative results): {} - {} are {}, what represents a {} of total assets.").format(self.mem.data.investments_active().pendiente_positivo(), self.mem.data.investments_active().pendiente_negativo(), sumpendiente, Percentage(sumpendiente, suminvertido)))
            self.simpleParagraph(self.tr(" Assets average age: {}").format(  days2string(self.mem.data.investments_active().average_age())))
        else:
            self.simpleParagraph(self.tr("There aren't invested assets"))
        self.pageBreak(True)
        
        
        ### Current Investment Operations list
        self.header(self.tr("Current investment operations"), 2)
        self.mem.frmMain.on_actionInvestmentsOperations_triggered()
        self.mem.frmMain.w.mqtwCurrent.officegeneratorModel(self.tr("CurrentInvestmentOperations")).odt_table(self, [3.1, 4.1, 3.3, 1.7, 1.7, 1.7, 1.7, 1.7, 1.7, 1.7, 1.7, 1.7], 5)
        self.pageBreak(True)
        
        ### Graphics wdgInvestments clases
        self.mem.frmMain.on_actionInvestmentsClasses_triggered()
        self.mem.frmMain.w.open_all_tabs()#Load tabs to finish animations
        self.mem.frmMain.w.viewTPC.on_actionShowData_triggered()
        self.mem.frmMain.w.viewTipo.on_actionShowData_triggered()
        self.mem.frmMain.w.viewApalancado.on_actionShowData_triggered()
        self.mem.frmMain.w.viewProduct.on_actionShowData_triggered()
        self.mem.frmMain.w.viewCountry.on_actionShowData_triggered()
        self.mem.frmMain.w.viewPCI.on_actionShowData_triggered()
        
        self.header(self.tr("Investments group by variable percentage"), 2)
        savefile="{}/wdgInvestmentsClasses_canvasTPC_legend.png".format(self.dir)
        self.mem.frmMain.w.tab.setCurrentIndex(0)
        self.sleep(2)
        self.mem.frmMain.w.viewTPC.pie.save(savefile)
        self.addImage(savefile, savefile)
        self.illustration([savefile, ], 25, 13, savefile)
        self.pageBreak(True)
        
        self.header(self.tr("Investments group by investment type"), 2)
        savefile="{}/wdgInvestmentsClasses_canvasTipo_legend.png".format(self.dir)
        self.mem.frmMain.w.tab.setCurrentIndex(2)
        self.sleep(2)
        self.mem.frmMain.w.viewTipo.pie.save(savefile)
        self.addImage(savefile, savefile)
        self.illustration([savefile, ], 25, 13, savefile)
        self.pageBreak(True)
        
        self.header(self.tr("Investments group by leverage"), 2)        
        savefile="{}/wdgInvestmentsClasses_canvasApalancado_legend.png".format(self.dir)
        self.mem.frmMain.w.tab.setCurrentIndex(3)
        self.sleep(2)
        self.mem.frmMain.w.viewApalancado.pie.save(savefile)
        self.addImage(savefile, savefile)
        self.illustration([savefile, ], 25, 13, savefile)
        self.pageBreak(True)
        
        self.header(self.tr("Investments group by investment product"), 2)
        savefile="{}/wdgInvestmentsClasses_canvasProduct_legend.png".format(self.dir)
        self.mem.frmMain.w.tab.setCurrentIndex(5)
        self.sleep(2)
        self.mem.frmMain.w.viewProduct.pie.save(savefile)
        self.addImage(savefile, savefile)
        self.illustration([savefile, ], 25, 13, savefile)
        self.pageBreak(True)
        
        self.header(self.tr("Investments group by country"), 2)
        savefile="{}/wdgInvestmentsClasses_canvasCountry_legend.png".format(self.dir)
        self.mem.frmMain.w.tab.setCurrentIndex(4)
        self.sleep(2)
        self.mem.frmMain.w.viewCountry.pie.save(savefile)
        self.addImage(savefile, savefile)
        self.illustration([savefile, ], 25, 13, savefile)
        self.pageBreak(True)
        
        self.header(self.tr("Investments group by Call/Put/Inline"), 2)
        savefile="{}/wdgInvestmentsClasses_canvasPCI_legend.png".format(self.dir)
        self.mem.frmMain.w.tab.setCurrentIndex(1)
        self.sleep(2)
        self.mem.frmMain.w.viewPCI.pie.save(savefile)
        self.addImage(savefile, savefile)
        self.illustration([savefile, ], 25, 13, savefile)
        
        self.mem.frmMain.showMaximized()
        self.pageBreak(True)
        
        #Dividend report
        self.header(self.tr("Dividend estimations report"), 1)
        self.mem.frmMain.on_actionDividendsReport_triggered()
        self.table(self.mem.frmMain.w.mqtw.listHorizontalHeaders(), self.mem.frmMain.w.mqtw.data, [8, 6, 2.6, 2.6, 2.6, 2.6, 2.6], 8)
        self.simpleParagraph(self.tr("If I keep this investment during a year, I'll get {0}").format(self.mem.frmMain.w.sum_of_estimated_dividends()))

    def sleep(self, seconds):
        dieTime= QTime.currentTime().addSecs(seconds);
        while (QTime.currentTime() < dieTime):
            QCoreApplication.processEvents(QEventLoop.AllEvents, 100)
