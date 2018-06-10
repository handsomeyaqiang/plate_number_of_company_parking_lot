from Python_tensorflow_LicensePlate.dao.ChargeDao import ChargeRulesDao
from Python_tensorflow_LicensePlate.utils.Pymysql import PyMySQLHelper
from Python_tensorflow_LicensePlate.entity.ChargeRules import ChargeRules


class ChargeRulesDaoImpl(ChargeRulesDao):
    def insertRules(self, chargerules):
        pass
    def updateRules(self, chargerules):
        sql = 'update  chargerules set (dayprice,nightprice,' \
              'daybegintime,dayendtime,nightbegintime,nightendtime,' \
              'firsthourprice)VALUES ({0},{1},{2},{3},{4},{5},{6}) where rid = {7}}'\
            .format(chargerules.dayprice,chargerules.nightprice,chargerules.daybegintime,

                    chargerules.dayendtime,chargerules.nightbegintime,chargerules.nightendtime,
                    chargerules.firsthourprice,chargerules.rid)
        count = PyMySQLHelper().update(sql)
        return count
    def showRules(self):
        sql = 'select * from chargerules'
        result = PyMySQLHelper().selectOnedictcursor(sql)
        rid = result ['rid']
        dayprice = result['dayprice']
        nightprice = result['nightprice']
        daybegintime = result['daybegintime']
        dayendtime = result['dayendtime']
        nightbegintime = result['nightbegintime']
        nightendtime = result['nightendtime']
        firsthourprice = result['dayfirsthourprice']
        chargerules = ChargeRules(rid,dayprice, nightprice, daybegintime, dayendtime,
                 nightbegintime, nightendtime, firsthourprice)
        return chargerules
