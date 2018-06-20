from Python_tensorflow_LicensePlate.daoimpl.StaffDaoImpl import staffDaoImpl
from Python_tensorflow_LicensePlate.utils.ParkResult import ParkResult
class StaffService(object):
    #员工信息管理业务层

    # 登记员工信息
    def addStaff(self, staff):
        result = ParkResult()
        try:
            staffDaoImpl().addStaff(staff)
            return result.ok()
        except:
            return result.error("添加员工失败！")


    #删除员工信息
    def deleteStaff(self,SID):
        count=staffDaoImpl().deleteStaff(SID)
        if count==0:
            return False
        return True

    #修改员工信息
    def updateStaff(self,Staff):
        count=staffDaoImpl().updateStaff(Staff)
        if count==0:
            return False
        else:
            return True

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
        list = staffDaoImpl.findStaffByName(SID)
        if len(list) == 0:
            return False
        else:
            return list


    # 按照员工姓名查找员工信息
    def findStaffByName(self,name):
        list=staffDaoImpl.findStaffByName(name)
        if len(list)==0:
            return False
        else:
            return list



