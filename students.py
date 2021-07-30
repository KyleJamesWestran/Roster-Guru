import os

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_studentsUI(object):
    def setupUi(self, studentsUI):
        #UI Setup
        studentsUI.setObjectName("studentsUI")
        studentsUI.resize(720, 350)
        studentsUI.setMinimumSize(QtCore.QSize(720, 350))
        studentsUI.setMaximumSize(QtCore.QSize(720, 350))
        self.gridLayout_2 = QtWidgets.QGridLayout(studentsUI)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.studentName = QtWidgets.QLineEdit(studentsUI)
        self.studentName.setObjectName("studentName")
        self.gridLayout_2.addWidget(self.studentName, 1, 2, 1, 2)

        self.studentGrade = QtWidgets.QSpinBox(studentsUI)
        self.studentGrade.setObjectName("studentGrade")
        self.studentGrade.setMaximum(12)
        self.gridLayout_2.addWidget(self.studentGrade, 2, 2, 1, 2)

        self.studentFocus = QtWidgets.QComboBox(studentsUI)
        self.studentFocus.setObjectName("studentFocus")
        self.gridLayout_2.addWidget(self.studentFocus, 3, 2, 1, 2)

        self.parentName = QtWidgets.QLineEdit(studentsUI)
        self.parentName.setObjectName("parentName")
        self.gridLayout_2.addWidget(self.parentName, 4, 2, 1, 2)

        self.parentContact = QtWidgets.QLineEdit(studentsUI)
        self.parentContact.setObjectName("parentContact")
        self.gridLayout_2.addWidget(self.parentContact, 5, 2, 1, 2)

        self.rate = QtWidgets.QSpinBox(studentsUI)
        self.rate.setObjectName("rate")
        self.rate.setMaximum(999999)
        self.gridLayout_2.addWidget(self.rate, 6, 2, 1, 2)

        self.btnAdd = QtWidgets.QPushButton(studentsUI)
        self.btnAdd.setMinimumSize(QtCore.QSize(175, 50))
        self.btnAdd.setMaximumSize(QtCore.QSize(175, 50))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Resources/user add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAdd.setIcon(icon)
        self.btnAdd.setObjectName("btnAdd")
        self.gridLayout_2.addWidget(self.btnAdd, 9, 2, 1, 2)
        self.btnRemove = QtWidgets.QPushButton(studentsUI)
        self.btnRemove.setMinimumSize(QtCore.QSize(175, 50))
        self.btnRemove.setMaximumSize(QtCore.QSize(175, 50))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Resources/cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnRemove.setIcon(icon2)
        self.btnRemove.setObjectName("btnRemove")
        self.gridLayout_2.addWidget(self.btnRemove, 9, 4, 1, 2)
        self.btnBack = QtWidgets.QPushButton(studentsUI)
        self.btnBack.setMinimumSize(QtCore.QSize(175, 50))
        self.btnBack.setMaximumSize(QtCore.QSize(128, 50))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Resources/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBack.setIcon(icon1)
        self.btnBack.setIconSize(QtCore.QSize(20, 20))
        self.btnBack.setObjectName("btnBack")
        self.gridLayout_2.addWidget(self.btnBack, 9, 6, 1, 1)
        self.label_9 = QtWidgets.QLabel(studentsUI)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 6, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(studentsUI)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 5, 0, 1, 2)
        self.listStudents = QtWidgets.QListWidget(studentsUI)
        self.listStudents.setObjectName("listStudents")
        self.gridLayout_2.addWidget(self.listStudents, 1, 4, 8, 3)
        self.label_6 = QtWidgets.QLabel(studentsUI)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(studentsUI)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 2)
        self.label = QtWidgets.QLabel(studentsUI)
        self.label.setMinimumSize(QtCore.QSize(0, 60))
        self.label.setMaximumSize(QtCore.QSize(16777215, 60))
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 7)
        self.label_5 = QtWidgets.QLabel(studentsUI)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 4, 0, 1, 2)
        self.label_7 = QtWidgets.QLabel(studentsUI)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 3, 0, 1, 2)
        self.retranslateUi(studentsUI)
        QtCore.QMetaObject.connectSlotsByName(studentsUI)

        # Call Functions
        self.btnBack.clicked.connect(lambda: toMenu(self, studentsUI))
        self.btnAdd.clicked.connect(lambda: addStudent(self))
        self.btnRemove.clicked.connect(lambda: removeStudent(self))

        # Ui Update
        with open("Files/focus.txt") as focusFile:
            for lines in focusFile:
                lines = lines.replace('\n', '')
                self.studentFocus.addItem(lines)
        focusFile.close()
        updateStudents(self)

    def retranslateUi(self, studentsUI):
        _translate = QtCore.QCoreApplication.translate
        studentsUI.setWindowTitle(_translate("studentsUI", "Students"))
        self.btnAdd.setText(_translate("studentsUI", " ADD"))
        self.label_9.setText(_translate("studentsUI", "Rate:"))
        self.label_8.setText(_translate("studentsUI", "Parent Contact:"))
        self.label_6.setText(_translate("studentsUI", "Student Grade:"))
        self.label_2.setText(_translate("studentsUI", "Student Full Name:"))
        self.label.setText(_translate("studentsUI", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; color:#0e3262;\">STUDENTS</span></p></body></html>"))
        self.label_5.setText(_translate("studentsUI", "Parent Full Name:"))
        self.btnBack.setText(_translate("studentsUI", "BACK"))
        self.btnRemove.setText(_translate("studentsUI", " REMOVE"))
        self.label_7.setText(_translate("studentsUI", "Focus:"))

from RosterGuru import Ui_tutoringMainUI

def toMenu(self,studentsUI):
    self.window = QtWidgets.QWidget()
    self.ui = Ui_tutoringMainUI()
    self.ui.setupUi(self.window)
    self.window.show()
    studentsUI.hide()
    # print("button clicked") #Debug event

def addStudent(self):
    stuName = self.studentName.text()
    stuGrade = self.studentGrade.text()
    stuFocus = self.studentFocus.currentText()
    clientName = self.parentName.text()
    clientContact = self.parentContact.text()
    rate = self.rate.text()

    studentFile = open("Students/{0}.txt".format(stuName), "w+")

    info = ("{0},{1},{2},{3},{4},R{5}".format(stuName,stuGrade,stuFocus,clientName,clientContact,rate))

    with open("Files/clients.txt", "a+") as clientFile:
        clientFile.seek(0)
        clientFile.write(info + "\n")
        clientFile.close()
    updateStudents(self)

def removeStudent(self):
    item = self.listStudents.currentRow()
    student = self.listStudents.currentItem().text()
    student = student.split(",")
    student = student[0]

    clientFile = open("Files/clients.txt", "r")
    lines = clientFile.readlines()
    clientFile.close()
    del lines[item]
    clientFile = open("Files/clients.txt", "w+")
    for line in lines:
        clientFile.write(line)
    clientFile.close()
    updateStudents(self)

    os.remove("Students/{0}.txt".format(student))

def updateStudents(self):
    self.listStudents.clear()
    clientsFile = open("Files/clients.txt", 'r')
    count = 0
    while True:
        count += 1
        line = clientsFile.readline()
        line = line.replace(",",", ")
        if not line:
            break
        self.listStudents.insertItem(count, line.strip())
    clientsFile.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    studentsUI = QtWidgets.QWidget()
    ui = Ui_studentsUI()
    ui.setupUi(studentsUI)
    studentsUI.show()
    sys.exit(app.exec_())
