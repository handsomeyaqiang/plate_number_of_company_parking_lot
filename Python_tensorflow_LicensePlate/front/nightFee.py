# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nightFee.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_nightFee(object):
    def setupUi(self, nightFee):
        nightFee.setObjectName("nightFee")
        nightFee.resize(400, 300)
        self.gridLayoutWidget = QtWidgets.QWidget(nightFee)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(80, 70, 251, 121))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 4, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 4, 0, 1, 1)
        self.timeEditend = QtWidgets.QTimeEdit(self.gridLayoutWidget)
        self.timeEditend.setObjectName("timeEditend")
        self.gridLayout.addWidget(self.timeEditend, 3, 1, 1, 1)
        self.timeEditstart = QtWidgets.QTimeEdit(self.gridLayoutWidget)
        self.timeEditstart.setObjectName("timeEditstart")
        self.gridLayout.addWidget(self.timeEditstart, 2, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(nightFee)
        self.pushButton.setGeometry(QtCore.QRect(120, 220, 101, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(nightFee)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 220, 101, 31))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(nightFee)
        QtCore.QMetaObject.connectSlotsByName(nightFee)

    def retranslateUi(self, nightFee):
        _translate = QtCore.QCoreApplication.translate
        nightFee.setWindowTitle(_translate("nightFee", "Form"))
        self.label_2.setText(_translate("nightFee", "   结束时间："))
        self.label_6.setText(_translate("nightFee", "   开始时间："))
        self.label.setText(_translate("nightFee", "    价格/次："))
        self.pushButton.setText(_translate("nightFee", "确 定"))
        self.pushButton_2.setText(_translate("nightFee", "取 消"))

