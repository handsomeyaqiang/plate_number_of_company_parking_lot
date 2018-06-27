from Python_tensorflow_LicensePlate.front.Hand_regis import *
import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QWidget
from PyQt5 .QtGui import *
class hand_Ui(QWidget):
    def __init__(self):
        super(hand_Ui, self).__init__()
        self.ui = Ui_Hand()
        self.ui.setupUi(self)

        self.setWindowTitle("手动登记页面")
        self.ui.pushButton.setFixedSize(70, 25)
        self.ui.pushButton_2.setFixedSize(70, 25)
        self.ui.lineEdit.setFixedSize(180, 26)
        self.setWindowIcon(QIcon('4.png'))

        self.ui.pushButton.setIcon(QIcon("sure.png"))
        self.ui.pushButton_2.setIcon(QIcon("cancle.png"))
        self.ui.lineEdit.setClearButtonEnabled(True)

        self.ui.label_2.setStyleSheet( "QLabel{color:rgb(100,100,100,250);font-size:13px;font-weight:bold;font-family:Roman times;}"
                                        "QLabel:hover{color:rgb(300,300,300,120);}")
        self.ui.label.setStyleSheet("QLabel{background:white;}"
                                      "QLabel{color:purple;font-size:15px;font-weight:bold;font-family:Roman times;}"
                                      )

        self.ui.pushButton.setStyleSheet("QPushButton{color:blue}"
                                         "QPushButton:hover{color:red}"
                                         )
        self.ui.pushButton_2.setStyleSheet("QPushButton{color:blue}"
                                         "QPushButton:hover{color:red}"
                                         )
        self.ui.pushButton.clicked.connect(self.register)
        self.ui.pushButton_2.clicked.connect(self.clear)

    # 手动登记函数
    # def register(self):
    #     carNum = self.ui.lineEdit()
    #     if carNum != '':
    #         # 操作数据库

    def clear(self):
        self.ui.lineEdit.clear()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my = hand_Ui()
    my.show()
    sys.exit(app.exec_())
