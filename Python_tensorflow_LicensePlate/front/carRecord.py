# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'carRecord.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_carRecord(object):
    def setupUi(self, carRecord):
        carRecord.setObjectName("carRecord")
        carRecord.resize(600, 408)
        self.tableWidget = QtWidgets.QTableWidget(carRecord)
        self.tableWidget.setGeometry(QtCore.QRect(90, 150, 401, 181))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.horizontalLayoutWidget = QtWidgets.QWidget(carRecord)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(80, 50, 419, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.setItemText(0, "")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)

        self.retranslateUi(carRecord)
        QtCore.QMetaObject.connectSlotsByName(carRecord)

    def retranslateUi(self, carRecord):
        _translate = QtCore.QCoreApplication.translate
        carRecord.setWindowTitle(_translate("carRecord", "Form"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("carRecord", "车牌号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("carRecord", "进入时间"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("carRecord", "离开时间"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("carRecord", "车辆类型"))
        self.label.setText(_translate("carRecord", "请输入"))
        self.comboBox.setItemText(1, _translate("carRecord", "车牌号"))
        self.comboBox.setItemText(2, _translate("carRecord", "进入时间"))
        self.comboBox.setItemText(3, _translate("carRecord", "离开时间"))
        self.comboBox.setItemText(4, _translate("carRecord", "内部车"))
        self.comboBox.setItemText(5, _translate("carRecord", "外部车"))
        self.pushButton.setText(_translate("carRecord", "查询"))

