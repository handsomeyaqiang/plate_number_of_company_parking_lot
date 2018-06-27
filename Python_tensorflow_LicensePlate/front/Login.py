from PyQt5.QtWidgets import *
from Python_tensorflow_LicensePlate.front.FPwd import *   # 导入文件的顺序不同会导致文件类识别异常，原因未知
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import *
from Python_tensorflow_LicensePlate.front.loginUI import *
from Python_tensorflow_LicensePlate.front.register import *
from Python_tensorflow_LicensePlate.front.Db_finance import *
from Python_tensorflow_LicensePlate.front.ComInfoManager import *
from Python_tensorflow_LicensePlate.front.Db_seatManager import *


from PyQt5.QtWidgets import QWidget
from PyQt5 .QtGui import *
from PyQt5.QtCore import *
#colon expected 缺少冒号
class Login(QWidget):
    def __init__(self):
        super(Login, self).__init__()
        self.ui = Ui_login_Ui()
        self.ui.setupUi(self)

        # self.setMinimumSize(QtCore.QSize(400, 200))  # 控制缩放范围
        # self.setMaximumSize(QtCore.QSize(400, 200))

        # .setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)

        # MainWindow.setFixedSize(MainWindow.width(), MainWindow.height());
        self.setWindowTitle("欢迎使用停车场管理系统")
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
        self.ui.pushButton.setStyleSheet("QPushButton{color:blue}"
                                      "QPushButton:hover{color:red}"
                                      )
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

        self.ui.loginButton.setStyleSheet("background-color:white")
        self.ui.registerButton.setStyleSheet("background-color:white")
        # 设置快捷键
        self.ui.loginButton.setShortcut('Enter')  # shortcut key
        # 登陆的槽函数登陆按钮 最好写在init的析构函数中，避免链接多次产生异常
        self.ui.loginButton.clicked.connect(self.slotLogin)
        self.ui.registerButton.clicked.connect(self.slotRegister)
        self.ui.pushButton.clicked.connect(self.findPwd)

        text = self.ui.comboBox.currentText()
        t = self.ui.comboBox.currentIndex()
        print(t)
        print(text)
    def findPwd(self):
        self.ui = FPwd_ui()
        self.ui.show()
    def slotLogin(self):
        # # 获得登录输入
        name = self.ui.userlineEdit.text()
        pwd = self.ui.pwdlineEdit.text()
        # conn = pymysql.connect(host='127.0.0.1',
        #                        port=3306, user='root', password='271996', db='company_parking_system',
        #                        charset='utf8')

        db = PyMySQLHelper()  # 不能直接用conn = PyMySQLHelper.getConnection
        # conn = db.getConnection()
        # cursor = conn.cursor()
        identity = self.ui.comboBox.currentIndex() # 获取下标
        #  因为数据库登录人员的身份设计为整形，0表示财务管理，1表示信息管理，2表示停车场管理
        if name != '' and pwd != '':
            if identity == 0:
                sql = "select * from administrater where username = '" + name + "' and password = '" + pwd + "' and identity= 0 "
                print(sql)
                # cursor.execute(sql)
                # results = cursor.fetchall()
                results = db.selectALL(sql)

                if results:
                    self.ui1 = Finance()
                    self.ui1.show()
                    self.close()
                else:
                    OK = QMessageBox.warning(self, ("警告"), ("""账号或密码错误！"""))
                # cursor.close()
                # conn.close()
            if identity == 1:

                sql = "select * from administrater where username = '" + name + "' and password = '" + pwd + "' and identity= 1"
                print(sql)
                # cursor.execute(sql)
                # results = cursor.fetchall()
                results = db.selectALL(sql)
                if results:
                    self.ui2 = InfoManage()
                    self.ui2.show()
                    self.close()
                else:
                    OK = QMessageBox.warning(self, ("警告"), ("""账号或密码错误！"""))

            if identity == 2:
                sql = "select * from administrater where username = '" + name + "' and password = '" + pwd + "' and identity= 2 "
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
        # cursor.close()
        # conn.close()
    def slotRegister(self):
        # Dialog = QtWidgets.QWidget()   #定义前必须加self 不然跳转的页面闪一下就会消失
         self.ui = reUi()
         self.ui.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my = Login()
    my.show()
    sys.exit(app.exec_())