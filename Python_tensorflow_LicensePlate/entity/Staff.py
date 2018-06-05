class Staff:
    def __init__(self, name, staffNumber,vehicleQuantity,phoneNB,departure,gender):
        self.name = name
        self.staffNumber=staffNumber
        self.departure=departure
        self.vehicleQuantity = vehicleQuantity
        self.phoneNB= phoneNB
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

    def setStaffNumber(self,staffnum):
        self._staffNumber = staffnum

    def getStaffNumber(self):
        return self._staffNumber

    def setDrivinglicenseNumber(self,DrivinglicenseNumber):
        self._drivinglicenseNumber = DrivinglicenseNumber

    def getDrivinglicenseNumber(self):
        return self._drivinglicenseNumber

    def setVehicleQuantity(self,vehicleQuantity):
        self._vehicleQuantity = vehicleQuantity

    def getVehicleQuantity(self):
        return self._vehicleQuantity

    def setPhoneNB(self,phoneNB):
        self._phoneNB = phoneNB

    def getPhoneNB(self):
        return self._phoneNB