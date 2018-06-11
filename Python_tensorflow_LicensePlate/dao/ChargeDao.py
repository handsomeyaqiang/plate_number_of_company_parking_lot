from abc import ABCMeta, abstractmethod

from Python_tensorflow_LicensePlate.entity.ChargeRules import ChargeRules

class ChargeRulesDao(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def insertRules(self,chargerules):
        pass
    @abstractmethod
    def updateRules(self,chargerules):
        pass
    @abstractmethod
    def showRules(self):
        pass

