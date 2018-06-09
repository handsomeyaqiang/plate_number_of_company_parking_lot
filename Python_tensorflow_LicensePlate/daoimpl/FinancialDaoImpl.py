from Python_tensorflow_LicensePlate.dao.FinancialDao import FinancialDao
from Python_tensorflow_LicensePlate.utils.Pymysql import PyMySQLHelper
from Python_tensorflow_LicensePlate.entity.Financial import Financial


class FinancialDaoImpl(FinancialDao):
    def insertfinancial(self, financial):
        sql = 'insert into financial (ParkPlaceID, time, money) VALUES ({0},{1},{2})'.format(
            financial.ParkPlaceID,financial.time,financial.money)
        count = PyMySQLHelper().update(sql)
        return count

    def deletefinancial(self, financialid):
        sql = 'delete from financial WHERE financialid = {0}'.format(financialid)
        count = PyMySQLHelper().update(sql)
        return  count

    def updatefinancial(self, financial):
        sql = 'update financial set (ParkPlaceID,' \
              'chargetime,money) VALUES ({0},{1},{2})' \
              ' WHERE Fid = {3}'.format(financial.ParkPlaceID,financial.chargetime,financial.money)
        count = PyMySQLHelper().update(sql)
        return count

    def listfinancialbyparkplaceid(self, parkplaceid):
        sql = 'select * from financial where parkPlaceID = {0}'.format(parkplaceid)
        result = PyMySQLHelper().selectalldictcursor(sql)
        list = []
        for rs in result:
            Fid = rs['Fid']
            ParkPlaceID = rs['ParkPlaceID']
            chargetime = rs['chargetime']
            money = rs['money']
            financial = Financial(Fid,ParkPlaceID,chargetime,money)
            list.append(financial)
        return list


    def listfinancialbyyear(self, year):
        sql = 'select * from financial year(chargetime) = {0}'.format(year)
        result = PyMySQLHelper().selectalldictcursor(sql)
        list = []
        for rs in result:
            Fid = rs['Fid']
            ParkPlaceID = rs['ParkPlaceID']
            chargetime = rs['chargetime']
            money = rs['money']
            financial = Financial(Fid, ParkPlaceID, chargetime, money)
            list.append(financial)
        return list

    def listfinancialbymonth(self, month):
        sql = 'select * from financial month(chargetime) = {0}'.format(month)
        result = PyMySQLHelper().selectalldictcursor(sql)
        list = []
        for rs in result:
            Fid = rs['Fid']
            ParkPlaceID = rs['ParkPlaceID']
            chargetime = rs['chargetime']
            money = rs['money']
            financial = Financial(Fid, ParkPlaceID, chargetime, money)
            list.append(financial)
        return list

    def listfinancialbyday(self, day):
        sql = 'select * from financial day(chargetime) = {0}'.format(day)
        result = PyMySQLHelper().selectalldictcursor(sql)
        list = []
        for rs in result:
            Fid = rs['Fid']
            ParkPlaceID = rs['ParkPlaceID']
            chargetime = rs['chargetime']
            money = rs['money']
            financial = Financial(Fid, ParkPlaceID, chargetime, money)
            list.append(financial)
        return list

    def listallfinancial(self):
        sql = 'select * from financial '
        result = PyMySQLHelper().selectalldictcursor(sql)
        list = []
        for rs in result:
            Fid = rs['Fid']
            ParkPlaceID = rs['ParkPlaceID']
            chargetime = rs['chargetime']
            money = rs['money']
            financial = Financial(Fid, ParkPlaceID, chargetime, money)
            list.append(financial)
        return list
