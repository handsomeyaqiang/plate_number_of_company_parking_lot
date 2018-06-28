import sys
import pymysql
from Python_tensorflow_LicensePlate.utils.Pymysql import *
from PyQt5.QtWidgets import *
from Python_tensorflow_LicensePlate.front.FPwd import *   # 导入文件的顺序不同会导致文件类识别异常，原因未知
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from loginUI import *
from register import *
from Db_finance import *
from ComInfoManager import *
from Db_seatManager import *


from PyQt5.QtWidgets import QWidget
from PyQt5 .QtGui import *
from PyQt5.QtCore import *
#colon expected 缺少冒号
class Login(QtWidgets.QDialog):
    def __init__(self):
        super(Login, self).__init__()
        self.ui = Ui_login_Ui()
        self.ui.setupUi(self)

        # self.setMinimumSize(QtCore.QSize(400, 200))  # 控制缩放范围
        # self.setMaximumSize(QtCore.QSize(400, 200))
        self.setWindowTitle("欢迎使用停车场管理系统")
        self.setFixedSize(self.width(), self.height())
        self.ui.labelTip.hide()
        self.ui.labelTip.setText("密码或用户名不能为空!")
        # 设置label字体
        labelFont = QFont()
        labelFont.setPixelSize(15)
        # 设置动态背景
        self.gif = QMovie('bg2.gif')
        self.ui.label_2.setMovie(self.gif)
        self.gif.start()
        # 这在label属性
        self.ui.labelTip.setStyleSheet(
            "QLabel{color:red;font-size:12px;font-weight:bold;font-family:Roman times;}"
                                    )
        self.ui.userLabel.setStyleSheet("QLabel{background:white;}"
                   "QLabel{color:rgb(100,100,100,250);font-size:15px;font-weight:bold;font-family:Roman times;}"
                   "QLabel:hover{color:rgb(300,300,300,120);}")
        self.ui.pwdlabel.setStyleSheet("QLabel{background:white;}"
                   "QLabel{color:rgb(100,100,100,250);font-size:15px;font-weight:bold;font-family:Roman times;}"
                   "QLabel:hover{color:rgb(300,300,300,120);}")
        self.ui.label.setStyleSheet("QLabel{background:white;}"
                    "QLabel{color:rgb(100,100,100,250);font-size:15px;font-weight:bold;font-family:Roman times;}"
                    "QLabel:hover{color:rgb(300,300,300,120);}")
        # 登录注册添加hover选择器失败
        # self.ui.registerButton.setStyleSheet("QPushButton{color:blue}"
        #                                      "QPushButton:hover{color:red}")
        # self.ui.loginButton.setStyleSheet("QPushButton:hover{color:rgb(300,300,300,120)}")
        # self.ui.loginButton.setStyleSheet("background-color:white")
        # self.ui.registerButton.setStyleSheet("background-color:white")
        self.ui.loginButton.setStyleSheet("QPushButton{color:black}"
                                               "QPushButton:hover{color:red}"
                                               "QPushButton{background-color:lightblue}"
                                               "QPushButton{border:2px}"
                                               "QPushButton{border-radius:10px}"
                                               "QPushButton{padding:2px 4px}")
        self.ui.registerButton.setStyleSheet("QPushButton{color:black}"
                                               "QPushButton:hover{color:red}"
                                               "QPushButton{background-color:lightgreen}"
                                               "QPushButton{border:2px}"
                                               "QPushButton{border-radius:10px}"
                                               "QPushButton{padding:2px 4px}")
        # self.ui.userlineEdit.setStyleSheet(    "QLineEdit{color:black}"
        #                                      "QLineEdit{border:2px}"
        #                                      # "QLineEdit{border-radius:10px}"
        #                                      "QLineEdit{padding:2px 4px}")

        palette = QPalette()
        icon = QPixmap('bg2.gif').scaled(800, 600)
        palette.setBrush(self.backgroundRole(), QBrush(icon))
        self.setPalette(palette)

        # self.ui.userlineEdit.setStyleSheet("background-color:green") # 背景色
        # self.ui.userLabel.setStyleSheet("background-color:gray")
        self.ui.userLabel.setFont(labelFont)
        self.ui.pwdlabel.setFont(labelFont)
        self.ui.label.setFont(labelFont)
        # 设置控件尺寸
        # self.ui.userlineEdit.setFrame(False)
        # self.ui.pwdlineEdit.setFrame(False)
        self.ui.pwdlineEdit.setEchoMode(QLineEdit.Password)# 输入框设为密码模式
        self.ui.pwdlineEdit.setClearButtonEnabled(True)
        self.ui.userlineEdit.setClearButtonEnabled(True)
        self.ui.userlineEdit.setFixedWidth(190)
        self.ui.userlineEdit.setFixedHeight(30)
        self.ui.pwdlineEdit.setFixedWidth(190)
        self.ui.pwdlineEdit.setFixedHeight(30)
        self.ui.comboBox.setFixedWidth(100)
        self.ui.comboBox.setFixedHeight(28)
        self.ui.loginButton.setFixedSize(75, 28)
        self.ui.registerButton.setFixedSize(75, 28)
        # 设置快捷键

        self.ui.loginButton.setShortcut('Enter')  # shortcut key
        # 登陆的槽函数登陆按钮 最好写在init的析构函数中，避免链接多次产生异常
        self.ui.loginButton.clicked.connect(self.slotLogin)
        self.ui.registerButton.clicked.connect(self.slotRegister)
        self.ui.pushButton.clicked.connect(self.findPwd)

        name = self.ui.userlineEdit.text()
        pwd = self.ui.pwdlineEdit.text()
        identity = self.ui.comboBox.currentIndex()
        identity = str(identity)
        sql = "select * from administrater where username = '" + name + "' and password = '" + pwd + "' and identity= '"+ identity +"' "
        db = PyMySQLHelper()
        db.selectALL(sql)
        # text = self.ui.comboBox.currentText()
        # t = self.ui.comboBox.currentIndex()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Enter:
            self.slotLogin()
    def findPwd(self):
        # self.accept()
        self.u = FPwd_ui()
        self.u.show()
        # self.ui.exec()
    def slotLogin(self):
        # # 获得登录输入
        name = self.ui.userlineEdit.text()
        pwd = self.ui.pwdlineEdit.text()
        print(name)
        db = PyMySQLHelper()  # 不能直接用conn = PyMySQLHelper.getConnection
        identity = self.ui.comboBox.currentIndex() # 获取下标
        identity = str(identity)
        if name != '' and pwd != '':
            if identity == '0':
                sql = "select * from administrater where username = '" + name + "' and " \
                     "password = '" + pwd + "' and identity= '" + identity + "' "
                print(sql)

                results = db.selectALL(sql)

                if results:
                    self.ui1 = Finance()
                    # self.ui1.exec()
                    self.ui1.show()
                    self.close()
                else:
                    OK = QMessageBox.warning(self, ("警告"), ("""账号或密码错误！"""))

            if identity == '1':

                sql = "select * from administrater where username = '" + name + "' and " \
                       "password = '" + pwd + "' and identity= '" + identity + "' "
                print(sql)

                results = db.selectALL(sql)
                if results:
                    self.ui2 = InfoManage()
                    self.ui2.show()
                    self.close()
                else:
                    OK = QMessageBox.warning(self, ("警告"), ("""账号或密码错误！"""))

            if identity == '2':
                sql = "select * from administrater where username = '" + name + "' and " \
                       "password = '" + pwd + "' and identity= '" + identity + "' "
                print(sql)

                results = db.selectALL(sql)
                # print(identity)

                if results:
                    self.ui3 = SeatManage()
                    self.ui3.show()
                    self.close()
                else:
                    OK = QMessageBox.warning(self, ("警告"), ("""账号或密码错误！"""))

        else:
            if name == '':
                OK = QMessageBox.warning(self, ("警告"), ("""请输入账号！"""))
            if pwd == '':
                OK = QMessageBox.warning(self, ("警告"), ("""请输入密码！"""))

    def slotRegister(self):
        self.i = reUi()  # self.i的窗口命名不能重复
        self.i.exec_()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my = Login()
    my.show()
    sys.exit(app.exec_())