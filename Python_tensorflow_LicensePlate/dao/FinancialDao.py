from abc import ABCMeta, abstractmethod


class FinancialDao(object):

    __metaclass__ = ABCMeta
    @abstractmethod
    def insertfinalcial(self,finalcial):
        pass
    @abstractmethod
    def deletefinalcial(self,finalcialid):
        pass
    @abstractmethod
    def updatefinalcial(self,finalcial):
        pass
    @abstractmethod
    def listfinalcialbyparkplaceid(self,parkplaceid):
        pass
    @abstractmethod
    def listfinalcialbyyear(self,year):
        pass
    @abstractmethod
    def listfinalcialbymonth(self,month):
        pass
    @abstractmethod
    def listfinalcialbyday(self,day):
        pass
    @abstractmethod
    def listfinalcialbyday(self,week):
        pass
    @abstractmethod
    def listallfinalcial(self):
        pass

