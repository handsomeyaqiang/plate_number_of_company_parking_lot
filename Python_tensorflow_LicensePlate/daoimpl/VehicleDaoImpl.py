from Python_tensorflow_LicensePlate.entity.Vehicle import Vehicle
from Python_tensorflow_LicensePlate.dao.VehicleDao import VehicleDao
from Python_tensorflow_LicensePlate.utils import Pymysql
#实现类
class VehilceDaoImpl(VehicleDao):
    def __init__(self):
        self.VehicleDaoImpl = ''

    #添加车辆信息实现
    def addVehicle(self,vehicle):
        py =Pymysql.PyMySQLHelper()
        sql = 'insert into vehicle(PlateID,owner,Vehicle_identity,SID) ' \
              'VALUES (%s,%s,%s,%s)'
        params = (vehicle.PlateID,vehicle.owner,vehicle.vehicle_identity,vehicle.SID)
        count = py.updateByParam(sql, params)
        return count

    # 修改车牌号修改车辆信息
    def updateVehicle(self,vehicle):
        py = Pymysql.PyMySQLHelper()
        sql = 'update vehicle set owner=%s,Vehicle_identity=%s,SID=%s where PlateID=%s'
        params = ( vehicle.owner, vehicle.vehicle_identity, vehicle.SID,vehicle.PlateID)
        count = py.updateByParam(sql, params)
        return count

    # 根据员工号删除车辆信息
    def deleteVehicleBySID(self,SID):
        py = Pymysql.PyMySQLHelper()
        sql = 'delete from vehicle WHERE SID =%s'
        params=(SID)
        count = py.updateByParam(sql, params)
        return count


    # 根据车牌号删除车辆信息
    def deleteVehicleByPlateID(self,PlateID):
        py = Pymysql.PyMySQLHelper()
        sql = 'delete from vehicle WHERE PlateID =%s'
        params=(PlateID)
        count = py.updateByParam(sql, params)
        return count


    # 通过员工号查找车辆信息实现
    def findVehicleBySID(self, SID):
        py = Pymysql.PyMySQLHelper()
        sql = "select * from vehicle where SID ='%s'"%(SID)
        result = py.selectalldictcursor(sql)
        list = []
        for rs in result:
            SID = rs['SID']
            PlateID=rs['PlateID']
            owner=rs['owner']
            vehicle_identity=rs['vehicle_identity']
            vehicle = Vehicle(SID,PlateID, owner, vehicle_identity)
            list.append(vehicle)
        return list

    # 通过车牌号查找车辆信息实现
    def findVehicleByPlateID(self, PlateID):
        py = Pymysql.PyMySQLHelper()
        sql = "select * from vehicle where PlateID = '%s'"%(PlateID)
        result=py.selectOne(sql)
        list = []
        for rs in result:
            SID = rs['SID']
            PlateID = rs['PlateID']
            owner = rs['owner']
            vehicle_identity =rs['vehicle_identity']
            vehicle = Vehicle(SID,PlateID, owner, vehicle_identity)
            list.append(vehicle)
        return list



    # 显示所有车辆信息实现
    def showallVehicle(self):
        py = Pymysql.PyMySQLHelper()
        sql = 'select * from vehicle'
        result = py.selectalldictcursor(sql)
        list = []
        for rs in result:
            SID = rs['SID']
            PlateID=rs['PlateID']
            owner=rs['owner']
            vehicle_identity=rs['vehicle_identity']
            vehicle = Vehicle(SID,PlateID,owner,vehicle_identity)
            list.append(vehicle)
        return list

