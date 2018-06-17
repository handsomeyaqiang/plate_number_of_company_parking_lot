# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ComInfoManage.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ConInfo(object):
    def setupUi(self, ConInfo):
        ConInfo.setObjectName("ConInfo")
        ConInfo.resize(687, 440)
        ConInfo.setMinimumSize(QtCore.QSize(0, 423))
        ConInfo.setMaximumSize(QtCore.QSize(687, 16777215))
        self.line = QtWidgets.QFrame(ConInfo)
        self.line.setGeometry(QtCore.QRect(20, 40, 631, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(ConInfo)
        self.label.setGeometry(QtCore.QRect(60, 10, 571, 20))
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(ConInfo)
        self.groupBox.setGeometry(QtCore.QRect(220, 90, 241, 301))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 80, 174, 137))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.staff_Button = QtWidgets.QCommandLinkButton(self.verticalLayoutWidget)
        self.staff_Button.setObjectName("staff_Button")
        self.verticalLayout.addWidget(self.staff_Button)
        self.car_Button = QtWidgets.QCommandLinkButton(self.verticalLayoutWidget)
        self.car_Button.setObjectName("car_Button")
        self.verticalLayout.addWidget(self.car_Button)
        self.record_Button = QtWidgets.QCommandLinkButton(self.verticalLayoutWidget)
        self.record_Button.setObjectName("record_Button")
        self.verticalLayout.addWidget(self.record_Button)
        self.openGLWidget = QtWidgets.QOpenGLWidget(ConInfo)
        self.openGLWidget.setGeometry(QtCore.QRect(-400, 580, 300, 200))
        self.openGLWidget.setObjectName("openGLWidget")
        self.line.raise_()
        self.label.raise_()
        self.groupBox.raise_()
        self.record_Button.raise_()
        self.openGLWidget.raise_()

        self.retranslateUi(ConInfo)
        QtCore.QMetaObject.connectSlotsByName(ConInfo)

    def retranslateUi(self, ConInfo):
        _translate = QtCore.QCoreApplication.translate
        ConInfo.setWindowTitle(_translate("ConInfo", "Form"))
        self.label.setText(_translate("ConInfo", "                        公司员工车辆信息管理"))
        self.groupBox.setTitle(_translate("ConInfo", "操作"))
        self.staff_Button.setText(_translate("ConInfo", "职工信息管理"))
        self.car_Button.setText(_translate("ConInfo", "车辆信息管理"))
        self.record_Button.setText(_translate("ConInfo", "车辆记录查询"))

