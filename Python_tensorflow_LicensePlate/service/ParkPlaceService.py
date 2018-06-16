from Python_tensorflow_LicensePlate.daoimpl.ParkPlaceImpl import ParkPlaceImpl
from Python_tensorflow_LicensePlate.entity.ParkPlace import ParkPlace


class ParkPlaceService(object):
    """车位业务层"""


    def initparklot(self,innernumber,tempnumber):
        """停车场初始化配置 只使用一次
        根据参数生成相应数量的车位
        :param innernumber: 内部车位数量
        :param tempnumber: 临时车位数量
        :return:
        """
        innerparkplace = ParkPlace()
        innerparkplace.lockStatus = 0
        innerparkplace.parkPlaceType = 0
        for i in range (innernumber):
            ParkPlaceImpl.insertparkplace(innerparkplace)
        tempparkplace = ParkPlace()
        tempparkplace.lockStatus = 0
        tempparkplace.parkPlaceType = 1
        for i in range (tempnumber):
            ParkPlaceImpl().insertparkplace(tempparkplace)

    def addsingletempparkplace(self):
        """增加一个临时车位 """
        parkplace  = ParkPlace()
        parkplace.parkPlaceType = 1
        parkplace.lockStatus = 0
        return ParkPlaceImpl().insertparkplace(parkplace)


    def addsingelinnerparkplace(self):
        """增加一个内部车位
        """
        parkplace = ParkPlace()
        parkplace.parkPlaceType = 0
        parkplace.lockStatus = 0
        return  ParkPlaceImpl().insertparkplace(parkplace)

    def deleteparkplacenyid(self,parkplaceid):

        return ParkPlaceImpl().deleteparkplace(parkplaceid)

    def showparkplaceinformation(self):
        """返回全部车位信息
        :return:
        """
        return ParkPlaceImpl().listall()

    def getinnernumber(self):
        """获取内部车位数量
        :return:
        """
        parkplaceType = 0
        count = ParkPlaceImpl().getcount(parkplaceType)
        return count

    def gettempnumber(self):
        """获取临时车车位数量"""

        parkplaceType = 1
        count =ParkPlaceImpl().getcount(parkplaceType)
        return  count

    def getinuse_innerparlplacecount(self):
        """获取已占用内部车位数量"""

        parkplaceType = 0
        count = ParkPlaceImpl().getinusecount(parkplaceType)
        return  count

    def getinuse_tempparkplacecount(self):
        """获取已占用临时车位数量"""
        parkplaceType = 1
        count = ParkPlaceImpl().getinusecount(parkplaceType)
        return count
    def getempty_innerparkplacecount(self):
        """获取空闲内部车位数量"""
        parkplaceType = 0
        count = ParkPlaceImpl().getemptycount(parkplaceType)
        return  count

    def getempty_tempparkplacecount(self):
        """获取空闲临时车数量"""
        parkplaceType = 1
        count = ParkPlaceImpl().getemptycount(parkplaceType)
        return count

    def lock(self,parkplaceid):
        """上锁
        """
        return ParkPlaceImpl().updatelockstatus(0,parkplaceid)

    def unlock(self,parkplaceid):
        """开锁"""
        return ParkPlaceImpl().updatelockstatus(1,parkplaceid)

    def updateparkplacetype(self,parkplace):
        """更新车位"""
        return ParkPlaceImpl().updateparkplace(parkplace)


