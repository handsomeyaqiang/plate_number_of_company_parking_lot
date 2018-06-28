from Python_tensorflow_LicensePlate.entity.Financial import Financial
from Python_tensorflow_LicensePlate.service.FinancialService import FinancialService


class FinancialController(object):
    """财务控制类"""

    def insertFinancial(self, ParkPlaceID, chargetime, money):
        """插入一条记录"""
        fin = Financial(ParkPlaceID, chargetime, money)
        rs = FinancialService().insertFinancial(fin)
        return rs

    def listallfinancial(self):
        """返回所有财务记录"""
        rs = FinancialService().listallfinancial()
        return rs

    def listbyday(self, day):
        """
        返回某一天的财务记录
        :param day: 日期 格式为：‘2018-06-05’
        :return:
        """

        resultlist = []
        result = FinancialService().listbyday(day)
        if result.status == 200:
            rsfinlist = result.data
            for findic in rsfinlist:
                finlist = []
                finlist.append(findic.ParkPlaceID)
                finlist.append(findic.chargetime)
                finlist.append(findic.money)
                resultlist.append(finlist)
        return resultlist

    def listbymonth(self, month):
        """
        返回某个月的所有记录
        :param month: 月份 格式为‘2018-06’
        :return:
        """
        resultlist = []
        result =  FinancialService().listbymonth(month)
        if result.status == 200:
            rsfinlist = result.data
            for findic in rsfinlist:
                finlist = []
                finlist.append(findic.ParkPlaceID)
                finlist.append(findic.chargetime)
                finlist.append(findic.money)
                resultlist.append(finlist)
        return resultlist

    def listbyyear(self, year):
        """
        返回某一年的全部记录
        :param year:年份 格式为‘2018’
        :return:
        """
        resultlist =[]
        result = FinancialService().listbyyear(year)
        if result.status==200:
            rsfinlist = result.data
            for findic in rsfinlist:
                finlist =[]
                finlist.append(findic.ParkPlaceID)
                finlist.append(findic.chargetime)
                finlist.append(findic.money)
                resultlist.append(finlist)
        return resultlist

    def listbyparkolaceid(self, parkplaceid):
        """
        返回某个车位的收入记录
        :param parkplaceid: 车位号
        :return:
        """
        rs = FinancialService().listbyparkplaceid(parkplaceid)
        return rs

    def listmonthsumbyyear(self, year):
        """
        返回某年的每个月份的收入和
        :param year: 年份格式为"2018"
        :return:
        """
        result = FinancialService().listmonthsumbyyear(year)
        x = []
        y = []
        if result.status == 200:
            if result.data is not None:
                yms = result.data
                for ym in yms:
                    x.append(ym['ymdatetime'])
                    y.append(ym['totalmoney'])
        return x,y

    def listdaysumbymonth(self, year_month):
        """
        返回某月的每个天的收入和
        :param year_month: 格式为‘2018-06’
        :return:返回x,y两个列表
        """
        result = FinancialService().listdaysumbymonth(year_month)
        x = []
        y = []
        if result.status == 200:
            if result.data is not None:
                mds = result.data
                for md in mds:
                    x.append(md['mddatetime'])
                    y.append(md['totalmoney'])
        print(x)
        print(y)
        return x,y

    def listhoursbyday(self, year_month_day):
        """
        返回某一天的每个时间段的收入和
        :param year_month_day: 格式为‘2018-06-22’
        :return:返回x[]列表和y[]列表
        """
        result = FinancialService().listhoursumbyday(year_month_day)
        x = []
        y = []
        if result.status == 200:
            dhs = result.data
            for dh in dhs:
                x.append(dh['dhdatetime'])
                y.append(dh['totalmoney'])
        print(x)
        print(y)
        return x, y
if __name__ == '__main__':
    # FinancialController().listdaysumbymonth('2018-06')
        FinancialController().listbyyear('2018')