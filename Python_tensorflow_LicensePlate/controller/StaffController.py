from Python_tensorflow_LicensePlate.service.StaffService import StaffService
from Python_tensorflow_LicensePlate.entity.Staff import Staff

class StaffController:

    def insertStaff(self, StaffNum, carNum, name, phone, gender, department):
        staff = Staff(name,StaffNum,carNum,phone,department,gender)
        s = StaffService()
        result = s.addStaff(staff)
        return result

    def updStaff(self, StaffNum, carNum, name, phone, gender, department):
        staff = Staff(name, StaffNum, carNum, phone, department, gender)
        s = StaffService()
        result = s.updateStaff(staff)
        return result

    def showStaff(self):
        s = StaffService()
        return s.showStaff()

    def delStaff(self,sid):
        s = StaffService()
        return s.deleteStaff(sid)

    def findStaffByid(self,sid):
        s = StaffService()
        return s.findStaffById(sid)

    def findStaffByname(self,sname):
        s = StaffService()
        return s.findStaffByName(sname)

    def findStaffBydepart(self,depart):
        s = StaffService()
        return s.findStaffByDepart(depart)




