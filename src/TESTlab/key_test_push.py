import sys
import json
from PyQt5 import QtCore, QtWidgets


class Ui_Form(object):
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

        # Dictionary to store input data
        self.rows = []  # To keep track of rows (lineEdit, comboBox)

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

        # Keep track of lineEdit and comboBox for this row
        self.rows.append((lineEdit, comboBox))

    def delete_row(self, rowWidget):
        """Delete a specific row."""
        # Find and remove the row from self.rows
        for i, (lineEdit, comboBox) in enumerate(self.rows):
            if lineEdit.parentWidget() == rowWidget:
                self.rows.pop(i)
                break
        rowWidget.setParent(None)

    def save_data(self):
        """Save all data from lineEdit and comboBox to a JSON file."""
        data = []
        for lineEdit, comboBox in self.rows:
            row_data = {
                "text": lineEdit.text(),
                "operation": comboBox.currentText()
            }
            data.append(row_data)

        # Save to JSON file
        with open("data.json", "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        print("Data saved:", data)


class MyForm(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def closeEvent(self, event):
        """Override the closeEvent to save data on exit."""
        self.save_data()
        super().closeEvent(event)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    form = MyForm()
    form.show()
    sys.exit(app.exec_())
