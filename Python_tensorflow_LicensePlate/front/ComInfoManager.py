from ComInfoManage import *
from Db_Staff import *
from Db_car import *
from Db_carRecord import *
import sys
import pymysql
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QWidget
from PyQt5 .QtGui import *
from PyQt5.QtCore import *
class InfoManage(QWidget):
    def __init__(self):
        super(InfoManage, self).__init__()
        self.ui = Ui_ConInfo()
        self.ui.setupUi(self)

        self.setWindowTitle(" ")
        self.setWindowIcon(QIcon('3.png'))

        self.ui.label.setFixedSize(650, 35)
        self.ui.label.setStyleSheet("QLabel{background:white;}"
                       "QLabel{color:rgb(100,100,100,250);font-size:15px;font-weight:bold;font-family:Roman times;}")

        palette = QPalette()
        icon = QPixmap('info1.jpg').scaled(680, 480)
        palette.setBrush(self.backgroundRole(), QBrush(icon))
        self.setPalette(palette)


        # ui文件尽量别采用默认的类名，否则当导入多个文件时，容易出错
        self.ui.staff_Button.clicked.connect(self.staffInfo)
        self.ui.car_Button.clicked.connect(self.carInfo)
        self.ui.record_Button.clicked.connect(self.recordInfo)
    def recordInfo(self):
        self.ui2 = CarRecord()
        self.ui2.show()
    def carInfo(self):
        self.ui1 = carManage()
        self.ui1.show()

    def staffInfo(self):
        self.ui = tableB()
        self.ui.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my = InfoManage()
    my.show()
    sys.exit(app.exec_())