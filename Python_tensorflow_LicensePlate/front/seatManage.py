# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'seatManage.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_seat(object):
    def setupUi(self, seat):
        seat.setObjectName("seat")
        seat.resize(777, 536)
        self.line = QtWidgets.QFrame(seat)
        self.line.setGeometry(QtCore.QRect(40, 20, 751, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(seat)
        self.line_2.setGeometry(QtCore.QRect(180, 40, 20, 491))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.groupBox = QtWidgets.QGroupBox(seat)
        self.groupBox.setGeometry(QtCore.QRect(30, 80, 151, 251))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 40, 106, 181))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_9 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout.addWidget(self.pushButton_9)
        self.pushButton_10 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_10.setObjectName("pushButton_10")
        self.verticalLayout.addWidget(self.pushButton_10)
        self.label = QtWidgets.QLabel(seat)
        self.label.setGeometry(QtCore.QRect(190, 60, 601, 351))
        self.label.setText("")
        self.label.setObjectName("label")
        self.tableWidget_3 = QtWidgets.QTableWidget(seat)
        self.tableWidget_3.setGeometry(QtCore.QRect(230, 130, 521, 221))
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(5)
        self.tableWidget_3.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, item)
        self.tableWidget_2 = QtWidgets.QTableWidget(seat)
        self.tableWidget_2.setGeometry(QtCore.QRect(340, 190, 301, 91))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(2)
        self.tableWidget_2.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(0, 1, item)
        self.groupBox_3 = QtWidgets.QGroupBox(seat)
        self.groupBox_3.setGeometry(QtCore.QRect(330, 130, 281, 221))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox_3)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 50, 238, 121))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_2.addWidget(self.lineEdit_2, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_2.addWidget(self.lineEdit_3, 1, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_2.addWidget(self.pushButton_6)
        self.pushButton_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 2, 1, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(seat)
        self.tableWidget.setGeometry(QtCore.QRect(230, 200, 531, 61))
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
        self.tableWidget_5 = QtWidgets.QTableWidget(seat)
        self.tableWidget_5.setGeometry(QtCore.QRect(230, 200, 411, 61))
        self.tableWidget_5.setObjectName("tableWidget_5")
        self.tableWidget_5.setColumnCount(4)
        self.tableWidget_5.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Castellar")
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        item.setFont(font)
        self.tableWidget_5.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(3, item)
        self.label_6 = QtWidgets.QLabel(seat)
        self.label_6.setGeometry(QtCore.QRect(290, 10, 54, 12))
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(seat)
        self.label_7.setGeometry(QtCore.QRect(300, 0, 231, 20))
        self.label_7.setObjectName("label_7")
        self.groupBox_2 = QtWidgets.QGroupBox(seat)
        self.groupBox_2.setGeometry(QtCore.QRect(260, 120, 421, 331))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.groupBox_2)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(20, 40, 381, 31))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_3.addWidget(self.lineEdit_4)
        self.comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget_3)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBox)
        self.pushButton_8 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_3.addWidget(self.pushButton_8)
        self.pushButton_7 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_3.addWidget(self.pushButton_7)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(100, 10, 231, 20))
        self.label_2.setObjectName("label_2")
        self.tableWidget_4 = QtWidgets.QTableWidget(self.groupBox_2)
        self.tableWidget_4.setGeometry(QtCore.QRect(40, 90, 351, 201))
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(3)
        self.tableWidget_4.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, item)
        self.pushButton_13 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_13.setGeometry(QtCore.QRect(90, 290, 75, 23))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_14.setGeometry(QtCore.QRect(260, 290, 75, 23))
        self.pushButton_14.setObjectName("pushButton_14")
        self.label_8 = QtWidgets.QLabel(seat)
        self.label_8.setGeometry(QtCore.QRect(250, 180, 91, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(seat)
        self.label_9.setGeometry(QtCore.QRect(230, 110, 111, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(seat)
        self.label_10.setGeometry(QtCore.QRect(230, 110, 81, 20))
        self.label_10.setObjectName("label_10")
        self.pushButton_11 = QtWidgets.QPushButton(seat)
        self.pushButton_11.setGeometry(QtCore.QRect(260, 350, 75, 23))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(seat)
        self.pushButton_12.setGeometry(QtCore.QRect(650, 350, 75, 23))
        self.pushButton_12.setObjectName("pushButton_12")

        self.retranslateUi(seat)
        QtCore.QMetaObject.connectSlotsByName(seat)

    def retranslateUi(self, seat):
        _translate = QtCore.QCoreApplication.translate
        seat.setWindowTitle(_translate("seat", "Form"))
        self.groupBox.setTitle(_translate("seat", "操作"))
        self.pushButton_4.setText(_translate("seat", "车位信息"))
        self.pushButton.setText(_translate("seat", "车位初始设置"))
        self.pushButton_2.setText(_translate("seat", "车位锁状态"))
        self.pushButton_3.setText(_translate("seat", "车位操作"))
        self.pushButton_9.setText(_translate("seat", "白天收费规则"))
        self.pushButton_10.setText(_translate("seat", "晚上收费规则"))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("seat", "车位号"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("seat", "车位锁状态"))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("seat", "车辆占用"))
        item = self.tableWidget_3.horizontalHeaderItem(3)
        item.setText(_translate("seat", "车辆类型"))
        item = self.tableWidget_3.horizontalHeaderItem(4)
        item.setText(_translate("seat", "状态操作"))
        item = self.tableWidget_2.verticalHeaderItem(0)
        item.setText(_translate("seat", "已占车位（个）"))
        item = self.tableWidget_2.verticalHeaderItem(1)
        item.setText(_translate("seat", "空闲车位（个）"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("seat", "内部车位"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("seat", "外部车位"))
        __sortingEnabled = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)
        self.tableWidget_2.setSortingEnabled(__sortingEnabled)
        self.label_3.setText(_translate("seat", "内部车辆数："))
        self.label_4.setText(_translate("seat", "外部车辆数："))
        self.pushButton_6.setText(_translate("seat", "确  定"))
        self.pushButton_5.setText(_translate("seat", "取  消"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("seat", "开始时间"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("seat", "结束时间"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("seat", "价格/小时"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("seat", "第一个小时的价格"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("seat", "操作"))
        item = self.tableWidget_5.horizontalHeaderItem(0)
        item.setText(_translate("seat", "开始时间"))
        item = self.tableWidget_5.horizontalHeaderItem(1)
        item.setText(_translate("seat", "结束时间"))
        item = self.tableWidget_5.horizontalHeaderItem(2)
        item.setText(_translate("seat", "价格/次"))
        item = self.tableWidget_5.horizontalHeaderItem(3)
        item.setText(_translate("seat", "操作"))
        self.label_7.setText(_translate("seat", "        车  位  管  理"))
        self.label_5.setText(_translate("seat", "请输入："))
        self.comboBox.setItemText(0, _translate("seat", "员工车位"))
        self.comboBox.setItemText(1, _translate("seat", "临时车位"))
        self.pushButton_8.setText(_translate("seat", "检索"))
        self.pushButton_7.setText(_translate("seat", "添加车位"))
        self.label_2.setText(_translate("seat", "请输入车位号或者选择车位类型检索"))
        item = self.tableWidget_4.horizontalHeaderItem(0)
        item.setText(_translate("seat", "车位号"))
        item = self.tableWidget_4.horizontalHeaderItem(1)
        item.setText(_translate("seat", "车位类型"))
        item = self.tableWidget_4.horizontalHeaderItem(2)
        item.setText(_translate("seat", "操作"))
        self.pushButton_13.setText(_translate("seat", "上一页"))
        self.pushButton_14.setText(_translate("seat", "下一页"))
        self.label_8.setText(_translate("seat", "白天收费规则"))
        self.label_9.setText(_translate("seat", "车位锁状态详情"))
        self.label_10.setText(_translate("seat", "TextLabel"))
        self.pushButton_11.setText(_translate("seat", "上一页"))
        self.pushButton_12.setText(_translate("seat", "下一页"))

