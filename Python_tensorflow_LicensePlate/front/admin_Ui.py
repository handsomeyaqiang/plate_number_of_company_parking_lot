# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin_Ui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_adin(object):
    def setupUi(self, adin):
        adin.setObjectName("adin")
        adin.resize(868, 535)
        self.pushButton = QtWidgets.QPushButton(adin)
        self.pushButton.setGeometry(QtCore.QRect(40, 100, 111, 31))
        self.pushButton.setObjectName("pushButton")
        self.groupBox = QtWidgets.QGroupBox(adin)
        self.groupBox.setGeometry(QtCore.QRect(40, 140, 781, 381))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox)
        self.tableWidget.setGeometry(QtCore.QRect(30, 30, 721, 301))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.line = QtWidgets.QFrame(adin)
        self.line.setGeometry(QtCore.QRect(80, 50, 651, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(adin)
        self.label.setGeometry(QtCore.QRect(220, 30, 311, 16))
        self.label.setObjectName("label")

        self.retranslateUi(adin)
        QtCore.QMetaObject.connectSlotsByName(adin)

    def retranslateUi(self, adin):
        _translate = QtCore.QCoreApplication.translate
        adin.setWindowTitle(_translate("adin", "Form"))
        self.pushButton.setText(_translate("adin", "查看所有用户信息"))
        self.label.setText(_translate("adin", "            管理员界面"))

