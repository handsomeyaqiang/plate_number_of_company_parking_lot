from Python_tensorflow_LicensePlate.front.seatManage import *
from Python_tensorflow_LicensePlate.front.Db_SeatUpdate import *
from Python_tensorflow_LicensePlate.front.Db_addSeat import *
from Python_tensorflow_LicensePlate.front.Db_dayFee import *
from Python_tensorflow_LicensePlate.front.Db_nightFee import *
import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Python_tensorflow_LicensePlate.controller.ParkPlaceController import ParkPlaceController
from Python_tensorflow_LicensePlate.controller.ChargeController import ChargeController


class SeatManage(QWidget):
    def __init__(self):
        super(SeatManage, self).__init__()
        self.ui = Ui_seat()
        self.ui.setupUi(self)

        self.setWindowTitle("车位管理")
        self.setFixedSize(self.width(), self.height())  # 实现禁止窗口最大化和禁止窗口拉伸

        self.ui.tableWidget_2.hide()
        self.ui.tableWidget_3.hide()
        self.ui.groupBox_2.hide()
        self.ui.groupBox_3.hide()
        self.ui.tableWidget_5.hide()
        self.ui.tableWidget.hide()

        # 设置lineEdit的删除

        self.ui.lineEdit_3.setClearButtonEnabled(True)
        self.ui.lineEdit_2.setClearButtonEnabled(True)
        pixmap = QPixmap("seat.jpg")  # 按指定路径找到图片，注意路径必须用双引号包围，不能用单引号
        self.ui.label.setPixmap(pixmap)  # 在label上显示图片
        self.ui.label.setScaledContents(True)  # 让图片自适应label大小

        self.ui.label_2.setStyleSheet("QLabel{background:white;}"
                                      "QLabel{color:rgb(300,300,300,120);font-size:12px;font-weight:bold;font-family:宋体;}"
                                      )
        self.ui.pushButton_5.setStyleSheet('text-align: center;'
                                           'width:40;'
                                           'height:20;'
                                           'background:lightgreen;')
        self.ui.pushButton_6.setStyleSheet('text-align: center;'
                                           'width:40;'
                                           'height:20;'
                                           'background:lightgreen;')

        # 槽函数
        self.ui.pushButton.clicked.connect(self.seatSet)  # 显示车位设置窗口
        self.ui.pushButton_2.clicked.connect(self.lockState)  # 显示车位锁状态窗口
        self.ui.pushButton_3.clicked.connect(self.operateSeat)  # 操作车位锁的窗口
        self.ui.pushButton_4.clicked.connect(self.seatDetailed)  # 查看车位详情的窗口
        self.ui.pushButton_6.clicked.connect(self.seatSet1)  # 设置车位，内外车位数目，总数目
        self.ui.pushButton_5.clicked.connect(self.clearInput)  # 清空车位设置的输入
        self.ui.pushButton_8.clicked.connect(self.operateSeat2)  # 车位操作的控制逻辑函数
        self.ui.pushButton_7.clicked.connect(self.addSeat)  # 添加车位
        self.ui.pushButton_9.clicked.connect(self.dayTimeFee)
        self.ui.pushButton_10.clicked.connect(self.nightFee)

    # 添加车位
    def addSeat(self):
        self.m2 = AddSeat()
        self.m2.exec()

    def nightFee(self):
        """夜间价格显示"""
        self.ui.tableWidget_5.verticalHeader().hide()
        self.ui.tableWidget_2.hide()
        self.ui.groupBox_2.hide()
        self.ui.groupBox_3.hide()
        self.ui.tableWidget_3.hide()
        self.ui.tableWidget_5.show()
        self.ui.tableWidget.hide()
        rulecontrol = ChargeController()
        result = rulecontrol.showrule()
        if result.status == 200:
            rule = result.data
            row = 1
            col = 3
            self.ui.tableWidget_5.setRowCount(row)  # 控件的名字保持一致，切莫想当然
            self.ui.tableWidget_5.setColumnCount(col + 1)  # 加1，开辟一列放操作按钮
            self.ui.tableWidget_5.setSelectionBehavior(QTableWidget.SelectColumns)  # 选中行
            self.ui.tableWidget_5.setEditTriggers(QTableWidget.NoEditTriggers)  # 将单元格设为不可更改类型
            # table字体等布局
            for index in range(self.ui.tableWidget_5.columnCount()):
                headItem = self.ui.tableWidget_5.horizontalHeaderItem(index)
                headItem.setFont(QFont("song", 10, QFont.Bold))
                headItem.setForeground(QBrush(Qt.darkBlue))
                headItem.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
            data = QTableWidgetItem(str(rule.nightbegintime))
            # 转换后可插入表格
            self.ui.tableWidget_5.setItem(0, 0, data)
            data = QTableWidgetItem(str(rule.nightendtime))
            self.ui.tableWidget_5.setItem(0, 1, data)
            data = QTableWidgetItem(str(rule.nightprice))
            self.ui.tableWidget_5.setItem(0, 2, data)
            self.ui.tableWidget_5.setCellWidget(0, 3, self.buttonForRow3(rule))

    def dayTimeFee(self):
        """白天价格显示"""
        self.ui.tableWidget.verticalHeader().hide()
        self.ui.tableWidget_2.hide()
        self.ui.groupBox_2.hide()
        self.ui.groupBox_3.hide()
        self.ui.tableWidget_3.hide()
        self.ui.tableWidget_5.hide()
        self.ui.tableWidget.show()
        rulecontrol = ChargeController()
        result = rulecontrol.showrule()

        if result.status == 200:
            rule = result.data
            row = 1
            col = 4
            self.ui.tableWidget.setColumnWidth(3, 130)
            self.ui.tableWidget.setRowCount(row)
            self.ui.tableWidget.setColumnCount(col + 1)  # 加1，开辟一列放操作按钮
            self.ui.tableWidget.setSelectionBehavior(QTableWidget.SelectColumns)  # 选中行
            self.ui.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)  # 将单元格设为不可更改类型


            # table字体等布局
            for index in range(self.ui.tableWidget.columnCount()):
                headItem = self.ui.tableWidget.horizontalHeaderItem(index)
                headItem.setFont(QFont("song", 10, QFont.Bold))
                headItem.setForeground(QBrush(Qt.darkBlue))
                headItem.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
            data = QTableWidgetItem(str(rule.daybegintime))
            self.ui.tableWidget.setItem(0, 0, data)
            data = QTableWidgetItem(str(rule.dayendtime))
            self.ui.tableWidget.setItem(0, 1, data)
            data = QTableWidgetItem(str(rule.dayprice))
            self.ui.tableWidget.setItem(0, 2, data)
            data = QTableWidgetItem(str(rule.firsthourprice))
            self.ui.tableWidget.setItem(0, 3, data)
            self.ui.tableWidget.setCellWidget(0, 4, self.button_updatedayrule(rule))

    def buttonForRow3(self, rule):
        """修改夜间规则信息的按钮函数"""
        widget = QWidget()
        # 修改
        updateBtn = QPushButton('修改')
        updateBtn.setStyleSheet(''' text-align : center;
                                                        background-color : DarkSeaGreen;
                                                        height : 30px;
                                                        border-style: outset;
                                                        font : 13px  ''')

        updateBtn.clicked.connect(lambda: self.updatenighrulewindow(rule))
        hLayout = QHBoxLayout()
        hLayout.addWidget(updateBtn)
        # hLayout.addWidget(viewBtn)
        hLayout.setContentsMargins(5, 2, 5, 2)
        widget.setLayout(hLayout)
        return widget

    def updatenighrulewindow(self, rule):
        """显示更新夜晚规则的界面"""
        self.m2 = nightfee(rule)
        self.m2.exec()

    # 修改白天停车费用专用
    def button_updatedayrule(self, rule):
        """修改白天规则按钮"""
        widget = QWidget()
        # 修改
        updateBtn = QPushButton('修改')
        updateBtn.setStyleSheet(''' text-align : center;
                                                      background-color : DarkSeaGreen;
                                                      height : 30px;
                                                      border-style: outset;
                                                      font : 13px  ''')

        updateBtn.clicked.connect(lambda: self.updatedayrule(rule))

        hLayout = QHBoxLayout()
        hLayout.addWidget(updateBtn)
        # hLayout.addWidget(viewBtn)
        hLayout.setContentsMargins(5, 2, 5, 2)
        widget.setLayout(hLayout)
        return widget

    def updatedayrule(self, rule):
        """显示更新白天收费规则的窗口"""
        self.m2 = dayfee(rule)
        self.m2.exec()

    # 删除修改的按钮函数
    def buttonForRow(self, parkplace, findtype):
        widget = QWidget()
        # 修改
        updateBtn = QPushButton('修改')
        updateBtn.setStyleSheet(''' text-align : center;
                                                   background-color : DarkSeaGreen;
                                                    height : 30px;
                                                   border-style: outset;
                                                   font : 13px  ''')

        updateBtn.clicked.connect(lambda: self.DB_update(parkplace, findtype))

        # 删除
        deleteBtn = QPushButton('删除')
        deleteBtn.setStyleSheet(''' text-align : center;
                                             background-color : LightCoral;
                                             height : 30px;
                                             border-style: outset;
                                             font : 13px; ''')
        deleteBtn.clicked.connect(lambda: self.DeleteTip(parkplace.parkPlaceID, findtype))

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
    def DeleteTip(self, id, findtype):
        reply = QMessageBox.question(self, '提示',
                                     "确定删除吗？", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.DB_delete(id, findtype)

    # 删除车位信息  先根据id删除数据，然后查找所有刷新展示页面 里面的数据库需要规范化
    def DB_delete(self, id, findtype):
        pcontrol = ParkPlaceController()

        if id != '':
            try:
                rs1 = pcontrol.deleteparkplacebyid(id)
                if rs1.status == 200:
                    # QMessageBox.information(self, ("提示"), ("删除成功"))
                    # 刷新页面
                    if findtype == -1:
                        rs = pcontrol.findbyid(eval(id))
                        list = rs.data
                    else:
                        rs = pcontrol.findbytype(findtype)
                        list = rs.data

                    row = len(list)
                    col = ["parkPlaceID", "parkPlaceType"]
                    self.ui.tableWidget_4.setRowCount(row)  # 控件的名字保持一致，切莫想当然
                    self.ui.tableWidget_4.setColumnCount(len(col) + 1)  # 加1，开辟一列放操作按钮
                    self.ui.tableWidget_4.setSelectionBehavior(QTableWidget.SelectRows)  # 选中行
                    self.ui.tableWidget_4.setEditTriggers(QTableWidget.NoEditTriggers)  # 将单元格设为不可更改类型

                    for i in range(row):
                        for j in range(len(col)):
                            parkplace = list[i]
                            if col[j] == "parkPlaceType":
                                if parkplace.parkPlaceType == 0:
                                    temp_data = "员工车位"
                                elif parkplace.parkPlaceType == 1:
                                    temp_data = "临时车位"
                                else:
                                    temp_data = "error"
                            else:
                                temp_data = parkplace.__getattribute__(col[j])  # 临时记录，不能直接插入表格
                            data = QTableWidgetItem(str(temp_data))  # 转换后可插入表格
                            self.ui.tableWidget_4.setItem(i, j, data)
                            # 数据库因为从0开始计数，所以列数减一
                            if j == len(col) - 1:
                                # print(rows[i][0])
                                # 传入id rows[i][0]
                                self.ui.tableWidget_4.setCellWidget(i, j + 1, self.buttonForRow(parkplace, findtype))
                    OK = QMessageBox.information(self, ("提示"), ("删除成功"))
            except Exception:
                QMessageBox.information(self, ("提示"), ("发生错误！"))

    # 修改 车位设置的信息
    def DB_update(self, parkplace, findtype):
        self.m2 = Update_seat(parkplace)
        self.m2.exec()

    # 车位初始详情
    def seatDetailed(self):
        self.ui.tableWidget_2.show()
        self.ui.groupBox_2.hide()
        self.ui.groupBox_3.hide()
        self.ui.tableWidget_3.hide()
        self.ui.tableWidget_5.hide()
        self.ui.tableWidget.hide()
        # 操作数据库 需要规范化

        pcontrol = ParkPlaceController()
        innercount = pcontrol.getinuse_innerparlplacecount().data
        tempcount = pcontrol.getinuse_tempparkplacecount().data
        self.ui.tableWidget_2.setRowCount(2)  # 控件的名字保持一致，切莫想当然
        self.ui.tableWidget_2.setColumnCount(2)  # 加1，开辟一列放操作按钮
        self.ui.tableWidget_2.setSelectionBehavior(QTableWidget.SelectRows)  # 选中行
        self.ui.tableWidget_2.setEditTriggers(QTableWidget.NoEditTriggers)  # 将单元格设为不可更改类型
        # 将查询到的数据显示在表格中
        data = QTableWidgetItem(str(innercount))  # 转换后可插入表格
        self.ui.tableWidget_2.setItem(0, 0, data)
        data = QTableWidgetItem(str(tempcount))  # 转换后可插入表格
        self.ui.tableWidget_2.setItem(0, 1, data)

    # 车位操作， 查看车位的状态信息
    def operateSeat(self):
        self.ui.groupBox_2.show()
        self.ui.groupBox_3.hide()
        self.ui.tableWidget_2.hide()
        self.ui.tableWidget_3.hide()
        self.ui.tableWidget_5.hide()
        self.ui.tableWidget.hide()

    # 车位操作的控制逻辑
    def operateSeat2(self):
        # 获取界面输入
        # 如果输入框不为空则按车位号进行检索
        category = self.ui.comboBox.currentText()
        input = self.ui.lineEdit_4.text()

        list = []
        pcontrol = ParkPlaceController()
        if input != '':
            result = pcontrol.findbyid(eval(input))
            findtype = -1
            if result.status == 200:

                if (result.data is not None):
                    list.append(result.data)
                else:
                    QMessageBox.information(self, ("提示"), ("未查询到该车位！"))
                    return
            else:
                QMessageBox.information(self, ("提示"), ("查找失败！"))
        elif category == "员工车位":
            findtype = 0
            result = pcontrol.findbytype(findtype)
            if result.status == 200:
                list = result.data
            else:
                # 查找失败弹窗
                pass
        elif category == "临时车位":
            findtype = 1
            result = pcontrol.findbytype(findtype)
            if result.status == 200:
                list = result.data
            else:
                # 查找失败弹窗
                pass
        # 显示查找结果
        row = len(list)
        col = ["parkPlaceID", "parkPlaceType"]
        self.ui.tableWidget_4.setRowCount(row)  # 控件的名字保持一致，切莫想当然
        self.ui.tableWidget_4.setColumnCount(len(col) + 1)  # 加1，开辟一列放操作按钮
        self.ui.tableWidget_4.setSelectionBehavior(QTableWidget.SelectRows)  # 选中行
        self.ui.tableWidget_4.setEditTriggers(QTableWidget.NoEditTriggers)  # 将单元格设为不可更改类型

        for i in range(row):
            for j in range(len(col)):
                parkplace = list[i]
                if col[j] == "parkPlaceType":
                    if parkplace.parkPlaceType == 0:
                        temp_data = "员工车位"
                    elif parkplace.parkPlaceType == 1:
                        temp_data = "临时车位"
                    else:
                        temp_data = "error"
                else:
                    temp_data = parkplace.__getattribute__(col[j])  # 临时记录，不能直接插入表格
                data = QTableWidgetItem(str(temp_data))  # 转换后可插入表格
                self.ui.tableWidget_4.setItem(i, j, data)
                # 数据库因为从0开始计数，所以列数减一
                if j == len(col) - 1:
                    # print(rows[i][0])
                    # 传入id rows[i][0]
                    self.ui.tableWidget_4.setCellWidget(i, j + 1, self.buttonForRow(parkplace, findtype))

    # 车位锁状态  查询所有，获得车位的id后进行打开关闭操作，点击打开时，先调用是否确认打开的提示
    # 然后根据id 查询到该车位的 车位状态，根据id 修改，在查询所有，放在table上
    def lockState(self):
        self.ui.tableWidget_3.show()
        self.ui.tableWidget_2.hide()
        self.ui.groupBox_3.hide()
        self.ui.groupBox_2.hide()
        self.ui.tableWidget_5.hide()
        self.ui.tableWidget.hide()
        pcontrol = ParkPlaceController()
        result = pcontrol.showparkplaceinformation()
        if result.status == 200:
            print(result.status)
            parkplacelist = result.data
            row = len(parkplacelist)
            col = ['parkPlaceID', 'lockStatus', 'useCarNumber', 'parkPlaceType']
            self.ui.tableWidget_3.setRowCount(row)  # 控件的名字保持一致，切莫想当然
            self.ui.tableWidget_3.setColumnCount(len(col) + 1)  # 加1，开辟一列放操作按钮
            self.ui.tableWidget_3.setSelectionBehavior(QTableWidget.SelectRows)  # 选中行
            self.ui.tableWidget_3.setEditTriggers(QTableWidget.NoEditTriggers)  # 将单元格设为不可更改类型
            # 将查询到的数据显示在表格中
            for i in range(row):
                for j in range(len(col)):
                    parkplace = parkplacelist[i]
                    if col[j] == 'lockStatus':
                        if parkplace.lockStatus == 1:
                            temp_data = "打开"
                        elif parkplace.lockStatus == 0:
                            temp_data = "关闭"
                        else:
                            temp_data = "error"

                    elif col[j] == "parkPlaceType":
                        if parkplace.parkPlaceType == 0:
                            temp_data = "内部车位"
                        elif parkplace.parkPlaceType == 1:
                            temp_data = "临时车位"
                        else:
                            temp_data = "error"
                    elif col[j] == "useCarNumber":
                        if parkplace.useCarNumber is None:
                            temp_data = "空闲"
                        else:
                            temp_data = parkplace.useCarNumber
                    else:
                        temp_data = parkplace.__getattribute__(col[j])  # 临时记录，不能直接插入表格
                    data = QTableWidgetItem(str(temp_data))  # 转换后可插入表格
                    self.ui.tableWidget_3.setItem(i, j, data)
                    if j == len(col) - 1:
                        # print(rows[i][0])
                        # 传入id rows[i][0]
                        self.ui.tableWidget_3.setCellWidget(i, j + 1,
                                                            self.buttonForRow1(str(parkplace.__getattribute__(col[0]))))

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
            pcontrol = ParkPlaceController()
            pcontrol.unlock(id)
            result = pcontrol.showparkplaceinformation()
            if result.status == 200:
                print(result.status)
                parkplacelist = result.data
                row = len(parkplacelist)
                col = ['parkPlaceID', 'lockStatus', 'useCarNumber', 'parkPlaceType']
                self.ui.tableWidget_3.setRowCount(row)  # 控件的名字保持一致，切莫想当然
                self.ui.tableWidget_3.setColumnCount(len(col) + 1)  # 加1，开辟一列放操作按钮
                self.ui.tableWidget_3.setSelectionBehavior(QTableWidget.SelectRows)  # 选中行
                self.ui.tableWidget_3.setEditTriggers(QTableWidget.NoEditTriggers)  # 将单元格设为不可更改类型
                # 将查询到的数据显示在表格中
            for i in range(row):
                for j in range(len(col)):
                    parkplace = parkplacelist[i]
                    if col[j] == 'lockStatus':
                        if parkplace.lockStatus == 1:
                            temp_data = "打开"
                        elif parkplace.lockStatus == 0:
                            temp_data = "关闭"
                        else:
                            temp_data = "error"

                    elif col[j] == "parkPlaceType":
                        if parkplace.parkPlaceType == 0:
                            temp_data = "内部车位"
                        elif parkplace.parkPlaceType == 1:
                            temp_data = "临时车位"
                        else:
                            temp_data = "error"
                    elif col[j] == "useCarNumber":
                        if parkplace.useCarNumber is None:
                            temp_data = "空闲"
                        else:
                            temp_data = parkplace.useCarNumber
                    else:
                        temp_data = parkplace.__getattribute__(col[j])  # 临时记录，不能直接插入表格
                    data = QTableWidgetItem(str(temp_data))  # 转换后可插入表格
                    self.ui.tableWidget_3.setItem(i, j, data)
                    if j == len(col) - 1:
                        # print(rows[i][0])
                        # 传入id rows[i][0]
                        self.ui.tableWidget_3.setCellWidget(i, j + 1,
                                                            self.buttonForRow1(str(parkplace.__getattribute__(col[0]))))
            # 然后根据id查询数据库 ，看该车位的状态是否打开 如果打开了 添加弹窗
            # OK = QMessageBox.information(self, ("提示"), ("打开成功！"))

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
            pcontrol = ParkPlaceController()
            pcontrol.lock(id)
            result = pcontrol.showparkplaceinformation()
            if result.status == 200:
                print(result.status)
                parkplacelist = result.data
                row = len(parkplacelist)
                col = ['parkPlaceID', 'lockStatus', 'useCarNumber', 'parkPlaceType']
                self.ui.tableWidget_3.setRowCount(row)  # 控件的名字保持一致，切莫想当然
                self.ui.tableWidget_3.setColumnCount(len(col) + 1)  # 加1，开辟一列放操作按钮
                self.ui.tableWidget_3.setSelectionBehavior(QTableWidget.SelectRows)  # 选中行
                self.ui.tableWidget_3.setEditTriggers(QTableWidget.NoEditTriggers)  # 将单元格设为不可更改类型
                # 将查询到的数据显示在表格中
            for i in range(row):
                for j in range(len(col)):
                    parkplace = parkplacelist[i]
                    if col[j] == 'lockStatus':
                        if parkplace.lockStatus == 1:
                            temp_data = "打开"
                        elif parkplace.lockStatus == 0:
                            temp_data = "关闭"
                        else:
                            temp_data = "error"

                    elif col[j] == "parkPlaceType":
                        if parkplace.parkPlaceType == 0:
                            temp_data = "内部车位"
                        elif parkplace.parkPlaceType == 1:
                            temp_data = "临时车位"
                        else:
                            temp_data = "error"
                    elif col[j] == "useCarNumber":
                        if parkplace.useCarNumber is None:
                            temp_data = "空闲"
                        else:
                            temp_data = parkplace.useCarNumber
                    else:
                        temp_data = parkplace.__getattribute__(col[j])  # 临时记录，不能直接插入表格
                    data = QTableWidgetItem(str(temp_data))  # 转换后可插入表格
                    self.ui.tableWidget_3.setItem(i, j, data)
                    if j == len(col) - 1:
                        # print(rows[i][0])
                        # 传入id rows[i][0]
                        self.ui.tableWidget_3.setCellWidget(i, j + 1,
                                                            self.buttonForRow1(str(parkplace.__getattribute__(col[0]))))
        # 然后根据id查询数据库 ，看该车位的状态是否关闭 如果关闭了 添加弹窗
        # OK = QMessageBox.information(self, ("提示"), ("关闭成功！"))

    # 车位设置 用来显示车位设置的窗口
    def seatSet(self):
        self.ui.groupBox_3.show()
        self.ui.groupBox_2.hide()
        self.ui.tableWidget_2.hide()
        self.ui.tableWidget_3.hide()
        self.ui.tableWidget_5.hide()
        self.ui.tableWidget.hide()

    # 操作车位设置的逻辑，车位总数，临时车位数目，员工车位数目
    def seatSet1(self):
        # 获得界面输入
        inNum = self.ui.lineEdit_2.text()
        outNum = self.ui.lineEdit_3.text()

        # 操作数据库时，把下面的注释清除

        if inNum != '' and outNum != '':
            inNum = eval(inNum)
            outNum = eval(outNum)
            control = ParkPlaceController()
            # 操作数据库，设置内外车位的数
            control.initparklot(inNum, outNum)
        else:

            if inNum == '':
                OK = QMessageBox.information(self, ("警告"), ("""请输入内部车数目！"""))
            if outNum == '':
                OK = QMessageBox.information(self, ("警告"), ("""请输入外部车数目！"""))

    def clearInput(self):
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit_3.clear()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my = SeatManage()
    my.show()
    sys.exit(app.exec_())
