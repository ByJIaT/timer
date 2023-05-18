from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QIcon


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(345, 136)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(0, 10, 231, 101))
        self.lcdNumber.setDigitCount(8)
        self.lcdNumber.setObjectName("lcdNumber")
        self.lcdNumber.display("00:00:00")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(240, 10, 101, 101))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.timeEdit = QtWidgets.QTimeEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.timeEdit.setFont(font)
        self.timeEdit.setTime(QtCore.QTime(0, 0, 0))
        self.timeEdit.setObjectName("timeEdit")
        self.verticalLayout.addWidget(self.timeEdit)

        self.start_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.start_button.setObjectName("start_button")
        self.verticalLayout.addWidget(self.start_button)

        self.stop_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.stop_button.setObjectName("stop_button")
        self.verticalLayout.addWidget(self.stop_button)

        self.reset_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.reset_button.setObjectName("reset_button")
        self.verticalLayout.addWidget(self.reset_button)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 347, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Timer"))
        MainWindow.setWindowIcon(QIcon("media/logo.ico"))
        self.timeEdit.setDisplayFormat(_translate("MainWindow", "H:mm:ss"))
        self.start_button.setText(_translate("MainWindow", "Start"))
        self.stop_button.setText(_translate("MainWindow", "Stop"))
        self.reset_button.setText(_translate("MainWindow", "Reset"))
