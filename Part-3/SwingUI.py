from javax.swing import JButton, JSplitPane, JScrollPane, JTable, JTextField, GroupLayout
from javax.swing.table import DefaultTableModel
from javax.swing import JPanel
from java.lang import Short
		
Importbutton = JButton("Import");
Exportbutton = JButton("Export");
Clearbutton = JButton("Clear");
jSplitPane1 = JSplitPane();
jScrollPane1 = JScrollPane();
jTable1 = JTable();
jSplitPane2 = JSplitPane();
RequestTextbox = JTextField();
ResponseTextbox = JTextField();
self.colname = ['Number','String']
self.rowvalue = [['1','One'],['2','Two']]
self.DefaultModel = DefaultTableModel(self.rowvalue, self.colname)
jTable1 = JTable(self.DefaultModel)
jScrollPane1.setViewportView(jTable1);
jSplitPane1.setLeftComponent(jScrollPane1);
RequestTextbox.setText("jTextField1");
jSplitPane2.setLeftComponent(RequestTextbox);

ResponseTextbox.setText("jTextField2");
jSplitPane2.setRightComponent(ResponseTextbox);

jSplitPane1.setRightComponent(jSplitPane2);
self.Customtabui = JPanel()
layout = GroupLayout(self.Customtabui)
self.Customtabui.setLayout(layout)
layout.setHorizontalGroup(
            layout.createParallelGroup(GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addGap(65, 65, 65)
                .addComponent(Importbutton)
                .addGap(40, 40, 40)
                .addComponent(Exportbutton)
                .addGap(50, 50, 50)
                .addComponent(Clearbutton)
                .addContainerGap(66, Short.MAX_VALUE))
            .addGroup(layout.createSequentialGroup()
                .addContainerGap()
                .addComponent(jSplitPane1, GroupLayout.PREFERRED_SIZE, 0, Short.MAX_VALUE)
                .addContainerGap())
        );
layout.setVerticalGroup(
            layout.createParallelGroup(GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addGap(28, 28, 28)
                .addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                    .addComponent(Importbutton)
                    .addComponent(Exportbutton)
                    .addComponent(Clearbutton))
                .addGap(18, 18, 18)
                .addComponent(jSplitPane1, GroupLayout.DEFAULT_SIZE, 440, Short.MAX_VALUE)
                .addContainerGap())
        );
    
