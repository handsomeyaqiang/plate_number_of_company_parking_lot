from Python_tensorflow_LicensePlate.daoimpl.RecordImpl import RecordImpl


class RecordService(object):
    def ListRecordByyear(self,year):
        #根据时间年获得车辆记录
        list = RecordImpl().findRecordByYear(year)
        return list

    def ListRecordByMonth(self,month):
        #根据时间月查询车辆记录
        list = RecordImpl().findRecordByMonth(month)
        return list

    def ListRecordByDay(self,day):
        #根据时间天获得车辆记录
        list = RecordImpl().findRecordByDay(day)
        return list

    def ListRecordByPlateID(self,platenumber):
        #根据车牌号查询车辆记录
        list = RecordImpl().findRecordByPlateNumber(platenumber)
        return list

