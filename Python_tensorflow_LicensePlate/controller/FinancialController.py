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
        rs = FinancialService().listbyday(day)
        return rs

    def listbymonth(self, month):
        """
        返回某个月的所有记录
        :param month: 月份 格式为‘2018-06’
        :return:
        """
        rs = FinancialService().listbymonth(month)
        return rs

    def listbyyear(self, year):
        """
        返回某一年的全部记录
        :param year:年份 格式为‘2018’
        :return:
        """
        rs = FinancialService().listbyyear(year)
        return rs

    def listbyparkolaceid(self,parkplaceid):
        """
        返回某个车位的收入记录
        :param parkplaceid: 车位号
        :return:
        """
        rs = FinancialService().listbyparkplaceid(parkplaceid)
        return rs

    def listmonthsumbyyear(self,year):
        """
        返回某年的每个月份的收入和
        :param year: 年份格式为"2018"
        :return:
        """
        rs = FinancialService().listmonthsumbyyear(year)
        return rs
    def listdaysumbymonth(self,year_month):
        """
        返回某月的每个天的收入和
        :param year_month: 格式为‘2018-06’
        :return:
        """
        rs = FinancialService().listdaysumbymonth(year_month)
        return rs
    def listhoursbyday(self,year_month_day):
        """
        返回某一天的每个时间段的收入和
        :param year_month_day: 格式为‘2018-06-22’
        :return:
        """
        rs = FinancialService().listhoursumbyday(year_month_day)
        return  rs
