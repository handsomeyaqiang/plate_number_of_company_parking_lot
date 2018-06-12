from updatePage import *
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

        self.setWindowTitle("修改信息页面")
        self.ui.name_lineEdit.setFrame(False)  # 无边框
        self.ui.phone_lineEdit.setFrame(False)
        self.ui.depart_lineEdit.setFrame(False)
        self.ui.car_lineEdit.setFrame(False)
        self.ui.lineEdit.setFrame(False)

        # 清除
        self.ui.car_lineEdit.setClearButtonEnabled(True)
        self.ui.lineEdit.setClearButtonEnabled(True)
        self.ui.phone_lineEdit.setClearButtonEnabled(True)
        self.ui.name_lineEdit.setClearButtonEnabled(True)
        self.ui.lineEdit.setClearButtonEnabled(True)

        # 槽函数
        self.ui.pushButton.clicked.connect(self.DB_insert)
        self.ui.pushButton_2.clicked.connect(self.clearInput)
    def clearInput(self):
        self.ui.lineEdit.setText('')
        self.ui.name_lineEdit.setText('')
        self.ui.phone_lineEdit.setText('')
        self.ui.depart_lineEdit.setText('')
        self.ui.car_lineEdit.setText('')
        self.ui.radioButton.setChecked(False)
        self.ui.radioButton_2.setChecked(False)
        self.ui.radioButton.setFocusPolicy(Qt.NoFocus)
        self.ui.radioButton_2.setFocusPolicy(Qt.NoFocus)
        # if self.ui.radioButton.isChecked():

        # if self.ui.radioButton_2.isChecked():





    def DB_insert(self):

        # 获得界面输入
        staffNum = self.ui.lineEdit.text()
        CarNum = self.ui.car_lineEdit.text()
        name = self.ui.name_lineEdit.text()
        phone = self.ui.name_lineEdit.text()
        depart = self.ui.depart_lineEdit.text()
        if self.ui.radioButton.isChecked():
            gender = '女'
        else:
            gender = '男'

        # OK = QMessageBox.information(self, ("警告"), ("""更改成功""")) 更改成功加入提示框

    def update(self, id):


        sql = "select Sid, vehicleQuantity, name, phone, gender,  department  from staff where Sid = '" + id + "'"
        try:
            conn = pymysql.connect(host='127.0.0.1',
                                   port=3306, user='root', password='271996', db='db_car', charset='utf8')
            cursor = conn.cursor()
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                print(row[0])
                self.ui.lineEdit.setText(row[0])
                self.ui.car_lineEdit.setText(row[1])
                self.ui.name_lineEdit.setText(row[2])
                self.ui.phone_lineEdit.setText(row[3])
              
                # if results[4] == '女':
                #     self.ui.radioButton.setChecked(True)
                # else:
                #     self.ui.radioButton_2.setChecked(True)
                self.ui.depart_lineEdit.setText(row[5])
                print(row[4])
        except Exception:
            self.ui.statusbar.showMessage("<font color='#ff0000'>查询异常</font>", 2000)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my = Update_Ui()
    my.show()
    sys.exit(app.exec_())