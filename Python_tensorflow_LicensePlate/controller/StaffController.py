from Python_tensorflow_LicensePlate.service.StaffService import StaffService
from Python_tensorflow_LicensePlate.entity.Staff import Staff

class StaffController:

    def insertStaff(self, StaffNum, carNum, name, phone, gender, department):
        staff = Staff()
        staff.setDepartment(department)
        staff.setGender(gender)
        staff.setName(name)
        staff.setPhoneNumber(phone)
        staff.setSID(StaffNum)
        staff.setVehicleQuantity(carNum)
        s = StaffService()
        result = s.addStaff(staff)
        return result

    def showStaff(self):
        s = StaffService()
        return s.showStaff()
