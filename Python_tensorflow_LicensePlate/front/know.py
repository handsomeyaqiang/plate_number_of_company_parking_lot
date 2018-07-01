import cv2
from PyQt5.QtWidgets import *
from Python_tensorflow_LicensePlate.front.hand_Register import *
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Python_tensorflow_LicensePlate.train.plateutils.getplatenumber import getplate
from Python_tensorflow_LicensePlate.train.plateutils.platenumbersplit import splitPlate
from Python_tensorflow_LicensePlate.service.RecongiseService import RecongiseService
from Python_tensorflow_LicensePlate.front.KnowTest import Ui_know
from Python_tensorflow_LicensePlate.utils import formattime
from Python_tensorflow_LicensePlate.front.hand_Register import hand_Ui
class Know_Ui(QWidget):
    def __init__(self):
        super(Know_Ui, self).__init__()
        self.ui = Ui_know()
        self.ui.setupUi(self)
        self.setWindowTitle("公司停车场管理")
        self.DIR_RECEIVED_IMAGES = "../resources/images/receivedplateimages"
        self.DIR_MIDEL_IMAGES = "../resources/images/midledimages"
        self.DIR_SPLIT_IMAGES = "../resources/images/splitplateimages"
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
        self.timer.setInterval(2300)

        self.ui.pushButton.clicked.connect(self.openimage)
        self.ui.pushButton_3.clicked.connect(self.handRegister)
        self.ui.pushButton_2.clicked.connect(self.start)
        self.ui.pushButton_4.clicked.connect(self.closeVideo)
        # 将按钮在qt设计时，先跟住窗口建立close()的槽函数，然后在将该按钮手动跟另一个窗口建立连接
        # 这样就实现了打开新窗口时，关闭主窗口的效果
        # self.ui.tableWidget.hide()
        data = QTableWidgetItem(str(1))  # 转换后可插入表格
        self.ui.tableWidget.setItem(0, 0, data)

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
            col = ["plate_num", "intime", "outtime", "vehicle_type", "park_place_id", "money"]
            self.ui.tableWidget.setRowCount(1)
            self.ui.tableWidget.setColumnCount(len(col))
            self.ui.tableWidget.verticalHeader().hide()
            result = self.judg_recongise(img)
            if result.status == 200:
                # 识别成功
                for i in range(len(col)):
                    recongiseResult = result.data
                    if i == 2:
                        temp_data = ""
                    elif i == 3:
                        temp_data = recongiseResult.vehicle_type
                        if temp_data == 0:
                            temp_data = "内部车"
                        else:
                            temp_data = "外部车"
                    elif i == 5:
                        temp_data = ""
                    else:
                        temp_data = recongiseResult.__getattribute__(col[i])  # 临时记录，不能直接插入表格
                    data = QTableWidgetItem(str(temp_data))  # 转换后可插入表格
                    self.ui.tableWidget.setItem(0, i, data)

            elif result.status == 300:
                # 缴费
                reply = QMessageBox.question(self, '提示',
                                             "需交费" + str(result.data.financial.money) + "元", QMessageBox.Yes |
                                             QMessageBox.No, QMessageBox.No)
                if reply == QMessageBox.Yes:
                    # 调用缴费业务
                    recongise = RecongiseService()
                    result = recongise.charge(result.data)
                    if result.status == 200:
                        # 缴费成功
                        OK = QMessageBox.information(self, ("提示"), ("""缴费成功"""))
                        # 识别成功
                        for i in range(len(col)):
                            recongiseResult = result.data
                            if i == 2:
                                temp_data = formattime.calc_time(recongiseResult.__getattribute__("outtime"),
                                                                 recongiseResult.__getattribute__("intime"))
                            elif i == 3:
                                temp_data = recongiseResult.vehicle_type
                                if temp_data == 0:
                                    temp_data = "内部车"
                                else:
                                    temp_data = "外部车"
                            else:
                                temp_data = recongiseResult.__getattribute__(col[i])  # 临时记录，不能直接插入表格
                            data = QTableWidgetItem(str(temp_data))  # 转换后可插入表格
                            self.ui.tableWidget.setItem(0, i, data)
                    else:
                        # 缴费失败
                        OK = QMessageBox.information(self, ("警告"), ("""缴费异常"""))
                        return
                else:
                    # print("缴费取消")
                    OK = QMessageBox.information(self, ("警告"), ("""已取消缴费"""))
                    return
            else:
                # 识别失败 过滤
                #OK = QMessageBox.information(self, ("警告"), (str(result.msg)))
                return

    # 关闭视频显示
    def closeVideo(self):
        self.cap.release()

    # 识别
    def judg_recongise(self, img):
        cv2.imwrite(self.DIR_RECEIVED_IMAGES + "/plate.jpg", img)
        # 调用车牌获取
        g = getplate()
        result = g.get_plateNum()
        if result.status != 200:
            return result
        # 调用车牌字符切割
        s = splitPlate()
        result = s.split_plate()
        if result.status != 200:
            return result
        # 调用识别业务
        recongise = RecongiseService()
        return recongise.judg_recongise()

    # 打开图片识别
    def openimage(self):
        imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片", "", "*.jpg;;*.png;;All Files(*)")
        if imgName == None or imgName == "":
            return
        jpg = QtGui.QPixmap(imgName).scaled(self.ui.label.width(), self.ui.label.height())
        self.ui.label.setPixmap(jpg)
        col = ["plate_num", "intime", "outtime", "vehicle_type", "park_place_id", "money"]
        self.ui.tableWidget.setRowCount(1)
        self.ui.tableWidget.setColumnCount(len(col))
        self.ui.tableWidget.verticalHeader().hide()
        img = cv2.imread(imgName)
        result = self.judg_recongise(img)
        if result.status == 200:
            # 识别成功
            for i in range(len(col)):
                recongiseResult = result.data
                if i == 2:
                    temp_data = ""
                elif i == 3:
                    temp_data = recongiseResult.vehicle_type
                    if temp_data == 0:
                        temp_data = "内部车"
                    else:
                         temp_data = "外部车"
                elif i == 5:
                    temp_data = ""
                else:
                    temp_data = recongiseResult.__getattribute__(col[i])  # 临时记录，不能直接插入表格
                data = QTableWidgetItem(str(temp_data))  # 转换后可插入表格
                self.ui.tableWidget.setItem(0, i, data)

        elif result.status == 300:
            # 缴费
            reply = QMessageBox.question(self, '提示',
                                         "需交费"+str(result.data.financial.money)+"元", QMessageBox.Yes |
                                         QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                # 调用缴费业务
                recongise = RecongiseService()
                result = recongise.charge(result.data)
                if result.status == 200:
                    # 缴费成功
                    OK = QMessageBox.information(self, ("提示"), ("""缴费成功"""))
                    # 识别成功
                    for i in range(len(col)):
                        recongiseResult = result.data
                        if i == 2:
                            temp_data = formattime.calc_time(recongiseResult.__getattribute__("outtime"),
                                                             recongiseResult.__getattribute__("intime"))
                        elif i == 3:
                            temp_data = recongiseResult.vehicle_type
                            if temp_data == 0:
                                temp_data = "内部车"
                            else:
                                temp_data = "外部车"
                        else:
                            temp_data = recongiseResult.__getattribute__(col[i])  # 临时记录，不能直接插入表格
                        data = QTableWidgetItem(str(temp_data))  # 转换后可插入表格
                        self.ui.tableWidget.setItem(0, i, data)
                else:
                    # 缴费失败
                    OK = QMessageBox.information(self, ("警告"), ("""缴费异常"""))
                    return
            else:
                #print("缴费取消")
                OK = QMessageBox.information(self, ("警告"), ("""已取消缴费"""))
                return
        else:
            # 识别失败
            OK = QMessageBox.information(self, ("警告"), (str(result.msg)))
            return


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my = Know_Ui()
    my.show()
    sys.exit(app.exec_())

