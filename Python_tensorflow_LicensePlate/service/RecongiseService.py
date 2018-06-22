from Python_tensorflow_LicensePlate.daoimpl.RecongiseDaoImpl import RecongiseDaoImpl
from Python_tensorflow_LicensePlate.service.VehicleService import VehicleService
from Python_tensorflow_LicensePlate.service.RecordService import RecordService
from Python_tensorflow_LicensePlate.entity.Record import Record
from Python_tensorflow_LicensePlate.utils.ParkResult import ParkResult
from Python_tensorflow_LicensePlate.service.ChargeService import ChargeService
from Python_tensorflow_LicensePlate.service.FinancialService import FinancialService
from Python_tensorflow_LicensePlate.service.ParkPlaceService import ParkPlaceService
from Python_tensorflow_LicensePlate.entity.RecongiseResult import RecongiseResult
import time


class RecongiseService:

    def recongise_in(self):
        recongiseDao = RecongiseDaoImpl()
        result = ParkResult()
        try:
           plate_num = recongiseDao.recongise()
           vehicleService = VehicleService()
           vehicle = vehicleService.findVehicleByPlateID(plate_num)
           parkPlaceService = ParkPlaceService()
           record = Record()
           current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
           record.__setattr__("platenumber", plate_num)
           record.__setattr__("intime", current_time)
           record.__setattr__("feestatus", 0)
           if vehicle != None:
               record.__setattr__("vehicletype", 0)
               # 分配车位
               parkPlaceService.

               resultData = RecongiseResult(plate_num, 0, None)
           else:
               record.__setattr__("vehicletype", 1)
               # 分配车位
               parkPlaceService.

               resultData = RecongiseResult(plate_num, 1, None)
           recordService = RecordService()
           recordService.insertRecord(record)
           return result.ok(resultData)
        except Exception as e:
            print(e)
            return result.error("识别出现异常")

    def recongise_out(self):

        recongiseDao = RecongiseDaoImpl()
        result = ParkResult()
        # 识别获取车牌
        plate_num = recongiseDao.recongise()
        # 根据车牌判断是否是内部车
        vehicleService = VehicleService()
        vehicle = vehicleService.findVehicleByPlateID(plate_num)
        recordService = RecordService()
        record = recordService.ListRecordByPlateID(plate_num)
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        record.__setattr__("outtime", current_time)
        if vehicle != None:
            recordService.saveRecord(record)
            # 收回车位

            resultData = RecongiseResult(plate_num, 0, None)
            return result.ok(resultData)
        else:
            # 外部车缴费
            chargeService = ChargeService()
            money = chargeService.charge(record.__getattribute__("intime", current_time))
            # 录入缴费记录
            financialService = FinancialService()
            financialService.insertFinancial()
            record.__setattr__("feestatus", 1)
            recordService.saveRecord(record)
            # 收回车位

            resultData = RecongiseResult(plate_num, 1, money)
            return result.ok(resultData)
