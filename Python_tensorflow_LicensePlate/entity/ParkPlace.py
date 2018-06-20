class ParkPlace(object):
    '停车位类'

    def __init__(self,  lockStatus, parkPlaceType,useCarNumber):
        self.parkPlaceID = None
        self.lockStatus = lockStatus
        self.parkPlaceType = parkPlaceType
        self.useCarNumber = useCarNumber


