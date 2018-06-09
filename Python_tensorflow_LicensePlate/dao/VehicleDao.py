from  Python_tensorflow_LicensePlate.entity.Vehicle import Vehicle
from abc import ABCMeta, abstractmethod
#抽象类
class VehicleDao(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        self.VehicleDao = ''

    @abstractmethod
    def _addVehicle(self):
            pass

    @abstractmethod
    def _updateVehicle(self,SID):
            pass

    @abstractmethod
    def _findVehicleBySID(self,SID):
            pass

    @abstractmethod
    def _findVehicleByPlateID(self,PlateID):
            pass

    @abstractmethod
    def _deleteVehicle(self,SID):
            pass