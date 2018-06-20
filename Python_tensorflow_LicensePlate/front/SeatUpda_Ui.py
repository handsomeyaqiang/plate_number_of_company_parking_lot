# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SeatUpda_Ui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_seatUp(object):
    def setupUi(self, seatUp):
        seatUp.setObjectName("seatUp")
        seatUp.resize(396, 300)
        self.gridLayoutWidget = QtWidgets.QWidget(seatUp)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(90, 60, 211, 121))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 1, 2, 1, 1)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(seatUp)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(150, 190, 158, 25))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.retranslateUi(seatUp)
        QtCore.QMetaObject.connectSlotsByName(seatUp)

    def retranslateUi(self, seatUp):
        _translate = QtCore.QCoreApplication.translate
        seatUp.setWindowTitle(_translate("seatUp", "Form"))
        self.label.setText(_translate("seatUp", "车位类型："))
        self.label_6.setText(_translate("seatUp", "  车位号："))
        self.comboBox.setItemText(0, _translate("seatUp", "临时车位"))
        self.comboBox.setItemText(1, _translate("seatUp", "员工车位"))
        self.pushButton.setText(_translate("seatUp", "确定"))
        self.pushButton_2.setText(_translate("seatUp", "取消"))

