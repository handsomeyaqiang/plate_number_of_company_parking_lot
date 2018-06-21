from Python_tensorflow_LicensePlate.daoimpl.VehicleDaoImpl import VehilceDaoImpl

class VehicleService(object):
    #车辆信息管理业务层

    #登记车辆信息
    def addVehicle(self,Vehicle):
        count=VehilceDaoImpl().addVehicle(Vehicle)
        if count==0:
            return False
        return True

    #删除车辆信息
    def deleteVehicle(self,SID):
        count=VehilceDaoImpl.deleteVehicle(SID)
        if count==0:
            return False
        return True

    #修改车辆信息
    def updateVehicle(self,Vehicle):
        count=VehilceDaoImpl().updateVehicle(Vehicle)
        if count==0:
            return False
        else:
            return True

    #车辆信息展示
    def showVehicle(self):
        list = VehilceDaoImpl().showallVehicle()
        if len(list) == 0:
            return False
        else:
            return list

    #按照工号查询车辆信息
    def findVehicleById(self,SID):
        list = VehilceDaoImpl().findVehicleBySID(SID)
        if len(list) == 0:
            return False
        else:
            return list


    # 按照车牌号查找车辆信息
    def findVehicleByPlateNum(self,pid):
        list=VehilceDaoImpl().findVehicleByPlateID(pid)
        if len(list)==0:
            return False
        else:
            return list



