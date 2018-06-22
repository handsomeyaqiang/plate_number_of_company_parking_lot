from Python_tensorflow_LicensePlate.daoimpl.StaffDaoImpl import staffDaoImpl
from Python_tensorflow_LicensePlate.utils.ParkResult import ParkResult
class StaffService(object):
    #员工信息管理业务层

    # 登记员工信息
    def addStaff(self, staff):
        result = ParkResult()
        try:
            staffDaoImpl().addStaff(staff)
            return result.ok2()
        except Exception as e:
            print(e)
            return result.error("添加员工失败！")


    #删除员工信息
    def deleteStaff(self,SID):
        result = ParkResult()
        try:
            staffDaoImpl().deleteStaff(SID)
            return result.ok2()
        except:
            return result.error("删除员工失败！")

    #修改员工信息
    def updateStaff(self,Staff):
        result = ParkResult()
        try:
            staffDaoImpl().updateStaff(Staff)
            return result.ok2()
        except:
            return result.error("修改员工失败！")

    #员工信息展示
    def showStaff(self):
        result = ParkResult()
        try:
            s = staffDaoImpl()
            list = s.showallStaff()
            return result.ok(list)
        except Exception as e:
            print(e)
            return result.error("查询员工信息失败！")

    #按照工号查询员工信息
    def findStaffById(self,SID):
        result = ParkResult()
        try:
            s = staffDaoImpl()
            list = s.findStaffBySid(SID)
            return result.ok(list)
        except Exception as e:
            print(e)
            return result.error("查询员工信息失败！")


    # 按照员工姓名查找员工信息
    def findStaffByName(self,name):
        result = ParkResult()
        try:
            s = staffDaoImpl()
            list = s.findStaffByName(name)
            return result.ok(list)
        except Exception as e:
            print(e)
            return result.error("查询员工信息失败！")


    # 按照部门查找员工信息
    def findStaffByDepart(self,depart):
        result = ParkResult()
        try:
            s = staffDaoImpl()
            list = s.findStaffByDepartment(depart)
            return result.ok(list)
        except Exception as e:
            print(e)
            return result.error("查询员工信息失败！")



