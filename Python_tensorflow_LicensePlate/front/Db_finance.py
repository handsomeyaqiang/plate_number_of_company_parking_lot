from Python_tensorflow_LicensePlate.front.finance_Ui import *
from Python_tensorflow_LicensePlate.front.Login import *
from Python_tensorflow_LicensePlate.controller.FinancialController import FinancialController
import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import matplotlib.pyplot as plt
from pylab import *
import matplotlib
# matplotlib.use("Qt5Agg")  # 声明使用QT5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class Figure_Canvas(
    FigureCanvas):  # 通过继承FigureCanvas类，使得该类既是一个PyQt5的Qwidget，又是一个matplotlib的FigureCanvas，这是连接pyqt5与matplot                                          lib的关键
    # width和height控制画布的大小,画布太小容易出现数据显示不全的情况
    def __init__(self, parent=None, width=5, height=2, dpi=100):
        fig = Figure(figsize=(width, height),
                     dpi=100)  # 创建一个Figure，注意：该Figure为matplotlib下的figure，不是matplotlib.pyplot下面的figure
        FigureCanvas.__init__(self, fig)  # 初始化父类
        self.setParent(parent)

        mpl.rcParams['font.sans-serif'] = ['SimHei']
        mpl.rcParams['axes.unicode_minus'] = False
        # matplotlib的图像都位于Figure对象中。你可以用plt.figure创建一个新的Figure：
        # 不能通过空Figure绘图。必须用add_subplot创建一个或多个subplot才行
        # 调用figure下面的add_subplot方法，类似于matplotlib.pyplot下面的subplot方法
        self.axes = fig.add_subplot(111)

        self.axes.set_title("公司停车系统财务走势图")

    # 按天查询
    def day(self, year_month_day):
        self.axes.set_xlabel("时间(小时)")
        self.axes.set_ylabel("收入(元)")
        fcontrol = FinancialController()
        x,y = fcontrol.listhoursbyday(year_month_day)
        for a, b in zip(x, y):
            # self.axes.text(a, b, (a, b), ha='center', va='bottom', fontsize=10)#显示两个坐标
            self.axes.text(a, b, b, ha='center', va='bottom', fontsize=12)  # 显示折线点的纵坐标值
        self.axes.plot(x, y, color='r', linewidth=1.0, markerfacecolor='blue', marker='o')

    def month(self, year_month):
        self.axes.set_xlabel("时间(天)")
        self.axes.set_ylabel("收入(元)")
        fcontrol = FinancialController()
        print(year_month)
        x,y = fcontrol.listdaysumbymonth(year_month)


        print(x)
        print(y)

        for a, b in zip(x, y):
            self.axes.text(a, b, b, ha='center', va='bottom', fontsize=12)  # 显示折线点的纵坐标值
        self.axes.plot(x, y, color='r', linewidth=1.0, markerfacecolor='blue', marker='o')

    def year(self, year):
        """
        画某一年的每个月的收入的曲线
        :param year: 年份
        :return:
        """
        self.axes.set_xlabel("时间(月)")
        self.axes.set_ylabel("收入(元)")

        fcontrol = FinancialController()
        x,y = fcontrol.listmonthsumbyyear(eval(year))

        for a, b in zip(x, y):
            self.axes.text(a, b, b, ha='center', va='bottom', fontsize=12)  # 显示折线点的纵坐标值
        self.axes.plot(x, y, color='r', linewidth=1.0, markerfacecolor='blue', marker='o')


class Finance(QtWidgets.QMainWindow):
    def __init__(self):
        super(Finance, self).__init__()
        self.ui = Ui_finance()
        self.ui.setupUi(self)

        self.setWindowTitle("财务管理")
        self.setFixedSize(self.width(), self.height())  # 实现禁止窗口最大化和禁止窗口拉伸

        palette = QPalette()
        icon = QPixmap('f1.gif').scaled(850, 550)
        palette.setBrush(self.backgroundRole(), QBrush(icon))
        self.setPalette(palette)
        self.ui.tableWidget.verticalHeader().hide()  # 水平表头隐藏
        # 隐藏控件
        self.ui.groupBox_3.hide()
        self.ui.groupBox_2.hide()
        self.ui.graphicsView.hide()
        self.ui.tableWidget.hide()

        self.gif = QMovie('f5.gif')
        self.ui.label_3.setScaledContents(True)
        self.ui.label_3.setMovie(self.gif)
        self.gif.start()
        # 动态显示时间在label上
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.showtime)
        timer.start()

        # time = self.ui.dateTimeEdit.dateTime()
        self.ui.pushButton.clicked.connect(self.finance)
        self.ui.pushButton_4.clicked.connect(self.finance)  # 折线统计图显示
        self.ui.pushButton_3.clicked.connect(self.table)  # table显示财务

    def mousePressEvent(self, QMouseEvent):
        self.ui.label_3.hide()

    def mouseReleaseEvent(self, QMouseEvent):
        self.ui.label_3.show()

    def showtime(self):
        datetime = QDateTime.currentDateTime()
        text = datetime.toString()
        self.ui.label_2.setText("  " + text)

    def table(self):
        self.ui.label_3.hide()
        self.ui.groupBox_3.show()
        self.ui.tableWidget.show()
        # 根据需求自己自己设置table的行列数
        self.ui.tableWidget.setRowCount(1)
        self.ui.tableWidget.setColumnCount(3)
        data = '竹指'
        data = QTableWidgetItem(str(data))
        self.ui.tableWidget.setItem(0, 0, data)
        self.ui.tableWidget.setHorizontalHeaderLabels(['姓名', '身高', '体重'])  # 设置table的表头信息

        self.ui.tableWidget.setSelectionBehavior(QTableWidget.SelectColumns)  # 选中行
        self.ui.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)  # 将单元格设为不可更改类型
        # table字体等布局
        for index in range(self.ui.tableWidget.columnCount()):
            headItem = self.ui.tableWidget.horizontalHeaderItem(index)
            headItem.setFont(QFont("song", 10, QFont.Bold))
            headItem.setForeground(QBrush(Qt.darkBlue))
            headItem.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)

    # 查询思路：在finance获得界面输入，判断搜索的类型， 由类型判断调用Figure_Canvas()里的哪一个构图类型day(),year(),
    # month()，因为按天和按年的坐标轴不同,同时输入的数据传入 Figure_Canvas()中的方法函数中，根据这个查询数据库中数据，画图
    def finance(self):
        # 获得输入
        self.ui.label_3.hide()
        self.ui.groupBox_2.show()
        self.ui.graphicsView.show()
        category = self.ui.comboBox.currentText()
        input = self.ui.lineEdit.text()

        dr = Figure_Canvas()
        # 实例化一个FigureCanvas
        if input != '':
            if category == '按日':
                dr.day(input)  # 画图
            elif category == '按月':
                dr.month(input)
            elif category == '按年':
                dr.year(input)
            else:
                QMessageBox.information(self, ("提示"), ("修改成功！"))

        graphicscene = QtWidgets.QGraphicsScene()  # 第三步，创建一个QGraphicsScene，因为加载的图形（FigureCanvas）不能直接放到graphicview控件中，必须先放到graphicScene，然后再把graphicscene放到graphicview中
        graphicscene.addWidget(dr)  # 第四步，把图形放到QGraphicsScene中，注意：图形是作为一个QWidget放到QGraphicsScene中的
        self.ui.graphicsView.setScene(graphicscene)  # 第五步，把QGraphicsScene放入QGraphicsView
        self.ui.graphicsView.show()  # 最后，调用show方法呈现图形


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my = Finance()
    my.show()
    sys.exit(app.exec_())
