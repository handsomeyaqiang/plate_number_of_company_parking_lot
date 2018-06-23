from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from register_Ui import *
import sys
import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets
class reUi(QWidget):
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

        self.ui.firmpushButton_2.setStyleSheet("background-color:lightblue")
        self.ui.concelpushButton.setStyleSheet("background-color:lightblue")
        self.ui.firmpushButton_2.setFixedSize(80, 28)
        self.ui.concelpushButton.setFixedSize(80, 28)
        # 设置背景
        palette = QPalette()
        icon = QPixmap('re.jpg').scaled(800, 600)
        palette.setBrush(self.backgroundRole(), QBrush(icon))
        self.setPalette(palette)

        self.ui.namelineEdit.setFixedSize(150, 24)
        self.ui.pwdlineEdit.setFixedSize(150, 24)
        self.ui.surePwdlineEdit.setFixedSize(150, 24)
        self.ui.emalineEdit_3.setFixedSize(150, 24)
        self.ui.phonelineEdit.setFixedSize(150, 24)
        self.ui.comboBox.setFixedSize(130, 24)
        self.ui.comboBox_2.setFixedSize(130, 24)
        # 槽函数
        self.ui.firmpushButton_2.clicked.connect(self.addAdmin)
        self.ui.concelpushButton.clicked.connect(self.clearInput)

        # 用clear()方法出现未知错误
    def clearInput(self):
        self.ui.namelineEdit.setText("")
        self.ui.pwdlineEdit.setText("")
        self.ui.surePwdlineEdit.setText("")
        self.ui.phonelineEdit.setText("")
        self.ui.emalineEdit_3.setText("")

    def addAdmin(self):

        name = self.ui.namelineEdit.text()
        pwd = self.ui.pwdlineEdit.text()
        repwd = self.ui.surePwdlineEdit.text()
        phone = self.ui.phonelineEdit.text()
        identity = self.ui.comboBox_2.currentText()

        MbQuestion = self.ui.comboBox.currentText()
        MbAnswer = self.ui.emalineEdit_3.text()

        if self.ui.nv_radioButton.isChecked():
            Gender = "女"
        else:
            Gender = "男"
        print('对方水电费')
        # print('姓名：%s 密码：%s 确认密码：%s 手机号：%s  性别：%s 密保问题：%s 密保答案：%s' %
        #       (name, pwd, repwd, phone, Gender, MbQuestion, MbAnswer))

        if pwd != repwd:
            OK = QMessageBox.warning(self, ("警告"), ("""两次密码输入不一致！"""))

        if name == "":
            OK = QMessageBox.warning(self, ("警告"), ("""用户名不能为空！"""))

        if pwd == "":
            OK = QMessageBox.warning(self, ("警告"), ("密码不能为空！"))
        if repwd == "":
            OK = QMessageBox.warning(self, ("警告"), ("请确认密码！"))
        if phone == "":
            OK = QMessageBox.warning(self, ("警告"), ("请输入手机号！"))
        if MbQuestion == " ":
            OK = QMessageBox.warning(self, ("警告"), ("请选择密保问题！"))
        if MbAnswer == " ":
            OK = QMessageBox.warning(self, ("警告"), ("密保答案不能为空！"))

        if name != "" and pwd != "" and repwd != "" and phone != "" and MbQuestion != "":
            db = pymysql.connect(host="localhost", user="root", password="271996", db="db_car", charset="utf8")
            cursor = db.cursor()
            sql = "insert into admin(name, pwd, gender, phone, question, answer, identity) values " \
                  "('" + name + "', " \
                                "'" + pwd + "'," \
                                            " '" + Gender + "'," \
                                                            " '" + phone + "'," \
                                                                           " '" + MbQuestion + "', " \
                                                                                               "'" + MbAnswer + "', " \
                                                                                                                "'" + identity + "')"
            print(sql)
            cursor.execute(sql)
            db.commit()
            db.close()
            try:
                cursor.execute(sql)
                db.commit()
            except Exception as e:
                db.rollback()
            finally:

                db.close()
            OK = QMessageBox.information(self, ("警告"), ("注册的用户信息不能为空！"))
        else:
            OK = QMessageBox.warning(self, ("警告"), ("注册的用户信息不能为空！"))


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
    f = reUi()
    f.show()
    sys.exit(app.exec_())