from abc import ABCMeta, abstractclassmethod


class FinalcialDao(object):

    __metaclass__ = ABCMeta
    @abstractclassmethod
    def insertfinalcial(self,finalcial):
        pass
    @abstractclassmethod
    def deletefinalcial(self,finalcialid):
        pass
    @abstractclassmethod
    def updatefinalcial(self,finalcial):
        pass
    @abstractclassmethod
    def listfinalcialbyparkplaceid(self,parkplaceid):
        pass
    @abstractclassmethod
    def listfinalcialbyyear(self,year):
        pass
    @abstractclassmethod
    def listfinalcialbymonth(self,month):
        pass
    @abstractclassmethod
    def listfinalcialbyday(self,day):
        pass
    @abstractclassmethod
    def listfinalcialbyday(self,week):
        pass
    @abstractclassmethod
    def listallfinalcial(self):
        pass

