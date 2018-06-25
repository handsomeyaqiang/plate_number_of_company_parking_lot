from addSeat import *
import sys
import pymysql
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QWidget
from PyQt5 .QtGui import *
class AddSeat(QWidget):
    def __init__(self):
        super(AddSeat, self).__init__()
        self.ui = Ui_addSeat()
        self.ui.setupUi(self)

        self.setWindowTitle("添加车位")
        self.setFixedSize(self.width(), self.height())  # 实现禁止窗口最大化和禁止窗口拉伸
        self.ui.lineEdit.setClearButtonEnabled(True)
        # self.ui.lineEdit.setFrame(False)
        self.ui.comboBox.setFixedSize(135, 24)
        self.ui.lineEdit.setFixedSize(135, 24)
        self.setWindowIcon(QIcon('2.png'))

        self.ui.pushButton.setStyleSheet('text-align: center;'
                                         'width:50;'
                                         'height:30;'
                                         'background:lightyellow;')

        self.ui.pushButton.setIcon(QIcon("sure.png"))
        self.ui.pushButton.clicked.connect(self.addseat)
    def addseat(self):
        seatNum = self.ui.lineEdit.text()
        carCategory = self.ui.comboBox.currentText()
        if seatNum != '' and carCategory != '':
            # 操作数据库
            OK = QMessageBox.information(self, ("提示"), ("修改成功！"))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my = AddSeat()
    my.show()
    sys.exit(app.exec_())