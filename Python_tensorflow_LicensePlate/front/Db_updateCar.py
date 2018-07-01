from Python_tensorflow_LicensePlate.front.updateCar import *
import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QWidget
from PyQt5 .QtGui import *
from Python_tensorflow_LicensePlate.controller.VehicleController import VehicleController
from Python_tensorflow_LicensePlate.controller.StaffController import StaffController
from PyQt5.QtCore import *
import re

class Update_Ui(QtWidgets.QDialog):

    def __init__(self,id):
        super(Update_Ui, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.update(id)

        self.setWindowTitle("修改车辆信息页面")
        self.setFixedSize(self.width(), self.height())  # 实现禁止窗口最大化和禁止窗口拉伸
        self.ui.name_lineEdit.setFrame(False)  # 无边框
        self.ui.Chejia_lineEdit.setFrame(False)
        self.ui.car_lineEdit.setFrame(False)
        self.ui.num_lineEdit.setFrame(False)

        palette = QPalette()
        icon = QPixmap('car.jpg').scaled(800, 600)
        palette.setBrush(self.backgroundRole(), QBrush(icon))
        self.setPalette(palette)

        self.ui.pushButton.setIcon(QIcon("sure.png"))
        self.ui.clear_pushButton.setIcon(QIcon("cancle.png"))
        # 清除
        # self.ui.car_lineEdit.setClearButtonEnabled(True)
        self.ui.Chejia_lineEdit.setClearButtonEnabled(True)
        self.ui.num_lineEdit.setClearButtonEnabled(True)
        self.ui.name_lineEdit.setClearButtonEnabled(True)
        self.ui.car_lineEdit.setReadOnly(True)

        # 槽函数
        self.ui.pushButton.clicked.connect(self.DB_insert)
        self.ui.clear_pushButton.clicked.connect(self.clearInput)


    def clearInput(self):

        self.ui.name_lineEdit.clear()
        self.ui.car_lineEdit.clear()
        self.ui.num_lineEdit.clear()
        self.ui.Chejia_lineEdit.clear()


    def DB_insert(self):
        # 获得界面输入
        staffNum = self.ui.num_lineEdit.text()   # 员工号
        CarNum = self.ui.car_lineEdit.text()      # 车牌号
        #此处车牌号不能被修改
        name = self.ui.name_lineEdit.text()      # 车主
        chejia = self.ui.Chejia_lineEdit.text()   # 车架号
        if staffNum == '':
            OK = QMessageBox.information(self, ("警告"), ("""请输入员工号"""))
            return
        if name == '':
            OK = QMessageBox.information(self, ("警告"), ("""车主姓名不能为空"""))
            return
        if CarNum == '':
            OK = QMessageBox.information(self, ("警告"), ("""车牌号不能为空"""))
            return
        if chejia == '':
            OK = QMessageBox.information(self, ("警告"), ("""车架号不能为空"""))
            return

        if re.match("[\u4e00-\u9fa5]{1}[A-Z]{1}[0-9]{4,5}", CarNum):  # 车牌号格式限制
            if re.match("^[\u4E00-\u9FA5]{2,4}$|^[a-zA-Z\/]{2,20}$", name):  # 姓名格式限制
                if re.match("[A-Z]+[0-9]", chejia):  # 车架号格式限制

                    sc = StaffController()
                    result1 = sc.findStaffByid(staffNum)
                    len2 = len(result1.data)
                    if len2 == 0:                   # 该员工不存在，不能添加
                        OK = QMessageBox.information(self, ("提示："), ("""<font color='red'>该员工不存在，无法添加他的车辆信息!</font>"""))
                        return
                    else:
                        vc = VehicleController()
                        result = vc.updVehicle(CarNum, name, chejia, staffNum)
                        if result.status == 200:
                            OK = QMessageBox.information(self, ("提示："), ("""修改成功！"""))
                            self.close()
                        elif result.status == 400:
                            OK = QMessageBox.information(self, ("提示："), ("""修改失败！"""))

                else:
                    OK = QMessageBox.information(self, ("提示："), ("""<font color='red'>车架号格式错误，输入应为字母和数字！</font>"""))
                    return
            else:
                OK = QMessageBox.information(self, ("提示："), ("""<font color='red'>姓名格式错误，输入为中文或英文名字！</font>"""))
                return
        else:
            OK = QMessageBox.information(self, ("提示："), ("""<font color='red'>车牌号格式错误，请检查您的输入！</font>"""))
            return


    def update(self, id):
        sc = VehicleController()
        result=sc.findVehicleByplatenumvague(id)
        vehicle = result.data[0]
        self.ui.num_lineEdit.setText(vehicle.SID)
        self.ui.name_lineEdit.setText(vehicle.owner)
        self.ui.Chejia_lineEdit.setText(vehicle.vehicle_identity)
        self.ui.car_lineEdit.setText(vehicle.PlateID)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my = Update_Ui(id)
    my.show()
    sys.exit(app.exec_())