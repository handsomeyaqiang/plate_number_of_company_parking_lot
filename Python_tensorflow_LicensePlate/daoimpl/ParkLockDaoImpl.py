from Python_tensorflow_LicensePlate.entity.ParkLock import ParkLock
from Python_tensorflow_LicensePlate.dao.ParkLockDao import ParkLockDao
from ..utils.Pymysql import PyMySQLHelper


class ParkLockDaoImpl(ParkLockDao):
    """ParkLockDao实现"""

    def isLocked(self, parklock):
        sql = str('select status from parklock where ParkLockID = ' + str(parklock.ParkLockID))
        result = PyMySQLHelper().selectOne(sql)
        return result[0]

    def findlock(self,parklockid):
        sql = str('select * from parklock where ParkLockID = ' + str(parklockid))
        result = PyMySQLHelper().selectOnedictcursor(sql)
        ParkLockID = result['ParkLockID']
        status = result['status']
        parklock = ParkLock(ParkLockID, status)
        return parklock

    def lock(self, parklock):
        sql = str("update  parklock  set status = 1 where ParkLockID = " + str(parklock.ParkLockID))
        count = PyMySQLHelper().update(sql)
        return count

    def unlock(self, parklock):
        sql = str('update  parklock  set status = 0 where ParkLockID = ' + str(parklock.ParkLockID))
        count = PyMySQLHelper().update(sql)
        return count

    def addlock(self, parklock):
        sql = 'insert into parklock ( ParkLockID) VALUES (%s) '
        params = (parklock.ParkLockID)
        count = PyMySQLHelper().updateByParam(sql, params)
        return count
    def deleteparklock(selfself, parklockid):
        sql = 'delete from  parklock  WHERE ParkLockID='+str(parklockid)

        count = PyMySQLHelper().update(sql)
        return count

    def updateparklock(self,parklock):
        sql = "update  parklock  set status ={0} where ParkLockID = {1}".format(parklock.status,parklock.ParkLockID)
        count = PyMySQLHelper().update(sql)
        return count

    def listlock(self):
        sql = 'select * from parklock'
        result = PyMySQLHelper().selectalldictcursor(sql)
        list = []
        for rs in result:
            ParkLockID = rs['ParkLockID']
            status = rs['status']
            parklock = ParkLock(ParkLockID,status)
            list.append(parklock)
        return list
