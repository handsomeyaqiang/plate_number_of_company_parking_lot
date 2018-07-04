from Python_tensorflow_LicensePlate.dao.ChargeDao import ChargeRulesDao
from Python_tensorflow_LicensePlate.utils.Pymysql import PyMySQLHelper
from Python_tensorflow_LicensePlate.entity.ChargeRules import ChargeRules
from Python_tensorflow_LicensePlate.utils.formattime import totime
import math
import datetime


class ChargeRulesDaoImpl(ChargeRulesDao):
    def insertRules(self, chargerules):
        pass

    def updateRules(self, chargerules):
        sql =( 'update  chargerules set dayprice = %s,nightprice = %s,' 
              'daybegintime = %s,dayendtime = %s,nightbegintime = %s,nightendtime = %s,' 
              'dayfirsthourprice = %s where rid = %s')
        params =(chargerules.dayprice, chargerules.nightprice, chargerules.daybegintime,
                chargerules.dayendtime, chargerules.nightbegintime, chargerules.nightendtime,
                chargerules.firsthourprice,chargerules.rid)
        count = PyMySQLHelper().updateByParam(sql,params)
        return count

    def showRules(self):
        sql = 'select * from chargerules'
        result = PyMySQLHelper().selectOnedictcursor(sql)
        rid = result['rid']
        dayprice = result['dayprice']
        nightprice = result['nightprice']
        daybegintime = result['daybegintime']
        dayendtime = result['dayendtime']
        nightbegintime = result['nightbegintime']
        nightendtime = result['nightendtime']
        firsthourprice = result['dayfirsthourprice']
        chargerules = ChargeRules(rid, dayprice, nightprice, daybegintime, dayendtime,
                                  nightbegintime, nightendtime, firsthourprice)
        return chargerules



    def chargemoney(self, rule, starttime, endtime):
        # 第一次的开始时间戳
        money = 0
        # 时间戳转datetime
        st = datetime.datetime.fromtimestamp(starttime)
        # 白天计费结束时间
        a = "{0}-{1}-{2} {3}".format(st.year, st.month, st.day, rule.dayendtime)
        # 白天计费开始时间
        a1 = "{0}-{1}-{2} {3}".format(st.year, st.month, st.day, rule.daybegintime)
        # 晚上计费结束时间
        # e = "{0}-{1}-{2} {3}".format(st.year, st.month, st.day + 1, rule.nightendtime)
        at = totime(a)  # 晚上开始时间戳即白天计费结束时间戳
        at1 = totime(a1)  # 白天开始计费时间戳
        et =at1+86400.0  # 晚上计费结束时间戳
        # 开始时间在0:00到7：00时
        if starttime < at1:
            et = at1
            st = datetime.datetime.fromtimestamp(starttime)
            # 白天计费结束时间
            a = "{0}-{1}-{2} {3}".format(st.year, st.month, st.day, rule.dayendtime)
            at = totime(a)-86400.0
        if endtime > et:
            print(endtime,et)
            money += ChargeRulesDaoImpl().chargemoney(rule, starttime, et)
            starttime = et
            money += ChargeRulesDaoImpl().chargemoney(rule, starttime, endtime)
        # 如果开始在第一段
        elif starttime < at:
            # 开始在第一段结束在第一段
            if endtime <= at:
                hour = math.ceil((endtime - starttime) / 3600)
                # 开始在第一段结束在第一段且时间小于等于一小时
                if hour <= 1:
                    money = rule.firsthourprice
                # 开始结束时间在第一段且时间大于一小时
                else:
                    money = rule.firsthourprice + (hour - 1) * rule.dayprice

            # 开始第一段，结束第二段
            elif (endtime > at) and (endtime <= et):
                dayhour = math.ceil((at - starttime) / 3600)
                if dayhour <= 1:
                    one = rule.firsthourprice
                else:
                    one = rule.firsthourprice + (dayhour - 1) * rule.dayprice
                two = rule.nightprice
                money = one + two
        # 开始时间，结束时间都在第二段
        elif (starttime >= at) and (endtime <= et):
            money = rule.nightprice
        return money
if __name__ == '__main__':
    rule = ChargeRulesDaoImpl().showRules()
    m =  ChargeRulesDaoImpl().chargemoney(rule,totime('2018-06-30 5:40:20'),totime('2018-7-01 08:40:20'))
    print(m)