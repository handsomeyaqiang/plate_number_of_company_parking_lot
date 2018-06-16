from Python_tensorflow_LicensePlate.daoimpl.FinancialDaoImpl import FinancialDaoImpl


class FinancialService(object):

    def insertFinancial(self,financial):
        """插入一条财务记录"""
        FinancialDaoImpl().insertfinancial(financial)

    def listbyyear(self,year):
        """获取某一年的报表"""
        list = FinancialDaoImpl().listfinancialbyyear(year)
        return list

    def listbymonth(self,month):
        """获取某一月的报表"""
        list = FinancialDaoImpl().listfinancialbymonth(month)
        return list

    def listbyday(self,day):
        """"获取某一天的报表"""
        list = FinancialDaoImpl().listfinancialbyday(day)
        return list

    def listbyparkplaceid(self,parkplaceid):
        """"获取某个车位的报表"""
        list = FinancialDaoImpl().listfinancialbyparkplaceid(parkplaceid)
        return list

    def listallfinancial(self):
        """返回所有报表"""
        list = FinancialDaoImpl().listfinancialbyday()
        return list