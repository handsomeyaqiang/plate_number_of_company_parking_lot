from KnowTest import *
import cv2
import sys
import pymysql
from PyQt5.QtWidgets import *
from hand_Register import *
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import *
from PyQt5.QtCore import *
class Know_Ui(QWidget):
    def __init__(self):
        super(Know_Ui, self).__init__()
        self.ui = Ui_know()
        self.ui.setupUi(self)
        self.setWindowTitle("公司停车场管理")

        self.ui.label_2.setStyleSheet("QLabel{background:white;}"
                                    "QLabel{color:rgb(300,300,300,120);font-size:10px;font-weight:bold;font-family:宋体;}"
                                    )

        # 动态显示时间在label上
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.showtime)
        timer.start()

        palette = QPalette()
        icon = QPixmap('bg.jpg').scaled(800, 600)
        palette.setBrush(self.backgroundRole(), QBrush(icon))  # 添加背景图片
        self.setPalette(palette)
        # 刷新摄像头的显示时间，实时显示
        self.timer = QTimer()
        self.timer.start()
        self.timer.setInterval(100)

        self.ui.pushButton.clicked.connect(self.openimage)
        self.ui.pushButton_3.clicked.connect(self.handRegister)
        self.ui.pushButton_2.clicked.connect(self.start)
        self.ui.pushButton_4.clicked.connect(self.closeVideo)
        # 将按钮在qt设计时，先跟住窗口建立close()的槽函数，然后在将该按钮手动跟另一个窗口建立连接
        # 这样就实现了打开新窗口时，关闭主窗口的效果
        # self.ui.tableWidget.hide()
    # 显示时间
    def showtime(self):
        datetime = QDateTime.currentDateTime()
        text = datetime.toString()
        self.ui.label_2.setText("  " + text)

    def start(self, event):
        self.cap = cv2.VideoCapture(0)
        self.timer.timeout.connect(self.capPicture)

    #手动登记
    def handRegister(self):
        self.ui1 = hand_Ui()
        self.ui1.show()
    # 视频识别
    def capPicture(self):
        # self.cap = cv2.VideoCapture(0)
        if (self.cap.isOpened()):
            # get a frame
            ret, img = self.cap.read()
            height, width, bytesPerComponent = img.shape
            bytesPerLine = bytesPerComponent * width
            # 变换彩色空间顺序
            cv2.cvtColor(img, cv2.COLOR_BGR2RGB, img)
            # 转为QImage对象
            self.image = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888)
            self.ui.label.setPixmap(QPixmap.fromImage(self.image).scaled(self.ui.label.width(), self.ui.label.height()))
    # 查询停车费用
    #         for i in range(row):
    #             for j in range(col):
    #                 temp_data = rows[i][j]  # 临时记录，不能直接插入表格
    #                 data = QTableWidgetItem(str(temp_data))  # 转换后可插入表格
    #                 self.ui.tableWidget_4.setItem(i, j, data)
    # # 显示视频时，鼠标点击视频暂停
    # def mousePressEvent(self, QMouseEvent):
    #     self.cap.release()
    # 关闭视频显示
    def closeVideo(self):
        cv2.imwrite("face.jpg")
        self.cap.release()

    # 打开图片识别
    def openimage(self):
        imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片", "", "*.jpg;;*.png;;All Files(*)")
        jpg = QtGui.QPixmap(imgName).scaled(self.ui.label.width(), self.ui.label.height())
        self.ui.label.setPixmap(jpg)
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my = Know_Ui()
    my.show()
    sys.exit(app.exec_())

