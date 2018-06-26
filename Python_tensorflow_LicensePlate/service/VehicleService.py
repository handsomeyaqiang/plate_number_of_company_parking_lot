from Python_tensorflow_LicensePlate.daoimpl.VehicleDaoImpl import VehilceDaoImpl
from Python_tensorflow_LicensePlate.utils.ParkResult import ParkResult
class VehicleService(object):
    #车辆信息管理业务层

    #登记车辆信息
    def addVehicle(self,Vehicle):
        result = ParkResult()
        try:
            VehilceDaoImpl().addVehicle(Vehicle)
            return result.ok2()
        except Exception as e:
            print(e)
            return result.error("添加车辆失败！")

    #删除车辆信息
    def deleteVehicle(self,SID):
        result = ParkResult()
        try:
            VehilceDaoImpl().deleteVehicleBySID(SID)
            return result.ok2()
        except Exception as e:
            print(e)
            return result.error("删除车辆失败！")

    #修改车辆信息
    def updateVehicle(self,Vehicle):
        result = ParkResult()
        try:
            VehilceDaoImpl().updateVehicle(Vehicle)
            return result.ok2()
        except Exception as e:
            print(e)
            return result.error("修改车辆失败！")

    #车辆信息展示
    def showVehicle(self):
        result = ParkResult()
        try:
            s = VehilceDaoImpl()
            list = s.showallVehicle()
            return result.ok(list)
        except Exception as e:
            print(e)
            return result.error("显示员工信息失败！")

    #按照工号查询车辆信息
    def findVehicleById(self,SID):
        result = ParkResult()
        try:
            s = VehilceDaoImpl()
            list = s.findVehicleBySID(SID)
            return result.ok(list)
        except Exception as e:
            print(e)
            return result.error("查询员工信息失败！")


    # 按照车牌号查找车辆信息
    def findVehicleByPlateNum(self,pid):
        result = ParkResult()
        try:
            s = VehilceDaoImpl()
            list = s.findVehicleByPlateID(pid)
            return result.ok(list)
        except Exception as e:
            print(e)
            return result.error("查询员工信息失败！")


    # 按照车主查找车辆信息
    def findVehicleByOwer(self,name):
        result = ParkResult()
        try:
            s = VehilceDaoImpl()
            list = s.findVehicleByOwner(name)
            return result.ok(list)
        except Exception as e:
            print(e)
            return result.error("查询员工信息失败！")

    # 按照车架号查找车辆信息
    def findVehicleByVehicleId(self,vid):
        result = ParkResult()
        try:
            s = VehilceDaoImpl()
            list = s.findVehicleByVehicleid(vid)
            return result.ok(list)
        except Exception as e:
            print(e)
            return result.error("查询员工信息失败！")



