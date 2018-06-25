from SeatUpda_Ui import *
import sys
import pymysql
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QWidget
from PyQt5 .QtGui import *
from PyQt5.QtCore import *
class Update_seat(QWidget):
    def __init__(self):
        super(Update_seat, self).__init__()
        self.ui = Ui_seatUp()
        self.ui.setupUi(self)

        self.setWindowTitle("车位更新")
        self.setFixedSize(self.width(), self.height())  # 实现禁止窗口最大化和禁止窗口拉伸
        palette = QPalette()
        icon = QPixmap('upSeat.jpg').scaled(400, 300)
        palette.setBrush(self.backgroundRole(), QBrush(icon))
        self.setPalette(palette)

        self.ui.lineEdit.setClearButtonEnabled(True)
        # self.ui.lineEdit.setFrame(False)
        self.ui.comboBox.setFixedSize(145, 24)
        self.ui.lineEdit.setFixedSize(145, 24)
        self.setWindowIcon(QIcon('2.png'))

        self.ui.pushButton.setStyleSheet('text-align: center;'
                                      'width:50;'
                                      'height:30;'
                                      'background:lightyellow;')
        self.ui.pushButton_2.setStyleSheet('text-align: center;'
                                      'width:50;'
                                      'height:30;'
                                      'background:lightyellow;')

        self.ui.pushButton.setIcon(QIcon("sure.png"))
        self.ui.pushButton_2.setIcon(QIcon("cancle.png"))
        self.setWindowTitle("车位信息修改")
        self.ui.comboBox.setCurrentText("外部车辆")

        # 槽函数
        self.ui.pushButton.clicked.connect(self.updateTip)
        self.ui.pushButton_2.clicked.connect(self.clear)
    def clear(self):
        self.ui.lineEdit.clear()
        self.ui.comboBox.setFocus(False)
    def updateTip(self, id):

        reply = QMessageBox.question(self, '提示',
                                     "确定修改？", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.Db_insert(id)

    # 将更改的数据插入数据库
    def Db_insert(self):
        # 获得界面输入 self.ui.currentIndex用来获得下拉框的下标
        seatNum = self.ui.lineEdit.text()
        seatCategory = self.ui.currentText()

        if seatNum != '' and seatCategory != '':
            # 操作数据库
            OK = QMessageBox.information(self, ("提示"), ("修改成功！"))









    # 将修改的数据展示
    def ShowUpdate(self, id):

        sql = "select Sid, vehicleQuantity, name, phone, gender,  department  from staff where Sid = '" + id + "'"
        try:
            conn = pymysql.connect(host='127.0.0.1',
                                   port=3306, user='root', password='271996', db='db_car', charset='utf8')
            cursor = conn.cursor()
            cursor.execute(sql)
            results = cursor.fetchall()

            # 将根据id 查询到的数据展示到控件row[]里面的数字为测试，需要根据实际修改
            for row in results:
                print(row[0])
                self.ui.lineEdit.setText(row[0])
                self.ui.comboBox.setCurrentText(row[1])


        except Exception:
            self.ui.statusbar.showMessage("<font color='#ff0000'>查询异常</font>", 2000)
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my = Update_seat()
    my.show()
    sys.exit(app.exec_())