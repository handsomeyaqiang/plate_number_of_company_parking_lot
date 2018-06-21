from abc import ABCMeta, abstractmethod
#抽象类
class staffDao(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        self.staffDao = ''

    #添加员工信息
    @abstractmethod
    def addStaff(self,Staff):
        pass

    #修改员工信息
    @abstractmethod
    def updateStaff(self,Staff):
        pass

    #根据员工号查找员工
    @abstractmethod
    def findStaffBySid(self,SID):
        pass

    #根据员工姓名查找员工
    @abstractmethod
    def findStaffByName(self,name):
        pass

    #根据员工部门查找员工
    @abstractmethod
    def findStaffByDepartment(self,depart):
        pass

    #显示所有员工
    @abstractmethod
    def showallStaff(self):
        pass

    #删除员工信息
    @abstractmethod
    def deleteStaff(self,SID):
        pass