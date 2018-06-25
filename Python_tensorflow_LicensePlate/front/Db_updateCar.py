from updateCar import *
import sys
import pymysql
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QWidget
from PyQt5 .QtGui import *
from Python_tensorflow_LicensePlate.controller.VehicleController import VehicleController
from PyQt5.QtCore import *

class Update_Ui(QWidget):

    def __init__(self):
        super(Update_Ui, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.setWindowTitle("修改车辆信息页面")
        self.setFixedSize(self.width(), self.height())  # 实现禁止窗口最大化和禁止窗口拉伸
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
        staffNum = self.ui.num_lineEdit.text()   # 员工号
        CarNum = self.ui.car_lineEdit.text()      # 车牌号
        #此处车牌号应该不能被修改
        name = self.ui.name_lineEdit.text()      # 车主
        chejia = self.ui.Chejia_lineEdit.text()   # 车架号
        if staffNum == '':
            OK = QMessageBox.information(self, ("警告"), ("""请输入员工号"""))
            return
        if name == '':
            OK = QMessageBox.information(self, ("警告"), ("""姓名不能为空"""))
            return
        if CarNum == '':
            OK = QMessageBox.information(self, ("警告"), ("""车牌号不能为空"""))
            return
        if chejia == '':
            OK = QMessageBox.information(self, ("警告"), ("""车架号不能为空"""))
            return

        vc = VehicleController()
        result=vc.updVehicle(CarNum, name, chejia, staffNum)
        if result.status == 200:
            OK = QMessageBox.information(self, ("提示："), ("""修改成功！"""))
        elif result.status == 400:
            OK = QMessageBox.information(self, ("提示："), ("""修改失败！"""))  # 单引号包围font 井号会报错



    def update(self, id):
        sc = VehicleController()
        result = sc.findVehicleByid(id)
        vehicle = result.data[0]
        self.ui.num_lineEdit.setText(vehicle.SID)
        self.ui.name_lineEdit.setText(vehicle.owner)
        self.ui.Chejia_lineEdit.setText(vehicle.vehicle_identity)
        self.ui.car_lineEdit.setText(vehicle.PlateID)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my = Update_Ui()
    my.show()
    sys.exit(app.exec_())