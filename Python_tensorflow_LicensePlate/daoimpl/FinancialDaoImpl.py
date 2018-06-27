from Python_tensorflow_LicensePlate.dao.FinancialDao import FinancialDao
from Python_tensorflow_LicensePlate.utils.Pymysql import PyMySQLHelper
from Python_tensorflow_LicensePlate.entity.Financial import Financial


class FinancialDaoImpl(FinancialDao):
    def insertfinancial(self, financial):
        """插入一个financial对象"""
        sql = 'insert into financial (ParkPlaceID, chargetime, money) VALUES (%s,%s,%s)'
        params = (financial.ParkPlaceID, financial.chargetime, financial.money)
        print(sql)
        count = PyMySQLHelper().updateByParam(sql, params)
        return count

    def deletefinancial(self, financialid):
        """根据id删除"""
        sql = 'delete from financial WHERE Fid = %s'
        parms = (financialid)
        count = PyMySQLHelper().updateByParam(sql, parms)
        return count

    def updatefinancial(self, financial):
        "更新"
        sql = ('update financial set ParkPlaceID = %s,'
               'chargetime = %s,money = %s  WHERE Fid = %s')
        parms = (financial.ParkPlaceID, financial.chargetime, financial.money, financial.Fid)
        count = PyMySQLHelper().updateByParam(sql, parms)
        return count

    def listfinancialbyparkplaceid(self, parkplaceid):
        """"按照车位号返回财务状况"""
        sql = 'select * from financial where parkPlaceID = {0}'.format(parkplaceid)
        result = PyMySQLHelper().selectalldictcursor(sql)
        list = []
        for rs in result:
            Fid = rs['Fid']
            ParkPlaceID = rs['ParkPlaceID']
            chargetime = rs['chargetime']
            money = rs['money']
            financial = Financial(ParkPlaceID, chargetime, money)
            financial.Fid = Fid
            list.append(financial)
        return list

    def listfinancialbyyear(self, year):
        """"返回某一年的财务列表
        参数为格式类型为 '2018'"""
        sql = 'select * from financial WHERE year(chargetime) = {0}'.format(year)
        result = PyMySQLHelper().selectalldictcursor(sql)
        list = []
        for rs in result:
            Fid = rs['Fid']
            ParkPlaceID = rs['ParkPlaceID']
            chargetime = rs['chargetime']
            money = rs['money']
            financial = Financial(ParkPlaceID, chargetime, money)
            financial.Fid = Fid
            list.append(financial)
        return list

    def listfinancialbymonth(self, month):
        """返回某一月的财务列表
        参数格式为'2018-06'
        """
        sql = "select * from financial WHERE DATE_FORMAT(chargetime,'%%Y-%%m')= %s"
        params = (month)
        result = PyMySQLHelper().selectalldictcursorByparams(sql, params)
        list = []
        for rs in result:
            Fid = rs['Fid']
            ParkPlaceID = rs['ParkPlaceID']
            chargetime = rs['chargetime']
            money = rs['money']
            financial = Financial(ParkPlaceID, chargetime, money)
            financial.Fid = Fid
            list.append(financial)
        return list

    def listfinancialbyday(self, day):
        """返回某一天的财务列表
        参数格式为'2018-6-20'"""
        sql = "select * from financial WHERE DATE_FORMAT(chargetime,'%%Y-%%m-%%d') = %s"
        params = (day)
        result = PyMySQLHelper().selectalldictcursorByparams(sql, params)
        print(result)
        list = []
        for rs in result:
            Fid = rs['Fid']
            ParkPlaceID = rs['ParkPlaceID']
            chargetime = rs['chargetime']
            money = rs['money']
            financial = Financial(ParkPlaceID, chargetime, money)
            financial.Fid = Fid
            list.append(financial)
        return list

    def listallfinancial(self):
        """返回全部财务列表"""
        sql = 'select * from financial '
        result = PyMySQLHelper().selectalldictcursor(sql)
        list = []
        for rs in result:
            Fid = rs['Fid']
            ParkPlaceID = rs['ParkPlaceID']
            chargetime = rs['chargetime']
            money = rs['money']
            financial = Financial(ParkPlaceID, chargetime, money)
            financial.Fid = Fid
            list.append(financial)
        return list

    def listsumeachmonthbyyear(self, year):
        """根据年份，返回该年
        每一个月的收入总和的列表
        :param year:年 格式为： 2018
        :return: 返回字典类型列表 [{'totalmonery':value,'ymdatetime':value}]
        """
        sql = ("select SUM(money) as totalmoney ,DATE_FORMAT(chargetime,'%%m')"
               " as ymdatetime from financial where chargetime in"
               "(select chargetime"
               " from financial WHERE DATE_FORMAT(chargetime,'%%Y')='%s'"
               ")"
               " GROUP BY DATE_FORMAT(chargetime,'%%Y-%%m')")%(year)
        result = PyMySQLHelper().selectalldictcursor(sql)
        return result

    def listsumeachdaybymonth(self, month):
        """
        返回某一个月每一天的收入和
        :param month: 月份 格式为‘2018-06’
        :return: 返回字典类型列表 [{'totalmonery':value,'mddatetime':value}]
        """
        sql =("select SUM(money) as totalmoney ,DATE_FORMAT(chargetime,'%%d')"
               " as mddatetime from financial where chargetime in"
               "(select chargetime"
               " from financial WHERE DATE_FORMAT(chargetime,'%%Y-%%m')='%s'"
               ")"
               " GROUP BY DATE_FORMAT(chargetime,'%%d')")%(month)
        result = PyMySQLHelper().selectalldictcursor(sql)
        return result

    def listsumeachhourbyday(self, day):
        """
        返回一天中每个时间点的收入和的list列表
        :param day: ’2018-06-8‘
        :return: 字典列表类型 [{'totalmonery':value,'dhdatetime':value}]
        """
        sql =("select SUM(money) as totalmoney ,DATE_FORMAT(chargetime,'%%H')"
               " as dhdatetime from financial where chargetime in"
               "(select chargetime"
               " from financial WHERE DATE_FORMAT(chargetime,'%%Y-%%m-%%d')='%s'"
               ")"
               " GROUP BY DATE_FORMAT(chargetime,'%%H')")%(day)

        result = PyMySQLHelper().selectalldictcursor(sql)
        return result


if __name__ == '__main__':
    # FinancialDaoImpl().listsumeachdaybymonth('2018-06')
    FinancialDaoImpl().listsumeachhourbyday('2018-06-20')