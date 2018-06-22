# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dayFee.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dayFee(object):
    def setupUi(self, dayFee):
        dayFee.setObjectName("dayFee")
        dayFee.resize(400, 300)
        self.gridLayoutWidget = QtWidgets.QWidget(dayFee)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(80, 70, 251, 121))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 3, 1, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 2, 1, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 4, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 4, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 5, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(dayFee)
        self.pushButton.setGeometry(QtCore.QRect(100, 220, 101, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(dayFee)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 220, 101, 31))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(dayFee)
        QtCore.QMetaObject.connectSlotsByName(dayFee)

    def retranslateUi(self, dayFee):
        _translate = QtCore.QCoreApplication.translate
        dayFee.setWindowTitle(_translate("dayFee", "Form"))
        self.label_6.setText(_translate("dayFee", "   开始时间："))
        self.label_2.setText(_translate("dayFee", "   结束时间："))
        self.label.setText(_translate("dayFee", "  价格/小时："))
        self.label_3.setText(_translate("dayFee", " 首小时价格："))
        self.pushButton.setText(_translate("dayFee", "确 定"))
        self.pushButton_2.setText(_translate("dayFee", "取 消"))

