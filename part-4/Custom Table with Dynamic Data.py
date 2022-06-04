
from burp import ITab
from burp import IBurpExtender
from javax.swing import JPanel
from javax.swing import JButton,JSplitPane,GroupLayout, LayoutStyle, JTextField
from java.lang import Short
from javax.swing import JTable
from javax.swing import JScrollPane
from javax.swing.table import DefaultTableModel, AbstractTableModel

class BurpExtender(IBurpExtender, ITab, AbstractTableModel):

    def registerExtenderCallbacks(self, callbacks):
        self.callbacks = callbacks
        self.Customtabui = JPanel()
        self.callbacks.setExtensionName("Test Extension")
        self.saveoutput =  []
        layout = GroupLayout(self.Customtabui)
        self.Customtabui.setLayout(layout)
        self.callbacks.addSuiteTab(self)
        Importbutton =  JButton("Import");
        Exportbutton =  JButton("Export");
        Clearbutton =  JButton("Clear");
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
