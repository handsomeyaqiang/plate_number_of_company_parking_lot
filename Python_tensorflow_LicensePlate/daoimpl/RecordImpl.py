from Python_tensorflow_LicensePlate.dao import RecordDao
from Python_tensorflow_LicensePlate.utils import Pymysql

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
