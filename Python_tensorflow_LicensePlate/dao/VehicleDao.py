from  Python_tensorflow_LicensePlate.entity.Vehicle import Vehicle
from abc import ABCMeta, abstractmethod
#抽象类
class VehicleDao(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        self.VehicleDao = ''

    @abstractmethod
    def addVehicle(self):
        pass

    @abstractmethod
    def updateVehicle(self,SID):
        pass

    @abstractmethod
    def findVehicleBySID(self,SID):
        pass

    @abstractmethod
    def findVehicleByPlateID(self,PlateID):
        pass

    @abstractmethod
    def showallVehicle(self):
        pass

    @abstractmethod
    def deleteVehicle(self,SID):
        pass