from Python_tensorflow_LicensePlate.daoimpl.StaffDaoImpl import staffDaoImpl
from Python_tensorflow_LicensePlate.entity.Staff import Staff
from Python_tensorflow_LicensePlate.service.StaffService import StaffService

class staffdemo:

    def serviceDemo(self):
        s = StaffService()
        result = s.showStaff()
        if result.status == 200:
            for staff in result.data:
                print(staff.getName())

    def getshow(self):
        sd = staffDaoImpl()
        list = sd.showallStaff()
        for l in list:
            print(l)

    def test(self):
        staff = Staff()
        staff.setVehicleQuantity(1)
        staff.setSID('0006')
        staff.setPhoneNumber('1536464515')
        staff.setName('vivo')
        staff.setGender(0)
        staff.setDepartment("卡发布")
        sd = staffDaoImpl()
        count = sd.addStaff(staff)
        print(count)

if __name__ == '__main__':
    s = staffdemo()
    s.serviceDemo()
