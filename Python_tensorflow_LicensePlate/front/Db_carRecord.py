from carRecord import *
import sys
import pymysql
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QWidget
from PyQt5 .QtGui import *
from PyQt5.QtCore import *
from Python_tensorflow_LicensePlate.controller.RecordController import RecordController

class CarRecord(QWidget):
    def __init__(self):
        super(CarRecord, self).__init__()
        self.ui = Ui_carRecord()
        self.ui.setupUi(self)
        self.setWindowTitle("车辆历史记录查询")
        self.setFixedSize(self.width(), self.height())  # 实现禁止窗口最大化和禁止窗口拉伸
        palette = QPalette()
        icon = QPixmap('re.jpg').scaled(800, 600)
        palette.setBrush(self.backgroundRole(), QBrush(icon))
        self.setPalette(palette)
        # self.ui.tableWidget.horizontalHeader().setFixedWidth(45)
        self.ui.tableWidget.setColumnWidth(2, 140) # 设置列的宽度
        self.ui.tableWidget.setColumnWidth(1, 140)
        # 槽函数
        self.ui.pushButton.clicked.connect(self.Query)

    def closeEvent(self, QCloseEvent):
        reply = QMessageBox.question(self, '提示',"确定退出？", QMessageBox.Yes |QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()

    def Query(self):
        #category = self.ui.comboBox.currentText() # 查询的类别
        text = self.ui.lineEdit.text()      # 获取输入的搜索条件

        if self.ui.comboBox.currentText() == '车牌号':
            #按输入的车牌查找记录实现
            sc = RecordController()
            result = sc.findRecordByPid(text)
            if result.status == 200:
                row = len(result.data)
                col = ["platenumber", "intime", "outtime", "vehicletype"]
                self.ui.tableWidget.setRowCount(row)  # 控件的名字保持一致，切莫想当然
                self.ui.tableWidget.setColumnCount(len(col))  # 加1，开辟一列放操作按钮
                self.ui.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)  # 选中行
                self.ui.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)  # 将单元格设为不可更改类型
                for i in range(row):
                    for j in range(len(col)):
                        record = result.data[i]
                        temp_data = record.__getattribute__(col[j])  # 临时记录，不能直接插入表格
                        if temp_data=='0':
                            temp_data='内部车'
                            data = QTableWidgetItem(str(temp_data))
                            self.ui.tableWidget.setItem(i, j, data)
                        elif temp_data=='1':
                            temp_data = '外部车'
                            data = QTableWidgetItem(str(temp_data))
                            self.ui.tableWidget.setItem(i, j, data)
                        else:
                            data = QTableWidgetItem(str(temp_data))
                            self.ui.tableWidget.setItem(i, j, data)

            else:
                OK = QMessageBox.information(self, ("提示："), ("""查询失败！"""))

        if self.ui.comboBox.currentText() == '进入时间(XX-YY-ZZ AA:BB:CC)':
            #按进入时间查找车辆记录实现
            sc = RecordController()
            result = sc.findRecordByIntime(text)
            if result.status == 200:
                row = len(result.data)
                col = ["platenumber", "intime", "outtime", "vehicletype"]
                self.ui.tableWidget.setRowCount(row)  # 控件的名字保持一致，切莫想当然
                self.ui.tableWidget.setColumnCount(len(col))  # 加1，开辟一列放操作按钮
                self.ui.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)  # 选中行
                self.ui.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)  # 将单元格设为不可更改类型
                for i in range(row):
                    for j in range(len(col)-1):
                        record = result.data[i]
                        temp_data = record.__getattribute__(col[j])  # 临时记录，不能直接插入表格
                        if temp_data == '0':
                            temp_data = '内部车'
                            data = QTableWidgetItem(str(temp_data))
                            self.ui.tableWidget.setItem(i, j, data)
                        elif temp_data == '1':
                            temp_data = '外部车'
                            data = QTableWidgetItem(str(temp_data))
                            self.ui.tableWidget.setItem(i, j, data)
                        else:
                            data = QTableWidgetItem(str(temp_data))
                            self.ui.tableWidget.setItem(i, j, data)

            else:
                OK = QMessageBox.information(self, ("提示："), ("""查询失败！"""))


        if self.ui.comboBox.currentText() == '离开时间(XX-YY-ZZ AA:BB:CC)':
            #按离开时间查找车辆记录的实现
            sc = RecordController()
            result = sc.findRecordByOuttime(text)
            if result.status == 200:
                row = len(result.data)
                col = ["platenumber", "intime", "outtime", "vehicletype"]
                self.ui.tableWidget.setRowCount(row)  # 控件的名字保持一致，切莫想当然
                self.ui.tableWidget.setColumnCount(len(col))  # 加1，开辟一列放操作按钮
                self.ui.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)  # 选中行
                self.ui.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)  # 将单元格设为不可更改类型
                for i in range(row):
                    for j in range(len(col)):
                        record = result.data[i]
                        temp_data = record.__getattribute__(col[j])  # 临时记录，不能直接插入表格
                        if temp_data == '0':
                            temp_data = '内部车'
                            data = QTableWidgetItem(str(temp_data))
                            self.ui.tableWidget.setItem(i, j, data)
                        elif temp_data == '1':
                            temp_data = '外部车'
                            data = QTableWidgetItem(str(temp_data))
                            self.ui.tableWidget.setItem(i, j, data)
                        else:
                            data = QTableWidgetItem(str(temp_data))
                            self.ui.tableWidget.setItem(i, j, data)

            else:
                OK = QMessageBox.information(self, ("提示："), ("""查询失败！"""))



        if self.ui.comboBox.currentText() == '内部车':
            #查找内部车辆记录的实现
            sc = RecordController()
            result = sc.findRecordType(0)
            if result.status == 200:
                row = len(result.data)
                col = ["platenumber", "intime", "outtime", "vehicletype"]
                self.ui.tableWidget.setRowCount(row)  # 控件的名字保持一致，切莫想当然
                self.ui.tableWidget.setColumnCount(len(col))  # 加1，开辟一列放操作按钮
                self.ui.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)  # 选中行
                self.ui.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)  # 将单元格设为不可更改类型
                for i in range(row):
                    for j in range(len(col)):
                        record = result.data[i]
                        temp_data = record.__getattribute__(col[j])  # 临时记录，不能直接插入表格
                        if temp_data == '0':
                            temp_data = '内部车'
                            data = QTableWidgetItem(str(temp_data))
                            self.ui.tableWidget.setItem(i, j, data)
                        else:
                            data = QTableWidgetItem(str(temp_data))
                            self.ui.tableWidget.setItem(i, j, data)

            else:
                OK = QMessageBox.information(self, ("提示："), ("""查询失败！"""))

        if self.ui.comboBox.currentText() == '外部车':
            #查找外部车辆的记录实现
            sc = RecordController()
            result = sc.findRecordType(1)
            if result.status == 200:
                row = len(result.data)
                col = ["platenumber", "intime", "outtime", "vehicletype"]
                self.ui.tableWidget.setRowCount(row)  # 控件的名字保持一致，切莫想当然
                self.ui.tableWidget.setColumnCount(len(col))  # 加1，开辟一列放操作按钮
                self.ui.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)  # 选中行
                self.ui.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)  # 将单元格设为不可更改类型
                for i in range(row):
                    for j in range(len(col)):
                        record = result.data[i]
                        temp_data = record.__getattribute__(col[j])  # 临时记录，不能直接插入表格
                        if temp_data == '1':
                            temp_data = '外部车'
                            data = QTableWidgetItem(str(temp_data))
                            self.ui.tableWidget.setItem(i, j, data)
                        else:
                            data = QTableWidgetItem(str(temp_data))
                            self.ui.tableWidget.setItem(i, j, data)

            else:
                OK = QMessageBox.information(self, ("提示："), ("""查询失败！"""))



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my = CarRecord()
    my.show()
    sys.exit(app.exec_())
