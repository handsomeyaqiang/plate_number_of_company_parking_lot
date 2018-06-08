
class Vehicle:
    def __init__(self, PlateID, owner,vehicle_identity,SID):
        self.PlateID = PlateID
        self.owner=owner
        self.vehicle_identity=vehicle_identity
        self.SID= SID

    def setPlateID(self,  PlateID):
        self._PlateID = PlateID

    def getPlateID(self):
        return self._PlateID

    def setOwner(self,owner):
        self._owner = owner

    def getOwner(self):
        return self._owner

    def setVehicle_identity(self,vehicle_identity):
        self._vehicle_identity = vehicle_identity

    def getVehicle_identity(self):
        return self._vehicle_identity

    def setSID(self,SID):
        self._SID = SID

    def getStaff_id(self):
        return self._SID

