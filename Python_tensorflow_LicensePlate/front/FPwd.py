from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Python_tensorflow_LicensePlate.utils.Pymysql import *
from Python_tensorflow_LicensePlate.front.findPwd import *
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
class FPwd_ui(QWidget):
    def __init__(self):
        super(FPwd_ui, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.label_3.setFixedSize(650, 35)
        self.ui.label_3.setStyleSheet("QLabel{background:white;}"
                                        "QLabel{color:rgb(100,100,100,250);font-size:15px;font-weight:bold;font-family:Roman times;}"
                                        "QLabel:hover{color:rgb(300,300,300,120);}")
        self.setWindowTitle('找回密码')
        # self.setWindowFlags(Qt.WindowMinimizeButtonHint)
        self.setFixedSize(self.width(), self.height()) # 实现禁止窗口最大化和禁止窗口拉伸
        palette = QPalette()
        icon = QPixmap('fp.jpg').scaled(700, 500)
        palette.setBrush(self.backgroundRole(), QBrush(icon))
        self.setPalette(palette)
        # 调整控件
        self.ui.Name_lineEdit.setClearButtonEnabled(True)
        self.ui.lineEdit_2.setClearButtonEnabled(True)
        self.ui.lineEdit.setClearButtonEnabled(True)
        self.ui.MbAnswerlineEdit.setClearButtonEnabled(True)

        self.ui.lineEdit.setEchoMode(QLineEdit.Password)
        self.ui.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.ui.MbAnswerlineEdit.setEchoMode(QLineEdit.Password)

        self.ui.Name_lineEdit.setFixedSize(150, 23)
        self.ui.lineEdit.setFixedSize(150, 23)
        # self.ui.NewPwd_lineEdit.setFixedWidth(150)
        self.ui.lineEdit_2.setFixedSize(150, 23)
        self.ui.MbAnswerlineEdit.setFixedSize(150, 23)
        self.ui.comboBox_2.setFixedSize(150, 23),
        self.ui.comboBox.setFixedSize(100, 23)
        self.ui.pushButton_2.setFixedSize(65, 24)
        self.ui.pushButton_4.setFixedSize(65, 24)
        self.ui.pushButton_3.setFixedSize(65, 24)
        # self.ui.pushButton_2.setStyleSheet("background-color:lightbule")

        self.ui.pushButton_4.setStyleSheet("QPushButton{color:blue}"
                                         "QPushButton:hover{color:red}"
                                         )

        self.ui.pushButton_2.setStyleSheet("QPushButton{color:blue}"
                                         "QPushButton:hover{color:red}"
                                         )
        self.ui.pushButton_3.setStyleSheet("QPushButton{color:blue}"
                                           "QPushButton:hover{color:red}"
                                           )
        # time.sleep(3)# 主程序3庙后显示输出
        # self.ui.textBrowser.clear()
        self.ui.pushButton_3.hide()
        # 设置新密码的控件隐藏
        self.ui.lineEdit_2.hide()
        self.ui.lineEdit.hide()
        self.ui.label_5.hide()
        self.ui.label_6.hide()
        # 槽函数
        self.ui.pushButton_2.clicked.connect(self.clearInput)
        self.ui.pushButton_4.clicked.connect(self.getPwd)
        self.ui.pushButton_3.clicked.connect(self.newPwd)
        self.ui.comboBox_2.currentIndexChanged.connect(self.currentIndexChanged)# comboBox的槽函数事件


    # def sleep(self):
    #
    #     t = Timer(4.0, self.sleep)
    #     t.start()  # 开始执行线程，但是不会打印"hello, world"
    #     self.ui.textBrowser.setText("")

    def currentIndexChanged(self):
        int = self.ui.comboBox_2.currentIndex()
        if int == 1:
            self.ui.lineEdit.show()
            self.ui.lineEdit_2.show()
            self.ui.label_5.show()
            self.ui.label_6.show()
            self.ui.pushButton_3.show()
            self.ui.pushButton_4.hide()

        else:
            self.ui.lineEdit_2.hide()
            self.ui.lineEdit.hide()
            self.ui.label_5.hide()
            self.ui.label_6.hide()
            self.ui.pushButton_4.show()
            self.ui.pushButton_3.hide()


    def newPwd(self):
        name = self.ui.Name_lineEdit.text()
        question = self.ui.comboBox.currentText()
        answer = self.ui.MbAnswerlineEdit.text()
        pwd = self.ui.lineEdit_2.text()
        SurePwd = self.ui.lineEdit.text()
        # conn = pymysql.connect(host='127.0.0.1',
        #                        port=3306, user='root', password='271996',
        #                        db='company_parking_system', charset='utf8')
        # cursor = conn.cursor()
        db = PyMySQLHelper()

        # 更新密码时，先判断根据账号，密保问题和密保答案能否查询成功，如果查询成功，将密码更新
        if name != '' and answer != '' and pwd != '' and SurePwd != '':
            if pwd == SurePwd:
                sql = "select * from administrater where username = '" + name + "' and question = '" + question + "' and answer='" + answer + "'"
                print(sql)
                # cursor.execute(sql)
                # results = cursor.fetchall()
                results = db.selectALL(sql)
                if results:
                    # 插入新密码
                    sql_up = "update administrater set password = '" + pwd + "'where username = '" + name + "' " \
                                                                                                            "and question = '" + question + "' and answer='" + answer + "'"
                    # cursor.execute(sql_up)
                    # conn.commit()\
                    db.update(sql)
                    self.ui.textBrowser.setText('密码更新成功！')
                else:
                    OK = QMessageBox.warning(self, ("警告"), ("""密保问题或密保答案错误！"""))
                # cursor.close()
                # conn.close()
            else:
                OK = QMessageBox.warning(self, ("警告"), ("""两次密码输入不一致！"""))
        else:
            if name == '':
                OK = QMessageBox.warning(self, ("警告"), ("""账号不能为空！"""))
            if answer == '':
                OK = QMessageBox.warning(self, ("警告"), ("""密保答案不能为空！"""))
            if pwd == '':
                OK = QMessageBox.warning(self, ("警告"), ("""密码不能为空！"""))
            if SurePwd == '':
                OK = QMessageBox.warning(self, ("警告"), ("""确认密码不能为空！"""))

    def getPwd(self):
        # 获取界面输入
        name = self.ui.Name_lineEdit.text()
        question = self.ui.comboBox.currentText()
        answer = self.ui.MbAnswerlineEdit.text()
        pwd = self.ui.lineEdit_2.text()
        SurePwd = self.ui.lineEdit.text()
        # 这种调用外部数据库链接的方式，没有直接在本函数内建立链接的操作响应迅速
        # conn = pymysql.connect(host='127.0.0.1',
        #                        port=3306, user='root', password='271996',
        #                        db='company_parking_system', charset='utf8')
        # cursor = conn.cursor()
        db = PyMySQLHelper()
        if name != ' ' and answer != '' and pwd == '' and SurePwd == '':

            sql = "select * from administrater where " \
                  "username = '" + name +"' and question = '"+ question +"' and answer='"+ answer +"'"
            print(sql)
            # cursor.execute(sql)
            # results = cursor.fetchall()
            results = db.selectALL(sql)
            if results:
                for row in results:
                    print(row[2])
                    self.ui.textBrowser.setText('你找回的密码是：' + row[2])# 点击按钮只显示一次文本
                    # self.ui.textBrowser.append('你找回的密码是：' + row[2])# append只要点击按钮会不断的输出
                # self.ui.textBrowser.clear()
                # cursor.close()
                # conn.close()
            else:
                OK = QMessageBox.warning(self, ("警告"), ("""密保问题或密保答案错误！"""))
        else:
            if name == '':
                OK = QMessageBox.warning(self, ("警告"), ("""账号不能为空！"""))

            if answer == '':
                OK = QMessageBox.warning(self, ("警告"), ("""密保答案不能为空！"""))

        # 如果账号密保问题和密保答案不等于空，密码和确认密码等于空，执行找回密码功能
        #如果账号密保问题密保答案密码和确认密码都不等于空，执行重新设置密码功能 用self.ui.textBrowser.append()显示密码

    def clearInput(self):
        self.ui.Name_lineEdit.setText("")
        self.ui.MbAnswerlineEdit.setText("")
        self.ui.lineEdit_2.setText("")
        self.ui.lineEdit.setText("")

    def closeEvent(self, QCloseEvent):
        reply = QMessageBox.question(self, '提示',
                                     "确定退出？", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()
if __name__=="__main__":

    app = QtWidgets.QApplication(sys.argv)
    f = FPwd_ui()
    f.show()
    sys.exit(app.exec_())
