from  Python_tensorflow_LicensePlate.entity.Record import Record
from abc import ABCMeta, abstractmethod
#抽象类
class RecordDao(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        self.staffDao = ''

    @abstractmethod
    def _findRecordByPlateID(self,PlateID):
            pass

    @abstractmethod
    def _findRecordByTime(self,InTime):
            pass

