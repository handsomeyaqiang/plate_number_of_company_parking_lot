from Python_tensorflow_LicensePlate.dao.RecongiseDao import RecongiseDao
from Python_tensorflow_LicensePlate.train import train_license_digits
from Python_tensorflow_LicensePlate.train import train_license_letters
from Python_tensorflow_LicensePlate.train import train_license_province
class RecongiseDaoImpl(RecongiseDao):
    # 通过调用模型进行车牌的识别返回车牌号
    def recongise(self):
        # province = train_license_province.predict()
        # letter = train_license_letters.predict()
        # digit = train_license_digits.predict()
        # license_num = province + letter + digit
        return "豫A23454"

if __name__ == '__main__':
    r = RecongiseDaoImpl()
    r.recongise()
