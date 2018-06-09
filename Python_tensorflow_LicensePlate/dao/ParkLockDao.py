from abc import ABCMeta,abstractclassmethod
from Python_tensorflow_LicensePlate.entity.ParkLock import ParkLock


class ParkLockDao (object):
    __metaclass__ = ABCMeta

    @abstractclassmethod
    def findlock(self,parklockid):
        pass
    @abstractclassmethod
    def addlock(self, parklock):
        pass
    @abstractclassmethod
    def updateparklock(self,parklock):
        pass
    @abstractclassmethod
    def deleteparklock(selfself, parklockid):
        pass
    @abstractclassmethod
    def listlock(self):
        pass




