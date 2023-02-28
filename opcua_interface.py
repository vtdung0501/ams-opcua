# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OPCUA1.ui'
#
# Created by: PyQt5 UI code generator 5.15.8
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from pyqtgraph import PlotWidget
from PyQt5 import QtCore, QtGui, QtWidgets

import resources_rc
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1315, 786)
        MainWindow.setWindowIcon(QtGui.QIcon('_Icon/smc_icon.ico'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(250, 0))
        self.frame.setMaximumSize(QtCore.QSize(250, 16777215))
        self.frame.setStyleSheet("background-color:rgb(120, 192, 255)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 130))
        self.frame_3.setStyleSheet("background-color:rgb(85, 170, 255)")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 1)
        self.le_url = QtWidgets.QLineEdit(self.frame_3)
        self.le_url.setMinimumSize(QtCore.QSize(100, 20))
        self.le_url.setMaximumSize(QtCore.QSize(16777215, 20))
        self.le_url.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.le_url.setObjectName("le_url")
        self.gridLayout_5.addWidget(self.le_url, 0, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_5.addWidget(self.label_2, 1, 0, 1, 1)
        self.le_username = QtWidgets.QLineEdit(self.frame_3)
        self.le_username.setMinimumSize(QtCore.QSize(0, 20))
        self.le_username.setMaximumSize(QtCore.QSize(50, 16777215))
        self.le_username.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.le_username.setObjectName("le_username")
        self.gridLayout_5.addWidget(self.le_username, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_5.addWidget(self.label_3, 2, 0, 1, 1)
        self.le_password = QtWidgets.QLineEdit(self.frame_3)
        self.le_password.setMinimumSize(QtCore.QSize(0, 20))
        self.le_password.setMaximumSize(QtCore.QSize(50, 16777215))
        self.le_password.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.le_password.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.le_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.le_password.setObjectName("le_password")
        self.gridLayout_5.addWidget(self.le_password, 2, 1, 1, 1)
        self.cb_remember = QtWidgets.QCheckBox(self.frame_3)
        self.cb_remember.setObjectName("cb_remember")
        self.gridLayout_5.addWidget(self.cb_remember, 2, 2, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout_5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_connect = QtWidgets.QPushButton(self.frame_3)
        self.btn_connect.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_connect.setFont(font)
        self.btn_connect.setStyleSheet("background-color:rgb(68, 170, 68);\n"
"")
        self.btn_connect.setObjectName("btn_connect")
        self.horizontalLayout_3.addWidget(self.btn_connect)
        self.btn_disconnect = QtWidgets.QPushButton(self.frame_3)
        self.btn_disconnect.setMinimumSize(QtCore.QSize(0, 25))
        self.btn_disconnect.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_disconnect.setFont(font)
        self.btn_disconnect.setStyleSheet("background-color:rgb(159, 0, 0);\n"
"color:rgb(255, 255, 255);")
        self.btn_disconnect.setObjectName("btn_disconnect")
        self.horizontalLayout_3.addWidget(self.btn_disconnect)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addWidget(self.frame_3)
        self.lb_status = QtWidgets.QLabel(self.frame)
        self.lb_status.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lb_status.setFont(font)
        self.lb_status.setStyleSheet("background-color:rgb(85, 170, 255)")
        self.lb_status.setText("")
        self.lb_status.setObjectName("lb_status")
        self.verticalLayout.addWidget(self.lb_status)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setStyleSheet("background-color:rgb(85, 170, 255)")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame_5.setStyleSheet("background-color:rgb(85, 170, 255)")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.frame_5)
        self.label_5.setMaximumSize(QtCore.QSize(180, 60))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("_Icon/smc-icon-1.ico"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.verticalLayout_2.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.frame_4)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.frame_6)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 300))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("_Icon/ams-icon.ico"))
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.label_22 = QtWidgets.QLabel(self.frame_6)
        self.label_22.setMinimumSize(QtCore.QSize(0, 0))
        self.label_22.setMaximumSize(QtCore.QSize(16777215, 200))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_4.addWidget(self.label_22)
        self.label_13 = QtWidgets.QLabel(self.frame_6)
        self.label_13.setMaximumSize(QtCore.QSize(16777215, 200))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setScaledContents(True)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_4.addWidget(self.label_13)
        self.verticalLayout_2.addWidget(self.frame_6)
        self.verticalLayout.addWidget(self.frame_4)
        self.horizontalLayout_6.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_7 = QtWidgets.QFrame(self.frame_2)
        self.frame_7.setStyleSheet("background-color:rgb(85, 170, 255)")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btn_operation = QtWidgets.QPushButton(self.frame_7)
        self.btn_operation.setMinimumSize(QtCore.QSize(120, 0))
        self.btn_operation.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_operation.setFont(font)
        self.btn_operation.setStyleSheet(" background-color:white;\n"
"color:blue;")
        self.btn_operation.setObjectName("btn_operation")
        self.horizontalLayout_4.addWidget(self.btn_operation)
        self.btn_standby = QtWidgets.QPushButton(self.frame_7)
        self.btn_standby.setMinimumSize(QtCore.QSize(120, 0))
        self.btn_standby.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_standby.setFont(font)
        self.btn_standby.setStyleSheet(" background-color:white;\n"
"color:blue;")
        self.btn_standby.setObjectName("btn_standby")
        self.horizontalLayout_4.addWidget(self.btn_standby)
        self.btn_Isolation = QtWidgets.QPushButton(self.frame_7)
        self.btn_Isolation.setMinimumSize(QtCore.QSize(120, 0))
        self.btn_Isolation.setMaximumSize(QtCore.QSize(70, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_Isolation.setFont(font)
        self.btn_Isolation.setStyleSheet(" background-color:white;\n"
"color:blue;")
        self.btn_Isolation.setObjectName("btn_Isolation")
        self.horizontalLayout_4.addWidget(self.btn_Isolation)
        self.btn_reset = QtWidgets.QLabel(self.frame_7)
        self.btn_reset.setMinimumSize(QtCore.QSize(120, 0))
        self.btn_reset.setMaximumSize(QtCore.QSize(120, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_reset.setFont(font)
        self.btn_reset.setObjectName("btn_reset")
        self.horizontalLayout_4.addWidget(self.btn_reset)
        self.verticalLayout_10.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_7 = QtWidgets.QLabel(self.frame_7)
        self.label_7.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_8.addWidget(self.label_7)
        self.lcd_pressure = QtWidgets.QLCDNumber(self.frame_7)
        self.lcd_pressure.setMinimumSize(QtCore.QSize(120, 25))
        self.lcd_pressure.setMaximumSize(QtCore.QSize(120, 25))
        self.lcd_pressure.setStyleSheet(" background-color:white;\n"
"color:red;")
        self.lcd_pressure.setObjectName("lcd_pressure")
        self.verticalLayout_8.addWidget(self.lcd_pressure)
        self.horizontalLayout_5.addLayout(self.verticalLayout_8)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_8 = QtWidgets.QLabel(self.frame_7)
        self.label_8.setMinimumSize(QtCore.QSize(0, 0))
        self.label_8.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_9.addWidget(self.label_8)
        self.lcd_instantflow = QtWidgets.QLCDNumber(self.frame_7)
        self.lcd_instantflow.setMinimumSize(QtCore.QSize(120, 25))
        self.lcd_instantflow.setMaximumSize(QtCore.QSize(120, 25))
        self.lcd_instantflow.setStyleSheet(" background-color:white;\n"
"color:red;")
        self.lcd_instantflow.setObjectName("lcd_instantflow")
        self.verticalLayout_9.addWidget(self.lcd_instantflow)
        self.horizontalLayout_5.addLayout(self.verticalLayout_9)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_6 = QtWidgets.QLabel(self.frame_7)
        self.label_6.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_7.addWidget(self.label_6)
        self.lcd_temp = QtWidgets.QLCDNumber(self.frame_7)
        self.lcd_temp.setMinimumSize(QtCore.QSize(120, 25))
        self.lcd_temp.setMaximumSize(QtCore.QSize(120, 25))
        self.lcd_temp.setStyleSheet(" background-color:white;\n"
"color:red;")
        self.lcd_temp.setObjectName("lcd_temp")
        self.verticalLayout_7.addWidget(self.lcd_temp)
        self.horizontalLayout_5.addLayout(self.verticalLayout_7)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_9 = QtWidgets.QLabel(self.frame_7)
        self.label_9.setMinimumSize(QtCore.QSize(120, 0))
        self.label_9.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_6.addWidget(self.label_9)
        self.lcd_accumflow = QtWidgets.QLCDNumber(self.frame_7)
        self.lcd_accumflow.setMinimumSize(QtCore.QSize(120, 25))
        self.lcd_accumflow.setMaximumSize(QtCore.QSize(120, 25))
        self.lcd_accumflow.setStyleSheet(" background-color:white;\n"
"color:red;")
        self.lcd_accumflow.setObjectName("lcd_accumflow")
        self.verticalLayout_6.addWidget(self.lcd_accumflow)
        self.horizontalLayout_5.addLayout(self.verticalLayout_6)
        self.verticalLayout_10.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_11.addLayout(self.verticalLayout_10)
        self.label_27 = QtWidgets.QLabel(self.frame_7)
        self.label_27.setMinimumSize(QtCore.QSize(20, 0))
        self.label_27.setMaximumSize(QtCore.QSize(10, 16777215))
        self.label_27.setText("")
        self.label_27.setObjectName("label_27")
        self.horizontalLayout_11.addWidget(self.label_27)
        self.label_28 = QtWidgets.QLabel(self.frame_7)
        self.label_28.setMinimumSize(QtCore.QSize(20, 0))
        self.label_28.setMaximumSize(QtCore.QSize(10, 16777215))
        self.label_28.setText("")
        self.label_28.setObjectName("label_28")
        self.horizontalLayout_11.addWidget(self.label_28)
        self.label_20 = QtWidgets.QLabel(self.frame_7)
        self.label_20.setMinimumSize(QtCore.QSize(35, 0))
        self.label_20.setMaximumSize(QtCore.QSize(10, 16777215))
        self.label_20.setText("")
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_11.addWidget(self.label_20)
        self.frame_8 = QtWidgets.QFrame(self.frame_7)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_11.addWidget(self.frame_8)
        self.verticalLayout_3.addWidget(self.frame_7)
        self.frame_9 = QtWidgets.QFrame(self.frame_2)
        self.frame_9.setStyleSheet("background-color:rgb(85, 170, 255)")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.frame_9)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setStyleSheet("background-color:rgb(85, 170, 255)")
        self.tab.setObjectName("tab")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.graphicsView_intansflow = PlotWidget(self.tab)
        self.graphicsView_intansflow.setObjectName("graphicsView_intansflow")
        self.graphicsView_intansflow.showGrid(x=True, y=True)
        self.graphicsView_intansflow.setTitle("Flow rate (L/min)", color = 'b')
        self.verticalLayout_11.addWidget(self.graphicsView_intansflow)
        self.graphicsView_pressure = PlotWidget(self.tab)
        self.graphicsView_pressure.setObjectName("graphicsView_pressure")
        self.graphicsView_pressure.showGrid(x=True, y=True)
        self.graphicsView_pressure.setTitle("Pressure (Kpa)", color = 'g')
        self.verticalLayout_11.addWidget(self.graphicsView_pressure)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("_Icon/pressure_icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tabWidget.addTab(self.tab, icon, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.graphicsView_temp = PlotWidget(self.tab_2)
        self.graphicsView_temp.setObjectName("graphicsView_temp")
        self.graphicsView_temp.showGrid(x=True, y=True)
        self.graphicsView_temp.setTitle("Temperature (°C)", color = "r")
        self.horizontalLayout_8.addWidget(self.graphicsView_temp)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/thermometer.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_2, icon1, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.tab_3)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.graphicsView_accumflow = PlotWidget(self.tab_3)
        self.graphicsView_accumflow.setObjectName("graphicsView_accumflow")
        self.graphicsView_accumflow.showGrid(x=True, y=True)
        self.graphicsView_accumflow.setTitle("Accumulation (L)", color ="blue")
        self.horizontalLayout_9.addWidget(self.graphicsView_accumflow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/git-merge.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_3, icon2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.tab_4)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.graphicsView_compare = PlotWidget(self.tab_4)
        self.graphicsView_compare.setStyleSheet("background-color:rgb(85, 170, 255)")
        self.graphicsView_compare.setObjectName("graphicsView_compare")
        self.graphicsView_compare.setObjectName("graphicsView_compare")
        self.graphicsView_compare.showGrid(x=True, y=True)
        self.horizontalLayout_10.addWidget(self.graphicsView_compare)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/bar-chart-2.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_4, icon3, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        self.verticalLayout_3.addWidget(self.frame_9)
        self.horizontalLayout_6.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AMS OPCUA Client"))
        self.label.setText(_translate("MainWindow", "URL Server:"))
        self.label_2.setText(_translate("MainWindow", "Username:"))
        self.label_3.setText(_translate("MainWindow", "Password:"))
        self.cb_remember.setText(_translate("MainWindow", "remember"))
        self.btn_connect.setText(_translate("MainWindow", "Connect"))
        self.btn_disconnect.setText(_translate("MainWindow", "Disconnect"))
        self.label_22.setText(_translate("MainWindow", "Air Management \n"
"System"))
        self.label_13.setText(_translate("MainWindow", "・Air consumption: \n"
"  Max. 62% reduction. \n"
"・Compatible with OPC UA. \n"
"・Compatible with wireless \n"
"  systems. \n"
"・IO-Link compatible."))
        self.btn_operation.setText(_translate("MainWindow", "Operation"))
        self.btn_standby.setText(_translate("MainWindow", "Standby"))
        self.btn_Isolation.setText(_translate("MainWindow", "Isolation"))
        self.btn_reset.setText(_translate("MainWindow", ""))
        self.label_7.setText(_translate("MainWindow", "Pressure( Kpa):"))
        self.label_8.setText(_translate("MainWindow", "Instant Flow (L/min):"))
        self.label_6.setText(_translate("MainWindow", "Temp (°C):"))
        self.lcd_temp.setToolTip(_translate("MainWindow", "<html><head/><body><pre style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'inherit\'; background-color:transparent;\">QLCDNumber{</span></pre><pre style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'inherit\'; background-color:transparent;\">    color: rgb(</span><span style=\" font-family:\'inherit\'; font-size:13px; color:#000000; background-color:transparent;\">255</span><span style=\" font-family:\'inherit\'; background-color:transparent;\">, </span><span style=\" font-family:\'inherit\'; font-size:13px; color:#000000; background-color:transparent;\">89</span><span style=\" font-family:\'inherit\'; background-color:transparent;\">, </span><span style=\" font-family:\'inherit\'; font-size:13px; color:#000000; background-color:transparent;\">242</span><span style=\" font-family:\'inherit\'; background-color:transparent;\">);    </span></pre><pre style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'inherit\'; background-color:transparent;\">    background-color: rgb(</span><span style=\" font-family:\'inherit\'; font-size:13px; color:#000000; background-color:transparent;\">0</span><span style=\" font-family:\'inherit\'; background-color:transparent;\">, </span><span style=\" font-family:\'inherit\'; font-size:13px; color:#000000; background-color:transparent;\">85</span><span style=\" font-family:\'inherit\'; background-color:transparent;\">, </span><span style=\" font-family:\'inherit\'; font-size:13px; color:#000000; background-color:transparent;\">0</span><span style=\" font-family:\'inherit\'; background-color:transparent;\">);</span></pre></body></html>"))
        self.label_9.setText(_translate("MainWindow", "Accum Flow (L):"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Pressure and flow rate"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Temperature"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Accumulation Flow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Comparison Chart"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())