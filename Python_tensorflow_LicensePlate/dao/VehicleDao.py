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

    #通过车牌模糊查找车辆信息
    @abstractmethod
    def findVehicleByPlateIDvague(self, PlateID):
        pass

    #通过车主查找车辆信息
    @abstractmethod
    def findVehicleByOwner(self,name):
        pass

    #通过车架号查找车辆信息
    @abstractmethod
    def findVehicleByVehicleid(self,hid):
        pass

    #显示所有车辆信息
    @abstractmethod
    def showallVehicle(self):
        pass

    #根据员工号删除车辆信息
    @abstractmethod
    def deleteVehicleBySID(self,SID):
        pass

    #根据车牌号删除车辆信息
    @abstractmethod
    def deleteVehicleByPlateID(self,PlateID):
        pass