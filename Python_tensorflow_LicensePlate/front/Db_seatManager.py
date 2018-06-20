from seatManage import *
from Db_SeatUpdate import *
from Python_tensorflow_LicensePlate.front.Db_SeatUpdate import *
import sys
import pymysql
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget
from PyQt5 .QtGui import *


class SeatManage(QWidget):
    def __init__(self):
        super(SeatManage, self).__init__()
        self.ui = Ui_seat()
        self.ui.setupUi(self)

        self.setWindowTitle("车位管理")

        self.ui.tableWidget_2.hide()
        self.ui.tableWidget_3.hide()
        self.ui.groupBox_2.hide()
        self.ui.groupBox_3.hide()

        # 设置lineEdit的删除
        self.ui.lineEdit.setClearButtonEnabled(True)
        self.ui.lineEdit_3.setClearButtonEnabled(True)
        self.ui.lineEdit_2.setClearButtonEnabled(True)
        pixmap = QPixmap("seat.jpg")  # 按指定路径找到图片，注意路径必须用双引号包围，不能用单引号
        self.ui.label.setPixmap(pixmap)  # 在label上显示图片
        self.ui.label.setScaledContents(True)  # 让图片自适应label大小

        # 槽函数
        self.ui.pushButton.clicked.connect(self.seatSet)   # 显示车位设置窗口
        self.ui.pushButton_2.clicked.connect(self.lockState)  # 显示车位锁状态窗口
        self.ui.pushButton_3.clicked.connect(self.operateSeat) # 操作车位锁的窗口
        self.ui.pushButton_4.clicked.connect(self.seatDetailed) # 查看车位详情的窗口
        self.ui.pushButton_6.clicked.connect(self.seatSet1)   # 设置车位，内外车位数目，总数目
        self.ui.pushButton_5.clicked.connect(self.clearInput)  # 清空车位设置的输入
        self.ui.pushButton_8.clicked.connect(self.operateSeat2) # 车位操作的控制逻辑函数

    # 删除修改的按钮函数
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


    # 车位锁的打开关闭按钮函数
    def buttonForRow1(self, id):
        widget = QWidget()
        # 修改
        updateBtn = QPushButton('打开')
        updateBtn.setStyleSheet(''' text-align : center;
                                                      background-color : DarkSeaGreen;
                                                      height : 30px;
                                                      border-style: outset;
                                                      font : 13px  ''')

        updateBtn.clicked.connect(lambda: self.openTip(id))

        # 删除
        deleteBtn = QPushButton('关闭')
        deleteBtn.setStyleSheet(''' text-align : center;
                                                background-color : LightCoral;
                                                height : 30px;
                                                border-style: outset;
                                                font : 13px; ''')
        deleteBtn.clicked.connect(lambda: self.closeTip(id))

        hLayout = QHBoxLayout()
        hLayout.addWidget(updateBtn)
        # hLayout.addWidget(viewBtn)
        hLayout.addWidget(deleteBtn)
        hLayout.setContentsMargins(5, 2, 5, 2)
        widget.setLayout(hLayout)
        return widget

    # 用来提示用户是否删除信息
    def DeleteTip(self, id):
        reply = QMessageBox.question(self, '提示',
                                     "确定删除吗？", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.DB_delete(id)

    # 删除车位信息  先根据id删除数据，然后查找所有刷新展示页面 里面的数据库需要规范化
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

                self.ui.tableWidget_4.setRowCount(row)  # 控件的名字保持一致，切莫想当然
                self.ui.tableWidget_4.setColumnCount(col + 1)  # 加1，开辟一列放操作按钮
                self.ui.tableWidget_4.setSelectionBehavior(QTableWidget.SelectRows)  # 选中行
                self.ui.tableWidget_4.setEditTriggers(QTableWidget.NoEditTriggers)  # 将单元格设为不可更改类型

                for i in range(row):
                    for j in range(col):
                        temp_data = rows[i][j]  # 临时记录，不能直接插入表格
                        data = QTableWidgetItem(str(temp_data))  # 转换后可插入表格
                        self.ui.tableWidget_4.setItem(i, j, data)
                        # 数据库因为从0开始计数，所以列数减一
                        if j == col - 1:
                            # print(rows[i][0])
                            # 传入id rows[i][0]
                            self.ui.tableWidget_4.setCellWidget(i, j + 1, self.buttonForRow(str(rows[i][0])))

                cursor.close()
                conn.close()
                OK = QMessageBox.information(self, ("提示"), ("删除成功"))
            except Exception:
                self.ui.statusbar.showMessage("删除异常", 2000)
    # 修改 车位设置的信息
    def DB_update(self, id):
        self.ui = Update_seat()
        self.ui.ShowUpdate(id)
        self.ui.show()
    # 车位初始详情
    def seatDetailed(self):
        self.ui.tableWidget_2.show()
        self.ui.groupBox_2.hide()
        self.ui.groupBox_3.hide()
        self.ui.tableWidget_3.hide()
        # 操作数据库 需要规范化

        conn = pymysql.connect(host='127.0.0.1',
                               port=3306, user='root', password='271996', db='db_car', charset='utf8')
        cursor = conn.cursor()
        sql_all = "select Sid, vehicleQuantity, name, phone, gender,  department  from staff"
        cursor.execute(sql_all)
        rows = cursor.fetchall()

        row = cursor.rowcount  # 通过查询的数据，取得记录条数，用来设置表格的行数
        col = len(rows[0])  # 取得每条记录的长度，用来设置表格的列数
        cursor.close()
        conn.close()

        self.ui.tableWidget_2.setRowCount(row)  # 控件的名字保持一致，切莫想当然
        self.ui.tableWidget_2.setColumnCount(col)  # 加1，开辟一列放操作按钮
        self.ui.tableWidget_2.setSelectionBehavior(QTableWidget.SelectRows)  # 选中行
        self.ui.tableWidget_2.setEditTriggers(QTableWidget.NoEditTriggers)  # 将单元格设为不可更改类型
        # 将查询到的数据显示在表格中
        for i in range(row):
            for j in range(col):
                temp_data = rows[i][j]  # 临时记录，不能直接插入表格
                data = QTableWidgetItem(str(temp_data))  # 转换后可插入表格
                self.ui.tableWidget_2.setItem(i, j, data)

    # 车位操作， 查看车位的状态信息
    def operateSeat(self):
        self.ui.groupBox_2.show()
        self.ui.groupBox_3.hide()
        self.ui.tableWidget_2.hide()
        self.ui.tableWidget_3.hide()


    # 车位操作的控制逻辑
    def operateSeat2(self):
        # 获取界面输入
        category = self.ui.comboBox.currentText()
        input = self.ui.lineEdit_4.text()
        if category != '' and input != '':
            # 开始操作数据库按输入的条件查询车位信息

            sql = "select SID, PlateID, owner, Vehicle_identity  from vehicle"
            try:
                conn = pymysql.connect(host='127.0.0.1',
                                       port=3306, user='root', password='271996', db='company_parking_system',
                                       charset='utf8')
                cursor = conn.cursor()
                cursor.execute(sql)

                rows = cursor.fetchall()
                row = cursor.rowcount  # 通过查询的数据，取得记录条数，用来设置表格的行数
                col = len(rows[0])  # 取得每条记录的长度，用来设置表格的列数

                cursor.close()
                conn.close()

                self.ui.tableWidget_4.setRowCount(row)  # 控件的名字保持一致，切莫想当然
                self.ui.tableWidget_4.setColumnCount(col + 1)  # 加1，开辟一列放操作按钮
                self.ui.tableWidget_4.setSelectionBehavior(QTableWidget.SelectRows)  # 选中行
                self.ui.tableWidget_4.setEditTriggers(QTableWidget.NoEditTriggers)  # 将单元格设为不可更改类型

                for i in range(row):
                    for j in range(col):
                        temp_data = rows[i][j]  # 临时记录，不能直接插入表格
                        data = QTableWidgetItem(str(temp_data))  # 转换后可插入表格
                        self.ui.tableWidget_4.setItem(i, j, data)
                        # 数据库因为从0开始计数，所以列数减一
                        if j == col - 1:
                            # print(rows[i][0])
                            # 传入id rows[i][0]
                            self.ui.tableWidget_4.setCellWidget(i, j + 1, self.buttonForRow(str(rows[i][0])))

                self.ui.statusbar.showMessage("查询成功")
            except Exception:

                self.ui.statusbar.showMessage("查询异常", 2000)





    # 车位锁状态  查询所有，获得车位的id后进行打开关闭操作，点击打开时，先调用是否确认打开的提示
    # 然后根据id 查询到该车位的 车位状态，根据id 修改，在查询所有，放在table上
    def lockState(self):
        self.ui.tableWidget_3.show()
        self.ui.tableWidget_2.hide()
        self.ui.groupBox_3.hide()
        self.ui.groupBox_2.hide()

        # 操作数据库
        conn = pymysql.connect(host='127.0.0.1',
                               port=3306, user='root', password='271996', db='db_car', charset='utf8')
        cursor = conn.cursor()
        sql_all = "select Sid, vehicleQuantity, name, phone, gender,  department  from staff"
        cursor.execute(sql_all)
        rows = cursor.fetchall()

        row = cursor.rowcount  # 通过查询的数据，取得记录条数，用来设置表格的行数
        col = len(rows[0])  # 取得每条记录的长度，用来设置表格的列数
        cursor.close()
        conn.close()

        self.ui.tableWidget_3.setRowCount(row)  # 控件的名字保持一致，切莫想当然
        self.ui.tableWidget_3.setColumnCount(col)  # 加1，开辟一列放操作按钮
        self.ui.tableWidget_3.setSelectionBehavior(QTableWidget.SelectRows)  # 选中行
        self.ui.tableWidget_3.setEditTriggers(QTableWidget.NoEditTriggers)  # 将单元格设为不可更改类型
        # 将查询到的数据显示在表格中
        for i in range(row):
            for j in range(col):
                temp_data = rows[i][j]  # 临时记录，不能直接插入表格
                data = QTableWidgetItem(str(temp_data))  # 转换后可插入表格
                self.ui.tableWidget_3.setItem(i, j, data)
                if j == col - 1:
                    # print(rows[i][0])
                    # 传入id rows[i][0]
                    self.ui.tableWidget_3.setCellWidget(i, j + 1, self.buttonForRow1(str(rows[i][0])))

    # 打开车位锁的提示
    def openTip(self, id):

        reply = QMessageBox.question(self, '提示',
                                     "确定打开车位锁吗吗？", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.lock_open(id)
    # 打开车位锁的逻辑数据库操作 根据id 将车位的状态设为打开 然后在查询数据库展示
    def lock_open(self, id):

        if id != '':
            # 操作数据库
            conn = pymysql.connect(host='127.0.0.1',
                                   port=3306, user='root', password='271996', db='db_car', charset='utf8')
            cursor = conn.cursor()
            sql_all = "select Sid, vehicleQuantity, name, phone, gender,  department  from staff"
            cursor.execute(sql_all)
            rows = cursor.fetchall()

            row = cursor.rowcount  # 通过查询的数据，取得记录条数，用来设置表格的行数
            col = len(rows[0])  # 取得每条记录的长度，用来设置表格的列数
            cursor.close()
            conn.close()

            self.ui.tableWidget_3.setRowCount(row)  # 控件的名字保持一致，切莫想当然
            self.ui.tableWidget_3.setColumnCount(col)  # 加1，开辟一列放操作按钮
            self.ui.tableWidget_3.setSelectionBehavior(QTableWidget.SelectRows)  # 选中行
            self.ui.tableWidget_3.setEditTriggers(QTableWidget.NoEditTriggers)  # 将单元格设为不可更改类型
            # 将查询到的数据显示在表格中
            for i in range(row):
                for j in range(col):
                    temp_data = rows[i][j]  # 临时记录，不能直接插入表格
                    data = QTableWidgetItem(str(temp_data))  # 转换后可插入表格
                    self.ui.tableWidget_3.setItem(i, j, data)
                    if j == col - 1:
                        # print(rows[i][0])
                        # 传入id rows[i][0]
                        self.ui.tableWidget_3.setCellWidget(i, j + 1, self.buttonForRow(str(rows[i][0])))
        # 然后根据id查询数据库 ，看该车位的状态是否打开 如果打开了 添加弹窗
        #OK = QMessageBox.information(self, ("提示"), ("打开成功！"))

    # 车位关闭的提示
    def closeTip(self, id):

        reply = QMessageBox.question(self, '提示',
                                     "确定关闭车位锁吗吗？", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.lock_close(id)

    # 车位关闭的逻辑
    def lock_close(self, id):

        if id != '':
            # 操作数据库
            conn = pymysql.connect(host='127.0.0.1',
                                   port=3306, user='root', password='271996', db='db_car', charset='utf8')
            cursor = conn.cursor()
            sql_all = "select Sid, vehicleQuantity, name, phone, gender,  department  from staff"
            cursor.execute(sql_all)
            rows = cursor.fetchall()

            row = cursor.rowcount  # 通过查询的数据，取得记录条数，用来设置表格的行数
            col = len(rows[0])  # 取得每条记录的长度，用来设置表格的列数
            cursor.close()
            conn.close()
            # 下面的不能更改
            self.ui.tableWidget_3.setRowCount(row)  # 控件的名字保持一致，切莫想当然
            self.ui.tableWidget_3.setColumnCount(col)  # 加1，开辟一列放操作按钮
            self.ui.tableWidget_3.setSelectionBehavior(QTableWidget.SelectRows)  # 选中行
            self.ui.tableWidget_3.setEditTriggers(QTableWidget.NoEditTriggers)  # 将单元格设为不可更改类型
            # 将查询到的数据显示在表格中
            for i in range(row):
                for j in range(col):
                    temp_data = rows[i][j]  # 临时记录，不能直接插入表格
                    data = QTableWidgetItem(str(temp_data))  # 转换后可插入表格
                    self.ui.tableWidget_3.setItem(i, j, data)
                    if j == col - 1:
                        # print(rows[i][0])
                        # 传入id rows[i][0]
                        self.ui.tableWidget_3.setCellWidget(i, j + 1, self.buttonForRow(str(rows[i][0])))
        # 然后根据id查询数据库 ，看该车位的状态是否关闭 如果关闭了 添加弹窗
        # OK = QMessageBox.information(self, ("提示"), ("关闭成功！"))

    # 车位设置 用来显示车位设置的窗口
    def seatSet(self):
        self.ui.groupBox_3.show()
        self.ui.groupBox_2.hide()
        self.ui.tableWidget_2.hide()
        self.ui.tableWidget_3.hide()

    # 操作车位设置的逻辑，车位总数，临时车位数目，员工车位数目
    def seatSet1(self):
        # 获得界面输入
        seatNum = self.ui.lineEdit.text()
        inNum = self.ui.lineEdit_2.text()
        outNum = self.ui.lineEdit_3.text()


        # 操作数据库时，把下面的注释清除


        # if seatNum != '' and inNum != '' and outNum != '':
        #     # 操作数据库，设置内外车位的数
        #
        #
        #
        # else:
        #     if seatNum == '':
        #         OK = QMessageBox.information(self, ("警告"), ("""请输入车位总数！"""))
        #     if inNum == '':
        #         OK = QMessageBox.information(self, ("警告"), ("""请输入内部车数目！"""))
        #     if outNum == '':
        #         OK = QMessageBox.information(self, ("警告"), ("""请输入外部车数目！"""))

    def clearInput(self):
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit_3.clear()
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my = SeatManage()
    my.show()
    sys.exit(app.exec_())
