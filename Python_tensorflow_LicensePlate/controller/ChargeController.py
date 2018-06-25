from Python_tensorflow_LicensePlate.entity.ChargeRules import ChargeRules
from Python_tensorflow_LicensePlate.service.ChargeService import ChargeService

class ChargeController(object):
    """收费控制层"""

    def chargemoney(self,begintime,endtime):
        """通过传入开始时间和结束时间，返回所需要缴纳的费用
        :param begintime: 计费开始时间 datetime 类型
        :param endtime: 计费结束时间 datetime 类型
        :return: 返回 应缴金额
        """
        return  ChargeService().charge(begintime,endtime)

    def updaterule(self,rid,dayprice,nightprice,daybegintime,dayendtime,
                 nightbegintime,nightendtime,firsthourprice):
        """更新收费规则"""
        rule = ChargeRules(rid,dayprice,nightprice,daybegintime,dayendtime,
                 nightbegintime,nightendtime,firsthourprice)
        return ChargeService().updaterule(rule)

    def update(self,rule):
        """参数为规则对象的方法"""
        return ChargeService().updaterule(rule)

    def  showrule(self):
        """
        获取收费规则
        :return: 返回 rule 对象
        """
        rule = ChargeService().showrule()
        return rule

    def initrule(self,rid,dayprice,nightprice,daybegintime,dayendtime,
                 nightbegintime,nightendtime,firsthourprice):
        """收费规则为空时初始化插入一条规则"""
        rule = (rid, dayprice, nightprice, daybegintime, dayendtime,
        nightbegintime, nightendtime, firsthourprice)
        return ChargeService().initrule(rule)