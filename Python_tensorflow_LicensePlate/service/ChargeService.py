from Python_tensorflow_LicensePlate.daoimpl.ChagreDaoImpl import ChargeRulesDaoImpl
from Python_tensorflow_LicensePlate.utils.formattime import totime
from Python_tensorflow_LicensePlate.utils import ParkResult
class ChargeService:
    """"收费业务层"""
    def charge(self,begintime,endtime):
        """
        根据开始时间和结束时间计算收费
        :param begintime:开始时间，datetime类型
        :param endtime: 结束时间 datetime类型
        :return: 返回应缴金额
        """
        result = ParkResult.ParkResult()
        try:
            # 将时间转换为时间戳
            begintime = totime(begintime)
            endtime = totime(endtime)
            # 获取收费规则
            rule = ChargeRulesDaoImpl().showRules()
            money = ChargeRulesDaoImpl().chargemoney(rule,begintime,endtime)
            return result.ok(money)
        except Exception as e:
            print(e)
            return result.error("获取应缴金额失败！")

    def updaterule(self,rule):
        """更新收费规则
        rule 为收费规则对象
        """
        result = ParkResult.ParkResult()
        try:
            ChargeRulesDaoImpl().updateRules(rule)
            return result.ok2()
        except Exception as e:
            print(e)
            return result.error('更新收费规则失败！')


    def initrule(self,rule):
        """初始化收费规则"""
        result = ParkResult.ParkResult()
        try:
            ChargeRulesDaoImpl().insertRules(rule)
            return result.ok2()
        except Exception as e :
            print(e)
            return result.error("初始化收费规则失败！")

    def showrule(self):
        """显示收费规则"""
        result = ParkResult.ParkResult()
        try:
            rule = ChargeRulesDaoImpl().showRules()
            return result.ok(rule)
        except Exception as e:
            print(e)
            return result.error("获取收费规则失败！")