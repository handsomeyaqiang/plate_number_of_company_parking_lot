
class Vehicle:
    def __init__(self, licensePlateNumber, owner,vehicle_identity,staff_id):
        self.licensePlateNumber = licensePlateNumber
        self.owner=owner
        self.vehicle_identity=vehicle_identity
        self.vehicleQuantity = vehicle_identity
        self.staff_id= staff_id

    def setLicensePlateNumber(self,  licensePlateNumber):
        self._licensePlateNumber = licensePlateNumber

    def getLicensePlateNumber(self):
        return self._licensePlateNumber

    def setOwner(self,owner):
        self._owner = owner

    def getOwner(self):
        return self._owner

    def setVehicle_identity(self,vehicle_identity):
        self._vehicle_identity = vehicle_identity

    def getVehicle_identity(self):
        return self._vehicle_identity

    def setStaff_id(self,staff_id):
        self._staff_id = staff_id

    def getStaff_id(self):
        return self._staff_id

