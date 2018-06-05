class ParkPlace:
    '停车位类'

    def __init__(self, parkplace_number, parklock, parkplace_type):
        self.parkplace_number = parkplace_number
        self.parklock = parklock
        self.parkplace_type = parkplace_type

    def showinformation(self):
        return self.parkplace_number, self.parklock.isLocked(), self.parkplace_type
