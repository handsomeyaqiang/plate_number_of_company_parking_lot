from Python_tensorflow_LicensePlate.dao import RecordDao
from Python_tensorflow_LicensePlate.utils import Pymysql
from Python_tensorflow_LicensePlate.entity.Record import Record

class RecordImpl(RecordDao):

    # 车辆进入时的信息登记
    def insertRecord(self, record):
        sql = 'insert into record(platenumber, intime, vehicletype, feestatus) values(%s,%s,%s,%s,%s)'
        params = (record.platenumber, record.intime, record.vehicletype, record.feestatus)
        Pymysql.PyMySQLHelper.updateByParam(sql, params)

    # 车辆离开时的信息更新
    def updateRecord(self, record):
        sql = 'update record set outtime = %s, feestatus = %s where platenumber = %s'
        params = (record.outtime, record.feestatus, record.platenumber)
        Pymysql.PyMySQLHelper.selectOneByParam(sql, params)

    # 根据车辆记录的id删除记录
    def deleteRecordByRid(self, rid):
        py = Pymysql.PyMySQLHelper()
        sql = 'delete from record WHERE rid =%s'
        params = (rid)
        count = py.updateByParam(sql, params)
        return count

    # 根据车辆记录的车牌号删除记录
    def deleteRecordByPlateNumber(self, platenumber):
        py = Pymysql.PyMySQLHelper()
        sql = 'delete from record WHERE platenumber =%s'
        params = (platenumber)
        count = py.updateByParam(sql, params)
        return count

    #根据车牌号查找车辆记录
    def findRecordByPlateID(self, platenumber):
        py = Pymysql.PyMySQLHelper()
        sql = "select * from record where platenumber = '%s'"%(platenumber)
        result = py.selectalldictcursor(sql)
        list = []
        for rs in result:
            rid=rs['rid']
            PNumber = rs['platenumber']
            intime = rs['intime']
            outtime = rs['outtime']
            vehicletype = rs['vehicletype']
            feestatus = rs['feestatus']
            record = Record(rid,PNumber, intime, outtime, vehicletype, feestatus)
            list.append(record)
        return list


    # 根据车辆离开时间按年查找车辆记录
    def findRecordByYear(self, year):
        py = Pymysql.PyMySQLHelper()
        sql = "select * from record WHERE DATE_FORMAT(outtime,'%%Y') = %s"
        params = (year)
        result=py.selectAllByParam(sql,params)
        list = []
        for rs in result:
            rid=rs['rid']
            PNumber = rs['platenumber']
            intime = rs['intime']
            outtime = rs['outtime']
            vehicletype = rs['vehicletype']
            feestatus = rs['feestatus']
            record = Record(rid,PNumber, intime, outtime, vehicletype, feestatus)
            list.append(record)
        return list

    # 根据车辆离开时间按月查找车辆记录
    def findRecordByMonth(self, month):
        py = Pymysql.PyMySQLHelper()
        sql = "select * from record WHERE DATE_FORMAT(outtime,'%%Y-%%m') = %s"
        params = (month)
        result = py.selectAllByParam(sql, params)
        list = []
        for rs in result:
            rid = rs['rid']
            PNumber = rs['platenumber']
            intime = rs['intime']
            outtime = rs['outtime']
            vehicletype = rs['vehicletype']
            feestatus = rs['feestatus']
            record = Record(rid, PNumber, intime, outtime, vehicletype, feestatus)
            list.append(record)
        return list

    # 根据车辆离开时间按日查找车辆记录
    def findRecordByDay(self, day):
        py = Pymysql.PyMySQLHelper()
        sql = "select * from record WHERE DATE_FORMAT(outtime,'%%Y-%%m-%%d') = %s"
        params = (day)
        result = py.selectAllByParam(sql, params)
        list = []
        for rs in result:
            rid = rs['rid']
            PNumber = rs['platenumber']
            intime = rs['intime']
            outtime = rs['outtime']
            vehicletype = rs['vehicletype']
            feestatus = rs['feestatus']
            record = Record(rid, PNumber, intime, outtime, vehicletype, feestatus)
            list.append(record)
        return list



