# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TableAndButton.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 340, 721, 221))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
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
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(520, 90, 221, 211))
        self.groupBox.setObjectName("groupBox")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(60, 50, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.add_pushButton = QtWidgets.QPushButton(self.groupBox)
        self.add_pushButton.setGeometry(QtCore.QRect(60, 80, 75, 23))
        self.add_pushButton.setObjectName("add_pushButton")
        self.exit_pushButton = QtWidgets.QPushButton(self.groupBox)
        self.exit_pushButton.setGeometry(QtCore.QRect(60, 110, 75, 23))
        self.exit_pushButton.setObjectName("exit_pushButton")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(60, 80, 251, 221))
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(50, 30, 160, 150))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.nan_radioButton = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.nan_radioButton.setObjectName("nan_radioButton")
        self.horizontalLayout.addWidget(self.nan_radioButton)
        self.nv_radioButton = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.nv_radioButton.setObjectName("nv_radioButton")
        self.horizontalLayout.addWidget(self.nv_radioButton)
        self.gridLayout.addLayout(self.horizontalLayout, 5, 1, 1, 1)
        self.car_lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.car_lineEdit.setObjectName("car_lineEdit")
        self.gridLayout.addWidget(self.car_lineEdit, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)
        self.phone_lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.phone_lineEdit.setObjectName("phone_lineEdit")
        self.gridLayout.addWidget(self.phone_lineEdit, 4, 1, 1, 1)
        self.name_lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.name_lineEdit.setObjectName("name_lineEdit")
        self.gridLayout.addWidget(self.name_lineEdit, 3, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 6, 0, 1, 1)
        self.depart_lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.depart_lineEdit.setObjectName("depart_lineEdit")
        self.gridLayout.addWidget(self.depart_lineEdit, 6, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.num_lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.num_lineEdit.setObjectName("num_lineEdit")
        self.gridLayout.addWidget(self.num_lineEdit, 0, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 180, 191, 21))
        self.pushButton_3.setObjectName("pushButton_3")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 30, 741, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(120, 10, 571, 25))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_2.addWidget(self.lineEdit_5)
        self.comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(390, 60, 20, 261))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "工号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "拥有车辆数"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "姓名"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "联系方式"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "性别"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "部门"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "操作"))
        self.groupBox.setTitle(_translate("MainWindow", "操作"))
        self.pushButton.setText(_translate("MainWindow", "查询所有"))
        self.add_pushButton.setText(_translate("MainWindow", "添加员工"))
        self.exit_pushButton.setText(_translate("MainWindow", "退  出"))
        self.groupBox_2.setTitle(_translate("MainWindow", "添加员工信息"))
        self.nan_radioButton.setText(_translate("MainWindow", "男"))
        self.nv_radioButton.setText(_translate("MainWindow", "女"))
        self.label_4.setText(_translate("MainWindow", "  性别："))
        self.label_2.setText(_translate("MainWindow", "  姓名："))
        self.label_5.setText(_translate("MainWindow", "  部门："))
        self.label_3.setText(_translate("MainWindow", "  电话："))
        self.label.setText(_translate("MainWindow", "车辆数："))
        self.label_7.setText(_translate("MainWindow", " 工 号："))
        self.pushButton_3.setText(_translate("MainWindow", "清空输入"))
        self.label_6.setText(_translate("MainWindow", "请输入"))
        self.comboBox.setItemText(0, _translate("MainWindow", "按姓名"))
        self.comboBox.setItemText(1, _translate("MainWindow", "按部门"))
        self.comboBox.setItemText(2, _translate("MainWindow", "按车牌号"))
        self.pushButton_2.setText(_translate("MainWindow", "确定"))

