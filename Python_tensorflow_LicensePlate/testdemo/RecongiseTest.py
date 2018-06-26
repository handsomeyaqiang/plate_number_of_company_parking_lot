from Python_tensorflow_LicensePlate.service.RecongiseService import RecongiseService
from Python_tensorflow_LicensePlate.daoimpl.RecordImpl import RecordImpl
from Python_tensorflow_LicensePlate.service.ChargeService import ChargeService
from Python_tensorflow_LicensePlate.train.plateutils import getplatenumber
import math
import time
import datetime
class RecongiseTest:

    def recongiseInDemo(self):
        r = RecongiseService()
        result = r.recongise_in()
        if result.status == 200:
            resultData = result.data
            print("车牌号：",resultData.plate_num)
            print("车辆类型：", resultData.vehicle_type)
            print("分配的车位号：", resultData.park_place_id)
            print("应缴费用：", resultData.money)
            print("进入时间：", resultData.intime)
            print("离开时间：", resultData.outtime)
        else:
            print(result.msg)

    def recongise_outdemo(self):
        r = RecongiseService()
        result = r.recongise_out()
        if result.status == 200:
            resultData = result.data
            print("车牌号：",resultData.plate_num)
            print("车辆类型：", resultData.vehicle_type)
            print("收回的车位号：", resultData.park_place_id)
            print("应缴费用：", resultData.money)
            print("进入时间：", resultData.intime)
            print("离开时间：", resultData.outtime)
        else:
            print(result.msg)

    def getSingleDemo(self):
        recordDao = RecordImpl()
        record = recordDao.getSingleRecordByPlateId("京B82343")
        print(record)

    def charge_demo(self):
        charge = ChargeService()
        money = charge.charge("2018-06-21 11:21:12", "2018-06-25 18:30:44")
        print(money)

    def judg_demo(self):
        r = RecongiseService()
        result = r.judg_recongise()
        if result.status == 200:
            resultData = result.data
            print("车牌号：", resultData.plate_num)
            print("车辆类型：", resultData.vehicle_type)
            print("收回的车位号：", resultData.park_place_id)
            print("应缴费用：", resultData.money)
            print("进入时间：", resultData.intime)
            print("离开时间：", resultData.outtime)
        else:
            print(result.msg)

    def getnum(self):
        start = "2018-06-26 10:52:22"
        end = "2018-06-28 14:20:36"
        # str_start = datetime.datetime.fromtimestamp(start)
        # str_end = datetime.datetime.fromtimestamp(end)
        # print(str_start)
        # print(str_end)
        # 转换成时间数组
        timeArray = time.strptime(start, "%Y-%m-%d %H:%M:%S")
        # 转换成时间戳
        timestamp = time.mktime(timeArray)
        str_start = datetime.datetime.fromtimestamp(timestamp)


        timeArray2 = time.strptime(end, "%Y-%m-%d %H:%M:%S")
        # 转换成时间戳
        timestamp2 = time.mktime(timeArray2)
        str_end = datetime.datetime.fromtimestamp(timestamp2)
        s = (str_end - str_start).seconds
        ss = (str_end - str_start)
        print(s, ss)
if __name__ == '__main__':
   r = RecongiseTest()
   #r.judg_demo()
   r.getnum()
   #r.recongiseInDemo()
   #r.recongise_outdemo()
   # r.getSingleDemo()
   #r.charge_demo()
