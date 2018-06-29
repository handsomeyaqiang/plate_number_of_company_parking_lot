from Python_tensorflow_LicensePlate.dao.RecongiseDao import RecongiseDao
from Python_tensorflow_LicensePlate.train.train_digits import trainDigit
from Python_tensorflow_LicensePlate.train.train_letters import trainLetter
from Python_tensorflow_LicensePlate.train.train_province import trainProvince
import threading


class RecongiseDaoImpl(RecongiseDao):
    # 通过调用模型进行车牌的识别返回车牌号
    def __init__(self):
        self.plate_num = ""
    def province(self):
        pv = trainProvince()
        self.plate_num += pv.predict()

    def letter(self):
        lv = trainLetter()
        self.plate_num += lv.predict()

    def digit(self):
        dv = trainDigit()
        self.plate_num += dv.predict()

    def recongise(self):
        p = threading.Thread(target=self.province, name='LoopThread')
        d = threading.Thread(target=self.digit, name="LoopThread1")
        l = threading.Thread(target=self.letter, name="LoopThread2")
        p.start()
        p.join()
        l.start()
        l.join()
        d.start()
        d.join()
        print(self.plate_num)
        return self.plate_num
if __name__ == '__main__':
    r = RecongiseDaoImpl()
    r.recongise()
