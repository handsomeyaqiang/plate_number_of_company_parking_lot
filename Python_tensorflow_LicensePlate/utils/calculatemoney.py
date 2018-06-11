from Python_tensorflow_LicensePlate.daoimpl.ChagreDaoImpl import ChargeRulesDaoImpl
from Python_tensorflow_LicensePlate.utils.formattime import totime
import math
import datetime


rule = ChargeRulesDaoImpl().showRules()
dayendtime = rule.dayendtime
nightendtime = rule.nightendtime
daybegintime = rule.daybegintime
nightbegintime = rule.nightbegintime
dayprice = rule.dayprice
firsthourprice = rule.firsthourprice
nightprice = rule.nightprice


def charge(starttime, endtime):
    # 第一次的开始时间戳
    money = 0
    # 时间戳转datetime
    st = datetime.datetime.fromtimestamp(starttime)
    # 白天计费结束时间
    a = "{0}-{1}-{2} {3}".format(st.year, st.month, st.day, dayendtime)
    # 白天计费开始时间
    a1 = "{0}-{1}-{2} {3}".format(st.year, st.month, st.day, daybegintime)
    # 晚上计费结束时间
    e = "{0}-{1}-{2} {3}".format(st.year, st.month, st.day + 1, nightendtime)
    at = totime(a)  # 晚上开始时间戳即白天计费结束时间戳
    at1 = totime(a1)  # 白天开始计费时间戳
    et = totime(e)  # 晚上计费结束时间戳
    # 开始时间在0:00到7：00时
    if starttime < at1:
        et = at1
        st = datetime.datetime.fromtimestamp(starttime)
        # 白天计费结束时间
        a = "{0}-{1}-{2} {3}".format(st.year, st.month, st.day - 1, dayendtime)
        at = totime(a)
    # 如果开始在第一段
    if starttime < at:
        # 开始在第一段结束在第一段
        if endtime <= at:
            hour = math.ceil((endtime - starttime) / 3600)
            # 开始在第一段结束在第一段且时间小于等于一小时
            if hour <= 1:
                money = firsthourprice
            # 开始结束时间在第一段且时间大于一小时
            else:
                money = firsthourprice + (hour - 1) * dayprice

        # 开始第一段，结束第二段
        elif (endtime > at) and (endtime <= et):
            dayhour = math.ceil((at - starttime) / 3600)
            if dayhour <= 1:
                one = firsthourprice
            else:
                one = firsthourprice + (dayhour - 1) * dayprice
            two = nightprice
            money = one + two
        else:
            money += charge(starttime, et)
            starttime = et
            money += charge(starttime, endtime)

    # 开始时间，结束时间都在第二段
    elif (starttime >= at) and (endtime <= et):
        money = nightprice
    else:
        money += charge(starttime,et)
        starttime = et
        money += charge(starttime,endtime)
    return money


