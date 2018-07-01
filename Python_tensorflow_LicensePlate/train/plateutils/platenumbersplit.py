import cv2
from Python_tensorflow_LicensePlate.utils.ParkResult import ParkResult
import os


class splitPlate:

    def __init__(self):
        self.init_fazhi = 120
        self.DIR_RECEIVED_IMAGES = "../resources/images/receivedplateimages"
        self.DIR_MIDEL_IMAGES = "../resources/images/midledimages"
        self.DIR_SPLIT_IMAGES = "../resources/images/splitplateimages"
        self.white = []  # 记录每一列的白色像素总和
        self.black = []  # ..........黑色.......
        self.arg = False  # False表示白底黑字；True表示黑底白字
        self.white_max = 0
        self.black_max = 0
        self.height = 0
        self.width = 0
        self.result = ParkResult()

    def split_plate(self):
        # 1、读取图像，并把图像转换为灰度图像并显示
        img = cv2.imread(self.DIR_MIDEL_IMAGES+'/number_plate.jpg')  # 读取图片

        try:
            img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 转换了灰度化

            # 高斯平滑
            gaussian = cv2.GaussianBlur(img_gray, (1, 1), 0, 0, cv2.BORDER_DEFAULT)

            # 中值滤波
            median = cv2.medianBlur(gaussian, 3)


            # 二值化
            img_thre = img_gray
            cv2.threshold(median, self.init_fazhi, 255, cv2.THRESH_BINARY, img_thre)

            # 3、保存黑白图片
            cv2.imwrite(self.DIR_MIDEL_IMAGES+'/thre_res.png', img_thre)
            # 4、分割字符

            self.height = img_thre.shape[0]
            self.width = img_thre.shape[1]


            # 计算每一列的黑白色像素总和
            # 0黑   255白
            for i in range(3, self.width - 3):
                sumWhite = 0  # 这一列白色总数
                sumBlack = 0  # 这一列黑色总数
                for j in range(self.height):
                    if img_thre[j][i] == 255:
                        sumWhite += 1
                    if img_thre[j][i] == 0:
                        sumBlack += 1
                self.white_max = max(self.white_max, sumWhite)
                self.black_max = max(self.black_max, sumBlack)
                self.white.append(sumWhite)
                self.black.append(sumBlack)

            self.fazhi = 0
            if self.white_max >= self.black_max:
                while self.black_max - self.white_max < 10:
                    self.white_max = 0
                    self.black_max = 0
                    self.white = []  # 记录每一列的白色像素总和
                    self.black = []  # ..........黑色.......
                    self.fazhi += 5
                    cv2.threshold(median, self.init_fazhi + self.fazhi, 255, cv2.THRESH_BINARY, img_thre)
                    # 计算每一列的黑白色像素总和
                    # 0黑   255白
                    for i in range(3, self.width - 3):
                        sumWhite = 0  # 这一列白色总数
                        sumBlack = 0  # 这一列黑色总数
                        for j in range(self.height):
                            if img_thre[j][i] == 255:
                                sumWhite += 1
                            if img_thre[j][i] == 0:
                                sumBlack += 1
                        self.white_max = max(self.white_max, sumWhite)
                        self.black_max = max(self.black_max, sumBlack)
                        self.white.append(sumWhite)
                        self.black.append(sumBlack)

            if self.black_max > self.white_max:
                self.arg = True

            count = 1
            col_start = 8
            col_end = 1
            while col_start < self.width - 6:
                if (self.white[col_start] if self.arg else self.black[col_start]) > (0.10 * self.white_max if self.arg else 0.10 * self.black_max):
                    # 上面这些判断用来辨别是白底黑字还是黑底白字
                    # 0.05这个参数请多调整，对应上面的0.95
                    col_end = self.find_end(col_start)
                    if col_end - col_start > 5:
                        cj = img_thre[20:76, col_start:col_end]
                        #cv2.imshow('caijian', cj)
                        newImage = cv2.resize(cj, (32, 40), interpolation=cv2.INTER_CUBIC)
                        cv2.imwrite(self.DIR_SPLIT_IMAGES + "/" + str(count) + ".jpg", newImage)
                        count += 1
                        cv2.waitKey(0)
                    col_start = col_end
                col_start += 1
            # 判断切割后的图片是否是为7张
            split_pic = 0
            for rt, dirs, files in os.walk(self.DIR_SPLIT_IMAGES):
                for filename in files:
                    split_pic += 1
            if split_pic == 7:
                return self.result.ok2()
            elif split_pic == 8:
                count = 1
                for rt, dirs, files in os.walk(self.DIR_SPLIT_IMAGES):
                    for filename in files:
                        if count == 3:
                            os.remove(rt + "/" + filename)
                        elif count > 3:
                            os.rename(rt + "/" + filename, rt + "/" + str(count-1) + ".jpg")
                        count += 1
                return self.result.ok2()
            else:
                return self.result.error("车牌切割图片读取失败")
        except Exception as e:
            print(e)
            return self.result.error("车牌切割图片读取失败")

    # 分割图像
    def find_end(self, start_):
        end_ = start_ + 1
        for m in range(start_ + 1, self.width - 6):
            if (self.black[m] if self.arg else self.white[m]) > (0.89 * self.black_max if self.arg else 0.89 * self.white_max):  # 0.95这个参数请多调整，对应下面的0.05
                end_ = m
                break
        return end_

if __name__ == '__main__':
    s = splitPlate()
    s.split_plate()


