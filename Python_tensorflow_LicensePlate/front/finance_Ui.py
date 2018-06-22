# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'finance_Ui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_finance(object):
    def setupUi(self, finance):
        finance.setObjectName("finance")
        finance.resize(843, 556)
        self.centralwidget = QtWidgets.QWidget(finance)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(100, 110, 641, 411))
        self.graphicsView.setObjectName("graphicsView")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(30, 70, 751, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(260, 20, 351, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 161, 21))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        finance.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(finance)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 843, 23))
        self.menubar.setObjectName("menubar")
        finance.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(finance)
        self.statusbar.setObjectName("statusbar")
        finance.setStatusBar(self.statusbar)

        self.retranslateUi(finance)
        QtCore.QMetaObject.connectSlotsByName(finance)

    def retranslateUi(self, finance):
        _translate = QtCore.QCoreApplication.translate
        finance.setWindowTitle(_translate("finance", "MainWindow"))
        self.label.setText(_translate("finance", "   请输入："))
        self.comboBox.setItemText(0, _translate("finance", "按年"))
        self.comboBox.setItemText(1, _translate("finance", "按月"))
        self.comboBox.setItemText(2, _translate("finance", "按日"))
        self.pushButton.setText(_translate("finance", "查看财务"))

