from Python_tensorflow_LicensePlate.front.Hand_regis import *
import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import *
from PyQt5 .QtGui import *
from Python_tensorflow_LicensePlate.service.RecongiseService import RecongiseService
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
    def register(self):
        carNum = self.ui.lineEdit.text()
        recongiseService = RecongiseService()
        if carNum != '':
            result = recongiseService.hand_recongise(carNum)
            if result.status == 200:
                # 识别成功
                OK = QMessageBox.information(self, ("提示"), ("""登记成功，车位号：""" + str(result.data.park_place_id)))
                return
            elif result.status == 300:
                # 缴费
                reply = QMessageBox.question(self, '提示',
                                             "需交费" + str(result.data.financial.money) + "元", QMessageBox.Yes |
                                             QMessageBox.No, QMessageBox.No)
                if reply == QMessageBox.Yes:
                    print("缴费")
                    # 调用缴费业务
                    recongise = RecongiseService()
                    result = recongise.charge(result.data)
                    if result.status == 200:
                        # 缴费成功
                        # 识别成功
                        OK = QMessageBox.information(self, ("警告"), ("""缴费成功"""))
                        return
                    else:
                        # 缴费失败
                        OK = QMessageBox.information(self, ("警告"), ("""缴费异常"""))
                        return
                else:
                     print("缴费取消")
            else:
                # 识别失败
                OK = QMessageBox.information(self, ("警告"), ("""识别失败"""))
                return
        else:
            OK = QMessageBox.information(self, ("警告"), ("""车牌不能为空"""))
            return

    def clear(self):
        self.ui.lineEdit.clear()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my = hand_Ui()
    my.show()
    sys.exit(app.exec_())
