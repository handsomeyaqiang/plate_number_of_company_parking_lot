from Python_tensorflow_LicensePlate.daoimpl.StaffDaoImpl import staffDaoImpl

class StaffService(object):
    #员工信息管理业务层

    #登记员工信息
    def addStaff(self,Staff):
        count=staffDaoImpl().addStaff(Staff)
        if count==0:
            return False
        return True

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
        list = staffDaoImpl.showallStaff()
        if len(list) == 0:
            return False
        else:
            return list

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



