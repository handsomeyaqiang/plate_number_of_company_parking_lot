import sys
import pymysql
from TableAndButton import *
from PyQt5.QtWidgets import *
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

        # 控制tableWidget item文字风格
        for index in range(self.ui.tableWidget.columnCount()):
            headItem = self.ui.tableWidget.horizontalHeaderItem(index)
            headItem.setFont(QFont("song", 12, QFont.Bold))
            headItem.setForeground(QBrush(Qt.gray))
            headItem.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)


        # 控制label

        self.setStyleSheet("QLabel{background:;}"
                           "QLabel{color:white;font-size:12px;font-weight:lighter;font-family:Roman times;}"
                           "QLabel:hover{color:rgb(350,250,100,120);}")
        self.ui.groupBox.setStyleSheet("QGroupBox{color:white;font-family:Roman times}")
        self.ui.groupBox_2.setStyleSheet("QGroupBox{color:white;font-family:Roman times}")
        self.ui.nan_radioButton.setStyleSheet("QRadioButton{color:white;font-family:Roman times}")
        self.ui.nv_radioButton.setStyleSheet("QRadioButton{color:white;font-family:Roman times}")
        palette = QPalette()
        icon = QPixmap('bg2.gif').scaled(800, 600)
        palette.setBrush(self.backgroundRole(), QBrush(icon))
        self.setPalette(palette)
        # item = self.ui.horizontalHeaderItem(3)
        # item.setTextColor(QColor("red"))
        # 槽函数
        self.ui.pushButton.clicked.connect(self.DB_query) # 查找所有
        self.ui.add_pushButton.clicked.connect(self.DB_add)# 添加员工
        self.ui.pushButton_2.clicked.connect(self.QueryBySid)

    def buttonForRow(self, id):
        widget = QWidget()
        # 修改
        updateBtn = QPushButton('修改')
        updateBtn.setStyleSheet(''' text-align : center;
                                                   background-color : DarkSeaGreen;
                                                   height : 30px;
                                                   border-style: outset;
                                                   font : 13px  ''')

        updateBtn.clicked.connect(lambda: self.updateTable(id))

        # 查看
        # viewBtn = QPushButton('查看')
        # viewBtn.setStyleSheet(''' text-align : center;
        #                                    background-color : NavajoWhite;
        #                                    height : 30px;
        #                                    border-style: outset;
        #                                    font : 13px; ''')
        #
        # viewBtn.clicked.connect(lambda: self.viewTable(id))

        # 删除
        deleteBtn = QPushButton('删除')
        deleteBtn.setStyleSheet(''' text-align : center;
                                             background-color : LightCoral;
                                             height : 30px;
                                             border-style: outset;
                                             font : 13px; ''')
        deleteBtn.clicked.connect(lambda: self.DB_delete(id))

        hLayout = QHBoxLayout()
        hLayout.addWidget(updateBtn)
        # hLayout.addWidget(viewBtn)
        hLayout.addWidget(deleteBtn)
        hLayout.setContentsMargins(5, 2, 5, 2)
        widget.setLayout(hLayout)
        return widget

    # 工号查询
    def QueryBySid(self):
        #获得输入  最好提供姓名和工号都可以查询，或者模糊查询
        sid = self.ui.lineEdit_5.text()
        print(sid)
        sql = "select Sid, vehicleQuantity, name, phone, gender,  department  from staff where Sid = '"+sid+"'"
        print(sql)

        #操作数据库
        try:
            conn = pymysql.connect(host='127.0.0.1',
                                   port=3306, user='root', password='271996', db='db_car', charset='utf8')
            cursor = conn.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            row = cursor.rowcount  # 取得记录个数，获得表格的行数
            col = len(rows[0])  # 取得得每个记录的字段数，获得表格的列数
            cursor.close()
            conn.close()
            # 控制表格属性
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
                        print(rows[i][0])
                        # 传入id rows[i][0]
                        self.ui.tableWidget.setCellWidget(i, j + 1, self.buttonForRow(str(rows[i][0])))

            self.ui.statusbar.showMessage("<font color='#ff0000'>查询成功</font>")
        except Exception:

            self.ui.statusbar.showMessage("<font color='#ff0000'>查询异常</font>", 2000)



    # 添加

    def DB_add(self):

        carNum = self.ui.car_lineEdit.text()
        name = self.ui.name_lineEdit.text()
        phone = self.ui.phone_lineEdit.text()

        if self.ui.nan_radioButton.isChecked():
            gender = '男'
        else:
            gender = '女'
        department = self.ui.depart_lineEdit.text()

        if carNum == '':
            OK = QMessageBox.information(self, ("警告"), ("请输入拥有的车辆数"))
        if name == '':
            OK = QMessageBox.information(self, ("警告"), ("姓名不能为空"))
        if phone == '':
            OK = QMessageBox.information(self, ("警告"), ("手机号不能为空"))
        if department == '':
            OK = QMessageBox.information(self, ("警告"), ("部门不能为空"))

        # 开始添加员工信息的数据库操作


    # 更新
    # def updateTable(self, id):

    # 删除
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
                cursor.close()
                conn.close()
                OK = QMessageBox.information(self, ("提示"), ("删除成功"))
            except Exception:

                self.ui.statusbar.showMessage("删除异常", 2000)


    def DB_query(self):
        sql = "select Sid, vehicleQuantity, name, phone, gender,  department  from staff"
        try:
            conn = pymysql.connect(host='127.0.0.1',
                                   port=3306, user='root', password='271996', db='db_car', charset='utf8')
            cursor = conn.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            row = cursor.rowcount       # 取得记录个数，获得表格的行数
            col = len(rows[0])          # 取得得每个记录的字段数，获得表格的列数
            cursor.close()
            conn.close()

            self.ui.tableWidget.setRowCount(row)  # 控件的名字保持一致，切莫想当然
            self.ui.tableWidget.setColumnCount(col+1)  # 加1，开辟一列放操作按钮
            self.ui.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)  # 选中行
            self.ui.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)   # 将单元格设为不可更改类型

            for i in range(row):
                for j in range(col):
                    temp_data = rows[i][j]  # 临时记录，不能直接插入表格
                    data = QTableWidgetItem(str(temp_data))  # 转换后可插入表格
                    self.ui.tableWidget.setItem(i, j, data)
                    # 数据库因为从0开始计数，所以列数减一
                    if j == col-1:
                        print(rows[i][0])
                        # 传入id rows[i][0]
                        self.ui.tableWidget.setCellWidget(i, j+1, self.buttonForRow(str(rows[i][0])))


            self.ui.statusbar.showMessage("<font color='#ff0000'>查询成功</font>")
        except Exception:

            self.ui.statusbar.showMessage("<font color='#ff0000'>查询异常</font>", 2000) # 单引号包围font 井号会报错



if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    my = tableB()
    my.show()
    sys.exit(app.exec_())