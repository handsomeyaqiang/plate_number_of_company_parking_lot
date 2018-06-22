from Python_tensorflow_LicensePlate.dao.ParkPlaceDao import ParkPlaceDao
from Python_tensorflow_LicensePlate.utils.Pymysql import PyMySQLHelper
from Python_tensorflow_LicensePlate.entity.ParkPlace import ParkPlace


class ParkPlaceImpl(ParkPlaceDao):
    """车位操作方法实现"""

    def findbyid(self,parkplaceid):
        """根据车位号查找车位信息
        :param parkplaceid: 车位id
        :return: ParkPlace对象
        """
        sql = 'select * from parkplace where parkPlaceID = %s' %(parkplaceid)
        result = PyMySQLHelper().selectOnedictcursor(sql)
        if result != None:
            parkplace = ParkPlace(result['lockStatus'],result['parkPlaceType'],result['useCarNumber'])
            parkplace.parkPlaceID =result['parkPlaceID']
            return parkplace
        else:
            return -1
    def updatecarnumber(self,parkplace):
        """更新车位中的车辆，车辆进入时写入车牌号
        车辆离开时将车牌号切换为null

        :param parkplace:
        :return:返回受影响行数
        """

        sql = ('update  parkplace  set useCarNumber = %s where parkPlaceID = %s' %(parkplace.useCarNumber,parkplace.parkPlaceID))
        count = PyMySQLHelper().update(sql)
        return count

    def switchtotemp(self, parkplaceid):
        """
        切换车位类型为临时车
        :param parkplaceid:车位id
        :return: 受影响记录条数
        """
        sql = ('update  parkplace  set parkPlaceType = 1 where parkPlaceID =(%s) '
               %(parkplaceid))
        count = PyMySQLHelper().update(sql)
        return count

    def switchtoinner(self, parkplaceid):
        """切换车位类型为内部专用车位
        :param parkplaceid: 车位id
        :return: 受影响记录条数
        """
        sql = 'update  parkplace  set parkPlaceType = 0 where parkPlaceID =(%s) '%(parkplaceid)
        count = PyMySQLHelper().update(sql)
        return count

    def insertparkplace(self, parkplace):
        """插入一个车位
        默认车辆号码为null
        :param parkplace:ParkPlace
        :return: 返回插入条数
        """
        sql = 'insert into  parkplace  (lockStatus,parkPlaceType)VALUES (%s,%s)'
        params = (parkplace.lockStatus,parkplace.parkPlaceType)
        count = PyMySQLHelper().updateByParam(sql,params)
        return count

    def deleteparkplace(selfself, parkplaceid):
        """删除车位

        :param parkplaceid:车位号
        :return:
        """
        sql = 'delete from  parkplace  WHERE parkPlaceID=%s'%(parkplaceid)

        count = PyMySQLHelper().update(sql)
        return count

    def updateparkplace(self, parkplace):
        """更新车位信息
        :param parkplace:车位
        :return:
        """
        sql = 'update  parkplace set lockStatus = %s,parkPlaceType = %s,useCarNumber =%s  Where parkPlaceID =%s'
        params = (parkplace.lockStatus,parkplace.parkPlaceType,parkplace.useCarNumber,parkplace.parkPlaceID)
        count = PyMySQLHelper().updateByParam(sql,params)
        return count

    def listall(self):
        """返回全部车位详细信息
        :return: 车位列表
        """
        sql = 'select * from parkplace'
        result = PyMySQLHelper().selectalldictcursor(sql)
        list = []
        for rs in result:
            parkplace = ParkPlace(rs['lockStatus'],rs['parkPlaceType'],rs['useCarNumber'])
            parkplace.parkPlaceID = rs['parkPlaceID']
            list.append(parkplace)

        return list

    def getcount(self, parkPlaceType):
        """根据传入车位类型获取相应车位的数量
        :param parkPlaceType: 车位类型，0：内部车位,1：临时车车位
        :return:数量
        """
        sql = ('SELECT COUNT(parkPlaceType) FROM parkplace WHERE parkPlaceType = %s'%(parkPlaceType))
        rs = PyMySQLHelper().selectOnedictcursor(sql)
        count = rs['COUNT(parkPlaceType)']
        return count

    def getemptycount(self, parkPlaceType):
        """根据传入的车位类型获取相应车位的剩余空位数量
        :param parkPlaceType: 车位型 0:内部车位 1：临时车车位
        :return: 数量
        """
        sql = ('SELECT COUNT(parkPlaceType) FROM parkplace WHERE'
               ' parkPlaceType = %s and useCarNumber is  NULL') %(parkPlaceType)
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
               ' parkPlaceType = %s and useCarNumber is NOT NULL')%(parkPlaceType)
        rs = PyMySQLHelper().selectOnedictcursor(sql)
        count = rs['COUNT(parkPlaceType)']
        return count

    def updatelockstatus(self, lockstatus,parkPlaceID):
        """更新车位的锁状态

        :param parkplace: 车位锁状态 0：关闭 1：打开
        :return:
        """
        sql =( 'update parkplace set lockStatus = %s '
               'WHERE  parkPlaceID = %s'%(lockstatus,parkPlaceID))
        count = PyMySQLHelper().update(sql)
        return count

    def findbytype(self, type):
        """根据车位类型查找车位信息
               :param parkplaceid: 车位类型
               :return: ParkPlace对象列表
               """
        sql = 'select * from parkplace where  parkPlaceType= %s' % (type)
        result = PyMySQLHelper().selectalldictcursor(sql)
        list = []
        if result != None:
            for rs in result:
                parkplace = ParkPlace(rs['lockStatus'], rs['parkPlaceType'], rs['useCarNumber'])
                parkplace.parkPlaceID = rs['parkPlaceID']
                list.append(parkplace)
            return list
        else:
            return -1