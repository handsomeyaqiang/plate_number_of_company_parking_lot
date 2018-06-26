from Python_tensorflow_LicensePlate.dao import RecordDao
from Python_tensorflow_LicensePlate.utils import Pymysql
from Python_tensorflow_LicensePlate.entity.Record import Record

class RecordImpl(RecordDao.RecordDao):

    # 车辆进入时的信息登记
    def insertRecord(self, record):
        py = Pymysql.PyMySQLHelper()
        sql = 'insert into record(platenumber, intime, outtime, vehicletype, leavestatus) values(%s,%s,%s,%s,%s)'
        params = (record.platenumber, record.intime, record.outtime, record.vehicletype, record.leavestatus)
        py.updateByParam(sql, params)

    # 车辆离开时的信息更新
    def updateRecord(self, record):
        py = Pymysql.PyMySQLHelper()
        sql = 'update record set outtime = %s, leavestatus = %s where platenumber = %s'
        params = (record.outtime, record.leavestatus, record.platenumber)
        py.updateByParam(sql, params)

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
        sql = "select platenumber,intime,outtime,vehicletype,leavestatus from record  where platenumber ='%s'"%(platenumber)
        result = py.selectalldictcursor(sql)
        list = []
        for rs in result:
            PNumber = rs['platenumber']
            intime = rs['intime']
            outtime = rs['outtime']
            vehicletype = rs['vehicletype']
            feestatus = rs['leavestatus']
            record = Record(PNumber, intime, outtime, vehicletype, feestatus)
            list.append(record)
        return list

    def getSingleRecordByPlateId(self, plate_num):
        py = Pymysql.PyMySQLHelper()
        sql = "select * from record where platenumber = '%s' and leavestatus = 0" %(plate_num)
        result = py.selectOnedictcursor(sql)
        if result != None:
            record = Record(result['platenumber'], result['intime'], result['outtime'], result['vehicletype'], result['leavestatus'])
            return record
        else:
            return None

    # 根据车辆进入时间查找车辆记录
    def findRecordByInTime(self, time):
        py = Pymysql.PyMySQLHelper()
        # args = ('%'+year+'%')
        # sql = "select platenumber,intime,outtime,vehicletype from record where outtime like '%s'" % args
        sql = "select * from record where intime like '%%%s%%'" % (time)
        result = py.selectalldictcursor(sql)
        list = []
        for rs in result:
            PNumber = rs['platenumber']
            intime = rs['intime']
            outtime = rs['outtime']
            vehicletype = rs['vehicletype']
            leavestaus = rs['leavestatus']
            record = Record(PNumber, intime, outtime, vehicletype, leavestaus)
            list.append(record)
        return list

    # 根据车辆离开时间查找车辆记录
    def findRecordByOutTime(self, time):
        py = Pymysql.PyMySQLHelper()
        sql = "select * from record where outtime like '%%%s%%'" % (time)
        result = py.selectalldictcursor(sql)
        list = []
        for rs in result:
            PNumber = rs['platenumber']
            intime = rs['intime']
            outtime = rs['outtime']
            vehicletype = rs['vehicletype']
            leavestaus = rs['leavestatus']
            record = Record(PNumber, intime, outtime, vehicletype,leavestaus)
            list.append(record)
        return list

    # 根据车辆类型查找车辆记录
    def findRecordByVehicleType(self, type):
        py = Pymysql.PyMySQLHelper()
        sql = "select * from record  where vehicletype ='%s'" % (type)
        result = py.selectalldictcursor(sql)
        list = []
        for rs in result:
            PNumber = rs['platenumber']
            intime = rs['intime']
            outtime = rs['outtime']
            vehicletype = rs['vehicletype']
            leavestaus = rs['leavestatus']
            record = Record(PNumber, intime, outtime, vehicletype,leavestaus)
            list.append(record)
        return list



