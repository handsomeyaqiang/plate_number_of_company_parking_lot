from updateCar import *
import sys
import pymysql
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QWidget
from PyQt5 .QtGui import *
from PyQt5.QtCore import *

class Update_Ui(QWidget):

    def __init__(self):
        super(Update_Ui, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.setWindowTitle("修改车辆信息页面")
        self.ui.name_lineEdit.setFrame(False)  # 无边框
        self.ui.Chejia_lineEdit.setFrame(False)
        self.ui.car_lineEdit.setFrame(False)
        self.ui.num_lineEdit.setFrame(False)

        self.ui.pushButton.setIcon(QIcon("sure.png"))
        self.ui.clear_pushButton.setIcon(QIcon("cancle.png"))
        # 清除
        self.ui.car_lineEdit.setClearButtonEnabled(True)
        self.ui.Chejia_lineEdit.setClearButtonEnabled(True)
        self.ui.num_lineEdit.setClearButtonEnabled(True)
        self.ui.name_lineEdit.setClearButtonEnabled(True)

        # 槽函数
        self.ui.pushButton.clicked.connect(self.DB_insert)
        self.ui.clear_pushButton.clicked.connect(self.clearInput)

    def closeEvent(self, QCloseEvent):
        reply = QMessageBox.question(self, '提示',
                                     "确定退出？", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()

    def clearInput(self):

        self.ui.name_lineEdit.clear()
        self.ui.car_lineEdit.clear()
        self.ui.num_lineEdit.clear()
        self.ui.Chejia_lineEdit.clear()


    def DB_insert(self):

        # 获得界面输入
        staffNum = self.ui.num_lineEdit.text()
        CarNum = self.ui.car_lineEdit.text()
        name = self.ui.name_lineEdit.text()
        chejia = self.ui.Chejia_lineEdit.text()

        if staffNum != '' and CarNum != '' and name != '' and chejia != '':

            # 操作数据库


            OK = QMessageBox.information(self, ("警告"), ("""更改成功""")) #改成功加入提示框


        else:
            if staffNum == '':
                OK = QMessageBox.information(self, ("警告"), ("""工号不能为空！"""))
            if CarNum == '':
                OK = QMessageBox.information(self, ("警告"), ("""车牌号不能为空！"""))
            if name == '':
                OK = QMessageBox.information(self, ("警告"), ("""车主姓名不能为空！"""))
            if chejia == '':
                OK = QMessageBox.information(self, ("警告"), ("""车架号不能为空！"""))




    def update(self, id):

      # 数据库语句需要修改
        sql = "select Sid, vehicleQuantity, name, phone, gender,  department  from staff where Sid = '" + id + "'"
        try:
            conn = pymysql.connect(host='127.0.0.1',
                                   port=3306, user='root', password='271996', db='db_car', charset='utf8')
            cursor = conn.cursor()
            cursor.execute(sql)
            results = cursor.fetchall()



            for row in results:
                # 将数据库查询要修改车辆的信息，展示在lineEidt
                self.ui.car_lineEdit.setText(row[0])
                self.ui.name_lineEdit.setText(row[1])
                self.ui.Chejia_lineEdit.setText(row[2])
                self.ui.num__lineEdit.setText(row[3])
                print(row[4])
        except Exception:
            self.ui.statusbar.showMessage("<font color='#ff0000'>查询异常</font>", 2000)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my = Update_Ui()
    my.show()
    sys.exit(app.exec_())