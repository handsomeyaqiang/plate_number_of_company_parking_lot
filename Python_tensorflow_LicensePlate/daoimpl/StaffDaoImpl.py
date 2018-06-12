from Python_tensorflow_LicensePlate.entity.Staff import Staff
from Python_tensorflow_LicensePlate.dao.StaffDao import staffDao
from ..utils import Pymysql
#实现类
class staffDaoImpl(staffDao):
    def __init__(self):
        self.staffDaoImpl = ''

    #添加员工信息实现
    def addStaff(self,Staff):
        py =Pymysql.PyMySQLHelper
        sql = 'insert into staff(SId,vehicleQuantity,name,phoneNumber,gender,department) VALUES ({0},{1},{2},{3},{4},{5})'.format(
            Staff.SID, Staff.vehicleQuantity, Staff.name, Staff.phoneNumber, Staff.gender, Staff._department)
        count = py.update(sql)
        return count

    #修改员工信息实现
    def updateStaff(self,Staff):
        py = Pymysql.PyMySQLHelper
        sql = 'update staff set (VehicleQuantity,name,phoneNumber,' \
              'gender,department) VALUES ({0},{1},{2},{3},{4})' \
              ' WHERE SID = {5}'.format(Staff.vehicleQuantity,Staff.name,Staff.phoneNumber,Staff.phoneNumber,Staff.gender,Staff.department)
        count = py.update(sql)
        return count

    #删除员工信息实现
    def deleteStaff(self, SID):
        py = Pymysql.PyMySQLHelper
        sql = 'delete from staff WHERE SID = {0}'.format(SID)
        count = py.update(sql)
        return count

    #根据工号查找员工信息实现
    def findStaffBySid(self, SID):
        py = Pymysql.PyMySQLHelper
        sql = 'select * from staff where SID = {0}'.format(SID)
        result = py.selectalldictcursor(sql)
        list = []
        for rs in result:
            SID = rs['SID']
            VehicleQuantity=rs['VehicleQuantity']
            name=rs['name']
            phoneNumber=rs['phoneNumber']
            gender=rs['gender']
            department=rs['department']
            staff = Staff(SID, VehicleQuantity,name,phoneNumber,gender,department)
            list.append(staff)
        return list

    #根据员工姓名查找员工信息实现
    def findStaffByName(self, name):
        py = Pymysql.PyMySQLHelper
        sql = "select * from staff where name = '%s'"%(name)
        result = py.selectalldictcursor(sql)
        list = []
        for rs in result:
            SID = rs['SID']
            VehicleQuantity=rs['VehicleQuantity']
            name=rs['name']
            phoneNumber=rs['phoneNumber']
            gender=rs['gender']
            department=rs['department']
            staff = Staff(SID, VehicleQuantity,name,phoneNumber,gender,department)
            list.append(staff)
        return list

    #显示所有员工信息实现
    def showallStaff(self):
        py = Pymysql.PyMySQLHelper
        sql = 'select * from staff'
        result = py.selectalldictcursor(sql)
        list = []
        for rs in result:
            SID = rs['SID']
            VehicleQuantity=rs['VehicleQuantity']
            name=rs['name']
            phoneNumber=rs['phoneNumber']
            gender=rs['gender']
            department=rs['department']
            staff = Staff(SID, VehicleQuantity,name,phoneNumber,gender,department)
            list.append(staff)
        return list

