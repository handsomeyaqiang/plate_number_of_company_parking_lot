from Python_tensorflow_LicensePlate.dao.ParkPlaceDao import ParkPlaceDao
from Python_tensorflow_LicensePlate.utils.Pymysql import PyMySQLHelper
from Python_tensorflow_LicensePlate.entity.ParkPlace import ParkPlace

class ParkPlaceImpl(ParkPlaceDao):
    def find(self,parkplaceid):
        sql = 'select * from parkplace where parkPlaceID = {0}'.format(parkplaceid)
        result = PyMySQLHelper().selectOnedictcursor(sql)
        parkplace = ParkPlace(result['parkPlaceID'],result[' parkPlaceType'],result['userCarNumber'])

        return parkplace

    def findparkplace(self, parkplace):
        sql = 'select * from parkplace WHERE parkPlaceID ={0} '.format(parkplace.parkPlaceID)

        result = PyMySQLHelper().selectOne(sql)
        return result

    def updatecarnumber(self,parkplace):
        sql = 'update  parkplace  set userCarNumber = {0} where parkPlaceID = {1}'.format(
            parkplace.userCarNumber,parkplace.parkPlaceID)
        count = PyMySQLHelper().update(sql)
        return count
    def switchtotemp(self, parkplace):
        sql = 'update  parkplace  set parkPlaceType = 1 where parkPlaceID =(%s) '+str(parkplace.parkPlaceID)
        count = PyMySQLHelper().update(sql)
        return count

    def switchtoinner(self, parkplace):
        sql = 'update  parkplace  set parkPlaceType = 0 where parkPlaceID =(%s) ' + str(parkplace.parkPlaceID)
        count = PyMySQLHelper().update(sql)
        return count

    def insertparkplace(self, parkplace):
        sql = 'insert into  parkplace  (parkPlaceID,parkLockID,parkPlaceType)VALUES (%s,%s,%s)'
        params = (parkplace.parkPlaceID,parkplace.parklockID,parkplace.parkPlaceType)
        count = PyMySQLHelper().update(sql,params)
        return count

    def deleteparkplace(selfself, parkplaceid):
        sql = 'delete from  parkplace  WHERE parkPlaceID='+str(parkplaceid)

        count = PyMySQLHelper().update(sql)
        return count

    def updateparkplace(self, parkplace):
        sql = 'update  parkplace set (parkLockID,parkPlaceType)VALUES (%s,%s)'
        params = (parkplace.parklockID,parkplace.parkPlaceType)
        count = PyMySQLHelper().update(sql,params)
        return count

    def listall(self):
        sql = 'select * from parkplace'
        result = PyMySQLHelper().selectalldictcursor(sql)
        list = []
        for rs in result:
            parkplace = ParkPlace(rs['parklockID'],rs['parkPlaceType'],
                                  rs['userCarNumber'])
            list.append(parkplace)

        return list
