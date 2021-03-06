from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
from PyQt5.QtGui import QPixmap, QPainter
import datetime

class AlignDelegate(QtWidgets.QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = QtCore.Qt.AlignCenter

class Ui_statementUI(object):
    def setupUi(self, statementUI):
        # UI Setup
        statementUI.setWindowIcon(QtGui.QIcon("Resources/icon.png"))
        statementUI.setObjectName("statementUI")
        statementUI.resize(998, 1673)
        statementUI.showMaximized()
        self.gridLayout = QtWidgets.QGridLayout(statementUI)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(statementUI)
        self.label.setMinimumSize(QtCore.QSize(0, 70))
        self.label.setMaximumSize(QtCore.QSize(16777215, 70))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 8)
        self.label_3 = QtWidgets.QLabel(statementUI)
        self.label_3.setMaximumSize(QtCore.QSize(120, 16777215))
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 5, 2, 3)
        self.label_2 = QtWidgets.QLabel(statementUI)
        self.label_2.setMaximumSize(QtCore.QSize(120, 16777215))
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.btnGenerate = QtWidgets.QPushButton(statementUI)
        self.btnGenerate.setMinimumSize(QtCore.QSize(0, 55))
        self.btnGenerate.setMaximumSize(QtCore.QSize(150, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Resources/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnGenerate.setIcon(icon)
        self.btnGenerate.setObjectName("btnGenerate")
        self.gridLayout.addWidget(self.btnGenerate, 1, 4, 2, 1)
        self.btnBack = QtWidgets.QPushButton(statementUI)
        self.btnBack.setMinimumSize(QtCore.QSize(100, 55))
        self.btnBack.setMaximumSize(QtCore.QSize(150, 16777215))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Resources/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBack.setIcon(icon1)
        self.btnBack.setObjectName("btnBack")
        self.gridLayout.addWidget(self.btnBack, 4, 6, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 4, 0, 1, 6)
        self.label_4 = QtWidgets.QLabel(statementUI)
        self.label_4.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 2, 1, 1)
        self.btnPrint = QtWidgets.QPushButton(statementUI)
        self.btnPrint.setMinimumSize(QtCore.QSize(100, 55))
        self.btnPrint.setMaximumSize(QtCore.QSize(150, 16777215))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Resources/printer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPrint.setIcon(icon2)
        self.btnPrint.setObjectName("btnPrint")
        self.gridLayout.addWidget(self.btnPrint, 4, 7, 1, 1)

        '''self.btnShare = QtWidgets.QPushButton(statementUI)
        self.btnShare.setMinimumSize(QtCore.QSize(100, 55))
        self.btnShare.setMaximumSize(QtCore.QSize(150, 16777215))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Resources/printer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnShare.setIcon(icon2)
        self.btnShare.setObjectName("btnPrint")
        self.gridLayout.addWidget(self.btnShare, 4, 5, 1, 1)'''

        self.selClient = QtWidgets.QComboBox(statementUI)
        self.selClient.setObjectName("selClient")
        self.gridLayout.addWidget(self.selClient, 1, 1, 1, 3)
        self.selFrom = QtWidgets.QDateEdit(statementUI)
        self.selFrom.setMaximumSize(QtCore.QSize(110, 16777215))
        self.selFrom.setObjectName("selFrom")
        self.gridLayout.addWidget(self.selFrom, 2, 1, 1, 1)
        self.selTo = QtWidgets.QDateEdit(statementUI)
        self.selTo.setMaximumSize(QtCore.QSize(110, 16777215))
        self.selTo.setObjectName("selTo")
        self.gridLayout.addWidget(self.selTo, 2, 3, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(statementUI)
        self.scrollArea.setStyleSheet("background: rgb(46, 52, 54)")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 978, 1453))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 3, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 0, 0, 1, 1)
        self.Page = QtWidgets.QScrollArea(self.scrollAreaWidgetContents)
        self.Page.setMinimumSize(QtCore.QSize(840, 1188))
        self.Page.setMaximumSize(QtCore.QSize(840, 1188))
        self.Page.setStyleSheet("background-color: rgb(255, 255, 255); border-width: 1px;")
        self.Page.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Page.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Page.setWidgetResizable(True)
        self.Page.setObjectName("Page")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 838, 1186))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.companyName = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.companyName.setMinimumSize(QtCore.QSize(0, 50))
        self.companyName.setStyleSheet("border-width: 1px; border-style: solid; border-color: #919191;")
        self.companyName.setObjectName("companyName")
        self.gridLayout_3.addWidget(self.companyName, 0, 0, 1, 2)
        self.label_18 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_18.setObjectName("label_18")
        self.gridLayout_3.addWidget(self.label_18, 7, 0, 1, 1)
        self.usrBank = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.usrBank.setMinimumSize(QtCore.QSize(375, 0))
        self.usrBank.setStyleSheet("border-width: 1px; border-style: solid; border-color: #919191;")
        self.usrBank.setObjectName("usrBank")
        self.gridLayout_3.addWidget(self.usrBank, 6, 1, 1, 1)
        self.clientContact = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.clientContact.setStyleSheet("border-width: 1px; border-style: solid; border-color: #919191;")
        self.clientContact.setObjectName("clientContact")
        self.gridLayout_3.addWidget(self.clientContact, 2, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_5.setMinimumSize(QtCore.QSize(0, 50))
        self.label_5.setStyleSheet("border-width: 1px; border-style: solid; border-color: #919191;")
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 4, 0, 1, 5)
        self.label_24 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_24.setObjectName("label_24")
        self.gridLayout_3.addWidget(self.label_24, 10, 0, 1, 1)
        self.usrMessage = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.usrMessage.setMinimumSize(QtCore.QSize(0, 50))
        self.usrMessage.setStyleSheet("border-width: 1px; border-style: solid; border-color: #919191;")
        self.usrMessage.setObjectName("usrMessage")
        self.gridLayout_3.addWidget(self.usrMessage, 11, 0, 1, 5)
        self.usrAccNum = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.usrAccNum.setMinimumSize(QtCore.QSize(375, 0))
        self.usrAccNum.setStyleSheet("border-width: 1px; border-style: solid; border-color: #919191;")
        self.usrAccNum.setObjectName("usrAccNum")
        self.gridLayout_3.addWidget(self.usrAccNum, 8, 1, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_20.setObjectName("label_20")
        self.gridLayout_3.addWidget(self.label_20, 8, 0, 1, 1)

        self.statementTable = QtWidgets.QTableWidget(self.scrollAreaWidgetContents_2)
        self.statementTable.setObjectName("statementTable")
        self.statementTable.horizontalHeader().setSortIndicatorShown(False)
        self.statementTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.statementTable.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.statementTable.verticalHeader().hide()
        self.statementTable.setColumnCount(4)
        self.statementTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.statementTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.statementTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.statementTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.statementTable.setHorizontalHeaderItem(3, item)
        self.statementTable.setStyleSheet("border-width: 1px; border-style: solid; border-color: #919191;")
        self.statementTable.horizontalHeader().setStyleSheet("border-width: 0px;")
        self.statementTable.setColumnWidth(0, 150)
        self.gridLayout_3.addWidget(self.statementTable, 5, 0, 1, 5)

        self.usrRef = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.usrRef.setMinimumSize(QtCore.QSize(375, 0))
        self.usrRef.setStyleSheet("border-width: 1px; border-style: solid; border-color: #919191;")
        self.usrRef.setObjectName("usrRef")
        self.gridLayout_3.addWidget(self.usrRef, 10, 1, 1, 1)
        self.companyLogo = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.companyLogo.setMinimumSize(QtCore.QSize(288, 120))
        self.companyLogo.setMaximumSize(QtCore.QSize(288, 120))
        self.companyLogo.setStyleSheet("border: 3px solid;border-color: rgb(181, 181, 181);border-radius: 10px;")
        self.companyLogo.setObjectName("companyLogo")
        self.gridLayout_3.addWidget(self.companyLogo, 0, 2, 3, 3)
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_6.setMinimumSize(QtCore.QSize(140, 0))
        self.label_6.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 1, 0, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_22.setObjectName("label_22")
        self.gridLayout_3.addWidget(self.label_22, 9, 0, 1, 1)
        self.usrAccName = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.usrAccName.setMinimumSize(QtCore.QSize(375, 0))
        self.usrAccName.setStyleSheet("border-width: 1px; border-style: solid; border-color: #919191;")
        self.usrAccName.setObjectName("usrAccName")
        self.gridLayout_3.addWidget(self.usrAccName, 7, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_16.setObjectName("label_16")
        self.gridLayout_3.addWidget(self.label_16, 6, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_7.setMinimumSize(QtCore.QSize(140, 0))
        self.label_7.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 2, 0, 1, 1)
        self.clientName = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.clientName.setStyleSheet("border-width: 1px; border-style: solid; border-color: #919191;")
        self.clientName.setObjectName("clientName")
        self.gridLayout_3.addWidget(self.clientName, 1, 1, 1, 1)
        self.usrBranch = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.usrBranch.setMinimumSize(QtCore.QSize(375, 0))
        self.usrBranch.setStyleSheet("border-width: 1px; border-style: solid; border-color: #919191;")
        self.usrBranch.setObjectName("usrBranch")
        self.gridLayout_3.addWidget(self.usrBranch, 9, 1, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox.setStyleSheet("border-width: 1px; border-style: solid; border-color: #919191;")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_12.setStyleSheet("border-width: 0px; border-style: solid; border-color: #919191;")
        self.label_12.setObjectName("label_12")
        self.gridLayout_4.addWidget(self.label_12, 1, 0, 1, 1)
        self.totalHours = QtWidgets.QLabel(self.groupBox)
        self.totalHours.setObjectName("totalHours")
        self.gridLayout_4.addWidget(self.totalHours, 1, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_8.setStyleSheet("border-width: 0px; border-style: solid; border-color: #919191;")
        self.label_8.setObjectName("label_8")
        self.gridLayout_4.addWidget(self.label_8, 2, 0, 1, 1)
        self.totalCost = QtWidgets.QLabel(self.groupBox)
        self.totalCost.setObjectName("totalCost")
        self.gridLayout_4.addWidget(self.totalCost, 2, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setStyleSheet("border-width: 0px; border-style: solid; border-color: #919191;")
        self.label_9.setObjectName("label_9")
        self.gridLayout_4.addWidget(self.label_9, 0, 0, 1, 2)
        self.gridLayout_3.addWidget(self.groupBox, 6, 2, 5, 3)
        self.Page.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_2.addWidget(self.Page, 0, 1, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 3, 0, 1, 8)
        self.retranslateUi(statementUI)
        QtCore.QMetaObject.connectSlotsByName(statementUI)
        header = self.statementTable.horizontalHeader()
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        QtCore.QMetaObject.connectSlotsByName(statementUI)

        # Call Functions
        updateCompanyInfo(self)
        updateList(self)
        updateDates(self)
        #self.btnPrint.clicked.connect(lambda: print(self))
        self.btnPrint.clicked.connect(self.printDialog)
        self.btnGenerate.clicked.connect(lambda: loadStatement(self))
        self.btnBack.clicked.connect(lambda: toMenu(self, statementUI))

    def retranslateUi(self, statementUI):
        _translate = QtCore.QCoreApplication.translate
        statementUI.setWindowTitle(_translate("statementUI", "Statement"))
        self.label.setText(_translate("statementUI", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; color:#0e3262;\">STATEMENT</span></p></body></html>"))
        self.label_3.setText(_translate("statementUI", "Select Month:"))
        self.label_2.setText(_translate("statementUI", "Select Client:"))
        self.btnGenerate.setText(_translate("statementUI", " GENERATE"))
        self.btnBack.setText(_translate("statementUI", " BACK"))
        self.label_4.setText(_translate("statementUI", "<html><head/><body><p align=\"center\">- TO -</p></body></html>"))
        self.btnPrint.setText(_translate("statementUI", " PRINT"))
        #self.btnShare.setText(_translate("statementUI", " SHARE"))
        self.companyName.setText(_translate("statementUI", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">COMPANY NAME</span></p></body></html>"))
        self.label_18.setText(_translate("statementUI", "<html><head/><body><p><span style=\" font-weight:600;\">ACCOUNT NAME:</span></p></body></html>"))
        self.usrBank.setText(_translate("statementUI", "BANK NAME HERE"))
        self.clientContact.setText(_translate("statementUI", "Number"))
        self.label_5.setText(_translate("statementUI", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; color:#000000;\">STATEMENT</span></p></body></html>"))
        self.label_24.setText(_translate("statementUI", "<html><head/><body><p><span style=\" font-weight:600;\">REFERENCE:</span></p></body></html>"))
        self.usrMessage.setText(_translate("statementUI", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">THANK YOU MESSAGE HERE</span></p></body></html>"))
        self.usrAccNum.setText(_translate("statementUI", "ACCOUNT NUMBER HERE"))
        self.label_20.setText(_translate("statementUI", "<html><head/><body><p><span style=\" font-weight:600;\">ACCOUNT NUMBER:</span></p></body></html>"))
        item = self.statementTable.horizontalHeaderItem(0)
        item.setText(_translate("statementUI", "Date"))
        item = self.statementTable.horizontalHeaderItem(1)
        item.setText(_translate("statementUI", "Descripition"))
        item = self.statementTable.horizontalHeaderItem(2)
        item.setText(_translate("statementUI", "Time (h)"))
        item = self.statementTable.horizontalHeaderItem(3)
        item.setText(_translate("statementUI", "Rate"))
        self.usrRef.setText(_translate("statementUI", "REFERENCE HERE"))
        self.companyLogo.setText(_translate("statementUI", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; font-weight:600; color:#888a85;\">LOGO</span></p></body></html>"))
        self.label_6.setText(_translate("statementUI", "<html><head/><body><p><span style=\" font-weight:600;\">CLIENT NAME:</span></p></body></html>"))
        self.label_22.setText(_translate("statementUI", "<html><head/><body><p><span style=\" font-weight:600;\">BRANCH CODE:</span></p></body></html>"))
        self.usrAccName.setText(_translate("statementUI", "ACCOUNT NAME HERE"))
        self.label_16.setText(_translate("statementUI", "<html><head/><body><p><span style=\" font-weight:600;\">BANK NAME:</span></p></body></html>"))
        self.label_7.setText(_translate("statementUI", "<html><head/><body><p><span style=\" font-weight:600;\">CONTACT NUMBER</span></p></body></html>"))
        self.clientName.setText(_translate("statementUI", "Name"))
        self.usrBranch.setText(_translate("statementUI", "BRANCH HERE"))
        self.label_12.setText(_translate("statementUI", "<html><head/><body><p align=\"right\"><span style=\" font-weight:600; color:#000000;\">TOTAL HOURS:</span></p></body></html>"))
        self.totalHours.setText(_translate("statementUI", "<html><head/><body><p align=\"right\">99 Hrs</p></body></html>"))
        self.label_8.setText(_translate("statementUI", "<html><head/><body><p align=\"right\"><span style=\" font-weight:600; color:#000000;\">TOTAL COST:</span></p></body></html>"))
        self.totalCost.setText(_translate("statementUI", "<html><head/><body><p align=\"right\">R999999.99</p></body></html>"))
        self.label_9.setText(_translate("statementUI", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">BREAKDOWN</span></p></body></html>"))

    def printDialog(self):
        printer = QPrinter(QPrinter.HighResolution)
        dialog = QPrintDialog(printer)
        printer.setPageSize(QPrinter.A4)
        width = printer.width()
        height = printer.height()

        if dialog.exec_() == QPrintDialog.Accepted:
            painter = QPainter()
            printer.setFullPage(True)
            painter.begin(printer)
            screen = self.Page.grab()
            painter.setRenderHint(QtGui.QPainter.SmoothPixmapTransform)
            screen = screen.scaledToWidth(width)
            screen = screen.scaledToHeight(height)
            painter.drawPixmap(0, 0, screen)

            painter.end()

from RosterGuru import Ui_tutoringMainUI

def toMenu(self,statementUI):
    self.window = QtWidgets.QWidget()
    self.ui = Ui_tutoringMainUI()
    self.ui.setupUi(self.window)
    self.window.show()
    statementUI.hide()
    # print("button clicked") #Debug event

def updateCompanyInfo(self):
    settingsFile = open("Files/settings.txt", "r")
    lines = settingsFile.readlines()
    myCompanyName = lines[0]

    lines[2] = lines[2].replace("\n", "")
    lines[3] = lines[3].replace("\n", "")
    lines[4] = lines[4].replace("\n", "")
    lines[5] = lines[5].replace("\n", "")
    lines[6] = lines[6].replace("\n", "")

    myMsg = lines[1]
    myBank = lines[2]
    myHolder = lines[3]
    myAccNum = lines[4]
    myBranch = lines[5]
    myRef = lines[6]

    self.companyName.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">{}</span></p></body></html>".format(myCompanyName))
    self.usrMessage.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">{0}</span></p></body></html>".format(myMsg))
    self.usrBank.setText(myBank)
    self.usrAccName.setText(myHolder)
    self.usrAccNum.setText(myAccNum)
    self.usrBranch.setText(myBranch)
    self.usrRef.setText(myRef)
    settingsFile.close()

    pathFile = open("Files/paths.txt", "r")
    imagePath = pathFile.readlines()
    imagePath = str(imagePath)
    imagePath = imagePath.replace("['", '')
    imagePath = imagePath.replace("']", '')
    pathFile.close()
    pixmap = QPixmap(imagePath)
    self.companyLogo.setPixmap(QPixmap(pixmap))
    self.companyLogo.setScaledContents(True)

    if imagePath == "[]":
        self.companyLogo.setStyleSheet("border: 3px solid;border-color: rgb(181, 181, 181);border-radius: 10px;")
        _translate = QtCore.QCoreApplication.translate
        self.companyLogo.setText(_translate("SettingsUI",
                                            "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; font-weight:600; color:#888a85;\">LOGO</span></p></body></html>"))
    else:
        self.companyLogo.setStyleSheet("")

def updateList(self):
    clientFile = open("Files/clients.txt","r")
    lines = clientFile.readlines()
    length = len(lines)
    counter = 0

    while counter < length:
        students = lines[counter]
        for student in students:
            student = students.split(",")

        self.selClient.addItem(student[0])
        self.selClient.setItemText(counter, student[0])
        counter += 1

def updateDates(self):
    today = datetime.date.today()
    dateFrom = today.replace(day=1)
    dateTo = (today.replace(day=1) + datetime.timedelta(days=32)).replace(day=1) - datetime. timedelta(days=1)
    self.selFrom.setDate(dateFrom)
    self.selTo.setDate(dateTo)

def loadStatement(self):
    self.statementTable.setRowCount(0)
    student = self.selClient.currentText()
    dateFrom = self.selFrom.date()
    dateTo = self.selTo.date()
    clientFile = open("Files/clients.txt", "r+")
    lines = clientFile.readlines()

    settingsFile = open("Files/settings.txt","r+")
    settings = settingsFile.readlines()
    settingsFile.close()

    description = settings[7]

    if any(student in string for string in lines) == True:
        index = [lines.index(i) for i in lines if student in i]
        display = lines[index[0]]
        client = display.split(",")
        client[5] = client[5].replace("\n", "")
        clientName = client[3]
        clientContact = client[4]
        rate = client[5]

    self.clientName.setText(clientName)
    self.clientContact.setText(clientContact)
    studentFile = open("Students/{0}.txt".format(student), "r+")
    statementSelection = []
    rowPosition = self.statementTable.rowCount()
    self.statementTable.setAlternatingRowColors(True)
    self.statementTable.verticalHeader().setSectionResizeMode(Qt.QHeaderView.ResizeToContents)
    self.statementTable.setShowGrid(False)

    for lines in studentFile:
        data = lines.split(",")
        data[3] = data[3].replace("\n","")
        if data[3] == "":
            data[3] = description
        session = data[0],data[1],data[2],data[3]

        date = QtCore.QDate.fromString(data[0], 'yyyy-MM-dd')

        if dateFrom <= date <= dateTo:
            statementSelection.append(session)
            self.statementTable.insertRow(rowPosition)
            self.statementTable.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(data[0]))
            self.statementTable.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(data[3]))
            self.statementTable.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(data[1]))
            self.statementTable.setItem(rowPosition, 3, QtWidgets.QTableWidgetItem(rate))

    delegate = AlignDelegate(self.statementTable)
    self.statementTable.setItemDelegateForColumn(0, delegate)
    self.statementTable.setItemDelegateForColumn(2, delegate)
    self.statementTable.setItemDelegateForColumn(3, delegate)
    self.statementTable.setStyleSheet("border-width: 1px; border-style: solid; border-color: #919191;alternate-background-color: #C0C0C0;")
    self.statementTable.horizontalHeader().setStyleSheet("border-width: 0px;")

    studentFile.close()
    self.statementTable.sortItems(0)
    calculateCosts(self, rate)

def calculateCosts(self,rate):
    nrows = self.statementTable.rowCount()
    hours = []

    for row in range(0, nrows):
        item = self.statementTable.item(row, 2)
        hours.append(float(item.text()))

    totalHours = sum(hours)
    self.totalHours.setText("<html><head/><body><p align=\"right\">{} hours</p></body></html>".format(totalHours))
    rate = rate.replace("R","")
    totalCost = float(rate) * totalHours
    self.totalCost.setText("<html><head/><body><p align=\"right\">R{}</p></body></html>".format(totalCost))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    statementUI = QtWidgets.QWidget()
    ui = Ui_statementUI()
    ui.setupUi(statementUI)
    statementUI.show()
    sys.exit(app.exec_())
