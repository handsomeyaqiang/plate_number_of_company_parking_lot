from carRecord import *
import sys
import pymysql
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QWidget
from PyQt5 .QtGui import *
from PyQt5.QtCore import *

class CarRecord(QWidget):
    def __init__(self):
        super(CarRecord, self).__init__()
        self.ui = Ui_carRecord()
        self.ui.setupUi(self)
        self.setWindowTitle("车辆历史记录查询")

        # 槽函数
        self.ui.pushButton.clicked.connect(self.Query)

    def closeEvent(self, QCloseEvent):
        reply = QMessageBox.question(self, '提示',
                                     "确定退出？", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()

    def Query(self):
        category = self.ui.comboBox.currentText() # 查询的类别
        input = self.ui.lineEdit.text()      # 输入的搜索条件
        if category != '' and input != ' ':

            # 执行数据库操作
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

            self.ui.tableWidget.setRowCount(row)  # 控件的名字保持一致，切莫想当然
            self.ui.tableWidget.setColumnCount(col + 1)  # 加1，开辟一列放操作按钮
            self.ui.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)  # 选中行
            self.ui.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)  # 将单元格设为不可更改类型

            for i in range(row):
                for j in range(col):
                    temp_data = rows[i][j]  # 临时记录，不能直接插入表格
                    data = QTableWidgetItem(str(temp_data))  # 转换后可插入表格
                    self.ui.tableWidget.setItem(i, j, data)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my = CarRecord()
    my.show()
    sys.exit(app.exec_())
