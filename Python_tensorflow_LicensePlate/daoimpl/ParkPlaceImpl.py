from Python_tensorflow_LicensePlate.dao.ParkPlaceDao import ParkPlaceDao
from Python_tensorflow_LicensePlate.utils.Pymysql import PyMySQLHelper
from Python_tensorflow_LicensePlate.entity.ParkPlace import ParkPlace


class ParkPlaceImpl(ParkPlaceDao):
    """车位操作方法实现"""

    def find(self,parkplaceid):
        """根据车位号查找车位信息
        :param parkplaceid: 车位id
        :return: ParkPlace对象
        """
        sql = 'select * from parkplace where parkPlaceID = {0}'.format(parkplaceid)
        result = PyMySQLHelper().selectOnedictcursor(sql)
        parkplace = ParkPlace(result['parkPlaceID'],result['lockStatus'],result[' parkPlaceType'],result['userCarNumber'])

        return parkplace

    def updatecarnumber(self,parkplace):
        """更新车位中的车辆，车辆进入时写入车牌号
        车辆离开时将车牌号切换为null

        :param parkplace:
        :return:返回受影响行数
        """

        sql = ('update  parkplace  set userCarNumber = {0} where parkPlaceID = '
               '{1}'.format(parkplace.userCarNumber,parkplace.parkPlaceID))
        count = PyMySQLHelper().update(sql)
        return count

    def switchtotemp(self, parkplaceid):
        """
        切换车位类型为临时车
        :param parkplaceid:车位id
        :return: 受影响记录条数
        """
        sql = ('update  parkplace  set parkPlaceType = 1 where parkPlaceID =(%s) '
               +str(parkplaceid))
        count = PyMySQLHelper().update(sql)
        return count

    def switchtoinner(self, parkplaceid):
        """切换车位类型为内部专用车位
        :param parkplaceid: 车位id
        :return: 受影响记录条数
        """
        sql = 'update  parkplace  set parkPlaceType = 0 where parkPlaceID =(%s) ' + str(parkplaceid)
        count = PyMySQLHelper().update(sql)
        return count

    def insertparkplace(self, parkplace):
        """插入一个车位
        默认车辆号码为null
        :param parkplace:ParkPlace
        :return: 返回插入条数
        """
        sql = 'insert into  parkplace  (lockStatus,parkPlaceType)VALUES (%s,%s)'
        params = (parkplace.parklockID,parkplace.parkPlaceType)
        count = PyMySQLHelper().update(sql,params)
        return count

    def deleteparkplace(selfself, parkplaceid):
        """删除车位

        :param parkplaceid:车位号
        :return:
        """
        sql = 'delete from  parkplace  WHERE parkPlaceID='+str(parkplaceid)

        count = PyMySQLHelper().update(sql)
        return count

    def updateparkplace(self, parkplace):
        """更新车位信息
        :param parkplace:车位
        :return:
        """
        sql = 'update  parkplace set (lockStatus,parkPlaceType,userCarNumber)VALUES (%s,%s,%s)'
        params = (parkplace.lockStatus,parkplace.parkPlaceType,parkplace.userCarNumber)
        count = PyMySQLHelper().update(sql,params)
        return count

    def listall(self):
        """返回全部车位详细信息
        :return: 车位列表
        """
        sql = 'select * from parkplace'
        result = PyMySQLHelper().selectalldictcursor(sql)
        list = []
        for rs in result:
            parkplace = ParkPlace(rs['parklockID'],rs['lockStatus'],rs['parkPlaceType'],
                                  rs['userCarNumber'])
            list.append(parkplace)

        return list

    def getcount(self, parkPlaceType):
        """根据传入车位类型获取相应车位的数量
        :param parkPlaceType: 车位类型，0：内部车位,1：临时车车位
        :return:数量
        """
        sql = ('SELECT COUNT(parkPlaceType) FROM parkplace WHERE parkPlaceType = '
               '{0}'.format(parkPlaceType))
        rs = PyMySQLHelper().selectOnedictcursor(sql)
        count = rs['COUNT(parkPlaceType)']
        return count

    def getemptycount(self, parkPlaceType):
        """根据传入的车位类型获取相应车位的剩余空位数量
        :param parkPlaceType: 车位型 0:内部车位 1：临时车车位
        :return: 数量
        """
        sql = ('SELECT COUNT(parkPlaceType) FROM parkplace WHERE'
               ' parkPlaceType = {0} and useCarNumber is  NULL').format(parkPlaceType)
        rs = PyMySQLHelper().selectOnedictcursor(sql)
        count = rs['COUNT(parkPlaceType)']
        return  count

    def getinusecount(self, parkPlaceType):
        """获取已占用的车位数量，
        根据传入的车位类型返回相应的数量
        :param parkPlaceType:车位类型 0：内部车位 1：临时车车位
        :return: 数量
        """
        sql = ('SELECT COUNT(parkPlaceType) FROM parkplace WHERE'
               ' parkPlaceType = {0} and useCarNumber is NOT NULL').format(parkPlaceType)
        rs = PyMySQLHelper().selectOnedictcursor(sql)
        count = rs['COUNT(parkPlaceType)']
        return count

    def updatelockstatus(self, lockstatus,parkPlaceID):
        """更新车位的锁状态

        :param parkplace: 车位锁状态 0：关闭 1：打开
        :return:
        """
        sql =( 'update parkplace set lockStatus = {0} '
               'WHERE  parkPlaceID = {1}'.format(lockstatus,parkPlaceID))
        count = PyMySQLHelper().update(sql)
        return count