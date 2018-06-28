from Python_tensorflow_LicensePlate.front.staffUpdate import *
#from updatePage import *    #直接调用ui转化来的文件闪退，还是需第三方py文件调用
from Python_tensorflow_LicensePlate.front.TableAndButton import *
from PyQt5.QtWidgets import *
from Python_tensorflow_LicensePlate.controller.StaffController import StaffController

# 导入文件的顺序不同会导致文件类识别异常，原因未知
from PyQt5 import QtWidgets, QtCore, QtGui

from PyQt5.QtWidgets import QWidget
from PyQt5 .QtGui import *
from PyQt5.QtCore import *
class tableB(QtWidgets.QMainWindow):
    def __init__(self):
        super(tableB, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.flag=0

        self.setWindowTitle("员工信息管理")
        self.setFixedSize(self.width(), self.height())  # 实现禁止窗口最大化和禁止窗口拉伸
        # 控制tableWidget item文字风格
        for index in range(self.ui.tableWidget.columnCount()):
            headItem = self.ui.tableWidget.horizontalHeaderItem(index)
            headItem.setFont(QFont("song", 12, QFont.Bold))
            headItem.setForeground(QBrush(Qt.gray))
            headItem.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)


        # 控制label

        self.setStyleSheet("QLabel{background:;}"
                           "QLabel{color: LightCoral;font-size:12px;font-weight:lighter;font-family:Roman times;}"
                           "QLabel:hover{color:}")
        self.ui.groupBox.setStyleSheet("QGroupBox{color:black;font-family:宋体}")
        self.ui.groupBox_2.setStyleSheet("QGroupBox{color:black;font-family:宋体}")
        self.ui.nan_radioButton.setStyleSheet("QRadioButton{color:black;font-family:Roman times}")
        self.ui.nv_radioButton.setStyleSheet("QRadioButton{colorblack;font-family:Roman times}")
        palette = QPalette()
        icon = QPixmap('cord.jpg').scaled(800, 600)
        palette.setBrush(self.backgroundRole(), QBrush(icon))
        self.setPalette(palette)
        # item = self.ui.horizontalHeaderItem(3)
        # item.setTextColor(QColor("red"))
        # 槽函数
        self.ui.pushButton.clicked.connect(self.DB_query) # 查找所有
        self.ui.add_pushButton.clicked.connect(self.DB_add)# 添加员工
        self.ui.pushButton_2.clicked.connect(self.QueryBySid)
        self.ui.exit_pushButton.clicked.connect(self.close)  # 直接调用closeEvent函数报错，用自带的close方法间接调用
        self.ui.pushButton_3.clicked.connect(self.clearInput)


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
        # hLayout.addWidget(viewBtn)
        hLayout.addWidget(deleteBtn)
        hLayout.setContentsMargins(5, 2, 5, 2)
        widget.setLayout(hLayout)
        return widget

    def clearInput(self):
        self.ui.car_lineEdit.clear()
        self.ui.depart_lineEdit.clear()
        self.ui.name_lineEdit.clear()
        self.ui.phone_lineEdit.clear()
        self.ui.num_lineEdit.clear()


    def closeEvent(self, QCloseEvent):
        reply = QMessageBox.question(self, '提示',
                                     "确定退出？", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()
    def DeleteTip(self, id):
        reply = QMessageBox.question(self, '提示',
                                     "确定删除吗？", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.DB_delete(id)



    #条件查询
    def QueryBySid(self):
        #获得输入  最好提供姓名和工号都可以查询，或者模糊查询
        text = self.ui.lineEdit_5.text()

    #按照工号查询
        if self.ui.comboBox.currentText() == '按工号':
            self.flag=3
            sc = StaffController()
            result = sc.findStaffByid(text)
            if len(result.data)==0:
                OK = QMessageBox.information(self, ("提示："), ("""未查询到记录！"""))
                return
            if result.status == 200:
                row = len(result.data)
                col = ["SID", "vehicleQuantity", "name", "phoneNumber", "gender", "department"]
                self.ui.tableWidget.setRowCount(row)  # 控件的名字保持一致，切莫想当然
                self.ui.tableWidget.setColumnCount(len(col) + 1)  # 加1，开辟一列放操作按钮
                self.ui.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)  # 选中行
                self.ui.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)  # 将单元格设为不可更改类型

                for i in range(row):
                    for j in range(len(col)):
                        staff = result.data[i]
                        if col[j] == 'gender':
                            temp_data = staff.__getattribute__(col[j])
                            if temp_data == 0:
                                temp_data = '女'
                                data = QTableWidgetItem(str(temp_data))
                                self.ui.tableWidget.setItem(i, j, data)
                            elif temp_data == 1:
                                temp_data = '男'
                                data = QTableWidgetItem(str(temp_data))
                                self.ui.tableWidget.setItem(i, j, data)
                        else:
                            temp_data = staff.__getattribute__(col[j])  # 临时记录，不能直接插入表格
                            data = QTableWidgetItem(str(temp_data))  # 转换后可插入表格
                            self.ui.tableWidget.setItem(i, j, data)
                            if j == len(col) - 1:
                                staff = result.data[i]
                                self.ui.tableWidget.setCellWidget(i, j + 1, self.buttonForRow(
                                    str(staff.__getattribute__(col[0]))))

                self.ui.statusbar.showMessage("查询成功")
            else:
                self.ui.statusbar.showMessage("查询异常", 2000)  # 单引号包围font 井号会报错

        # 按照姓名查询
        if self.ui.comboBox.currentText() == '按姓名':
            self.flag=2
            sc = StaffController()
            result = sc.findStaffByname(text)
            if len(result.data)==0:
                OK = QMessageBox.information(self, ("提示："), ("""未查询到记录！"""))
                return
            if result.status == 200:
                row = len(result.data)
                col = ["SID", "vehicleQuantity", "name", "phoneNumber", "gender", "department"]
                self.ui.tableWidget.setRowCount(row)  # 控件的名字保持一致，切莫想当然
                self.ui.tableWidget.setColumnCount(len(col) + 1)  # 加1，开辟一列放操作按钮
                self.ui.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)  # 选中行
                self.ui.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)  # 将单元格设为不可更改类型

                for i in range(row):
                    for j in range(len(col)):

                        staff = result.data[i]
                        if col[j] == 'gender':
                            temp_data = staff.__getattribute__(col[j])
                            if temp_data == 0:
                                temp_data = '女'
                                data = QTableWidgetItem(str(temp_data))
                                self.ui.tableWidget.setItem(i, j, data)
                            elif temp_data == 1:
                                temp_data = '男'
                                data = QTableWidgetItem(str(temp_data))
                                self.ui.tableWidget.setItem(i, j, data)
                        else:
                            temp_data = staff.__getattribute__(col[j])  # 临时记录，不能直接插入表格
                            data = QTableWidgetItem(str(temp_data))  # 转换后可插入表格
                            self.ui.tableWidget.setItem(i, j, data)
                            if j == len(col) - 1:
                                staff = result.data[i]
                                self.ui.tableWidget.setCellWidget(i, j + 1, self.buttonForRow(
                                    str(staff.__getattribute__(col[0]))))

                self.ui.statusbar.showMessage("查询成功")
            else:
                self.ui.statusbar.showMessage("查询异常", 2000)  # 单引号包围font 井号会报错

            # 按照部门查询
        if self.ui.comboBox.currentText() == '按部门':
            sc = StaffController()
            result = sc.findStaffBydepart(text)
            self.flag=1
            if len(result.data)==0:
                OK = QMessageBox.information(self, ("提示："), ("""未查询到记录！"""))
                return
            if result.status == 200:
                row = len(result.data)
                col = ["SID", "vehicleQuantity", "name", "phoneNumber", "gender", "department"]
                self.ui.tableWidget.setRowCount(row)  # 控件的名字保持一致，切莫想当然
                self.ui.tableWidget.setColumnCount(len(col) + 1)  # 加1，开辟一列放操作按钮
                self.ui.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)  # 选中行
                self.ui.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)  # 将单元格设为不可更改类型

                for i in range(row):
                    for j in range(len(col)):

                        staff = result.data[i]
                        if col[j] == 'gender':
                            temp_data = staff.__getattribute__(col[j])
                            if temp_data == 0:
                                temp_data = '女'
                                data = QTableWidgetItem(str(temp_data))
                                self.ui.tableWidget.setItem(i, j, data)
                            elif temp_data == 1:
                                temp_data = '男'
                                data = QTableWidgetItem(str(temp_data))
                                self.ui.tableWidget.setItem(i, j, data)
                        else:
                            temp_data = staff.__getattribute__(col[j])  # 临时记录，不能直接插入表格
                            data = QTableWidgetItem(str(temp_data))  # 转换后可插入表格
                            self.ui.tableWidget.setItem(i, j, data)
                            if j == len(col) - 1:
                                staff = result.data[i]
                                self.ui.tableWidget.setCellWidget(i, j + 1, self.buttonForRow(
                                    str(staff.__getattribute__(col[0]))))

                self.ui.statusbar.showMessage("查询成功")
            else:
                self.ui.statusbar.showMessage("查询异常", 2000)  # 单引号包围font 井号会报错



    # 添加

    def DB_add(self):

        StaffNum = self.ui.num_lineEdit.text()
        carNum = self.ui.car_lineEdit.text()
        name = self.ui.name_lineEdit.text()
        phone = self.ui.phone_lineEdit.text()

        if self.ui.nan_radioButton.isChecked():
            gender = 1
            gender1='男'
        else:
            gender = 0
            gender1='女'
        department = self.ui.depart_lineEdit.text()

        if carNum == '':
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

        #开始添加员工信息的数据库操作
        sc = StaffController()
        result = sc.insertStaff(StaffNum,carNum,name,phone,gender,department)
        if result.status == 200:
            OK = QMessageBox.information(self,("提示："), ("""添加成功！"""))
            self.DB_query()
        elif result.status == 400:
            OK = QMessageBox.information(self, ("提示："),("""添加失败！"""))  # 单引号包围font 井号会报错



    # 更新
    def DB_update(self, id):
        # 引入更新界面
        # self.ui = Update_Ui()
        # self.ui.update(id)
        # self.ui.show()
        self.m = Update_Ui(id)
        self.m.exec()
        if self.flag == 0:
            self.DB_query()
        else:
            self.QueryBySid()



    # 删除  先根据id删除数据，然后查找所有刷新展示页面
    def DB_delete(self, id):
        sc = StaffController()
        result = sc.delStaff(id)
        if result.status == 200:
            OK = QMessageBox.information(self, ("提示："), ("""删除成功！"""))
            if self.flag==0:
                self.DB_query()
            else :
                self.QueryBySid()
        elif result.status == 400:
            OK = QMessageBox.information(self, ("提示："), ("""删除失败！"""))



    def DB_query(self):
        sc = StaffController()
        result = sc.showStaff()
        if result.status == 200:
            row = len(result.data)
            col = ["SID", "vehicleQuantity", "name", "phoneNumber", "gender", "department"]
            self.ui.tableWidget.setRowCount(row)
            self.ui.tableWidget.setColumnCount(len(col)+1)  # 加1，开辟一列放操作按钮
            self.ui.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)  # 选中行
            self.ui.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)   # 将单元格设为不可更改类型
            for i in range(row):
                for j in range(len(col)):
                    staff = result.data[i]
                    if col[j]=='gender':
                        temp_data = staff.__getattribute__(col[j])
                        if  temp_data==0:
                            temp_data = '女'
                            data = QTableWidgetItem(str(temp_data))
                            self.ui.tableWidget.setItem(i, j, data)
                        elif temp_data == 1:
                            temp_data = '男'
                            data = QTableWidgetItem(str(temp_data))
                            self.ui.tableWidget.setItem(i, j, data)
                    else:
                        temp_data = staff.__getattribute__(col[j]) # 临时记录，不能直接插入表格
                        data = QTableWidgetItem(str(temp_data))  # 转换后可插入表格
                        self.ui.tableWidget.setItem(i, j, data)
                        if j == len(col)-1:
                            staff = result.data[i]
                            self.ui.tableWidget.setCellWidget(i, j+1, self.buttonForRow(str(staff.__getattribute__(col[0]))))
            self.ui.statusbar.showMessage("查询成功")
        else:
            self.ui.statusbar.showMessage("查询异常", 2000) # 单引号包围font 井号会报错



if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    my = tableB()
    my.show()
    sys.exit(app.exec_())