from  Python_tensorflow_LicensePlate.entity.Staff import Staff
from abc import ABCMeta, abstractmethod
#抽象类
class staffDao(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        self.staffDao = ''

    @abstractmethod
    def _addStaff(self):
            pass

    @abstractmethod
    def _updateStaff(self,SID):
            pass

    @abstractmethod
    def _findStaffBySid(self,SID):
            pass

    @abstractmethod
    def _findStaffByName(self,name):
            pass

    @abstractmethod
    def _deleteStaff(self,SID):
            pass