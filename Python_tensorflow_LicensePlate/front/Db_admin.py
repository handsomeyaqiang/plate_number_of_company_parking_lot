import sys
import pymysql
from admin_Ui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5 .QtGui import *
from PyQt5.QtCore import *
from Python_tensorflow_LicensePlate.utils.Pymysql import *

class Admin(QWidget):
    def __init__(self):
        super(Admin, self).__init__()
        self.ui = Ui_adin()
        self.ui.setupUi(self)

        self.setWindowTitle("超级管理员")
        self.setWindowIcon(QIcon('ad1.png'))
        self.setFixedSize(self.width(), self.height())
        # self.ui.tableWidget.hide()
        self.ui.label.setStyleSheet(
            "QLabel{color:hotpink;font-size:17px;font-weight:bold;font-family:宋体;}"
        )
        # self.ui.pushButton.setStyleSheet("QPushButton{color:black}"
        #                                   "QPushButton:hover{color:red}"
        #                                   "QPushButton{background-color:yellow}"
        #                                   "QPushButton{border:2px}"
        #                                   "QPushButton{border-radius:10px}"
        #                                   "QPushButton{padding:2px 4px}")

        self.ui.pushButton.clicked.connect(self.chakan)
    def buttonForRow(self, id):
        widget = QWidget()
        # # 修改
        # updateBtn = QPushButton('修改')
        # updateBtn.setStyleSheet(''' text-align : center;
        #                                            background-color : DarkSeaGreen;
        #                                            height : 30px;
        #                                            border-style: outset;
        #                                            font : 13px  ''')
        #
        # updateBtn.clicked.connect(lambda: self.DB_update(id))


        # 删除 LightCoral;
        deleteBtn = QPushButton('删除')
        deleteBtn.setStyleSheet(''' text-align : center;
                                             background-color : lightblue;
                                             height : 30px;
                                             border-style: outset;
                                             font : 13px;
                                             border:2px;
                                             border-radius:10px;
                                             padding:2px 4px;
                                              
                                              ''')
        deleteBtn.clicked.connect(lambda: self.DeleteTip(id))

        hLayout = QHBoxLayout()
        #
        # hLayout.addWidget(viewBtn)
        hLayout.addWidget(deleteBtn)
        hLayout.setContentsMargins(5, 2, 5, 2)
        widget.setLayout(hLayout)
        return widget
    def DeleteTip(self, id):
        print(id)
        reply = QMessageBox.question(self, '提示',
                                     "确定删除该用户吗？", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.DB_delete(id)

   # 根据用户名删除
    def DB_delete(self, id):
        sql_del = "delete from administrater where username = '" + id + "'"
        print(sql_del)
        db = PyMySQLHelper()
        count = db.update(sql_del)
        print(count)
        self.chakan()
    def chakan(self):
        # conn = pymysql.connect(host='127.0.0.1',
        #                        port=3306, user='root', password='root', db='company_parking_system', charset='utf8')
        # cursor = conn.cursor()
        # cursor.execute(sql)
        # rows = cursor.fetchall()
        # row = cursor.rowcount  # 取得记录个数，获得表格的行数
        #
        # cursor.close()
        # conn.close()
        self.ui.tableWidget.verticalHeader().hide()
        self.ui.tableWidget.setColumnCount(7)
        self.ui.tableWidget.setRowCount(4)
        self.ui.tableWidget.setHorizontalHeaderLabels(['用户名', '性别', '电话', '密保问题', '密保答案', '身份', '操作'])

        sql_all = 'select username, gender,phone, question, answer, identity from administrater'
        # row = 5 自定义条数
        db = PyMySQLHelper()

        rows, row = db.selectALL1(sql_all)

        # 取得得每个记录的字段数，获得表格的列数
        col = ["username", "gender", "phone", "question", "answer", "identity"]
        self.ui.tableWidget.setRowCount(row)  # 控件的名字保持一致，切莫想当然
        self.ui.tableWidget.setColumnCount(len(col) + 1)  # 加1，开辟一列放操作按钮
        self.ui.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)  # 选中行
        self.ui.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)  # 将单元格设为不可更改类型
        for index in range(self.ui.tableWidget.columnCount()):
            headItem = self.ui.tableWidget.horizontalHeaderItem(index)
            headItem.setFont(QFont("song", 10, QFont.Bold))
            headItem.setForeground(QBrush(Qt.darkBlue))
            headItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        for i in range(row):
            for j in range(len(col)):
                data = rows[i][j]  # 临时记录，不能直接插入表格
                test = col[j]  # 不赋值性别出现乱码
                if test == 'gender':
                    if data == 0:
                        data = '女'
                        data = QTableWidgetItem(str(data))
                        self.ui.tableWidget.setItem(i, j, data)
                        self.ui.tableWidget.item(i, j).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    else:
                        data = '男'
                        data = QTableWidgetItem(str(data))
                        self.ui.tableWidget.setItem(i, j, data)
                        self.ui.tableWidget.item(i, j).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                elif test == "identity":
                    if data == 0:
                        data = '财务管理员'
                        data = QTableWidgetItem(str(data))
                        self.ui.tableWidget.setItem(i, j, data)
                        self.ui.tableWidget.item(i, j).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    elif data == 1:
                        data = '信息管理员'
                        data = QTableWidgetItem(str(data))
                        self.ui.tableWidget.setItem(i, j, data)
                        self.ui.tableWidget.item(i, j).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    else:
                        data = '停车场管理员'
                        data = QTableWidgetItem(str(data))
                        self.ui.tableWidget.setItem(i, j, data)
                        self.ui.tableWidget.item(i, j).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                else:
                    data = QTableWidgetItem(str(data))
                    self.ui.tableWidget.setItem(i, j, data)
                    self.ui.tableWidget.item(i, j).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                if j == len(col) - 1:
                    self.ui.tableWidget.setCellWidget(i, j + 1, self.buttonForRow(rows[i][0]))
                    print(rows[i][0])

                    # print(rows[i][0])



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my = Admin()
    my.show()
    sys.exit(app.exec_())