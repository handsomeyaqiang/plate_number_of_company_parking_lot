from abc import ABCMeta, abstractmethod


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
    @abstractmethod
    def chargemoney(self,rule,starttime,endtime):
        pass

