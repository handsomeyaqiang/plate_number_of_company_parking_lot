class Staff:
    def __init__(self, name, SID,vehicleQuantity,phoneNumber,department,gender):
        self.name = name
        self.SID=SID
        self.department=department
        self.vehicleQuantity = vehicleQuantity
        self.phoneNumber= phoneNumber
        self.gender=gender

    # def __init__(self):
    #     print("hello")

    def setName(self,  name):
        self.name = name

    def getName(self):
        return self.name

    def setGender(self,gender):
        self.gender = gender

    def getGender(self):
        return self.gender

    def setDepartment(self,department):
        self.department = department

    def getDepartment(self):
        return self.department

    def setSID(self,staffnum):
        self.SID = staffnum

    def getSID(self):
        return self.SID

    def setVehicleQuantity(self,vehicleQuantity):
        self.vehicleQuantity = vehicleQuantity

    def getVehicleQuantity(self):
        return self.vehicleQuantity

    def setPhoneNumber(self,phoneNumber):
        self.phoneNumber = phoneNumber

    def getPhoneNumber(self):
        return self.phoneNumber