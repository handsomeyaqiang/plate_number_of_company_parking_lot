from Python_tensorflow_LicensePlate.daoimpl.RecongiseDaoImpl import RecongiseDaoImpl
from Python_tensorflow_LicensePlate.daoimpl.VehicleDaoImpl import VehilceDaoImpl
from Python_tensorflow_LicensePlate.daoimpl.RecordImpl import RecordImpl
from Python_tensorflow_LicensePlate.entity.Record import Record
import time
class RecongiseService:
    def recongiseIN(self):
        plateNum = RecongiseDaoImpl.recongise()
        if plateNum != '':
            vehicle = VehilceDaoImpl.findVehicleByPlateID(plateNum)
            record = Record()
            record.__setattr__("platenumber", plateNum)
            record.__setattr__("intime", time.localtime())
            record.__setattr__("feestatus", 0)
            if vehicle != None:
                record.__setattr__("vehicletype", 0)
            else:
                record.__setattr__("vehicletype", 1)
            RecordImpl.insertRecord(record)
        else:
            return False

    def recongiseIN(self):
        pass
