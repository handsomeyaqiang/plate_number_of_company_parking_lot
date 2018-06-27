from Python_tensorflow_LicensePlate.entity.Staff import Staff
from Python_tensorflow_LicensePlate.dao.StaffDao import staffDao
from ..utils import Pymysql
#实现类
class staffDaoImpl(staffDao):
    def __init__(self):
        self.staffDaoImpl = ''

    #添加员工信息实现
    def addStaff(self,staff):
        py =Pymysql.PyMySQLHelper()
        sql = 'insert into staff(SID,vehicleQuantity,name,phoneNumber,gender,department) ' \
              'VALUES (%s,%s,%s,%s,%s,%s)'
        params = (staff.SID, staff.vehicleQuantity, staff.name, staff.phoneNumber, staff.gender, staff.department)
        count = py.updateByParam(sql, params)
        return count

    #修改员工信息实现
    def updateStaff(self,Staff):
        py = Pymysql.PyMySQLHelper()
        sql = 'update staff set VehicleQuantity=%s,name=%s,phoneNumber=%s,gender=%s,department=%s WHERE SID =%s'
        params=(Staff.vehicleQuantity,Staff.name,Staff.phoneNumber,Staff.gender,Staff.department,Staff.SID)
        count = py.updateByParam(sql, params)
        return count

    #删除员工信息实现
    def deleteStaff(self, SID):
        py = Pymysql.PyMySQLHelper()
        sql1 = 'delete from vehicle WHERE SID =%s'
        params1 = (SID)
        py.updateByParam(sql1, params1)
        sql = 'delete from staff WHERE SID =%s'
        params = (SID)
        count = py.updateByParam(sql, params)
        return count

    #根据工号查找员工信息实现
    def findStaffBySid(self, SID):
        py = Pymysql.PyMySQLHelper()
        sql = "select * from staff where SID ='%s'"%(SID)
        result = py.selectalldictcursor(sql)
        list = []
        for rs in result:
            SID = rs['SID']
            VehicleQuantity=rs['vehicleQuantity']
            name=rs['name']
            phoneNumber=rs['phoneNumber']
            gender=rs['gender']
            department=rs['department']
            staff = Staff(name, SID, VehicleQuantity, phoneNumber, department, gender)
            list.append(staff)
        return list

    #根据员工姓名查找员工信息实现
    def findStaffByName(self, name):
        py = Pymysql.PyMySQLHelper()
        sql = "select * from staff where name like '%%%s%%'" % (name)
        result = py.selectalldictcursor(sql)
        list = []
        for rs in result:
            SID = rs['SID']
            VehicleQuantity=rs['vehicleQuantity']
            name=rs['name']
            phoneNumber=rs['phoneNumber']
            gender=rs['gender']
            department=rs['department']
            staff = Staff(name, SID, VehicleQuantity, phoneNumber, department, gender)
            list.append(staff)
        return list



        # 根据部门查找员工信息实现

    def findStaffByDepartment(self,depart):
        py = Pymysql.PyMySQLHelper()
        sql = "select * from staff where department = '%s'" % (depart)
        result = py.selectalldictcursor(sql)
        list = []
        for rs in result:
            SID = rs['SID']
            VehicleQuantity = rs['vehicleQuantity']
            name = rs['name']
            phoneNumber = rs['phoneNumber']
            gender = rs['gender']
            department = rs['department']
            staff = Staff(name, SID, VehicleQuantity, phoneNumber, department, gender)
            list.append(staff)
        return list

    #显示所有员工信息实现
    def showallStaff(self):
        py = Pymysql.PyMySQLHelper()
        sql = 'select * from staff'
        result = py.selectalldictcursor(sql)
        list = []
        for rs in result:
            SID = rs['SID']
            VehicleQuantity=rs['vehicleQuantity']
            name=rs['name']
            phoneNumber=rs['phoneNumber']
            gender=rs['gender']
            department=rs['department']
            staff = Staff(name,SID, VehicleQuantity,phoneNumber,department,gender)
            list.append(staff)
        return list

