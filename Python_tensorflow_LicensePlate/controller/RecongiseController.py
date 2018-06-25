from Python_tensorflow_LicensePlate.service.RecongiseService import RecongiseService
class RecongiseController:

    def recongise_in(self):
        r = RecongiseService()
        return r.recongise_in()
