
from burp import ITab
from burp import IBurpExtender
from javax.swing import JPanel
from javax.swing import JButton,JSplitPane,GroupLayout, LayoutStyle, JTextField
from java.lang import Short
from javax.swing import JTable
from javax.swing import JScrollPane
from javax.swing.table import DefaultTableModel

class BurpExtender(IBurpExtender, ITab):

    def registerExtenderCallbacks(self, callbacks):
        self.callbacks = callbacks
        self.Customtabui = JPanel()
        self.callbacks.setExtensionName("Test Extension")
        layout = GroupLayout(self.Customtabui)
        self.Customtabui.setLayout(layout)
        self.callbacks.addSuiteTab(self)
        Importbutton =  JButton("Import");
        Exportbutton =  JButton("Export");
        Clearbutton =  JButton("Clear");
        jSplitPane2 =  JSplitPane(JSplitPane.VERTICAL_SPLIT);
        self.colname = ['Number','String']
        self.rowvalue = [['1','One'],['2','Two']]
        self.DefaultModel = DefaultTableModel(self.rowvalue, self.colname)
        jScrollPane1 =  JScrollPane();
        jTable1 =  JTable(self.DefaultModel);
        jSplitPane3 =  JSplitPane();
        RequestTextbox =  JTextField()
        ResponseTextbox =  JTextField()
        jScrollPane1.setViewportView(jTable1);

        jSplitPane2.setLeftComponent(jScrollPane1);

        RequestTextbox.setText("Request");
        jSplitPane3.setLeftComponent(RequestTextbox);
        
        ResponseTextbox.setText("Response");
        jSplitPane3.setRightComponent(ResponseTextbox);

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
