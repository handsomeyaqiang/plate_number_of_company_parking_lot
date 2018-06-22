from Python_tensorflow_LicensePlate.service.ParkPlaceService import ParkPlaceService
from Python_tensorflow_LicensePlate.entity.ParkPlace import ParkPlace


class ParkPlaceController(object):
    """车位管理控制层"""

    def initparklot(self, innernumber, tempnumber):
        """初始化车位数量，根据输入的数量生成相应数量的车位"""
        rs = ParkPlaceService().initparklot(innernumber, tempnumber)
        return rs

    def addsingletempparkplace(self):
        """增加一个临时车位"""
        rs = ParkPlaceService().addsingletempparkplace()
        return rs

    def addsingleinnerparkplace(self):
        """增加一个内部车位"""
        rs = ParkPlaceService().addsingelinnerparkplace()
        return rs

    def adddulparkplace(self, type, number):
        """增加多个车位"""
        rs = ParkPlaceService().adddulparkplace(type, number)
        return rs

    def deleteparkplacebyid(self, parkplaceid):
        """根据车位号删除车位"""
        rs = ParkPlaceService().deleteparkplacenyid(parkplaceid)
        return rs

    def getempty_innerparkplacecount(self):
        """获取空闲内部车位数量"""
        rs = ParkPlaceService().getempty_innerparkplacecount()
        return rs

    def getempty_tempparkplacecount(self):
        """获取空闲临时车位数量"""
        rs = ParkPlaceService().getempty_tempparkplacecount()
        return rs

    def getinnernumber(self):
        """获取内部车位数量"""
        rs = ParkPlaceService().getinnernumber()
        return rs

    def getinuse_innerparlplacecount(self):
        """获取已占用的内部车位数量"""
        rs = ParkPlaceService().getinuse_innerparlplacecount()
        return rs

    def getinuse_tempparkplacecount(self):
        """获取已占用的临时车位数量"""
        rs = ParkPlaceService().getinuse_tempparkplacecount()
        return rs

    def gettempnumber(self):
        """获取临时车位数量"""
        rs = ParkPlaceService().gettempnumber()
        return rs

    def lock(self, parkplaceid):
        """根据传入的车位号进行关锁操作"""
        rs = ParkPlaceService().lock(parkplaceid)
        return rs

    def showparkplaceinformation(self):
        """显示全部车位信息"""
        rs = ParkPlaceService().showparkplaceinformation()
        return rs

    def unlock(self, parkplaceid):
        """根据传入的车位号进行打开锁操作"""
        rs = ParkPlaceService().unlock(parkplaceid)
        return rs

    def updateparkplace(self, parkPlaceID, lockStatus, parkPlaceType, useCarNumber):
        """更新车位信息"""
        parkplace = ParkPlace(lockStatus, parkPlaceType, useCarNumber)
        parkplace.parkPlaceID = parkPlaceID
        rs = ParkPlaceService().updateparkplace(parkplace)
        return rs

    def allocateparkplace(self, carnumber, type):
        """
        进入停车场时根据车辆类型随机分配相应类型的车位
        :param carnumber: 车牌号
        :param type: 车辆类型 0 内部车 1 临时车
        :return: rs中的data属性携带所分配的车位号
        """
        rs = ParkPlaceService().allocateparkplace(carnumber, type)
        return rs

    def reclaimparkpalce(self, parkplaceid):
        """
        离开停车场时，根据传入的车位号回收车位
        :param parkplaceid: 车位号
        :return:
        """
        rs = ParkPlaceService().reclaimparkpalce(parkplaceid)
        return rs
