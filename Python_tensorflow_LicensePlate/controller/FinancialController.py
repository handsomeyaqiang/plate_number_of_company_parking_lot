from  Python_tensorflow_LicensePlate.entity.Financial import Financial
from Python_tensorflow_LicensePlate.service.FinancialService import FinancialService


class FinancialController(object):
    """财务控制类"""
    def insertFinancial(self,ParkPlaceID, chargetime, money):
        """插入一条记录"""
        fin = Financial(ParkPlaceID, chargetime, money)
        rs = FinancialService().insertFinancial(fin)
        return rs
