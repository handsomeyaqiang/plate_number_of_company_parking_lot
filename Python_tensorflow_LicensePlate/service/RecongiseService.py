from Python_tensorflow_LicensePlate.daoimpl.RecongiseDaoImpl import RecongiseDaoImpl
from Python_tensorflow_LicensePlate.service.VehicleService import VehicleService
from Python_tensorflow_LicensePlate.service.RecordService import RecordService
from Python_tensorflow_LicensePlate.entity.Record import Record
from Python_tensorflow_LicensePlate.utils.ParkResult import ParkResult
from Python_tensorflow_LicensePlate.service.ChargeService import ChargeService
from Python_tensorflow_LicensePlate.service.FinancialService import FinancialService
from Python_tensorflow_LicensePlate.entity.Financial import Financial
from Python_tensorflow_LicensePlate.service.ParkPlaceService import ParkPlaceService
from Python_tensorflow_LicensePlate.entity.RecongiseResult import RecongiseResult
from Python_tensorflow_LicensePlate.utils.chargeResult import chargeResult
import time


class RecongiseService:

    def recongise_in(self, plate_num):
        result = ParkResult()
        recordService = RecordService()
        try:
            vehicleService = VehicleService()
            # 根据识别的车牌号进行车辆查询 查到：内部车， 查不到：外部车
            result = vehicleService.findVehicleByPlateNum(plate_num)
            parkPlaceService = ParkPlaceService()
            if result.status == 200:
                # 成功查询到车辆
                # 创建一个空的记录对象
                record = Record(None, None, None, None, None)
                # 获取当前的时间 格式：2018-06-25 11:21:12
                current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
                record.__setattr__("platenumber", plate_num)
                record.__setattr__("intime", current_time)
                record.__setattr__("leavestatus", 0)
                if result.data != None:
                    # 内部车
                   record.__setattr__("vehicletype", 0)
                   # 分配车位
                   result = parkPlaceService.allocateparkplace(plate_num, 0)
                   if result.status == 200:
                       # 分配车位成功
                       resultData = RecongiseResult(plate_num, 0, result.data, None, str(current_time), None)
                       # 将记录插入到数据库
                       recordService.insert_record(record)
                       return result.ok(resultData)
                   else:
                       # 分配车位失败
                       return result.error(result.data)
                else:
                   # 外部车
                   record.__setattr__("vehicletype", 1)
                   # 分配车位
                   result = parkPlaceService.allocateparkplace(plate_num, 1)
                   if result.status == 200:
                       # 分配车位成功
                       resultData = RecongiseResult(plate_num, 1, result.data, None, str(current_time), None)
                       # 将记录插入到数据库
                       recordService.insert_record(record)
                       return result.ok(resultData)
                   else:
                       # 分配车位失败
                       return result.error(result.msg)
            else:
                return result.error(result.msg)
        except Exception as e:
            print(e)
            return result.error("进入识别出现异常")

    def recongise_out(self, plate_num):
        result = ParkResult()
        try:
            vehicleService = VehicleService()
            # 根据识别的车牌号进行车辆查询 查到：内部车， 查不到：外部车
            result = vehicleService.findVehicleByPlateNum(plate_num)
            parkPlaceService = ParkPlaceService()
            if result.status == 200:
                # 成功查询到车辆
                recordService = RecordService()
                # 根据车牌号查找进入的车辆的停车记录
                recordResult = recordService.getSingleRecordByPlateId(plate_num)
                record = recordResult.data
                # 获取当前的时间 格式：2018-06-25 11:21:12
                current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
                record.__setattr__("outtime", current_time)
                if result.data != None:
                    # 收回车位
                    result = parkPlaceService.reclaimparkpalce(plate_num)
                    if result.status == 200:
                        # 收回车位成功
                        resultData = RecongiseResult(plate_num, 0, result.data, None, str(record.__getattribute__("intime")), str(current_time))
                        # 内部车位不用交费直接放行
                        # 更新停车记录
                        record.__setattr__("leavestatus", 1)
                        recordService.update_record(record)
                        return result.ok(resultData)
                    else:
                        # 收回车位失败
                        return result.error(result.msg)
                else:
                    # 收回车位
                    result = parkPlaceService.reclaimparkpalce(plate_num)
                    # 计算应缴费用
                    chargeService = ChargeService()
                    money = chargeService.charge(str(record.__getattribute__("intime")), current_time)
                    if result.status == 200:
                        # 收回车位成功
                        # 外部车缴费
                        # 封装缴费记录
                        financial = Financial(result.data, current_time, money)
                        # 补充record
                        record.__setattr__("leavestatus", 1)
                        chargeResultdata = chargeResult(financial, record)
                        # 设置状态码为300表示前端需要缴费
                        result = result.ok(chargeResultdata)
                        result.status = 300
                        return result
                    else:
                        # 收回车位失败
                        return result.error(result.msg)
            else:
                return result.error(result.msg)
        except Exception as e:
            print(e)
            return result.error("离开自动识别异常")

    def judg_recongise(self):
        recongiseDao = RecongiseDaoImpl()
        # 调用车牌识别的实现DaoImpl
        plate_num = recongiseDao.recongise()
        recordService = RecordService()
        # 根据车牌号查找进入的车辆的停车记录
        result = recordService.getSingleRecordByPlateId(plate_num)
        if result.status == 200:
            if result.data != None:
                return self.recongise_out(plate_num)
            else:
                return self.recongise_in(plate_num)
        else:
            return result.error("自动识别异常")

    def hand_recongise(self, plate_num):
        recordService = RecordService()
        # 根据车牌号查找进入的车辆的停车记录
        result = recordService.getSingleRecordByPlateId(plate_num)
        if result.status == 200:
            if result.data != None:
                return self.recongise_out(plate_num)
            else:
                return self.recongise_in(plate_num)
        else:
            return result.error("自动识别异常")

    def charge(self, chargeResult):
        financialService = FinancialService()
        recordService = RecordService()
        result = ParkResult()
        financial = chargeResult.financial
        record = chargeResult.record
        financialService.insertFinancial(financial)
        recordService.update_record(record)
        resultData = RecongiseResult(record.platenumber, record.vehicletype,
                                     financial.ParkPlaceID, financial.money, str(record.intime), str(record.outtime))
        return result.ok(resultData)
