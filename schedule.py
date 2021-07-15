from PyQt5 import QtCore, QtGui, QtWidgets
import os

class Ui_scheduleUI(object):
    def setupUi(self, scheduleUI):
        # UI Setup
        scheduleUI.setObjectName("scheduleUI")
        scheduleUI.resize(717, 724)
        self.gridLayout = QtWidgets.QGridLayout(scheduleUI)
        self.gridLayout.setObjectName("gridLayout")
        self.listStudents = QtWidgets.QComboBox(scheduleUI)
        self.listStudents.setMaximumSize(QtCore.QSize(196, 25))
        self.listStudents.setObjectName("listStudents")
        self.gridLayout.addWidget(self.listStudents, 1, 1, 1, 3)
        self.lblDate = QtWidgets.QLabel(scheduleUI)
        self.lblDate.setObjectName("lblDate")
        self.gridLayout.addWidget(self.lblDate, 11, 2, 1, 7)
        self.label_5 = QtWidgets.QLabel(scheduleUI)
        self.label_5.setMinimumSize(QtCore.QSize(141, 30))
        self.label_5.setMaximumSize(QtCore.QSize(141, 30))
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 11, 0, 1, 2)
        self.label_13 = QtWidgets.QLabel(scheduleUI)
        self.label_13.setMinimumSize(QtCore.QSize(141, 40))
        self.label_13.setMaximumSize(QtCore.QSize(141, 40))
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 5, 0, 1, 2)
        self.btnBack = QtWidgets.QPushButton(scheduleUI)
        self.btnBack.setMinimumSize(QtCore.QSize(0, 30))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Resources/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBack.setIcon(icon)
        self.btnBack.setObjectName("btnBack")
        self.gridLayout.addWidget(self.btnBack, 12, 9, 1, 1)
        self.lblHours = QtWidgets.QLabel(scheduleUI)
        self.lblHours.setObjectName("lblHours")
        self.gridLayout.addWidget(self.lblHours, 12, 2, 1, 7)

        self.lcdTimeFrom = QtWidgets.QLCDNumber(scheduleUI)
        self.lcdTimeFrom.setMinimumSize(QtCore.QSize(100, 40))
        self.lcdTimeFrom.setMaximumSize(QtCore.QSize(100, 40))
        self.lcdTimeFrom.setInputMethodHints(QtCore.Qt.ImhTime)
        self.lcdTimeFrom.setFrameShape(QtWidgets.QFrame.Panel)
        self.lcdTimeFrom.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lcdTimeFrom.setSmallDecimalPoint(False)
        self.lcdTimeFrom.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdTimeFrom.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdTimeFrom.setObjectName("lcdTimeFrom")
        self.gridLayout.addWidget(self.lcdTimeFrom, 5, 6, 1, 1)

        self.label_12 = QtWidgets.QLabel(scheduleUI)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 6, 0, 1, 10)
        self.label = QtWidgets.QLabel(scheduleUI)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.btnUpdate = QtWidgets.QPushButton(scheduleUI)
        self.btnUpdate.setMinimumSize(QtCore.QSize(0, 30))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Resources/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnUpdate.setIcon(icon1)
        self.btnUpdate.setObjectName("btnUpdate")
        self.gridLayout.addWidget(self.btnUpdate, 11, 9, 1, 1)
        self.label_14 = QtWidgets.QLabel(scheduleUI)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 5, 7, 1, 1)

        self.lcdTimeTo = QtWidgets.QLCDNumber(scheduleUI)
        self.lcdTimeTo.setMinimumSize(QtCore.QSize(100, 40))
        self.lcdTimeTo.setMaximumSize(QtCore.QSize(100, 40))
        self.lcdTimeTo.setInputMethodHints(QtCore.Qt.ImhTime)
        self.lcdTimeTo.setFrameShape(QtWidgets.QFrame.Panel)
        self.lcdTimeTo.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lcdTimeTo.setSmallDecimalPoint(False)
        self.lcdTimeTo.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdTimeTo.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdTimeTo.setObjectName("lcdTimeTo")
        self.gridLayout.addWidget(self.lcdTimeTo, 5, 8, 1, 2)

        self.label_6 = QtWidgets.QLabel(scheduleUI)
        self.label_6.setMinimumSize(QtCore.QSize(141, 30))
        self.label_6.setMaximumSize(QtCore.QSize(141, 30))
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 12, 0, 1, 2)
        self.label_3 = QtWidgets.QLabel(scheduleUI)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 5, 5, 1, 1)
        self.label_2 = QtWidgets.QLabel(scheduleUI)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 10)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 4, 1, 6)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(scheduleUI)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.label_10 = QtWidgets.QLabel(scheduleUI)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_2.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(scheduleUI)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_2.addWidget(self.label_11)
        self.gridLayout.addLayout(self.horizontalLayout_2, 7, 0, 1, 10)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 5, 3, 1, 1)
        self.spinDuration = QtWidgets.QDoubleSpinBox(scheduleUI)
        self.spinDuration.setDecimals(1)
        self.spinDuration.setMinimum(0.5)
        self.spinDuration.setMaximum(24.0)
        self.spinDuration.setSingleStep(0.5)
        self.spinDuration.setProperty("value", 1.0)
        self.spinDuration.setObjectName("spinDuration")
        self.gridLayout.addWidget(self.spinDuration, 5, 2, 1, 1)
        self.sliderTime = QtWidgets.QScrollBar(scheduleUI)
        self.sliderTime.setMinimumSize(QtCore.QSize(0, 40))
        self.sliderTime.setMaximumSize(QtCore.QSize(16777215, 40))
        self.sliderTime.setInputMethodHints(QtCore.Qt.ImhTime)
        self.sliderTime.setMaximum(48)
        self.sliderTime.setPageStep(1)
        self.sliderTime.setOrientation(QtCore.Qt.Horizontal)
        self.sliderTime.setObjectName("sliderTime")
        self.gridLayout.addWidget(self.sliderTime, 8, 0, 1, 10)
        self.label_7 = QtWidgets.QLabel(scheduleUI)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 9, 0, 1, 1)
        self.calendar = QtWidgets.QCalendarWidget(scheduleUI)
        self.calendar.setObjectName("calendar")
        self.gridLayout.addWidget(self.calendar, 2, 0, 1, 10)
        self.notes = QtWidgets.QTextEdit(scheduleUI)
        self.notes.setMaximumSize(QtCore.QSize(16777215, 50))
        self.notes.setObjectName("notes")
        self.gridLayout.addWidget(self.notes, 10, 0, 1, 10)
        self.retranslateUi(scheduleUI)
        QtCore.QMetaObject.connectSlotsByName(scheduleUI)

        # Call Functions
        self.btnBack.clicked.connect(lambda: toMenu(self, scheduleUI))
        self.sliderTime.valueChanged.connect(self.updateLCD)
        self.listStudents.currentIndexChanged.connect(lambda: loadLable(self))
        self.calendar.selectionChanged.connect(lambda: loadLable(self))
        self.spinDuration.valueChanged.connect(self.lcdRefresh)
        self.btnUpdate.clicked.connect(lambda: updateInfo(self))
        updateList(self)

    def retranslateUi(self, scheduleUI):
        _translate = QtCore.QCoreApplication.translate
        scheduleUI.setWindowTitle(_translate("scheduleUI", "Schedule"))
        self.lblDate.setText(_translate("scheduleUI", "No record found"))
        self.label_5.setText(_translate("scheduleUI", "Date:"))
        self.label_13.setText(_translate("scheduleUI", "Set Slot Duration"))
        self.btnBack.setText(_translate("scheduleUI", " Back"))
        self.lblHours.setText(_translate("scheduleUI", "No record found"))
        self.label_12.setText(_translate("scheduleUI", "Set Time:"))
        self.label.setText(_translate("scheduleUI", "Student:"))
        self.btnUpdate.setText(_translate("scheduleUI", " Update"))
        self.label_14.setText(_translate("scheduleUI", "To:"))
        self.label_6.setText(_translate("scheduleUI", "Total Hours:"))
        self.label_3.setText(_translate("scheduleUI", "From:"))
        self.label_2.setText(_translate("scheduleUI", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; color:#0f3362;\">SCHEDULE</span></p></body></html>"))
        self.label_4.setText(_translate("scheduleUI", "00:00"))
        self.label_10.setText(_translate("scheduleUI", "<html><head/><body><p align=\"center\">12:00</p></body></html>"))
        self.label_11.setText(_translate("scheduleUI", "<html><head/><body><p align=\"right\">24:00</p></body></html>"))
        self.label_7.setText(_translate("scheduleUI", "Notes:"))

    def updateLCD(self,time):
        time = time*50
        strTime = str(time)
        if len(strTime) < 3:
            strTime = ("00" + strTime)
            hoursTo = strTime[:2]
            minutesTo = strTime[-2:]
            if minutesTo == "50":
                minutesTo = "30"
        elif len(strTime) < 4:
            strTime = ("0"+strTime)
            hoursTo = strTime[:2]
            minutesTo = strTime[-2:]
            if minutesTo == "50":
                minutesTo = "30"
        else:
            hoursTo = strTime[:2]
            minutesTo = strTime[-2:]
            if minutesTo == "50":
                minutesTo = "30"

        self.lcdTimeTo.display("{0}:{1}".format(hoursTo, minutesTo))
        setTo = ("{0}:{1}".format(hoursTo, minutesTo))

        hoursTo = int(hoursTo)*60
        minutesTo = int(minutesTo)

        totalTo = hoursTo + minutesTo
        duration = int(self.spinDuration.value() * 60)
        timeFrom = totalTo - duration
        timeFrom = (timeFrom/60)*100
        timeFrom = int(timeFrom)
        timeFrom = str(timeFrom)

        if len(timeFrom)<3:
            timeFrom = ("00" + timeFrom)
            hoursFrom = timeFrom[:2]
            minutesFrom = timeFrom[-2:]
            if minutesFrom == "50":
                minutesFrom = "30"
        elif len(timeFrom)<4:
            timeFrom = ("0" + timeFrom)
            hoursFrom = timeFrom[:2]
            minutesFrom = timeFrom[-2:]
            if minutesFrom == "50":
                minutesFrom = "30"
        else:
            hoursFrom = timeFrom[:2]
            minutesFrom = timeFrom[-2:]
            if minutesFrom == "50":
                minutesFrom = "30"

        self.lcdTimeFrom.display("{0}:{1}".format(hoursFrom, minutesFrom))

        setFrom = ("{0}:{1}".format(hoursFrom, minutesFrom))

        global setTimeFrom
        setTimeFrom = setFrom
        global setTimeTo
        setTimeTo = setTo

    def store(self):
        return ("{0} - {1}".format(setTimeFrom, setTimeTo))

    def lcdRefresh(self):
        curTime = self.sliderTime.value()
        self.updateLCD(curTime)

from tutoringMain import Ui_tutoringMainUI

def toMenu(self,scheduleUI):
    self.window = QtWidgets.QWidget()
    self.ui = Ui_tutoringMainUI()
    self.ui.setupUi(self.window)
    self.window.show()
    scheduleUI.hide()
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

        self.listStudents.addItem(student[0])
        self.listStudents.setItemText(counter, student[0])
        counter += 1

def updateInfo(self):
    student = self.listStudents.currentText()
    date = self.calendar.selectedDate().toString()
    hours = self.spinDuration.value()
    times = self.store()
    note = self.notes.toPlainText()
    checkFile(student)

    studentFile = open("Students/{0}.txt".format(student), "r+")
    lines = studentFile.readlines()
    studentFile.close()
    open("Students/{0}.txt".format(student), 'w').close()
    studentFile = open("Students/{0}.txt".format(student), "w+")

    if any(date in string for string in lines) == True:
        index = [lines.index(i) for i in lines if date in i]
        lines[index[0]] = ("{0},{1},{2},{3}\n".format(date,hours,times,note))
    else:
        lines.append("{0},{1},{2},{3}\n".format(date,hours,times,note))

    studentFile.writelines(lines)
    studentFile.close()
    loadLable(self)

def checkFile(student):
    if not os.path.exists("Students/{0}.txt".format(student)):
        open("Students/{0}.txt".format(student), "w+")
    return

def loadLable(self):
    student = self.listStudents.currentText()
    checkFile(student)
    date = self.calendar.selectedDate().toString()
    studentFile = open("Students/{0}.txt".format(student), "r+")
    lines = studentFile.readlines()

    if any(date in string for string in lines) == True:
        index = [lines.index(i) for i in lines if date in i]
        display = lines[index[0]]
        day = display.split(",")
        date = day[0]
        hours = day[1]
        self.lblDate.setText(date)
        self.lblHours.setText(hours)
    else:
        self.lblDate.setText("No record found")
        self.lblHours.setText("No record found")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    scheduleUI = QtWidgets.QWidget()
    ui = Ui_scheduleUI()
    ui.setupUi(scheduleUI)
    scheduleUI.show()
    sys.exit(app.exec_())
