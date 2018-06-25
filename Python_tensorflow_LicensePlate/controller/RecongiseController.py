from Python_tensorflow_LicensePlate.service.RecongiseService import RecongiseService
class RecongiseController:

    # 车辆进入识别Controller
    def recongise_in(self):
        r = RecongiseService()
        return r.recongise_in()

    # 车辆离开识别Controller
    def recongise_out(self):
        r = RecongiseService()
        return r.recongise_out()
