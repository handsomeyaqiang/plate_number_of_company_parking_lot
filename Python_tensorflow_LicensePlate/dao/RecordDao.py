from abc import ABCMeta, abstractmethod


# 抽象类
class RecordDao(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        self.staffDao = ''

    @abstractmethod
    def findRecordByPlateID(self, platenumber):
            pass

    @abstractmethod
    def findRecordByTime(self, intime):
            pass
    @abstractmethod
    def insertRecord(self, record):
        pass