from dayFee import *
import sys
import pymysql
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QWidget
from PyQt5 .QtGui import *
class dayfee(QWidget):
    def __init__(self):
        super(dayfee, self).__init__()
        self.ui = Ui_dayFee()
        self.ui.setupUi(self)

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
        # 根据传过来的id修改
    def updateFee(self):
        startTime = self.ui.lineEdit.text()
        endTime = self.ui.lineEdit_2.text()
        fee = self.ui.lineEdit_3.text()
        firstFee = self.ui.lineEdit_4.text()
        if startTime != '' and endTime != '' and fee != '' and firstFee != '':
            # 操作数据库

            OK = QMessageBox.information(self, ("提示"), ("修改成功！"))
        else:
            if startTime == '':
                OK = QMessageBox.warning(self, ("提示"), ("开始时间不能为空！"))
            if endTime == '':
                OK = QMessageBox.warning(self, ("提示"), ("结束时间不能为空！"))
            if fee == '':
                OK = QMessageBox.warning(self, ("提示"), ("每小时单价不能为空！"))
            if firstFee == '':
                OK = QMessageBox.warning(self, ("提示"), ("首小时单价不能为空！"))
    # 修改提示
    def updateTip(self, id):
        reply = QMessageBox.question(self, '提示',
                                "确定修改？", QMessageBox.Yes |
                             QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.updateFee(id)


        # 将修改的数据展示

    def ShowUpdate(self, id):
        # 数据库随意更改
        sql = "select Sid, vehicleQuantity, name, phone, gender,  department  from staff where Sid = '" + id + "'"
        conn = pymysql.connect(host='127.0.0.1',
                               port=3306, user='root', password='271996', db='db_car', charset='utf8')
        cursor = conn.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()

        # 将根据id 查询到的数据展示到控件row[]里面的数字为测试，需要根据数据库字段顺序修改
        for row in results:
            print(row[0])
            self.ui.lineEdit.setText(row[0])
            self.ui.lineEdit_2.setText(row[1])
            self.ui.lineEdit_3.setText(row[2])
            self.ui.lineEdit_4.setText(row[3])



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my = dayfee()
    my.show()
    sys.exit(app.exec_())