from Python_tensorflow_LicensePlate.service.RecordService import RecordService

class RecordController:
    def findRecordByPid(self,pid):
        s = RecordService()
        return s.ListRecordByPlateID(pid)

    def findRecordByYear(self,year):
        s = RecordService()
        return s.ListRecordByPlateID(year)

    def findRecordByMonth(self,month):
        s = RecordService()
        return s.ListRecordByMonth(month)

    def findRecordByDay(self,day):
        s = RecordService()
        return s.ListRecordByDay(day)



