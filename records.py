from PyQt5 import QtCore, QtGui, QtWidgets, Qt

class AlignDelegate(QtWidgets.QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = QtCore.Qt.AlignCenter

class Ui_Records(object):
    def setupUi(self, recordsUi):
        recordsUi.setObjectName("Form")
        recordsUi.setMinimumSize(380,600)
        recordsUi.setMaximumSize(380,600)
        self.gridLayout = QtWidgets.QGridLayout(recordsUi)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(recordsUi)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 2)
        self.label = QtWidgets.QLabel(recordsUi)
        self.label.setMinimumWidth(100)
        self.label.setMaximumWidth(100)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.listStudent = QtWidgets.QComboBox(recordsUi)
        self.listStudent.setObjectName("listStudent")
        self.gridLayout.addWidget(self.listStudent, 1, 1, 1, 1)

        self.listRecords = QtWidgets.QTableWidget(recordsUi)
        self.listRecords.setObjectName("listRecords")
        self.listRecords.verticalHeader().hide()
        self.listRecords.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.listRecords.horizontalHeader().setSortIndicatorShown(False)
        #self.listRecords.horizontalHeader().setSectionResizeMode(Qt.QHeaderView.ResizeToContents)

        self.listRecords.horizontalHeader().stretchLastSection()
        self.gridLayout.addWidget(self.listRecords, 2, 0, 1, 2)
        self.btnRemove = QtWidgets.QPushButton(recordsUi)
        self.btnRemove.setMinimumSize(QtCore.QSize(175, 50))
        self.btnRemove.setMaximumSize(QtCore.QSize(175, 50))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Resources/cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnRemove.setIcon(icon2)
        self.btnRemove.setObjectName("btnRemove")
        self.gridLayout.addWidget(self.btnRemove, 3, 0, 1, 1)
        self.btnBack = QtWidgets.QPushButton(recordsUi)
        self.btnBack.setMinimumSize(QtCore.QSize(175, 50))
        self.btnBack.setMaximumSize(QtCore.QSize(128, 50))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Resources/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBack.setIcon(icon1)
        self.btnBack.setIconSize(QtCore.QSize(20, 20))
        self.btnBack.setObjectName("btnBack")
        self.gridLayout.addWidget(self.btnBack, 3, 1, 1, 1)
        self.retranslateUi(recordsUi)
        QtCore.QMetaObject.connectSlotsByName(recordsUi)

        # Call Functions
        #self.listStudent.currentIndexChanged.connect(lambda: displayRecords(self))
        updateList(self)
        displayRecords(self)
        self.btnBack.clicked.connect(lambda: toMenu(self, recordsUi))

    def retranslateUi(self, recordsUi):
        _translate = QtCore.QCoreApplication.translate
        recordsUi.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; color:#0f3362;\">RECORDS</span></p></body></html>"))
        self.label.setText(_translate("Form", "Student:"))
        self.btnRemove.setText(_translate("Form", "Remove"))
        self.btnBack.setText(_translate("Form", "Back"))

from RosterGuru import Ui_tutoringMainUI

def toMenu(self,recordsUi):
    self.window = QtWidgets.QWidget()
    self.ui = Ui_tutoringMainUI()
    self.ui.setupUi(self.window)
    self.window.show()
    recordsUi.hide()
    # print("button clicked") #Debug event

def updateList(self):
    clientFile = open("Files/clients.txt","r")
    lines = clientFile.readlines()
    length = len(lines)
    counter = 0

    while counter < length:
        students = lines[counter]
        for student in students:
            student = students.split(",")

        self.listStudent.addItem(student[0])
        self.listStudent.setItemText(counter, student[0])
        counter += 1

def displayRecords(self):
    student = self.listStudent.currentText()
    studentFile = open("Students/{0}.txt".format(student), "r+")
    rowNum = 0
    lines = studentFile.readlines()
    rowCount = len(lines)
    self.listRecords.setColumnCount(4)
    self.listRecords.setHorizontalHeaderLabels(['Date', 'Hours', 'Slot', 'Notes'])
    self.listRecords.setRowCount(rowCount)

    for row in lines:
        list = row.split(",")
        counter = 0
        for item in list:
            item = item.replace("\n", "")
            self.listRecords.setItem(rowNum, counter, QtWidgets.QTableWidgetItem(item))
            counter += 1
        rowNum += 1

    delegate = AlignDelegate(self.listRecords)
    self.listRecords.setItemDelegateForColumn(0, delegate)
    self.listRecords.setItemDelegateForColumn(1, delegate)
    self.listRecords.setItemDelegateForColumn(2, delegate)

def removeRecords(self):
    pass

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    recordsUi = QtWidgets.QWidget()
    ui = Ui_Records()
    ui.setupUi(recordsUi)
    recordsUi.show()
    sys.exit(app.exec_())
