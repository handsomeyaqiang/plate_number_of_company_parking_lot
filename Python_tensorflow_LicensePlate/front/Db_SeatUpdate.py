from Python_tensorflow_LicensePlate.front.SeatUpda_Ui import *

import sys
import pymysql
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QWidget
from PyQt5 .QtGui import *
from PyQt5.QtCore import *
from Python_tensorflow_LicensePlate.controller.ParkPlaceController import ParkPlaceController
class Update_seat(QtWidgets.QDialog):
    def __init__(self, parkplace):
        super(Update_seat, self).__init__()
        self.ui = Ui_seatUp()
        self.ui.setupUi(self)

        self.setWindowTitle("车位更新")
        self.setFixedSize(self.width(), self.height())  # 实现禁止窗口最大化和禁止窗口拉伸
        palette = QPalette()
        icon = QPixmap('upSeat.jpg').scaled(400, 300)
        palette.setBrush(self.backgroundRole(), QBrush(icon))
        self.setPalette(palette)
        self.ui.lineEdit.setReadOnly(True)
        # self.ui.lineEdit.setClearButtonEnabled(True)
        self.ui.lineEdit.setFrame(False)
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
        self.parkplace = parkplace
        self.ShowUpdate()
        # 槽函数
        self.ui.pushButton.clicked.connect(self.updateTip)
        self.ui.pushButton_2.clicked.connect(self.clear)
    def clear(self):
        pass
        # self.ui.lineEdit.clear()
        # self.ui.comboBox.setFocus(False)
    def updateTip(self):

        reply = QMessageBox.question(self, '提示',
                                     "确定修改？", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.Db_insert()

    # 将更改的数据插入数据库
    def Db_insert(self):
        # 获得界面输入 self.ui.currentIndex用来获得下拉框的下标
        seatCategory = self.ui.comboBox.currentText()

        if self.parkplace.parkPlaceID != '' and seatCategory != '':
            # 操作数据库
            pcontrol = ParkPlaceController()
            if seatCategory =="员工车位":
                self.parkplace.parkPlaceType =0
            elif seatCategory =="临时车位":
                self.parkplace.parkPlaceType =1

            rs = pcontrol.updateparkplace(self.parkplace.parkPlaceID,self.parkplace.lockStatus,self.parkplace.parkPlaceType,self.parkplace.useCarNumber)
            if rs.status ==200:
                OK = QMessageBox.information(self, ("提示"), ("修改成功！"))
                self.close()
            else:
                QMessageBox.information(self, ("提示"), ("error"))

    # 将修改的数据展示
    def ShowUpdate(self):
        self.ui.lineEdit.setText(str(self.parkplace.parkPlaceID))

        if self.parkplace.parkPlaceType ==0:
           self.ui.comboBox.setCurrentIndex(1)
        else:
           self.ui.comboBox.setCurrentIndex(0)
        # results = ParkPlaceController().findbyid(id).data
        #   # 将根据id 查询到的数据展示到控件row[]里面的数字为测试，需要根据实际修改
        # for row in results:
        #     print(row[0])
        #     self.ui.lineEdit.setText(row[0])
        #     self.ui.comboBox.setCurrentText(row[1])


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my = Update_seat()
    my.show()
    sys.exit(app.exec_())