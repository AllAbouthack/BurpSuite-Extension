
from burp import ITab
from burp import IBurpExtender, IContextMenuFactory, IContextMenuInvocation
from javax.swing import JPanel
from javax.swing import JButton,JSplitPane,GroupLayout, LayoutStyle, JTextField, JMenuItem, JFileChooser
from java.lang import Short
from javax.swing import JTable
from javax.swing import JScrollPane
from javax.swing.table import DefaultTableModel, AbstractTableModel
import csv
from javax.swing.filechooser import FileNameExtensionFilter

class BurpExtender(IBurpExtender, ITab, AbstractTableModel, IContextMenuFactory):

    def registerExtenderCallbacks(self, callbacks):
        self.callbacks = callbacks
        self.Customtabui = JPanel()
        self.helpers = callbacks.getHelpers()
        self.callbacks.setExtensionName("Test Extension")
        self.saveoutput =  []
        self.callbacks.registerContextMenuFactory(self)
        layout = GroupLayout(self.Customtabui)
        self.Customtabui.setLayout(layout)
        self.callbacks.addSuiteTab(self)
        Importbutton =  JButton("Import", actionPerformed=self.importclicked);
        Exportbutton =  JButton("Export", actionPerformed=self.exportclicked);
        Clearbutton =  JButton("Clear", actionPerformed=self.clearclicked);
        jSplitPane2 =  JSplitPane(JSplitPane.VERTICAL_SPLIT);
        #self.colname = ['Number','String']
        #self.rowvalue = [['1','One'],['2','Two']]
        #self.DefaultModel = DefaultTableModel(self.rowvalue, self.colname)
        jScrollPane1 =  JScrollPane();
        #jTable1 =  JTable(self.DefaultModel);
        self.mytable = CustomTable(self)
        jSplitPane3 =  JSplitPane();
        #RequestTextbox =  JTextField()
        #ResponseTextbox =  JTextField()
        
        RequestTextbox = self.callbacks.createMessageEditor(None, True)
        ResponseTextbox = self.callbacks.createMessageEditor(None, True)
        jScrollPane1.setViewportView(self.mytable);

        jSplitPane2.setLeftComponent(jScrollPane1);

        #RequestTextbox.setText("Request");
        jSplitPane3.setLeftComponent(RequestTextbox.getComponent());
        
        #ResponseTextbox.setText("Response");
        jSplitPane3.setRightComponent(ResponseTextbox.getComponent());

        jSplitPane2.setRightComponent(jSplitPane3);

        layout.setHorizontalGroup(
            layout.createParallelGroup(GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addGap(90, 90, 90)
                .addComponent(Importbutton)
                .addPreferredGap(LayoutStyle.ComponentPlacement.UNRELATED)
                .addComponent(Exportbutton)
                .addGap(18, 18, 18)
                .addComponent(Clearbutton)
                .addContainerGap(101, Short.MAX_VALUE))
            .addGroup(layout.createSequentialGroup()
                .addContainerGap()
                .addComponent(jSplitPane2, GroupLayout.PREFERRED_SIZE, 0, Short.MAX_VALUE)
                .addContainerGap())
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(GroupLayout.Alignment.LEADING)
            .addGroup(GroupLayout.Alignment.TRAILING, layout.createSequentialGroup()
                .addGap(14, 14, 14)
                .addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                    .addComponent(Importbutton)
                    .addComponent(Exportbutton)
                    .addComponent(Clearbutton))
                .addGap(18, 18, 18)
                .addComponent(jSplitPane2)
                .addContainerGap())
        );

        
        
    def exportclicked(self,e):
    	chooseFile = JFileChooser()
        chooseFile.setFileSelectionMode(JFileChooser.DIRECTORIES_ONLY)
        returnedFile = chooseFile.showDialog(self.Customtabui, "Output Path")
        if returnedFile == JFileChooser.APPROVE_OPTION:
            fileLoad = chooseFile.getSelectedFile()
            #self.filepath = fileLoad.getAbsolutePath()
            self.filepath = fileLoad.getPath()
            fname = "Output"+"."+"csv"
            fnameWithPath = os.path.join(self.filepath,fname)
           
            with open(fnameWithPath, 'wb') as loggerdata:
                writer = csv.writer(loggerdata)
                for tableentry in self.saveoutput:
                    
                    
                    writer.writerow([str(tableentry.request), str(tableentry.response) ,str(tableentry.url) ,str(tableentry.method) ,str(tableentry.hostname),])
            loggerdata.close()

    def importclicked(self,e):
    	chooseFile = JFileChooser()
        filter = FileNameExtensionFilter("csv files", ["csv"])
        chooseFile.addChoosableFileFilter(filter)
        ret = chooseFile.showDialog(self.Customtabui, "Choose file")
        if ret == JFileChooser.APPROVE_OPTION:
            fileLoad = chooseFile.getSelectedFile()
            self.filepath = fileLoad.getAbsolutePath()
            with open(self.filepath, 'rb') as f:
                reader = csv.reader(f,  delimiter=',')
                for rows in reader:
                    request = rows[0]
                    response = rows[1]
                    url = rows[2]
                    method = rows[3]
                    hostname = rows[4]
                    self.saveoutput.append(OutputList(request,response, url,method,hostname))
                f.close()
                self.fireTableDataChanged()

    def clearclicked(self,e):
    	for item in self.saveoutput:
    		self.saveoutput.remove(item)
    		self.fireTableDataChanged()



    def getTabCaption(self):
    	return "Custom Tab"

    def getUiComponent(self):
    	return self.Customtabui

    def getRowCount(self):
        try:
            return len(self.saveoutput)
        except:
            return 0

    def getColumnCount(self):
        return 3

    def getColumnName(self, columnIndex):
        
        if columnIndex == 0:
            return "URL"
        if columnIndex == 1:
            return "Method"
        if columnIndex == 2:
            return "Hostname"
        return ""

    def getValueAt(self, rowIndex, columnIndex):
        
        Tabledata = self.saveoutput[rowIndex]
        if columnIndex == 0:
            return Tabledata.url
        if columnIndex == 1:
            return Tabledata.method
        if columnIndex == 2:
            return Tabledata.hostname
        return ""

    def createMenuItems(self,invocation):
        menu = []
        menu.append(JMenuItem("Send To test Extension", None,actionPerformed=lambda x, inv=invocation: self.sendtotable(inv)))
        return menu

    def sendtotable(self, invocation):
    	requestinformation = invocation.getSelectedMessages()
    	for items in requestinformation:
    		req = self.helpers.analyzeRequest(items)
    		#req = self.helpers.analyzeRequest(items)
    		self.httpmethodmethod = req.getMethod()
    		self.url = items.getUrl()
    		self.hostname = items.getHost()
    		requestinbytes = items.getRequest()
    		self.requestinstring = self.helpers.bytesToString(requestinbytes)
    		responseinbytes = items.getResponse()
    		self.responseinstring = self.helpers.bytesToString(responseinbytes)
    		self.saveoutput.append(OutputList(self.requestinstring,self.responseinstring,self.url,self.httpmethodmethod,self.hostname))
    		row = len(self.saveoutput)
    		self.fireTableRowsInserted(row, row)

            

class CustomTable(JTable):
  
    def __init__(self, tableextend):
        self.tableextend = tableextend
        self.setModel(tableextend)
        self.setRowSelectionAllowed(True)
        self.setAutoCreateRowSorter(True)

class OutputList: 
    def __init__(self, request, response,url,method,hostname): 
        self.request = request
        self.response = response
        self.url = url
        self.method = method
        self.hostname = hostname
