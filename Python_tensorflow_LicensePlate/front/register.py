from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Python_tensorflow_LicensePlate.utils.Pymysql import *
from PyQt5.QtCore import *
from Python_tensorflow_LicensePlate.front.register_Ui import *
import sys
from Login import *
import pymysql

from PyQt5 import QtCore, QtGui, QtWidgets
class reUi(QtWidgets.QDialog):
    def __init__(self):
        super(reUi, self).__init__()
        self.ui = Ui_register_2()
        self.ui.setupUi(self)            # 导入的界面投放到新的类上


        self.setWindowTitle('用户注册')
        labelFont = QFont()
        labelFont.setPixelSize(14)
        self.ui.label_2.setFont(QFont("黑体"))

        self.ui.label_2.setFont(labelFont)
        self.ui.label_3.setFont(labelFont)
        self.ui.firmpushButton_2.setStyleSheet("QPushButton{color:blue}"
                                         "QPushButton:hover{color:red}"
                                        "QPushButton{background-color:lightblue}"
                                        "QPushButton{border:2px}"
                                        "QPushButton{border-radius:10px}")
        self.ui.concelpushButton.setStyleSheet("QPushButton{color:blue}"
                                               "QPushButton:hover{color:red}"
                                               "QPushButton{background-color:lightblue}"
                                               "QPushButton{border:2px}"
                                               "QPushButton{border-radius:10px}"
                                               "QPushButton{padding:2px 4px}")
        # self.ui.concelpushButton.setStyleSheet("border:2px groove gray;border-radius:10px;padding:2px 4px;");
        # self.ui.firmpushButton_2.setStyleSheet("background-color:lightblue"
        self.ui.firmpushButton_2.setFixedSize(80, 28)
        self.ui.concelpushButton.setFixedSize(80, 28)
        # 设置背景
        palette = QPalette()
        icon = QPixmap('timg.jpg').scaled(800, 600)
        palette.setBrush(self.backgroundRole(), QBrush(icon))
        self.setPalette(palette)

        self.ui.namelineEdit.setFixedSize(150, 24)
        self.ui.pwdlineEdit.setFixedSize(150, 24)
        self.ui.surePwdlineEdit.setFixedSize(150, 24)
        self.ui.emalineEdit_3.setFixedSize(150, 24)
        self.ui.phonelineEdit.setFixedSize(150, 24)
        self.ui.comboBox.setFixedSize(130, 24)
        self.ui.comboBox_2.setFixedSize(130, 24)

        self.ui.namelineEdit.setFocus()

        self.ui.pwdlineEdit.setEchoMode(QLineEdit.Password)
        self.ui.surePwdlineEdit.setEchoMode(QLineEdit.Password)
        self.ui.emalineEdit_3.setEchoMode(QLineEdit.Password)
        self.ui.namelineEdit.setClearButtonEnabled(True)
        self.ui.phonelineEdit.setClearButtonEnabled(True)
        self.ui.emalineEdit_3.setClearButtonEnabled(True)
        self.ui.surePwdlineEdit.setClearButtonEnabled(True)
        self.ui.pwdlineEdit.setClearButtonEnabled(True)
        # 槽函数
        self.ui.firmpushButton_2.clicked.connect(self.addAdmin)
        self.ui.concelpushButton.clicked.connect(self.clearInput)

        # self.setModal(False)#设置为非模态
    def clearInput(self):
        self.ui.namelineEdit.setText("")
        self.ui.pwdlineEdit.setText("")
        self.ui.surePwdlineEdit.setText("")
        self.ui.phonelineEdit.setText("")
        self.ui.emalineEdit_3.setText("")
    # def login(self, name, pwd):
    #     self.ui1 = Login()
    #     self.ui1.userlineEdit.setText(name)
    #     self.ui1.pwdlineEdit.setText(pwd)
    def addAdmin(self):

        name = self.ui.namelineEdit.text()
        pwd = self.ui.pwdlineEdit.text()
        repwd = self.ui.surePwdlineEdit.text()
        phone = self.ui.phonelineEdit.text()
        identity = self.ui.comboBox_2.currentText()
        MbQuestion = self.ui.comboBox.currentText()
        MbAnswer = self.ui.emalineEdit_3.text()

        if self.ui.nv_radioButton.isChecked():
            Gender = 0
        else:
            Gender = 1
        if identity == '财务管理员':
            identity = 0
        elif identity == '信息管理员':
            identity = 1
        else:
            identity = 2
        Gender = str(Gender) #Expected type 'int', got 'str' instead的错误 把性别和identity转化成str 用str()
        identity = str(identity)
        # print('姓名：%s 密码：%s 确认密码：%s 手机号：%s  性别：%s 密保问题：%s 密保答案：%s' %
        #       (name, pwd, repwd, phone, Gender, MbQuestion, MbAnswer))
        db = PyMySQLHelper()
        if name != "" and pwd != "" and repwd != "" and phone != "" and MbQuestion != "" and Gender != ''and MbAnswer != "":
            if pwd != repwd:
                OK = QMessageBox.warning(self, ("警告"), ("""两次密码输入不一致！"""))
            else:
                sql_name = "select * from administrater WHERE  username = '" + name + "'"
                # cursor.execute(sql_name)
                # results = cursor.fetchall()
                results = db.selectALL(sql_name)
                if results:
                    OK = QMessageBox.warning(self, ("警告"), ("该用户名已注册！"))
                else:
                    sql = "insert into administrater(username, password, gender, phone, question,answer, identity) values " \
                          "('" + name + "', " \
                                        "'" + pwd + "'," \
                                                    " '" + Gender + "'," \
                                                                    " '" + phone + "'," \
                                                                                   " '" + MbQuestion + "', " \
                                                                                                       "'" + MbAnswer + "', " \
                                                                                                                        "'" + identity + "')"
                    print(sql)
                    db.update(sql)
                    OK = QMessageBox.information(self, ("提示"), ("注册成功！"))
                    self.close()
                    # self.quit1()



        else:
            if name == "" and pwd == "" and repwd == "" and phone == "" and MbAnswer == '':
                OK = QMessageBox.warning(self, ("警告"), ("请输入用户信息！"))
            else:  # Gender有默认值，待解觉
                if name == "":
                    OK = QMessageBox.warning(self, ("警告"), ("""用户名不能为空！"""))
                if Gender == "":
                    OK = QMessageBox.warning(self, ("警告"), ("""用户名不能为空！"""))
                if pwd == "":
                    OK = QMessageBox.warning(self, ("警告"), ("密码不能为空！"))
                if repwd == "":
                    OK = QMessageBox.warning(self, ("警告"), ("请确认密码！"))
                if phone == "":
                    OK = QMessageBox.warning(self, ("警告"), ("请输入手机号！"))
                if MbAnswer == " ":
                    OK = QMessageBox.warning(self, ("警告"), ("密保答案不能为空！"))


    # def closeEvent(self, QCloseEvent):
    #     reply = QMessageBox.question(self, '提示',
    #                                  "确定退出？", QMessageBox.Yes |
    #                                  QMessageBox.No, QMessageBox.No)
    #     if reply == QMessageBox.Yes:
    #         QCloseEvent.accept()
    #     else:
    #         QCloseEvent.ignore()

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    f = reUi()
    f.show()
    sys.exit(app.exec_())