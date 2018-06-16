from abc import ABCMeta, abstractmethod


class FinancialDao(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def insertfinancial(self,finalcial):
        pass

    @abstractmethod
    def deletefinancial(self,finalcialid):
        pass

    @abstractmethod
    def updatefinancial(self,finalcial):
        pass

    @abstractmethod
    def listfinancialbyparkplaceid(self,parkplaceid):
        pass

    @abstractmethod
    def listfinancialbyyear(self,year):
        pass

    @abstractmethod
    def listfinancialbymonth(self,month):
        pass

    @abstractmethod
    def listfinancialbyday(self,day):
        pass

    @abstractmethod
    def listfinancialbyday(self,week):
        pass

    @abstractmethod
    def listallfinancial(self):
        pass

