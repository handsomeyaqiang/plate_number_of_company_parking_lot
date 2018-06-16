from Python_tensorflow_LicensePlate.daoimpl.ChagreDaoImpl import ChargeRulesDaoImpl
from Python_tensorflow_LicensePlate.utils.formattime import totime
class ChargeService:
    """"收费业务层"""
    def charge(self,begintime,endtime):
        """
        根据开始时间和结束时间计算收费
        :param begintime:开始时间，datetime类型
        :param endtime: 结束时间 datetime类型
        :return: 返回应缴金额
        """
        #将时间转换为时间戳
        begintime = totime(begintime)
        endtime = totime(endtime)
        #获取收费规则
        rule = ChargeRulesDaoImpl().showRules()
        money = ChargeRulesDaoImpl().chargemoney(rule,begintime,endtime)
        return money

    def updaterule(self,rule):
        """更新收费规则
        rule 为收费规则对象
        """
        return ChargeRulesDaoImpl().updateRules(rule)

    def initrule(self,rule):
        """初始化收费规则"""
        return ChargeRulesDaoImpl().insertRules(rule)
