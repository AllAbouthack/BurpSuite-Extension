        from javax.swing import JButton, JSplitPane, JScrollPane, JTable, JTextField, GroupLayout
		from javax.swing.table import DefaultTableModel
		Importbutton = JButton();
        Exportbutton = JButton();
        Clearbutton = JButton();
        jSplitPane1 = JSplitPane();
        jScrollPane1 = JScrollPane();
        jTable1 = JTable();
        jSplitPane2 = JSplitPane();
        RequestTextbox = JTextField();
        ResponseTextbox = JTextField();

        Importbutton.setText("Import");
        

        Exportbutton.setText("Export");

        Clearbutton.setText("Clear");

        jSplitPane1.setOrientation(JSplitPane.VERTICAL_SPLIT);

        jTable1.setModel(DefaultTableModel(
            Object [][] {
                {null, null, null, null},
                {null, null, null, null},
                {null, null, null, null},
                {null, null, null, null}
            },
            String [] {
                "Title 1", "Title 2", "Title 3", "Title 4"
            }
        ));
        jScrollPane1.setViewportView(jTable1);

        jSplitPane1.setLeftComponent(jScrollPane1);

        RequestTextbox.setText("jTextField1");
        jSplitPane2.setLeftComponent(RequestTextbox);

        ResponseTextbox.setText("jTextField2");
        jSplitPane2.setRightComponent(ResponseTextbox);

        jSplitPane1.setRightComponent(jSplitPane2);

        GroupLayout layout = GroupLayout(this);
        this.setLayout(layout);
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
    
