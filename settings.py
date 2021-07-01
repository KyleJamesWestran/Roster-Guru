from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap

class Ui_SettingsUI(object):
    def setupUi(self, SettingsUI):
        #UI Setup
        SettingsUI.setObjectName("SettingsUI")
        SettingsUI.setMinimumSize(QtCore.QSize(690, 450))
        SettingsUI.setMaximumSize(QtCore.QSize(690, 450))
        self.gridLayout = QtWidgets.QGridLayout(SettingsUI)
        self.gridLayout.setObjectName("gridLayout")

        self.companyName = QtWidgets.QLineEdit(SettingsUI)
        self.companyName.setObjectName("companyName")
        self.gridLayout.addWidget(self.companyName, 2, 2, 1, 1)
        self.usrMessage = QtWidgets.QTextEdit(SettingsUI)
        self.usrMessage.setObjectName("usrMessage")
        self.usrMessage.setFixedWidth(300)
        self.gridLayout.addWidget(self.usrMessage, 4, 1, 6, 2)
        self.usrBank = QtWidgets.QLineEdit(SettingsUI)
        self.usrBank.setObjectName("usrButton")
        self.gridLayout.addWidget(self.usrBank, 2, 5, 1, 2)
        self.usrAccHold = QtWidgets.QLineEdit(SettingsUI)
        self.usrAccHold.setObjectName("usrAccHold")
        self.gridLayout.addWidget(self.usrAccHold, 3, 5, 1, 2)
        self.usrAccNum = QtWidgets.QLineEdit(SettingsUI)
        self.usrAccNum.setObjectName("usrAccNum")
        self.gridLayout.addWidget(self.usrAccNum, 4, 5, 1, 2)
        self.usrBankCode = QtWidgets.QLineEdit(SettingsUI)
        self.usrBankCode.setObjectName("usrBankCode")
        self.gridLayout.addWidget(self.usrBankCode, 5, 5, 1, 2)
        self.usrRef = QtWidgets.QLineEdit(SettingsUI)
        self.usrRef.setObjectName("usrRef")
        self.gridLayout.addWidget(self.usrRef, 6, 5, 1, 2)
        self.usrFocus = QtWidgets.QLineEdit(SettingsUI)
        self.usrFocus.setObjectName("usrFocus")
        self.gridLayout.addWidget(self.usrFocus, 7, 5, 1, 1)
        self.btnAdd = QtWidgets.QPushButton(SettingsUI)
        #self.btnAdd.setMinimumSize(QtCore.QSize(0, 55))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Resources/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAdd.setIcon(icon1)
        self.btnAdd.setIconSize(QtCore.QSize(13, 13))
        self.btnAdd.setObjectName("btnAdd")
        self.gridLayout.addWidget(self.btnAdd, 7, 6, 1, 1)
        self.btnRemove = QtWidgets.QPushButton(SettingsUI)
        # self.btnRemove.setMinimumSize(QtCore.QSize(0, 55))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Resources/cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnRemove.setIcon(icon1)
        self.btnRemove.setIconSize(QtCore.QSize(13, 13))
        self.btnRemove.setObjectName("btnRemove")
        self.gridLayout.addWidget(self.btnRemove, 8, 6, 1, 1)
        self.listFocus = QtWidgets.QComboBox(SettingsUI)
        self.listFocus.setObjectName("listFocus")
        self.gridLayout.addWidget(self.listFocus, 8, 5, 1, 1)
        self.btnBrowse = QtWidgets.QPushButton(SettingsUI)
        self.btnBrowse.setMinimumSize(QtCore.QSize(0, 100))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Resources/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBrowse.setIcon(icon)
        self.btnBrowse.setObjectName("btnBrowse")
        self.gridLayout.addWidget(self.btnBrowse, 9, 3, 1, 2)
        self.btnBack = QtWidgets.QPushButton(SettingsUI)
        self.btnBack.setMinimumSize(QtCore.QSize(0, 40))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Resources/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBack.setIcon(icon2)
        self.btnBack.setObjectName("btnBack")
        self.gridLayout.addWidget(self.btnBack, 10, 6, 1, 1)

        self.label_4 = QtWidgets.QLabel(SettingsUI)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 3, 1, 2)
        self.companyLogo = QtWidgets.QLabel(SettingsUI)
        self.companyLogo.setMinimumSize(QtCore.QSize(230, 100))
        self.companyLogo.setMaximumSize(QtCore.QSize(230, 100))
        self.companyLogo.setObjectName("companyLogo")
        self.gridLayout.addWidget(self.companyLogo, 9, 5, 1, 2)
        self.label_9 = QtWidgets.QLabel(SettingsUI)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 6, 3, 1, 2)
        self.label_3 = QtWidgets.QLabel(SettingsUI)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 3, 1, 1)
        self.label_7 = QtWidgets.QLabel(SettingsUI)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 4, 3, 1, 2)
        self.label_11 = QtWidgets.QLabel(SettingsUI)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 7, 3, 1, 1)
        self.label_10 = QtWidgets.QLabel(SettingsUI)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 3, 1, 1, 2)
        self.label = QtWidgets.QLabel(SettingsUI)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 2, 7)
        self.label_2 = QtWidgets.QLabel(SettingsUI)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(SettingsUI)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 5, 3, 1, 2)

        self.retranslateUi(SettingsUI)
        QtCore.QMetaObject.connectSlotsByName(SettingsUI)

        #Update UI
        settingsFile = open("settings.txt", "r")
        lines = settingsFile.readlines()
        myCompanyName = lines[0]
        myMsg = lines[1]
        myBank = lines[2]
        myHolder = lines[3]
        myAccNum = lines[4]
        myBranch = lines[5]
        myRef = lines[6]
        self.companyName.setText(myCompanyName)
        self.usrMessage.setPlainText(myMsg)
        self.usrBank.setText(myBank)
        self.usrAccHold.setText(myHolder)
        self.usrAccNum.setText(myAccNum)
        self.usrBankCode.setText(myBranch)
        self.usrRef.setText(myRef)
        settingsFile.close()

        focusFile = open("focus.txt", "r")
        with open("focus.txt") as file:
            for lines in focusFile:
                lines = lines.replace('\n', '')
                self.listFocus.addItem(lines)
        focusFile.close()

        pathFile = open("paths.txt", "r")
        imagePath = pathFile.readlines()
        imagePath = str(imagePath)
        imagePath = imagePath.replace("['",'')
        imagePath = imagePath.replace("']", '')
        print(imagePath)
        pathFile.close()
        pixmap = QPixmap(imagePath)
        self.companyLogo.setPixmap(QPixmap(pixmap))
        self.companyLogo.setScaledContents(True)
        if imagePath == "[]":
            self.companyLogo.setStyleSheet("border: 3px solid;border-color: rgb(181, 181, 181);border-radius: 10px;")
            _translate = QtCore.QCoreApplication.translate
            self.companyLogo.setText(_translate("SettingsUI","<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; font-weight:600; color:#888a85;\">LOGO</span></p></body></html>"))
        else:
            self.companyLogo.setStyleSheet("")


        #Call Functions
        self.btnBack.clicked.connect(lambda: updateSettings(self, SettingsUI))
        self.btnAdd.clicked.connect(lambda: addFocus(self))
        self.btnRemove.clicked.connect(lambda: removeFocus(self))
        self.btnBrowse.clicked.connect(lambda: getImage(self, self.companyLogo))

    def retranslateUi(self, SettingsUI):
        _translate = QtCore.QCoreApplication.translate
        SettingsUI.setWindowTitle(_translate("SettingsUI", "Settings"))
        self.label_4.setText(_translate("SettingsUI", "Account Holder:"))
        self.btnBrowse.setText(_translate("SettingsUI", " BROWSE"))
        self.label_9.setText(_translate("SettingsUI", "Reference:"))
        self.label_3.setText(_translate("SettingsUI", "Bank:"))
        self.label_7.setText(_translate("SettingsUI", "Account Number:"))
        self.label_11.setText(_translate("SettingsUI", "Focus:"))
        self.label_10.setText(_translate("SettingsUI", "Statement Thank you message:"))
        self.label.setText(_translate("SettingsUI", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; color:#0f3362;\">SETTINGS</span></p></body></html>"))
        self.label_2.setText(_translate("SettingsUI", "Company Name:"))
        self.label_8.setText(_translate("SettingsUI", "Branch Code:"))
        self.btnAdd.setText(_translate("SettingsUI", " Add"))
        self.btnRemove.setText(_translate("SettingsUI", " Remove"))
        self.btnBack.setText(_translate("SettingsUI", " Back"))

from tutoringMain import Ui_tutoringMainUI

def toMenu(self,SettingsUI):
    self.window = QtWidgets.QWidget()
    self.ui = Ui_tutoringMainUI()
    self.ui.setupUi(self.window)
    self.window.show()
    SettingsUI.hide()
    #print("button clicked") #Debug event

def updateSettings(self,SettingsUI):
    open('settings.txt', 'w').close()
    cName = self.companyName.text()
    cName = cName.replace('\n', '')
    uMessage = self.usrMessage.toPlainText()
    uMessage = uMessage.replace('\n', '')
    uBank = self.usrBank.text()
    uBank = uBank.replace('\n', '')
    uAccHold = self.usrAccHold.text()
    uAccHold = uAccHold.replace('\n', '')
    uAccNum = self.usrAccNum.text()
    uAccNum = uAccNum.replace('\n', '')
    uBankCode = self.usrBankCode.text()
    uBankCode = uBankCode.replace('\n', '')
    uRef = self.usrRef.text()
    uRef = uRef.replace('\n', '')

    settingsFile = open("settings.txt","a")
    settingsFile.write(cName + "\n")
    settingsFile.write(uMessage + "\n")
    settingsFile.write(uBank + "\n")
    settingsFile.write(uAccHold + "\n")
    settingsFile.write(uAccNum + "\n")
    settingsFile.write(uBankCode + "\n")
    settingsFile.write(uRef)

    settingsFile.close()
    toMenu(self, SettingsUI)

def addFocus(self):

    focus = self.usrFocus.text()
    if focus == "":
        return
    else:
        self.listFocus.clear()
        focusFile = open("focus.txt", "a")
        focusFile.write(focus + "\n")
        focusFile.close()

        focusFile = open("focus.txt", "r")
        with open("focus.txt") as file:
            for lines in focusFile:
                lines = lines.replace('\n', '')
                self.listFocus.addItem(lines)

        last = self.listFocus.count()
        last = last - 1
        self.listFocus.setCurrentIndex(last)

def removeFocus(self):
    item = self.listFocus.currentText()
    focusFile = open("focus.txt", "r")
    lines = focusFile.readlines()
    focusFile.close()

    focusFile = open("focus.txt", "w")
    for line in lines:
        if line.strip("\n") != item:
            focusFile.write(line)
    focusFile.close()

    index = self.listFocus.currentIndex()
    self.listFocus.removeItem(index)

def getImage(self, logo):
    open('paths.txt', 'w').close()
    fname = QFileDialog.getOpenFileName(logo, 'Open file','c:\\', "Image files (*.jpg *.gif *.jpg *.png)")
    imagePath = fname[0]
    pathFile = open("paths.txt", "a")
    pathFile.write(imagePath)
    pathFile.close()
    pixmap = QPixmap(imagePath)
    self.companyLogo.setPixmap(QPixmap(pixmap))
    self.companyLogo.setScaledContents(True)
    self.companyLogo.setStyleSheet("")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SettingsUI = QtWidgets.QWidget()
    ui = Ui_SettingsUI()
    ui.setupUi(SettingsUI)
    SettingsUI.show()
    sys.exit(app.exec_())