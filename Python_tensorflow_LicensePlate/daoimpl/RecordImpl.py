from Python_tensorflow_LicensePlate.dao import RecordDao
from Python_tensorflow_LicensePlate.utils import Pymysql
from Python_tensorflow_LicensePlate.entity.Record import Record

class RecordImpl(RecordDao.RecordDao):

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
        sql = "select platenumber,intime,outtime,vehicletype from record  where platenumber ='%s'"%(platenumber)
        result = py.selectalldictcursor(sql)
        list = []
        for rs in result:
            PNumber = rs['platenumber']
            intime = rs['intime']
            outtime = rs['outtime']
            vehicletype = rs['vehicletype']
            record = Record(PNumber, intime, outtime, vehicletype)
            list.append(record)
        return list


    # 根据车辆进入时间查找车辆记录
    def findRecordByInTime(self, time):
        py = Pymysql.PyMySQLHelper()
        # args = ('%'+year+'%')
        # sql = "select platenumber,intime,outtime,vehicletype from record where outtime like '%s'" % args
        sql = "select platenumber,intime,outtime,vehicletype from record where intime like '%%%s%%'" % (time)
        result = py.selectalldictcursor(sql)
        list = []
        for rs in result:
            PNumber = rs['platenumber']
            intime = rs['intime']
            outtime = rs['outtime']
            vehicletype = rs['vehicletype']
            record = Record(PNumber, intime, outtime, vehicletype)
            list.append(record)
        return list

    # 根据车辆离开时间查找车辆记录
    def findRecordByOutTime(self, time):
        py = Pymysql.PyMySQLHelper()
        sql = "select platenumber,intime,outtime,vehicletype from record where outtime like '%%%s%%'" % (time)
        result = py.selectalldictcursor(sql)
        list = []
        for rs in result:
            PNumber = rs['platenumber']
            intime = rs['intime']
            outtime = rs['outtime']
            vehicletype = rs['vehicletype']
            record = Record(PNumber, intime, outtime, vehicletype)
            list.append(record)
        return list

    # 根据车辆类型查找车辆记录
    def findRecordByVehicleType(self, type):
        py = Pymysql.PyMySQLHelper()
        sql = "select platenumber,intime,outtime,vehicletype from record  where vehicletype ='%s'" % (type)
        result = py.selectalldictcursor(sql)
        list = []
        for rs in result:
            PNumber = rs['platenumber']
            intime = rs['intime']
            outtime = rs['outtime']
            vehicletype = rs['vehicletype']
            record = Record(PNumber, intime, outtime, vehicletype)
            list.append(record)
        return list



