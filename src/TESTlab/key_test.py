from PyQt5 import QtCore, QtWidgets


class key_process(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 400)
        Form.setStyleSheet("background-color: rgb(172, 172, 172);")

        # Main vertical layout
        self.mainLayout = QtWidgets.QVBoxLayout(Form)
        self.mainLayout.setContentsMargins(10, 10, 10, 10)

        # Scroll area for dynamic widgets
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setWidgetResizable(True)
        self.scrollContent = QtWidgets.QWidget()
        self.scrollLayout = QtWidgets.QVBoxLayout(self.scrollContent)
        self.scrollContent.setLayout(self.scrollLayout)
        self.scrollArea.setWidget(self.scrollContent)
        self.mainLayout.addWidget(self.scrollArea)

        # Button to add new widgets
        self.addButton = QtWidgets.QPushButton(Form)
        self.addButton.setText("+ เพิ่ม")
        self.addButton.setStyleSheet("background-color: rgb(85, 255, 0);\n"
                                     "font: 75 10pt \"MS Shell Dlg 2\";")
        self.addButton.clicked.connect(self.add_new_row)
        self.mainLayout.addWidget(self.addButton)

        # Add the first row by default
        self.add_new_row()

    def add_new_row(self):
        """Add a new row with lineEdit, comboBox, and pushButton."""
        rowWidget = QtWidgets.QWidget(self.scrollContent)
        rowLayout = QtWidgets.QHBoxLayout(rowWidget)

        # Create lineEdit
        lineEdit = QtWidgets.QLineEdit(rowWidget)
        lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                               "font: 16pt \"MS Shell Dlg 2\";")
        rowLayout.addWidget(lineEdit)

        # Create comboBox
        comboBox = QtWidgets.QComboBox(rowWidget)
        comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        comboBox.addItems(["Operation", "Inspection", "Transportation", "Delay", "Storage"])
        rowLayout.addWidget(comboBox)

        # Create delete button
        delButton = QtWidgets.QPushButton(rowWidget)
        delButton.setText("Del")
        delButton.setStyleSheet("background-color: rgb(255, 0, 0);\n"
                                "color: rgb(255, 255, 255);\n"
                                "font: 75 10pt \"MS Shell Dlg 2\";")
        delButton.clicked.connect(lambda: self.delete_row(rowWidget))
        rowLayout.addWidget(delButton)

        # Add the row to the scroll layout
        self.scrollLayout.addWidget(rowWidget)

    def delete_row(self, rowWidget):
        """Delete a specific row."""
        rowWidget.setParent(None)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = key_process()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
