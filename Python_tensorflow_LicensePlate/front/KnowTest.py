# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'KnowTest.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_know(object):
    def setupUi(self, know):
        know.setObjectName("know")
        know.resize(689, 453)
        self.groupBox = QtWidgets.QGroupBox(know)
        self.groupBox.setGeometry(QtCore.QRect(440, 70, 211, 161))
        self.groupBox.setObjectName("groupBox")
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(70, 10, 77, 141))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 3, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 2, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 4, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 5, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(know)
        self.groupBox_2.setGeometry(QtCore.QRect(50, 60, 261, 201))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(10, 20, 241, 171))
        self.label.setText("")
        self.label.setObjectName("label")
        self.dial = QtWidgets.QDial(know)
        self.dial.setGeometry(QtCore.QRect(350, 200, 50, 64))
        self.dial.setObjectName("dial")
        self.label_2 = QtWidgets.QLabel(know)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 171, 21))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(know)
        self.label_3.setGeometry(QtCore.QRect(310, 270, 141, 20))
        self.label_3.setObjectName("label_3")
        self.textBrowser = QtWidgets.QTextBrowser(know)
        self.textBrowser.setGeometry(QtCore.QRect(250, 300, 256, 61))
        self.textBrowser.setObjectName("textBrowser")
        self.tableWidget = QtWidgets.QTableWidget(know)
        self.tableWidget.setGeometry(QtCore.QRect(130, 360, 511, 91))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)

        self.retranslateUi(know)
        QtCore.QMetaObject.connectSlotsByName(know)

    def retranslateUi(self, know):
        _translate = QtCore.QCoreApplication.translate
        know.setWindowTitle(_translate("know", "Form"))
        self.groupBox.setTitle(_translate("know", "功能列表"))
        self.pushButton_3.setText(_translate("know", "手动登记"))
        self.pushButton.setText(_translate("know", "图片识别"))
        self.pushButton_2.setText(_translate("know", "视频识别"))
        self.pushButton_4.setText(_translate("know", "关闭视频"))
        self.pushButton_5.setText(_translate("know", "放行"))
        self.groupBox_2.setTitle(_translate("know", "识别区域"))
        self.label_3.setText(_translate("know", "       识别结果"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("know", "车牌号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("know", "进入时间"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("know", "停车时长"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("know", "车辆类型"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("know", "应缴费用(元)"))

