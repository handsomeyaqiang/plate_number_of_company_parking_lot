from  Python_tensorflow_LicensePlate.entity.ParkPlace import ParkPlace
from abc import ABCMeta,abstractclassmethod


class ParkPlaceDao(object):
    """定义车位的操作方法的抽象类
    """
    __metaclass__ = ABCMeta

    @abstractclassmethod

    def find(self,parkplaceid):
        pass
    @abstractclassmethod
    def findparkplace(self,parkplace):
        pass
    @abstractclassmethod
    def updateparkplace(self,parkplace):
        pass
    @abstractclassmethod
    def switchtotemp(self, parkplace):
         pass
    @abstractclassmethod
    def switchtoinner(self, parkplace):
         pass
    @abstractclassmethod
    def insertparkplace(self,parkplace):
        pass
    @abstractclassmethod
    def deleteparkplace(selfself,parkplace):
        pass
    @abstractclassmethod
    def updateparkplace(self,parkplace):
        pass
    @abstractclassmethod
    def listall(self):
        pass
