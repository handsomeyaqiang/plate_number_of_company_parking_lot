
class Vehicle:
    def __init__(self,SID, PlateID, owner,vehicle_identity):
        self.PlateID = PlateID
        self.owner=owner
        self.vehicle_identity=vehicle_identity
        self.SID= SID

    def setPlateID(self,  PlateID):
        self.PlateID = PlateID

    def getPlateID(self):
        return self.PlateID

    def setOwner(self,owner):
        self.owner = owner

    def getOwner(self):
        return self.owner

    def setVehicle_identity(self,vehicle_identity):
        self.vehicle_identity = vehicle_identity

    def getVehicle_identity(self):
        return self.vehicle_identity

    def setSID(self,SID):
        self.SID = SID

    def getStaff_id(self):
        return self.SID

