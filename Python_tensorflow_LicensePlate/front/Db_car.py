import sys
import pymysql
from CarInformation import *
from updateCarInfo import *
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class carManage(QtWidgets.QMainWindow):
    def __init__(self):
        super(carManage, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("车辆信息管理")

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
        self.ui = Update_Ui()
        self.ui.update(id)
        self.ui.show()


    # 用来提示用户是否删除信息
    def DeleteTip(self, id):
        reply = QMessageBox.question(self, '提示',
                                     "确定删除吗？", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.DB_delete(id)

    # 删除车辆信息  先根据id删除数据，然后查找所有刷新展示页面
    def DB_delete(self, id):
        sql = "delete  from staff where Sid = '" + id + "'"
        print(sql)
        if id != '':
            try:
                conn = pymysql.connect(host='127.0.0.1',
                                       port=3306, user='root', password='271996', db='db_car', charset='utf8')
                cursor = conn.cursor()
                cursor.execute(sql)
                conn.commit()
                sql_all ="select Sid, vehicleQuantity, name, phone, gender,  department  from staff"
                cursor.execute(sql_all)
                rows = cursor.fetchall()



                row = cursor.rowcount  # 通过查询的数据，取得记录条数，用来设置表格的行数
                col = len(rows[0])  # 取得每条记录的长度，用来设置表格的列数
                cursor.close()
                conn.close()

                self.ui.tableWidget.setRowCount(row)  # 控件的名字保持一致，切莫想当然
                self.ui.tableWidget.setColumnCount(col + 1)  # 加1，开辟一列放操作按钮
                self.ui.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)  # 选中行
                self.ui.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)  # 将单元格设为不可更改类型

                for i in range(row):
                    for j in range(col):
                        temp_data = rows[i][j]  # 临时记录，不能直接插入表格
                        data = QTableWidgetItem(str(temp_data))  # 转换后可插入表格
                        self.ui.tableWidget.setItem(i, j, data)
                        # 数据库因为从0开始计数，所以列数减一
                        if j == col - 1:
                            # print(rows[i][0])
                            # 传入id rows[i][0]
                            self.ui.tableWidget.setCellWidget(i, j + 1, self.buttonForRow(str(rows[i][0])))

                cursor.close()
                conn.close()
                OK = QMessageBox.information(self, ("提示"), ("删除成功"))
            except Exception:

                self.ui.statusbar.showMessage("删除异常", 2000)


    # 添加车辆信息
    def DB_Add(self):

        #获得界面输入
        staffNum = self.ui.num_lineEdit.text()
        name = self.ui.name_lineEdit.text()
        carNum = self.ui.carNum_lineEdit.text()

        #车架号
        driverNum = self.ui.driverNum_lineEdit.text()

        if staffNum != '' and name != '' and carNum != '' and driverNum != '':
            # 操作数据添加信息





            OK = QMessageBox.information(self, ("提示"), ("""添加成功!"""))
        else:
            if staffNum == '':
                OK = QMessageBox.information(self, ("警告"), ("""工号不能为空!"""))
            if name == '':
                OK = QMessageBox.information(self, ("警告"), ("""姓名不能为空!"""))
            if carNum == '':
                OK = QMessageBox.information(self, ("警告"), ("""车牌号不能为空!"""))
            if driverNum == '':
                OK = QMessageBox.information(self, ("警告"), ("""驾驶证号不能为空!"""))

        # 工号查询

    def QueryBySid(self):
        # 获得输入  最好提供姓名和工号都可以查询，或者模糊查询
        sid = self.ui.lineEdit_5.text()
        category = self.ui.comboBox.currentText()  # 用户选择的条件，按工号等等
        if sid == '':
            OK = QMessageBox.information(self, ("警告"), ("""请输入查询内容!"""))
        else:

            print(sid)   # 测试是否捕获到用户输入
            # 操作数据库
            sql = "select Sid, vehicleQuantity, name, phone, gender,  department  from staff where Sid = '" + sid + "'"
            print(sql)


            try:
                conn = pymysql.connect(host='127.0.0.1',
                                       port=3306, user='root', password='271996', db='db_car', charset='utf8')
                cursor = conn.cursor()
                cursor.execute(sql)
                rows = cursor.fetchall()


                row = cursor.rowcount  # 通过查询的数据，取得记录条数，用来设置表格的行数
                col = len(rows[0])  # 取得每条记录的长度，用来设置表格的列数

                cursor.close()
                conn.close()
                # 控制表格属性
                self.ui.tableWidget.setRowCount(row)
                self.ui.tableWidget.setColumnCount(col + 1)  # 加1，开辟一列放操作按钮
                self.ui.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)  # 选中行
                self.ui.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)  # 将单元格设为不可更改类型
                for i in range(row):
                    for j in range(col):
                        temp_data = rows[i][j]  # 临时记录，不能直接插入表格
                        data = QTableWidgetItem(str(temp_data))  # 转换后可插入表格
                        self.ui.tableWidget.setItem(i, j, data)
                        # 数据库因为从0开始计数，所以列数减一
                        if j == col - 1:
                            print(rows[i][0])
                            # 传入id rows[i][0]
                            self.ui.tableWidget.setCellWidget(i, j + 1, self.buttonForRow(str(rows[i][0])))

                self.ui.statusbar.showMessage("<font color='#ff0000'>查询成功</font>")
            except Exception:

                self.ui.statusbar.showMessage("<font color='#ff0000'>查询异常</font>", 2000)



    # 清空用户输入
    def Clear(self):
        self.ui.num_lineEdit.clear()
        self.ui.name_lineEdit.clear()
        self.ui.carNum_lineEdit.clear()
        self.ui.driverNum_lineEdit.clear()

    def DB_queryAll(self):

        # 获得查询的类型    数据库操作

        sql = "select SID, PlateID, owner, Vehicle_identity  from vehicle"
        try:
            conn = pymysql.connect(host='127.0.0.1',
                                   port=3306, user='root', password='271996', db='company_parking_system', charset='utf8')
            cursor = conn.cursor()
            cursor.execute(sql)

            rows = cursor.fetchall()
            row = cursor.rowcount  # 通过查询的数据，取得记录条数，用来设置表格的行数
            col = len(rows[0])  # 取得每条记录的长度，用来设置表格的列数

            cursor.close()
            conn.close()



            self.ui.tableWidget.setRowCount(row)  # 控件的名字保持一致，切莫想当然
            self.ui.tableWidget.setColumnCount(col + 1)  # 加1，开辟一列放操作按钮
            self.ui.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)  # 选中行
            self.ui.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)  # 将单元格设为不可更改类型

            for i in range(row):
                for j in range(col):
                    temp_data = rows[i][j]  # 临时记录，不能直接插入表格
                    data = QTableWidgetItem(str(temp_data))  # 转换后可插入表格
                    self.ui.tableWidget.setItem(i, j, data)
                    # 数据库因为从0开始计数，所以列数减一
                    if j == col - 1:
                        # print(rows[i][0])
                        # 传入id rows[i][0]
                        self.ui.tableWidget.setCellWidget(i, j + 1, self.buttonForRow(str(rows[i][0])))

            self.ui.statusbar.showMessage("<font color='red'>查询成功</font>")
        except Exception:

            self.ui.statusbar.showMessage("<font color='red'>查询异常</font>", 2000)

        # 查询语句




if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    my = carManage()
    my.show()
    sys.exit(app.exec_())
