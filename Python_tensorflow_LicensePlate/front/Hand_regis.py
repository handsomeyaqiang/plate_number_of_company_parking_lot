# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Hand_regis.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Hand(object):
    def setupUi(self, Hand):
        Hand.setObjectName("Hand")
        Hand.resize(400, 300)
        self.label = QtWidgets.QLabel(Hand)
        self.label.setGeometry(QtCore.QRect(60, 10, 291, 31))
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Hand)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(80, 140, 251, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(Hand)
        self.pushButton.setGeometry(QtCore.QRect(160, 190, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Hand)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 190, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Hand)
        QtCore.QMetaObject.connectSlotsByName(Hand)

    def retranslateUi(self, Hand):
        _translate = QtCore.QCoreApplication.translate
        Hand.setWindowTitle(_translate("Hand", "Form"))
        self.label.setText(_translate("Hand", "           车辆入场登记"))
        self.label_2.setText(_translate("Hand", " 车牌号："))
        self.pushButton.setText(_translate("Hand", "确 定"))
        self.pushButton_2.setText(_translate("Hand", "取 消"))

