from Python_tensorflow_LicensePlate.daoimpl.RecordImpl import RecordImpl
from Python_tensorflow_LicensePlate.utils.ParkResult import ParkResult

class RecordService(object):
    def ListRecordByIntime(self,time):
        #根据进入时间获得车辆记录
        result = ParkResult()
        try:
            s = RecordImpl()
            print("调用impl")
            list = s.findRecordByInTime(time)
            print("获得记录返回")
            return result.ok(list)
        except Exception as e:
            print(e)
            return result.error("查询记录信息失败！")

    def ListRecordByOuttime(self,time):
        #根据车辆离开时间获得车辆记录
        result = ParkResult()
        try:
            s = RecordImpl()
            list = s.findRecordByOutTime(time)
            return result.ok(list)
        except Exception as e:
            print(e)
            return result.error("查询记录信息失败！")

    def ListRecordByType(self,type):
        #根据类型获得车辆记录
        result = ParkResult()
        try:
            s = RecordImpl()
            list = s.findRecordByVehicleType(type)
            return result.ok(list)
        except Exception as e:
            print(e)
            return result.error("查询记录信息失败！")

    def ListRecordByPlateID(self,platenumber):
        #根据车牌号查询车辆记录
        result = ParkResult()
        try:
            s = RecordImpl()
            list = s.findRecordByPlateID(platenumber)
            return result.ok(list)
        except Exception as e:
            print(e)
            return result.error("查询记录信息失败！")

    def saveRecord(self, record):
        recordDao = RecordImpl()
        recordDao.insertRecord(record)
