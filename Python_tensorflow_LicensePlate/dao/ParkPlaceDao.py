from abc import ABCMeta,abstractmethod


class ParkPlaceDao(object):
    """定义车位的操作方法的抽象类
    """
    metaclass = ABCMeta

    @abstractmethod

    def findbyid(self,parkplaceid):
        pass
    @abstractmethod
    def updatecarnumber(self, parkplace):
        pass
    @abstractmethod
    def updateparkplace(self,parkplace):
        pass
    @abstractmethod
    def switchtotemp(self, parkplaceid):
         pass
    @abstractmethod
    def switchtoinner(self, parkplaceid):
         pass
    @abstractmethod
    def insertparkplace(self,parkplace):
        pass
    @abstractmethod
    def deleteparkplace(selfself,parkplace):
        pass
    @abstractmethod
    def updateparkplace(self,parkplace):
        pass
    @abstractmethod
    def listall(self):
        pass
    @abstractmethod
    def getcount(self,parkPlaceType):
        pass
    @abstractmethod
    def getemptycount(self,parkPlaceType):
        pass
    @abstractmethod
    def getinusecount(self,parkPlaceType):
        pass
    @abstractmethod
    def updatelockstatus(self,lockstatus,parkPlaceID):
        pass
    @abstractmethod
    def findbytype(self,type):
        pass

