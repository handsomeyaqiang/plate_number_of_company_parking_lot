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
        sql = "delete from record where rid = {0}".format(rid)
        Pymysql.PyMySQLHelper.update(sql)

    # 根据车辆记录的车牌号删除记录
    def deleteRecordByPlateNumber(self, platenumber):
        sql = "delete from record where platenumber = {0}".format(platenumber)
        Pymysql.PyMySQLHelper.update(sql)

    #根据车牌号查找车辆记录
    def findRecordByPlateID(self, platenumber):
        py = Pymysql.PyMySQLHelper
        sql = 'select * from record where PNumber = {0}'.format(platenumber)
        result = py.selectalldictcursor(sql)
        list = []
        for rs in result:
            PNumber = rs['PNumber']
            intime = rs['intime']
            outtime = rs['outtime']
            vehicletype = rs['vehicletype']
            feestatus = rs['feestatus']
            record = Record(PNumber, intime, outtime, vehicletype, feestatus)
            list.append(record)
        return list

    # 根据车辆离开时间按年查找车辆记录
    def findRecordByYear(self, year):
        py = Pymysql.PyMySQLHelper
        sql = 'select * from record where year(outtime) = {0}'.format(year)
        result = py.selectalldictcursor(sql)
        list = []
        for rs in result:
            PNumber = rs['PNumber']
            intime = rs['intime']
            outtime = rs['outtime']
            vehicletype = rs['vehicletype']
            feestatus = rs['feestatus']
            record = Record(PNumber, intime, outtime, vehicletype, feestatus)
            list.append(record)
        return list

    # 根据车辆离开时间按月查找车辆记录
    def findRecordByMonth(self, month):
        py = Pymysql.PyMySQLHelper
        sql = 'select * from record where month(outtime) = {0}'.format(month)
        result = py.selectalldictcursor(sql)
        list = []
        for rs in result:
            PNumber = rs['PNumber']
            intime = rs['intime']
            outtime = rs['outtime']
            vehicletype = rs['vehicletype']
            feestatus = rs['feestatus']
            record = Record(PNumber, intime, outtime, vehicletype, feestatus)
            list.append(record)
        return list

    # 根据车辆离开时间按日查找车辆记录
    def findRecordByDay(self, day):
        py = Pymysql.PyMySQLHelper
        sql = 'select * from record where day(outtime) = {0}'.format(day)
        result = py.selectalldictcursor(sql)
        list = []
        for rs in result:
            PNumber = rs['PNumber']
            intime = rs['intime']
            outtime = rs['outtime']
            vehicletype = rs['vehicletype']
            feestatus = rs['feestatus']
            record = Record(PNumber, intime, outtime, vehicletype, feestatus)
            list.append(record)
        return list



