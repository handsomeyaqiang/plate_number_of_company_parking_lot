from abc import ABCMeta, abstractclassmethod

from Python_tensorflow_LicensePlate.entity.ChargeRules import ChargeRules

class ChargeRulesDao(object):
    __metaclass__ = ABCMeta

    @abstractclassmethod
    def insertRules(self,chargerules):
        pass
    @abstractclassmethod
    def updateRules(self,chargerules):
        pass
    @abstractclassmethod
    def showRules(self):
        pass

