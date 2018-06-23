from Python_tensorflow_LicensePlate.daoimpl.RecordImpl import RecordImpl
from Python_tensorflow_LicensePlate.utils.ParkResult import ParkResult

class RecordService(object):
    def ListRecordByyear(self,year):
        #根据时间年获得车辆记录
        result = ParkResult()
        try:
            s = RecordImpl()
            list = s.findRecordByYear(year)
            return result.ok(list)
        except Exception as e:
            print(e)
            return result.error("查询记录信息失败！")

    def ListRecordByMonth(self,month):
        #根据时间月查询车辆记录
        result = ParkResult()
        try:
            s = RecordImpl()
            list = s.findRecordByMonth(month)
            return result.ok(list)
        except Exception as e:
            print(e)
            return result.error("查询记录信息失败！")

    def ListRecordByDay(self,day):
        #根据时间天获得车辆记录
        result = ParkResult()
        try:
            s = RecordImpl()
            list = s.findRecordByDay(day)
            return result.ok(list)
        except Exception as e:
            print(e)
            return result.error("查询记录信息失败！")

    def ListRecordByPlateID(self,platenumber):
        #根据车牌号查询车辆记录
        result = ParkResult()
        try:
            s = RecordImpl()
            list = s
            return result.ok(list)
        except Exception as e:
            print(e)
            return result.error("查询记录信息失败！")

    def saveRecord(self, record):
        recordDao = RecordImpl()
        recordDao.insertRecord(record)
