import sys
import pymysql
from CarInformation import *
from Db_updateCar import *
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Python_tensorflow_LicensePlate.controller.VehicleController import VehicleController


class carManage(QtWidgets.QMainWindow):
    def __init__(self):
        super(carManage, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("车辆信息管理")
        self.setFixedSize(self.width(), self.height())  # 实现禁止窗口最大化和禁止窗口拉伸
        self.flag = 0

        palette = QPalette()
        icon = QPixmap('car.jpg').scaled(800, 600)
        palette.setBrush(self.backgroundRole(), QBrush(icon))
        self.setPalette(palette)
        # 控制tableWidget item文字风格
        for index in range(self.ui.tableWidget.columnCount()):
            headItem = self.ui.tableWidget.horizontalHeaderItem(index)
            headItem.setFont(QFont("song", 12, QFont.Bold))
            headItem.setForeground(QBrush(Qt.gray))
            headItem.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        # 设置lineEdit
        self.ui.carNum_lineEdit.setClearButtonEnabled(True)
        self.ui.name_lineEdit.setClearButtonEnabled(True)
        self.ui.num_lineEdit.setClearButtonEnabled(True)
        self.ui.driverNum_lineEdit.setClearButtonEnabled(True)


        # 槽函数
        self.ui.clear_pushButton.clicked.connect(self.Clear)
        self.ui.add_pushButton.clicked.connect(self.DB_Add)
        self.ui.query_pushButton.clicked.connect(self.QueryBySid)
        self.ui.pushButton.clicked.connect(self.DB_queryAll)
        self.ui.exit_pushButton.clicked.connect(self.close)
    # 退出
    def closeEvent(self, QCloseEvent):
        reply = QMessageBox.question(self, '提示',
                                     "确定退出？", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()


    #   设置修改和删除按钮
    def buttonForRow(self, id):
        widget = QWidget()
        # 修改
        updateBtn = QPushButton('修改')
        updateBtn.setStyleSheet(''' text-align : center;
                                                   background-color : DarkSeaGreen;
                                                   height : 30px;
                                                   border-style: outset;
                                                   font : 13px  ''')

        updateBtn.clicked.connect(lambda: self.DB_update(id))

        # 删除
        deleteBtn = QPushButton('删除')
        deleteBtn.setStyleSheet(''' text-align : center;
                                             background-color : LightCoral;
                                             height : 30px;
                                             border-style: outset;
                                             font : 13px; ''')
        deleteBtn.clicked.connect(lambda: self.DeleteTip(id))

        hLayout = QHBoxLayout()
        hLayout.addWidget(updateBtn)
        hLayout.addWidget(deleteBtn)
        hLayout.setContentsMargins(5, 2, 5, 2)
        widget.setLayout(hLayout)
        return widget


    # 修改车辆信息

    def DB_update(self, id):
        # 引入更新界面
        # self.ui = Update_Ui()
        # self.ui.update(id)
        # self.ui.show()
        self.m = Update_Ui(id)
        self.m.exec()
        if self.flag == 0:
            self.DB_queryAll()
        else:
            self.QueryBySid()


    # 用来提示用户是否删除信息
    def DeleteTip(self, id):
        reply = QMessageBox.question(self, '提示',
                                     "确定删除吗？", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.DB_delete(id)

    # 删除车辆信息  先根据id删除数据，然后查找所有刷新展示页面
    def DB_delete(self, id):
        sc = VehicleController()
        result = sc.delVehicle(id)
        if result.status == 200:
            OK = QMessageBox.information(self, ("提示："), ("""删除成功！"""))
            if self.flag==0:
                self.DB_queryAll()
            else :
                self.QueryBySid()



    # 添加车辆信息
    def DB_Add(self):
        staffNum = self.ui.num_lineEdit.text()    #员工号
        name = self.ui.name_lineEdit.text()       #车主
        carNum = self.ui.carNum_lineEdit.text()    #车牌号
        driverNum = self.ui.driverNum_lineEdit.text()    # 车架号
        if staffNum == '':
            OK = QMessageBox.information(self, ("警告"), ("""请输入员工号"""))
            return
        if name == '':
            OK = QMessageBox.information(self, ("警告"), ("""姓名不能为空"""))
            return
        if carNum == '':
            OK = QMessageBox.information(self, ("警告"), ("""车牌号不能为空"""))
            return
        if driverNum == '':
            OK = QMessageBox.information(self, ("警告"), ("""车架号不能为空"""))
            return

        vc = VehicleController()
        result=vc.insertVehicle(carNum, name, driverNum, staffNum)
        if result.status == 200:
            OK = QMessageBox.information(self, ("提示："), ("""添加成功！"""))
            self.DB_queryAll()
        elif result.status == 400:
            OK = QMessageBox.information(self, ("提示："), ("""添加失败！"""))  # 单引号包围font 井号会报错



        # 查询

    def QueryBySid(self):

        # 获得输入  最好提供姓名和工号都可以查询，或者模糊查询
        text = self.ui.lineEdit_5.text()

        # 按照工号查询
        if self.ui.comboBox.currentText() == '按工号':
            self.flag = 3
            sc = VehicleController()
            result = sc.findVehicleByid(text)
            if result.status == 200:
                row = len(result.data)
                col = ["SID", "PlateID", "owner", "vehicle_identity"]
                self.ui.tableWidget.setRowCount(row)  # 控件的名字保持一致，切莫想当然
                self.ui.tableWidget.setColumnCount(len(col) + 1)  # 加1，开辟一列放操作按钮
                self.ui.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)  # 选中行
                self.ui.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)  # 将单元格设为不可更改类型
                for i in range(row):
                    for j in range(len(col)):
                        staff = result.data[i]
                        temp_data = staff.__getattribute__(col[j])  # 临时记录，不能直接插入表格
                        data = QTableWidgetItem(str(temp_data))  # 转换后可插入表格
                        self.ui.tableWidget.setItem(i, j, data)
                        # 数据库因为从0开始计数，所以列数减一
                        if j == len(col) - 1:
                                    # print(rows[i][0])
                                    # 传入id rows[i][0]
                            staff = result.data[i]
                            self.ui.tableWidget.setCellWidget(i, j + 1,self.buttonForRow(str(staff.__getattribute__(col[1]))))
                self.ui.statusbar.showMessage("查询成功")
            else:
                self.ui.statusbar.showMessage("查询异常", 2000)  # 单引号包围font 井号会报错

                # 按照车牌号查询
        if self.ui.comboBox.currentText() == '按车牌号':
            self.flag = 2
            sc = VehicleController()
            result = sc.findVehicleByplatenum(text)
            if result.status == 200:
                row = len(result.data)
                col = ["SID", "PlateID", "owner", "vehicle_identity"]
                self.ui.tableWidget.setRowCount(row)  # 控件的名字保持一致，切莫想当然
                self.ui.tableWidget.setColumnCount(len(col) + 1)  # 加1，开辟一列放操作按钮
                self.ui.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)  # 选中行
                self.ui.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)  # 将单元格设为不可更改类型
                for i in range(row):
                    for j in range(len(col)):
                        staff = result.data[i]
                        temp_data = staff.__getattribute__(col[j])  # 临时记录，不能直接插入表格
                        data = QTableWidgetItem(str(temp_data))  # 转换后可插入表格
                        self.ui.tableWidget.setItem(i, j, data)
                                # 数据库因为从0开始计数，所以列数减一
                        if j == len(col) - 1:
                            staff = result.data[i]
                            self.ui.tableWidget.setCellWidget(i, j + 1, self.buttonForRow(str(staff.__getattribute__(col[1]))))
                self.ui.statusbar.showMessage("查询成功")
            else:
                self.ui.statusbar.showMessage("查询异常", 2000)  # 单引号包围font 井号会报错

        if self.ui.comboBox.currentText() == '按车主':
            self.flag = 3
            sc = VehicleController()
            result = sc.findVehicleByowner(text)
            if result.status == 200:
                row = len(result.data)
                col = ["SID", "PlateID", "owner", "vehicle_identity"]
                self.ui.tableWidget.setRowCount(row)  # 控件的名字保持一致，切莫想当然
                self.ui.tableWidget.setColumnCount(len(col) + 1)  # 加1，开辟一列放操作按钮
                self.ui.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)  # 选中行
                self.ui.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)  # 将单元格设为不可更改类型
                for i in range(row):
                    for j in range(len(col)):
                        staff = result.data[i]
                        temp_data = staff.__getattribute__(col[j])  # 临时记录，不能直接插入表格
                        data = QTableWidgetItem(str(temp_data))  # 转换后可插入表格
                        self.ui.tableWidget.setItem(i, j, data)
                        # 数据库因为从0开始计数，所以列数减一
                        if j == len(col) - 1:
                            # print(rows[i][0])
                            # 传入id rows[i][0]
                            staff = result.data[i]
                            self.ui.tableWidget.setCellWidget(i, j + 1, self.buttonForRow(
                                str(staff.__getattribute__(col[1]))))
                self.ui.statusbar.showMessage("查询成功")
            else:
                self.ui.statusbar.showMessage("查询异常", 2000)  # 单引号包围font 井号会报错

        if self.ui.comboBox.currentText() == '按车架号':
            self.flag = 3
            sc = VehicleController()
            result = sc.findVehicleByvehicleid(text)
            if result.status == 200:
                row = len(result.data)
                col = ["SID", "PlateID", "owner", "vehicle_identity"]
                self.ui.tableWidget.setRowCount(row)  # 控件的名字保持一致，切莫想当然
                self.ui.tableWidget.setColumnCount(len(col) + 1)  # 加1，开辟一列放操作按钮
                self.ui.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)  # 选中行
                self.ui.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)  # 将单元格设为不可更改类型
                for i in range(row):
                    for j in range(len(col)):
                        staff = result.data[i]
                        temp_data = staff.__getattribute__(col[j])  # 临时记录，不能直接插入表格
                        data = QTableWidgetItem(str(temp_data))  # 转换后可插入表格
                        self.ui.tableWidget.setItem(i, j, data)
                        # 数据库因为从0开始计数，所以列数减一
                        if j == len(col) - 1:
                            # print(rows[i][0])
                            # 传入id rows[i][0]
                            staff = result.data[i]
                            self.ui.tableWidget.setCellWidget(i, j + 1, self.buttonForRow(
                                str(staff.__getattribute__(col[1]))))
                self.ui.statusbar.showMessage("查询成功")
            else:
                self.ui.statusbar.showMessage("查询异常", 2000)  # 单引号包围font 井号会报错


    # 清空用户输入
    def Clear(self):
        self.ui.num_lineEdit.clear()
        self.ui.name_lineEdit.clear()
        self.ui.carNum_lineEdit.clear()
        self.ui.driverNum_lineEdit.clear()

    def DB_queryAll(self):
        # 显示全部的车辆信息
        sc = VehicleController()
        result = sc.showVehicle()
        if result.status == 200:
            row = len(result.data)
            col = ["SID", "PlateID", "owner", "vehicle_identity"]
            self.ui.tableWidget.setRowCount(row)  # 控件的名字保持一致，切莫想当然
            self.ui.tableWidget.setColumnCount(len(col) + 1)  # 加1，开辟一列放操作按钮
            self.ui.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)  # 选中行
            self.ui.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)  # 将单元格设为不可更改类型

            for i in range(row):
                for j in range(len(col)):
                    vehicle = result.data[i]
                    temp_data = vehicle.__getattribute__(col[j])  # 临时记录，不能直接插入表格
                    data = QTableWidgetItem(str(temp_data))  # 转换后可插入表格
                    self.ui.tableWidget.setItem(i, j, data)
                    # 数据库因为从0开始计数，所以列数减一
                    if j == len(col) - 1:
                        # print(rows[i][0])
                        # 传入id rows[i][0]
                        vehicle = result.data[i]
                        self.ui.tableWidget.setCellWidget(i, j + 1,self.buttonForRow(str(vehicle.__getattribute__(col[1]))))
            self.ui.statusbar.showMessage("查询成功")
        else:
            self.ui.statusbar.showMessage("查询异常", 2000)  # 单引号包围font 井号会报错


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    my = carManage()
    my.show()
    sys.exit(app.exec_())
