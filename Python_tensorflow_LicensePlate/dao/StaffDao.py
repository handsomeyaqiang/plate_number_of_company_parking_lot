from  Python_tensorflow_LicensePlate.entity.Staff import Staff
from abc import ABCMeta, abstractmethod
#抽象类
class staffDao(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        self.staffDao = ''

    @abstractmethod
    def addStaff(self):
        pass

    @abstractmethod
    def updateStaff(self,SID):
        pass

    @abstractmethod
    def findStaffBySid(self,SID):
        pass

    @abstractmethod
    def findStaffByName(self,name):
        pass

    @abstractmethod
    def showallStaff(self):
        pass

    @abstractmethod
    def deleteStaff(self,SID):
        pass