class Staff:
    def __init__(self, name, SID,vehicleQuantity,phoneNumber,departure,gender):
        self.name = name
        self.SID=SID
        self.departure=departure
        self.vehicleQuantity = vehicleQuantity
        self.phoneNumber= phoneNumber
        self.gender=gender

    def setName(self,  name):
        self._name = name

    def getName(self):
        return self._name

    def setGender(self,gender):
        self._gender = gender

    def getGender(self):
        return self._gender

    def setDeparture(self,departure):
        self._departure = departure

    def getDeparture(self):
        return self._departure

    def setSID(self,staffnum):
        self._SID = staffnum

    def getSID(self):
        return self._SID

    def setVehicleQuantity(self,vehicleQuantity):
        self._vehicleQuantity = vehicleQuantity

    def getVehicleQuantity(self):
        return self._vehicleQuantity

    def setPhoneNumber(self,phoneNumber):
        self._phoneNumber = phoneNumber

    def getPhoneNumber(self):
        return self._phoneNumber