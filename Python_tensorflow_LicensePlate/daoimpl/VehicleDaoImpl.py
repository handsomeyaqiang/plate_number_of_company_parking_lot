from Python_tensorflow_LicensePlate.entity.Vehicle import Vehicle
from Python_tensorflow_LicensePlate.dao.VehicleDao import VehicleDao
from ..utils import Pymysql
#实现类
class staffDaoImpl(VehicleDao):
    def __init__(self):
        self.VehicleDaoImpl = ''

    #添加车辆信息实现
    def addVehicle(self,Vehicle):
        py =Pymysql.PyMySQLHelper
        sql = 'insert into vehicle(PlateID,owner,vehicle_identity,SID) VALUES ({0},{1},{2},{3})'.format(
            Vehicle.PlateID,Vehicle.owner,Vehicle.vehicle_identity,Vehicle.SID)
        count = py.update(sql)
        return count

    # 修改车辆信息
    def updateVehicle(self,SID):
        py = Pymysql.PyMySQLHelper
        sql = 'update vehicle set (PlateID,owner,vehicle_identity) VALUES ({0},{1},{2})' \
              ' WHERE SID = {3}'.format(Vehicle.PlateID,Vehicle.owner,Vehicle.vehicle_identity)
        count = py.update(sql)
        return count

    # 删除车辆信息
    def deleteVehicle(self,SID):
        py = Pymysql.PyMySQLHelper
        sql = 'delete from vehicle WHERE SID = {0}'.format(SID)
        count = py.update(sql)
        return count

    # 通过员工号查找车辆信息实现
    def findVehicleBySID(self, SID):
        py = Pymysql.PyMySQLHelper
        sql = 'select * from vehicle where SID = {0}'.format(SID)
        result = py.selectalldictcursor(sql)
        list = []
        for rs in result:
            SID = rs['SID']
            PlateID=['PlateID']
            owner=['owner']
            vehicle_identity=['vehicle_identity']
            vehicle = Vehicle(SID, PlateID,owner,vehicle_identity)
            list.append(vehicle)
        return list

    # 通过车牌号查找车辆信息实现
    def findVehicleByPlateID(self, PlateID):
        py = Pymysql.PyMySQLHelper
        sql = "select * from vehicle where PlateID = '%s'"%(PlateID)
        result = py.selectalldictcursor(sql)
        list = []
        for rs in result:
            SID = rs['SID']
            PlateID=['PlateID']
            owner=['owner']
            vehicle_identity=['vehicle_identity']
            vehicle = Vehicle(SID, PlateID,owner,vehicle_identity)
            list.append(vehicle)
        return list

    # 显示所有车辆信息实现
    def showallVehicle(self):
        py = Pymysql.PyMySQLHelper
        sql = 'select * from vehicle'
        result = py.selectalldictcursor(sql)
        list = []
        for rs in result:
            SID = rs['SID']
            PlateID=['PlateID']
            owner=['owner']
            vehicle_identity=['vehicle_identity']
            vehicle = Vehicle(SID, PlateID,owner,vehicle_identity)
            list.append(vehicle)
        return list

