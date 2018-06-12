from abc import ABCMeta, abstractmethod


# 抽象类
class RecordDao(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def findRecordByPlateID(self, platenumber):
        pass

    @abstractmethod
    def findRecordByTime(self, intime):
        pass

    @abstractmethod
    def insertRecord(self, record):
        pass

    @abstractmethod
    def updateRecord(self, record):
        pass

    @abstractmethod
    def deleteRecordByRid(self, rid):
        pass

    @abstractmethod
    def deleteRecordByPlateNumber(self, platenumber):
        pass
