from Python_tensorflow_LicensePlate.service.VehicleService import VehicleService
from Python_tensorflow_LicensePlate.entity.Vehicle import Vehicle

class VehicleController:

    def insertVehicle(self, PlateID, owner, Vehicle_identity, SID):
        vehicle = Vehicle(PlateID, owner, Vehicle_identity, SID)
        s = VehicleService()
        result = s.addVehicle(vehicle)
        return result

    def updVehicle(self, PlateID, owner, Vehicle_identity, SID):
        vehicle = Vehicle(PlateID, owner, Vehicle_identity, SID)
        s = VehicleService()
        result = s.updateVehicle(vehicle)
        return result

    def showVehicle(self):
        s = VehicleService()
        return s.showVehicle()

    def delVehicle(self,rid):
        s = VehicleService()
        return s.deleteVehicle(rid)

    def findVehicleByid(self,sid):
        s = VehicleService()
        return s.findVehicleById(sid)

    def findVehicleByplatenum(self,platenum):
        s = VehicleService()
        return s.findVehicleByPlateNum(platenum)





