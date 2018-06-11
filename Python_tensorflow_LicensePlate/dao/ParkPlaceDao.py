from  Python_tensorflow_LicensePlate.entity.ParkPlace import ParkPlace
from abc import ABCMeta,abstractmethod


class ParkPlaceDao(object):
    """定义车位的操作方法的抽象类
    """
    metaclass = ABCMeta

    @abstractmethod

    def find(self,parkplaceid):
        pass
    @abstractmethod
    def findparkplace(self,parkplace):
        pass
    @abstractmethod
    def updateparkplace(self,parkplace):
        pass
    @abstractmethod
    def switchtotemp(self, parkplace):
         pass
    @abstractmethod
    def switchtoinner(self, parkplace):
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
