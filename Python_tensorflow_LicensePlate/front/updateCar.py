# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'updateCar.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(90, 40, 211, 150))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.car_lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.car_lineEdit.setObjectName("car_lineEdit")
        self.gridLayout.addWidget(self.car_lineEdit, 2, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.Chejia_lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.Chejia_lineEdit.setObjectName("Chejia_lineEdit")
        self.gridLayout.addWidget(self.Chejia_lineEdit, 4, 2, 1, 1)
        self.num_lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.num_lineEdit.setObjectName("num_lineEdit")
        self.gridLayout.addWidget(self.num_lineEdit, 0, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.name_lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.name_lineEdit.setObjectName("name_lineEdit")
        self.gridLayout.addWidget(self.name_lineEdit, 1, 2, 1, 1)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(140, 220, 160, 25))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.clear_pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.clear_pushButton.setObjectName("clear_pushButton")
        self.horizontalLayout_2.addWidget(self.clear_pushButton)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "车牌号："))
        self.label_3.setText(_translate("Form", "车架号："))
        self.label_6.setText(_translate("Form", " 工 号："))
        self.label_2.setText(_translate("Form", " 姓 名："))
        self.pushButton.setText(_translate("Form", "确定"))
        self.clear_pushButton.setText(_translate("Form", "取消"))

