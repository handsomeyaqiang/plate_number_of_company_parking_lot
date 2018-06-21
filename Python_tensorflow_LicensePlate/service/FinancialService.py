from Python_tensorflow_LicensePlate.daoimpl.FinancialDaoImpl import FinancialDaoImpl
from Python_tensorflow_LicensePlate.utils import ParkResult


class FinancialService(object):

    def insertFinancial(self, financial):
        """插入一条财务记录"""
        result = ParkResult.ParkResult()
        try:
            FinancialDaoImpl().insertfinancial(financial)
            return result.ok2()
        except Exception as e:
            print(e)
            return result.error("插入记录失败！")

    def listbyyear(self, year):
        """获取某一年的报表"""
        result = ParkResult.ParkResult()
        try:
            list = FinancialDaoImpl().listfinancialbyyear(year)
            return result.ok(list)
        except Exception as e:
            print(e)
            return result.error('获取报表信息失败！')

    def listbymonth(self, month):
        """获取某一月的报表"""
        result = ParkResult.ParkResult()
        try:
            list = FinancialDaoImpl().listfinancialbymonth(month)
            return result.ok(list)
        except Exception as e:
            print(e)
            return result.error("获取报表信息失败！")

    def listbyday(self, day):
        """"获取某一天的报表"""
        result = ParkResult.ParkResult()
        try:
            list = FinancialDaoImpl().listfinancialbyday(day)
            return  result.ok(list)
        except Exception as e:
            print(e)
            return result.error("获取报表失败！")

    def listbyparkplaceid(self, parkplaceid):
        """"获取某个车位的报表"""
        result = ParkResult.ParkResult()
        try:
            list = FinancialDaoImpl().listfinancialbyparkplaceid(parkplaceid)
            return result.ok(list)
        except Exception as e:
            print(e)
            return result.error("获取报表失败！")

    def listallfinancial(self):
        """返回所有报表"""
        result = ParkResult.ParkResult()
        try:
            list = FinancialDaoImpl().listallfinancial()
            return result.ok(list)
        except Exception as e:
            print(e)
            return result.errror("获取报表失败！")
