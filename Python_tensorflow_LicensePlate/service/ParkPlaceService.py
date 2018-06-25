from Python_tensorflow_LicensePlate.daoimpl.ParkPlaceImpl import ParkPlaceImpl
from Python_tensorflow_LicensePlate.entity.ParkPlace import ParkPlace
from Python_tensorflow_LicensePlate.utils import ParkResult
import random

class ParkPlaceService(object):
    """车位业务层"""

    def initparklot(self, innernumber, tempnumber):
        """停车场初始化配置 只使用一次
        根据参数生成相应数量的车位
        :param innernumber: 内部车位数量
        :param tempnumber: 临时车位数量
        :return:
        """
        result = ParkResult.ParkResult()
        try:
            innerparkplace = ParkPlace(0, 0, None)
            for i in range(innernumber):
                ParkPlaceImpl().insertparkplace(innerparkplace)
            tempparkplace = ParkPlace(0, 1, None)
            for i in range(tempnumber):
                ParkPlaceImpl().insertparkplace(tempparkplace)
            return result.ok2()
        except Exception as e:
            print(e)
            return result.error("初始化停车场车位信息失败！")

    def addsingletempparkplace(self):
        """增加一个临时车位 """
        result = ParkResult.ParkResult()
        try:
            parkplace = ParkPlace(0, 1, None)
            ParkPlaceImpl().insertparkplace(parkplace)
            return result.ok2()
        except Exception as e:
            print(e)
            return result.error("增加一个临时车位失败！")

    def addsingelinnerparkplace(self):
        """增加一个内部车位
        """
        result = ParkResult.ParkResult()
        try:
            parkplace = ParkPlace(0, 0, None)
            ParkPlaceImpl().insertparkplace(parkplace)
            return result.ok2()
        except Exception as e:
            print(e)
            return result.error("增加内部车位失败！")

    def deleteparkplacebyid(self, parkplaceid):
        """删除车位，传入参数为车位号"""
        result = ParkResult.ParkResult()
        try:
            ParkPlaceImpl().deleteparkplace(parkplaceid)
            return result.ok2()
        except Exception as e:
            print(e)
            return result.error("删除车位失败！")

    def showparkplaceinformation(self):
        """返回全部车位信息
        :return:
        """
        result = ParkResult.ParkResult()
        try:
            list = ParkPlaceImpl().listall()
            return result.ok(list)
        except Exception as e:
            print(e)
            return result.error("获取信息失败！")

    def getinnernumber(self):
        """获取内部车位数量
        :return:
        """
        result = ParkResult.ParkResult()
        try:
            parkplaceType = 0
            count = ParkPlaceImpl().getcount(parkplaceType)
            return result.ok(count)
        except Exception as e:
            print(e)
            return result.error("获取内部车位数量失败！")

    def gettempnumber(self):
        """获取临时车车位数量"""
        result = ParkResult.ParkResult()
        try:
            parkplaceType = 1
            count = ParkPlaceImpl().getcount(parkplaceType)
            return result.ok(count)
        except Exception as e:
            print(e)
            return result.error("获取临时车车位数量失败！")

    def getinuse_innerparlplacecount(self):
        """获取已占用内部车位数量"""
        result = ParkResult.ParkResult()
        try:
            parkplaceType = 0
            count = ParkPlaceImpl().getinusecount(parkplaceType)
            return result.ok(count)
        except Exception as e:
            print(e)
            return result.error("获取已占用的内部车位数量失败！")

    def getinuse_tempparkplacecount(self):
        """获取已占用临时车位数量"""
        result = ParkResult.ParkResult()
        try:
            parkplaceType = 1
            count = ParkPlaceImpl().getinusecount(parkplaceType)
            return result.ok(count)
        except Exception as e:
            return result.error("获取已占用的临时车位数量失败！")

    def getempty_innerparkplacecount(self):
        """获取空闲内部车位数量"""
        result = ParkResult.ParkResult()
        try:
            parkplaceType = 0
            count = ParkPlaceImpl().getemptycount(parkplaceType)
            return result.ok(count)
        except Exception as e:
            return result.error("获取空闲内部车车位数量失败！")

    def getempty_tempparkplacecount(self):
        """获取空闲临时车数量"""
        result = ParkResult.ParkResult()
        try:
            parkplaceType = 1
            count = ParkPlaceImpl().getemptycount(parkplaceType)
            return result.ok(count)
        except Exception as e:
            print(e)
            return result.error("获取空闲临时车数量失败！")

    def lock(self, parkplaceid):
        """上锁
        """
        result = ParkResult.ParkResult()
        try:
            ParkPlaceImpl().updatelockstatus(0, parkplaceid)
            return result.ok2()
        except Exception as e:
            print(e)
            return result.error("关闭车位锁失败!")

    def unlock(self, parkplaceid):
        """开锁"""
        result = ParkResult.ParkResult()
        try:
            ParkPlaceImpl().updatelockstatus(1, parkplaceid)
            return result.ok2()
        except Exception as e:
            print(e)
            return result.error("打开车位锁失败！")

    def updateparkplace(self, parkplace):
        """更新车位"""
        result = ParkResult.ParkResult()
        try:
            ParkPlaceImpl().updateparkplace(parkplace)
            return result.ok2()
        except Exception as e:
            print(e)
            return result.error("更新车位信息失败！")

    def adddulparkplace(self,type,number):
        result = ParkResult.ParkResult()
        try:
            place = ParkPlace(0, type, None)
            for i in range(number):
                ParkPlaceImpl.insertparkplace(place)
            return result.ok2()
        except Exception as e:
            print(e)
            return result.error("添加车位失败！")

    def findbyid(self,parkplaceid):
        """按照车位号返回车位信息"""
        result = ParkResult.ParkResult()
        try:
            parkplace = ParkPlaceImpl().findbyid(parkplaceid)
            return result.ok(parkplace)
        except Exception as e:
            print(e)
            return result.error("查找失败！")

    def findbytype(self,type):
        """按照车位类型返回车位信息"""
        result = ParkResult.ParkResult()
        try:
            list = ParkPlaceImpl().findbytype(type)
            return result.ok(list)
        except Exception as e:
            print(e)
            return result.error("查找失败！")

    def allocateparkplace(self,carnumber,type):
        """
        随机分配车位函数 更改车位状态 返回车位号
        :param carnumber:车牌号
        :param type: 车辆类型 0 内部 1 临时车
        :return: 返回车位号
        """
        result = ParkResult.ParkResult()
        pimpl = ParkPlaceImpl()
        try:
            parkplacelist = pimpl.findemptybytype(type)
            if len(parkplacelist)!=0:
                parkplace = random.choice(parkplacelist)
                parkplace.useCarNumber = carnumber
                parkplace.lockStatus = 1
                pimpl.updateparkplace(parkplace)
                return result.ok(parkplace.parkPlaceID)
            else:
                return result.error("车位已满！")
        except Exception as e:
            print(e)
            return result.error("分配失败！")

    def reclaimparkpalce(self,plate_num):
        """
        车辆离开时调用，回收车位
        :param parkplaceid: 车位号
        :return:
        """
        result = ParkResult.ParkResult()
        try:
            pimpl = ParkPlaceImpl()
            parkplace = pimpl.findbyplateid(plate_num)
            parkplace.lockStatus = 0
            parkplace.useCarNumber=None
            pimpl.updateparkplace(parkplace)
            return result.ok(parkplace.parkPlaceID)
        except Exception as e:
            print(e)
            return result.error("回收车位失败！")

    def updateparkplacetype(self,parkplaceid,type):
        """
        根据车位号更新车位类型
        :param parkplaceid: 车位号
        :param type: 更新后的车位类型 0 内部 1 外部
        :return:
        """
        result = ParkResult()
        try:
            ParkPlaceImpl().updatetypebyparkplaceid(parkplaceid,type)
            return result.ok2()
        except Exception as e:
            print(e)
            return result.error("更新失败！")


