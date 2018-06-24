from Python_tensorflow_LicensePlate.service.RecordService import RecordService

class RecordController:
    def findRecordByPid(self,pid):
        s = RecordService()
        return s.ListRecordByPlateID(pid)

    def findRecordByIntime(self,time):
        s = RecordService()
        return s.ListRecordByIntime(time)

    def findRecordByOuttime(self,time):
        s = RecordService()
        return s.ListRecordByOuttime(time)

    def findRecordType(self,type):
        s = RecordService()
        return s.ListRecordByType(type)



