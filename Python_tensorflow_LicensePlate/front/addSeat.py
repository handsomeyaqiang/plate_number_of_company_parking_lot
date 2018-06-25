# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addSeat.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_addSeat(object):
    def setupUi(self, addSeat):
        addSeat.setObjectName("addSeat")
        addSeat.resize(400, 300)
        self.gridLayoutWidget = QtWidgets.QWidget(addSeat)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(80, 70, 211, 71))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 2, 1, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 1, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(addSeat)
        self.pushButton.setGeometry(QtCore.QRect(170, 170, 101, 31))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(addSeat)
        QtCore.QMetaObject.connectSlotsByName(addSeat)

    def retranslateUi(self, addSeat):
        _translate = QtCore.QCoreApplication.translate
        addSeat.setWindowTitle(_translate("addSeat", "Form"))
        self.label_6.setText(_translate("addSeat", " 车位类型："))
        self.label_2.setText(_translate("addSeat", "   车位数："))
        self.comboBox.setItemText(0, _translate("addSeat", "员工车位"))
        self.comboBox.setItemText(1, _translate("addSeat", "临时车位"))
        self.pushButton.setText(_translate("addSeat", "确定"))

