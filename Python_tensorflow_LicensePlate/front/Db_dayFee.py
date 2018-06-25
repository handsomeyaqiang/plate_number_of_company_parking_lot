from Python_tensorflow_LicensePlate.controller.ChargeController import ChargeController
from Python_tensorflow_LicensePlate.front.dayFee import *
import sys
import pymysql
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import *


class dayfee(QWidget):
    def __init__(self, rule):
        super(dayfee, self).__init__()
        self.ui = Ui_dayFee()
        self.ui.setupUi(self)
        self.rule = rule
        self.setWindowTitle("修改白天停车收费")
        self.setFixedSize(self.width(), self.height())  # 实现禁止窗口最大化和禁止窗口拉伸
        self.ui.lineEdit.setClearButtonEnabled(True)
        self.ui.lineEdit_2.setClearButtonEnabled(True)
        self.ui.lineEdit_3.setClearButtonEnabled(True)
        self.ui.lineEdit_4.setClearButtonEnabled(True)
        # self.ui.lineEdit.setFrame(False)

        self.ui.lineEdit.setFixedSize(160, 24)
        self.ui.lineEdit_2.setFixedSize(160, 24)
        self.ui.lineEdit_3.setFixedSize(160, 24)
        self.ui.lineEdit_4.setFixedSize(160, 24)
        self.setWindowIcon(QIcon('2.png'))

        self.ui.pushButton.setStyleSheet('text-align: center;'
                                         'width:50;'
                                         'height:30;'
                                         'background:lightgreen;')
        self.ui.pushButton_2.setStyleSheet('text-align: center;'
                                           'width:50;'
                                           'height:30;'
                                           'background:lightgreen;')

        self.ui.pushButton.setIcon(QIcon("sure.png"))
        self.ui.pushButton_2.setIcon(QIcon("concle.png"))
        self.ui.pushButton.clicked.connect(self.updateTip)
        self.ui.pushButton_2.clicked.connect(self.clearInput)

    def clearInput(self):
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit_3.clear()
        self.ui.lineEdit_4.clear()

    def updateFee(self):
        """更新白天收费规则"""
        startTime = self.ui.lineEdit_2.text()
        endTime = self.ui.lineEdit.text()
        price = self.ui.lineEdit_3.text()
        firsthourprice = self.ui.lineEdit_4.text()
        rulecontrol = ChargeController()
        if startTime != '' and endTime != '' and price != '' and firsthourprice != '':
            # 操作数据库
            self.rule.dayprice = price
            self.rule.firsthourprice = firsthourprice
            self.rule.daybegintime = startTime
            self.rule.dayendtime = endTime
            self.rule.nightbegintime = endTime
            self.rule.nightendtime = startTime
            rulecontrol.update(self.rule)
            QMessageBox.information(self, ("提示"), ("修改成功！"))
        else:
            if startTime == '':
                QMessageBox.warning(self, ("提示"), ("开始时间不能为空！"))
            if endTime == '':
                QMessageBox.warning(self, ("提示"), ("结束时间不能为空！"))
            if price == '':
                QMessageBox.warning(self, ("提示"), ("每小时单价不能为空！"))
            if firsthourprice == '':
                QMessageBox.warning(self, ("提示"), ("首小时单价不能为空！"))

    # 修改提示
    def updateTip(self):
        reply = QMessageBox.question(self, '提示',
                                     "确定修改？", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.updateFee()


    def ShowUpdate(self):
        """修改页面"""
        self.ui.lineEdit_2.setText(str(self.rule.daybegintime))
        self.ui.lineEdit.setText(str(self.rule.dayendtime))
        self.ui.lineEdit_3.setText(str(self.rule.dayprice))
        self.ui.lineEdit_4.setText(str(self.rule.firsthourprice))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my = dayfee()
    my.show()
    sys.exit(app.exec_())
