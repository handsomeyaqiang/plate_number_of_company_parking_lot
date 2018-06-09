from Python_tensorflow_LicensePlate.daoimpl.ChagreDaoImpl import ChargeRulesDaoImpl
from Python_tensorflow_LicensePlate.entity.ChargeRules import ChargeRules
class ChargeService:

    def charge(self,begintime,endtime):
        chargerules = ChargeRulesDaoImpl().showRules()
        c
