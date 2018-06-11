from abc import ABCMeta,abstractmethod
from Python_tensorflow_LicensePlate.entity.ParkLock import ParkLock


class ParkLockDao (object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def findlock(self,parklockid):
        pass
    @abstractmethod
    def addlock(self, parklock):
        pass
    @abstractmethod
    def updateparklock(self,parklock):
        pass
    @abstractmethod
    def deleteparklock(selfself, parklockid):
        pass
    @abstractmethod
    def listlock(self):
        pass




