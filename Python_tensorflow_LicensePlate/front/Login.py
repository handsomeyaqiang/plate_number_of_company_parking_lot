import sys
from PyQt5.QtWidgets import *
from FPwd import *   # 导入文件的顺序不同会导致文件类识别异常，原因未知
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import *
from loginUI import *
from register import *
from Admin import *

from PyQt5.QtWidgets import QWidget
from PyQt5 .QtGui import *
from PyQt5.QtCore import *
#colon expected 缺少冒号
class Login(QWidget):
    def __init__(self):
        super(Login, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # self.setMinimumSize(QtCore.QSize(400, 200))  # 控制缩放范围
        # self.setMaximumSize(QtCore.QSize(400, 200))

        # .setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)

        # MainWindow.setFixedSize(MainWindow.width(), MainWindow.height());
        self.setWindowTitle("欢迎使用停车场管理系统")
        self.ui.labelTip.hide()

        # 设置label字体
        labelFont = QFont()
        labelFont.setPixelSize(15)
        # 设置动态背景
        self.gif = QMovie('bg2.gif')
        self.ui.label_2.setMovie(self.gif)
        self.gif.start()
        # 这在label属性
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
        print(text)
    def findPwd(self):
        self.ui = FPwd_ui()
        self.ui.show()
    def slotLogin(self):
        if self.ui.userlineEdit.text() != "admin" or self.ui.pwdlineEdit.text() != "123":
            self.ui.labelTip.show()
        elif self.ui.userlineEdit.text() == " " or self.ui.pwdlineEdit.text() == " ":
            self.ui.labelTip.setText("<font color=red>密码或用户名不能为空</font>")
        else:
            self.ui = AdminUi()
            self.ui.show()
            print("登陆成功！")
    def slotRegister(self):

        # Dialog = QtWidgets.QWidget()   #定义前必须加self 不然跳转的页面闪一下就会消失
         self.ui = reUi()
         self.ui.show()
        # ui.setupUi(Dialog)
        # Dialog.show()
    def closeEvent(self, QCloseEvent):
        reply = QMessageBox.question(self, '提示',
                                     "确定退出？", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()
#
# class reUi(QWidget):
#     def __init__(self):
#         super(reUi, self).__init__()
#         self.ui = Ui_register()
#         self.ui.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my = Login()
    my.show()
    sys.exit(app.exec_())