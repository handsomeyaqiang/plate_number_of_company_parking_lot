from Python_tensorflow_LicensePlate.service.RecongiseService import RecongiseService
from Python_tensorflow_LicensePlate.daoimpl.RecordImpl import RecordImpl
from Python_tensorflow_LicensePlate.service.ChargeService import ChargeService

class RecongiseTest:

    def recongiseInDemo(self):
        r = RecongiseService()
        result = r.recongise_in()
        if result.status == 200:
            resultData = result.data
            print(resultData.plate_num, resultData.vehicle_type, resultData.park_place_id, resultData.money)
        else:
            print(result.msg)

    def recongise_outdemo(self):
        r = RecongiseService()
        result = r.recongise_out()
        if result.status == 200:
            resultData = result.data
            print(resultData.plate_num, resultData.vehicle_type, resultData.park_place_id, resultData.money)
        else:
            print(result.msg)

    def getSingleDemo(self):
        recordDao = RecordImpl()
        record = recordDao.getSingleRecordByPlateId("京B82343")
        print(record)

    def charge_demo(self):
        charge = ChargeService()
        money = charge.charge("2018-06-22 11:21:12", "2018-06-25 18:30:44")
        print(money)

if __name__ == '__main__':
   r = RecongiseTest()
   #r.recongiseInDemo()
   #r.recongise_outdemo()
   # r.getSingleDemo()
   #r.charge_demo()
