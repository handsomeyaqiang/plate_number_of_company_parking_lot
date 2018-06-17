from abc import ABCMeta, abstractmethod
#抽象类
class VehicleDao(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        self.VehicleDao = ''

    #添加车辆信息
    @abstractmethod
    def addVehicle(self,Vehicle):
        pass

    #修改车辆信息
    @abstractmethod
    def updateVehicle(self,Vehicle):
        pass

    #通过员工号查找车辆信息
    @abstractmethod
    def findVehicleBySID(self,SID):
        pass

    #通过车牌号查找车辆信息
    @abstractmethod
    def findVehicleByPlateID(self,PlateID):
        pass

    #显示所有车辆信息
    @abstractmethod
    def showallVehicle(self):
        pass

    #删除车辆信息
    @abstractmethod
    def deleteVehicle(self,SID):
        pass