# from Python_tensorflow_LicensePlate.entity.Vehicle import Vehicle
# from Python_tensorflow_LicensePlate.daoimpl.VehicleDaoImpl import VehilceDaoImpl
from Python_tensorflow_LicensePlate.daoimpl.StaffDaoImpl import staffDaoImpl
from Python_tensorflow_LicensePlate.entity.Staff import Staff
#from Python_tensorflow_LicensePlate.dao.VehicleDao import VehicleDao

class test:
    def demo(self):
        imp=staffDaoImpl()
        #staff=Staff('yan1','0008',3,'11837161085','人事部',0)
        re=imp.deleteStaff('0008')
        print(re)

if __name__ == '__main__':
    t = test()
    t.demo()


