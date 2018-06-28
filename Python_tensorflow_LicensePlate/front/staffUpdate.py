from Python_tensorflow_LicensePlate.front.updatePage import *
import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QWidget
from PyQt5 .QtGui import *
from PyQt5.QtCore import *
from Python_tensorflow_LicensePlate.controller.StaffController import StaffController
from Python_tensorflow_LicensePlate.front.Db_Staff import *
class Update_Ui(QtWidgets.QDialog):

    def __init__(self,id):
        super(Update_Ui, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.update(id)

        self.setWindowTitle("修改职工信息页面")
        self.ui.name_lineEdit.setFrame(False)  # 无边框
        self.ui.phone_lineEdit.setFrame(False)
        self.ui.depart_lineEdit.setFrame(False)
        self.ui.car_lineEdit.setFrame(False)
        self.ui.lineEdit.setFrame(False)
        self.ui.lineEdit.setReadOnly(True)  # 工号设为只读


        self.ui.pushButton.setIcon(QIcon("sure.png"))
        self.ui.pushButton_2.setIcon(QIcon("cancle.png"))

        self.setFixedSize(self.width(), self.height())
        # 清除
        self.ui.car_lineEdit.setClearButtonEnabled(True)
        # self.ui.lineEdit.setClearButtonEnabled(True)
        self.ui.phone_lineEdit.setClearButtonEnabled(True)
        self.ui.name_lineEdit.setClearButtonEnabled(True)

        self.ui.depart_lineEdit.setClearButtonEnabled(True)

        palette = QPalette()
        icon = QPixmap('cord.jpg').scaled(800, 600)
        palette.setBrush(self.backgroundRole(), QBrush(icon))
        self.setPalette(palette)

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
    # 更改员工信息， 更改成功后，应该在把更改的信息展示出来，调用Db_Staff函数里的查询所有
    def DB_insert(self):
        # 获得界面输入
        StaffNum = self.ui.lineEdit.text()
        carNum = self.ui.car_lineEdit.text()
        name = self.ui.name_lineEdit.text()
        phone = self.ui.phone_lineEdit.text()
        if self.ui.radioButton.isChecked():
            gender = 0
        else:
            gender = 1
        department = self.ui.depart_lineEdit.text()

        if carNum == '':  # 空检查
            OK = QMessageBox.information(self, ("警告"), ("""请输入拥有的车辆数"""))
            return
        if name == '':
            OK = QMessageBox.information(self, ("警告"), ("""姓名不能为空"""))
            return
        if phone == '':
            OK = QMessageBox.information(self, ("警告"), ("""手机号不能为空"""))
            return
        if department == '':
            OK = QMessageBox.information(self, ("警告"), ("""部门不能为空"""))
            return
        if carNum.isdigit() == False:  # 车辆数检查判断
            OK = QMessageBox.information(self, ("提示："), ("""车辆数必须为数字，请检查您的输入！"""))
            return
        if StaffNum.isdigit() == False:  # 员工号是否为数字检查判断
            OK = QMessageBox.information(self, ("提示："), ("""员工号必须为数字，请检查您的输入！"""))
            return
        if phone.isdigit() == False:  # 电话号是否为数字检查判断
            OK = QMessageBox.information(self, ("提示："), ("""电话号必须为数字，请检查您的输入！"""))
            return
        if len(str(StaffNum)) > 8:  # 员工号长度检查判断
            OK = QMessageBox.information(self, ("提示："), ("""员工号最多8位，请检查您的输入！"""))
            return
        if len(str(phone)) == 11 or len(str(phone)) == 7:  # 电话号长度检查判断
            # 开始添加员工信息的数据库操作
            sc = StaffController()
            result = sc.updStaff(StaffNum, int(carNum), name, phone, gender, department)
            if result.status == 200:
                OK = QMessageBox.information(self, ("提示："), ("""修改成功！"""))
                self.close()
            elif result.status == 400:
                OK = QMessageBox.information(self, ("提示："), ("""修改失败！"""))  # 单引号包围font 井号会报错
        else:
            OK = QMessageBox.information(self, ("提示："), ("""电话号位数不正确，请检查您的输入！"""))
            return

    def update(self, id):
          #获得当前要修改的员工信息，填入文本框中
            sc = StaffController()
            result = sc.findStaffByid(id)
            staff=result.data[0]
            self.ui.lineEdit.setText(staff.SID)
            self.ui.car_lineEdit.setText(str(staff.vehicleQuantity))
            self.ui.name_lineEdit.setText(staff.name)
            self.ui.phone_lineEdit.setText(staff.phoneNumber)
            if staff.gender == 0:
                self.ui.radioButton.setChecked(True)
            elif staff.gender == 1:
                self.ui.radioButton_2.setChecked(True)
            self.ui.depart_lineEdit.setText(staff.department)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my = Update_Ui()
    my.show()
    sys.exit(app.exec_())