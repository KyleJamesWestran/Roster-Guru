from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_tutoringMainUI(object):
    def setupUi(self, tutoringMainUI):
        #UI Setup
        tutoringMainUI.setWindowIcon(QtGui.QIcon("Resources/icon.png"))
        tutoringMainUI.setObjectName("tutoringMainUI")
        tutoringMainUI.resize(357, 421)
        tutoringMainUI.setMinimumSize(QtCore.QSize(357, 421))
        tutoringMainUI.setMaximumSize(QtCore.QSize(357, 421))
        self.gridLayout = QtWidgets.QGridLayout(tutoringMainUI)
        self.gridLayout.setObjectName("gridLayout")
        self.btnStatement = QtWidgets.QPushButton(tutoringMainUI)
        self.btnStatement.setMinimumSize(QtCore.QSize(0, 60))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Resources/statement.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnStatement.setIcon(icon)
        self.btnStatement.setIconSize(QtCore.QSize(20, 20))
        self.btnStatement.setObjectName("btnStatement")
        self.gridLayout.addWidget(self.btnStatement, 3, 0, 1, 1)
        self.btnSchedule = QtWidgets.QPushButton(tutoringMainUI)
        self.btnSchedule.setMinimumSize(QtCore.QSize(0, 60))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Resources/calendar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSchedule.setIcon(icon1)
        self.btnSchedule.setObjectName("btnSchedule")
        self.gridLayout.addWidget(self.btnSchedule, 5, 0, 1, 1)
        self.label = QtWidgets.QLabel(tutoringMainUI)
        self.label.setMaximumSize(QtCore.QSize(16777215, 80))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.btnAdd = QtWidgets.QPushButton(tutoringMainUI)
        self.btnAdd.setMinimumSize(QtCore.QSize(0, 60))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Resources/user add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAdd.setIcon(icon2)
        self.btnAdd.setObjectName("btnAdd")
        self.gridLayout.addWidget(self.btnAdd, 6, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(tutoringMainUI)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.btnRecord = QtWidgets.QPushButton(tutoringMainUI)
        self.btnRecord.setMinimumSize(QtCore.QSize(0, 60))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Resources/records.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnRecord.setIcon(icon3)
        self.btnRecord.setIconSize(QtCore.QSize(20, 20))
        self.btnRecord.setObjectName("btnRecord")
        self.gridLayout.addWidget(self.btnRecord, 7, 0, 1, 1)

        self.btnSetting = QtWidgets.QPushButton(tutoringMainUI)
        self.btnSetting.setMinimumSize(QtCore.QSize(0, 60))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Resources/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSetting.setIcon(icon3)
        self.btnSetting.setIconSize(QtCore.QSize(20, 20))
        self.btnSetting.setObjectName("btnSetting")
        self.gridLayout.addWidget(self.btnSetting, 8, 0, 1, 1)
        self.retranslateUi(tutoringMainUI)
        QtCore.QMetaObject.connectSlotsByName(tutoringMainUI)

        #Call Functions
        uiHandling(self)
        self.btnAdd.clicked.connect(lambda: toAddStudent(self,tutoringMainUI))
        self.btnStatement.clicked.connect(lambda: toStatement(self,tutoringMainUI))
        self.btnSetting.clicked.connect(lambda: toSettings(self, tutoringMainUI))
        self.btnSchedule.clicked.connect(lambda: toSchedule(self, tutoringMainUI))
        self.btnRecord.clicked.connect(lambda: toRecords(self, tutoringMainUI))

    def retranslateUi(self, tutoringMainUI):
        _translate = QtCore.QCoreApplication.translate
        tutoringMainUI.setWindowTitle(_translate("tutoringMainUI", "Roster Guru"))
        self.btnStatement.setText(_translate("tutoringMainUI", " STATEMENT"))
        self.btnSchedule.setText(_translate("tutoringMainUI", " SHEDULE"))
        self.label.setText(_translate("tutoringMainUI", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\"><html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">p, li { white-space: pre-wrap; }</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\"><p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt; color:#0e3262;\">ROSTER GURU</span></p></body></html>"))
        self.btnAdd.setText(_translate("tutoringMainUI", " ADD STUDENT"))
        self.label_2.setText(_translate("tutoringMainUI", "<html><head/><body><p align=\"center\"><span style=\" color:#0e3262;\">TUTORING TIME KEEPING SERVICE</span></p></body></html>"))
        self.btnRecord.setText(_translate("tutoringMainUI", " RECORDS"))
        self.btnSetting.setText(_translate("tutoringMainUI", " SETTINGS"))

from students import Ui_studentsUI
from statement import Ui_statementUI
from settings import Ui_SettingsUI
from schedule import Ui_scheduleUI
from records import Ui_Records

def uiHandling(self):
    settingsFile = open("Files/settings.txt","r")
    settingLine = settingsFile.readlines()
    settingsFile.close()

    if settingLine[0] == "default\n":
        self.btnRecord.setDisabled(True)
        self.btnSchedule.setDisabled(True)
        self.btnAdd.setDisabled(True)
        self.btnStatement.setDisabled(True)

    clientFile = open("Files/clients.txt","r")
    clientLine = clientFile.readlines()
    clientFile.close()

    if len(clientLine) == 0:
        self.btnRecord.setDisabled(True)
        self.btnSchedule.setDisabled(True)
        self.btnStatement.setDisabled(True)

def toAddStudent(self,tutoringMainUI):
    self.window = QtWidgets.QWidget()
    self.ui = Ui_studentsUI()
    self.ui.setupUi(self.window)
    self.window.show()
    tutoringMainUI.hide()
    # print("button clicked") #Debug event

def toRecords(self,tutoringMainUI):
    self.window = QtWidgets.QWidget()
    self.ui = Ui_Records()
    self.ui.setupUi(self.window)
    self.window.show()
    tutoringMainUI.hide()
    # print("button clicked") #Debug event

def toStatement(self,tutoringMainUI):
    self.window = QtWidgets.QWidget()
    self.ui = Ui_statementUI()
    self.ui.setupUi(self.window)
    self.window.show()
    tutoringMainUI.hide()
    # print("button clicked") #Debug event

def toSettings(self,tutoringMainUI):
    self.window = QtWidgets.QWidget()
    self.ui = Ui_SettingsUI()
    self.ui.setupUi(self.window)
    self.window.show()
    tutoringMainUI.hide()
    # print("button clicked") #Debug event

def toSchedule(self,tutoringMainUI):
    self.window = QtWidgets.QWidget()
    self.ui = Ui_scheduleUI()
    self.ui.setupUi(self.window)
    self.window.show()
    tutoringMainUI.hide()
    # print("button clicked") #Debug event

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    tutoringMainUI = QtWidgets.QWidget()
    ui = Ui_tutoringMainUI()
    ui.setupUi(tutoringMainUI)
    tutoringMainUI.show()
    sys.exit(app.exec_())
