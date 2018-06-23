# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginUI.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(581, 533)
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(160, 330, 295, 141))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.loginButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.loginButton.setObjectName("loginButton")
        self.horizontalLayout_2.addWidget(self.loginButton)
        self.registerButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.registerButton.setObjectName("registerButton")
        self.horizontalLayout_2.addWidget(self.registerButton)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.gridLayout.addLayout(self.horizontalLayout_2, 4, 1, 1, 1)
        self.userlineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.userlineEdit.setObjectName("userlineEdit")
        self.gridLayout.addWidget(self.userlineEdit, 0, 1, 1, 1)
        self.userLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.userLabel.setObjectName("userLabel")
        self.gridLayout.addWidget(self.userLabel, 0, 0, 1, 1)
        self.labelTip = QtWidgets.QLabel(self.gridLayoutWidget)
        self.labelTip.setObjectName("labelTip")
        self.gridLayout.addWidget(self.labelTip, 3, 1, 1, 1)
        self.pwdlineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.pwdlineEdit.setObjectName("pwdlineEdit")
        self.gridLayout.addWidget(self.pwdlineEdit, 1, 1, 1, 1)
        self.pwdlabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.pwdlabel.setObjectName("pwdlabel")
        self.gridLayout.addWidget(self.pwdlabel, 1, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(-10, 0, 601, 321))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.loginButton.setText(_translate("Form", "登 陆"))
        self.registerButton.setText(_translate("Form", "注 册"))
        self.pushButton.setText(_translate("Form", "找回密码"))
        self.userLabel.setText(_translate("Form", "  账  户"))
        self.labelTip.setText(_translate("Form", "密码或用户名错误"))
        self.pwdlabel.setText(_translate("Form", "  密  码"))
        self.comboBox.setItemText(0, _translate("Form", "财务管理员"))
        self.comboBox.setItemText(1, _translate("Form", "信息管理员"))
        self.comboBox.setItemText(2, _translate("Form", "停车场管理员"))
        self.label.setText(_translate("Form", "  请选择"))

