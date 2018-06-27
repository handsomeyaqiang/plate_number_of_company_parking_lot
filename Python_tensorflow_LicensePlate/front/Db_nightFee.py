from Python_tensorflow_LicensePlate.front.nightFee import *
from  Python_tensorflow_LicensePlate.controller.ChargeController import ChargeController
import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import *


class nightfee(QtWidgets.QDialog):
    def __init__(self,rule):
        super(nightfee, self).__init__()
        self.ui = Ui_nightFee()
        self.ui.setupUi(self)
        self.rule =rule

        self.setWindowTitle("修改夜晚停车收费")
        self.setFixedSize(self.width(), self.height())  # 实现禁止窗口最大化和禁止窗口拉伸
        self.ui.lineEdit.setClearButtonEnabled(True)
        self.ui.lineEdit_2.setClearButtonEnabled(True)
        self.ui.lineEdit_3.setClearButtonEnabled(True)

        self.ui.lineEdit.setFixedSize(160, 24)
        self.ui.lineEdit_2.setFixedSize(160, 24)
        self.ui.lineEdit_3.setFixedSize(160, 24)
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
        self.ShowUpdate()
    def clearInput(self):
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit_3.clear()

    def updateFee(self):

        startTime = self.ui.lineEdit_2.text()
        endTime = self.ui.lineEdit.text()
        price = self.ui.lineEdit_3.text()
        rulecontrol = ChargeController()
        self.rule.nightbegintime = startTime
        self.rule.nightendtime = endTime
        self.rule.nightprice = price
        self.rule.daybegintime = endTime
        self.rule.dayendtime = startTime
        if startTime != '' and endTime != '' and price != '':
            # 操作数据库
            rulecontrol.update(self.rule)
            OK = QMessageBox.information(self, ("提示"), ("修改成功！"))
            self.close()

        else:
            if startTime == '':
                OK = QMessageBox.warning(self, ("提示"), ("开始时间不能为空！"))
            if endTime == '':
                OK = QMessageBox.warning(self, ("提示"), ("结束时间不能为空！"))
            if price == '':
                OK = QMessageBox.warning(self, ("提示"), ("每次单价不能为空！"))

    # 修改提示
    def updateTip(self):
        reply = QMessageBox.question(self, '提示',
                                     "确定修改？", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.updateFee()

        # 将修改的数据展示

    def ShowUpdate(self):
        """更新页面"""
        self.ui.lineEdit_2.setText(str(self.rule.nightbegintime))
        self.ui.lineEdit.setText(str(self.rule.nightendtime))
        self.ui.lineEdit_3.setText(str(self.rule.nightprice))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my = nightfee()
    my.show()
    sys.exit(app.exec_())
