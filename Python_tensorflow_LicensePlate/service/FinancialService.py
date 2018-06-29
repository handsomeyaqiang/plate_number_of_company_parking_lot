from Python_tensorflow_LicensePlate.daoimpl.FinancialDaoImpl import FinancialDaoImpl
from Python_tensorflow_LicensePlate.utils import ParkResult
import calendar
import time


class FinancialService(object):

    def insertFinancial(self, financial):
        """插入一条财务记录"""
        result = ParkResult.ParkResult()
        try:
            FinancialDaoImpl().insertfinancial(financial)
            return result.ok2()
        except Exception as e:
            print(e)
            return result.error("插入记录失败！")

    def listbyyear(self, year):
        """获取某一年的报表"""
        result = ParkResult.ParkResult()
        try:
            list = FinancialDaoImpl().listfinancialbyyear(year)
            return result.ok(list)
        except Exception as e:
            print(e)
            return result.error('获取报表信息失败！')

    def listbymonth(self, month):
        """获取某一月的报表"""
        result = ParkResult.ParkResult()
        try:
            list = FinancialDaoImpl().listfinancialbymonth(month)
            return result.ok(list)
        except Exception as e:
            print(e)
            return result.error("获取报表信息失败！")

    def listbyday(self, day):
        """"获取某一天的报表"""
        result = ParkResult.ParkResult()
        try:
            list = FinancialDaoImpl().listfinancialbyday(day)
            return result.ok(list)
        except Exception as e:
            print(e)
            return result.error("获取报表失败！")

    def listbyparkplaceid(self, parkplaceid):
        """"获取某个车位的报表"""
        result = ParkResult.ParkResult()
        try:
            list = FinancialDaoImpl().listfinancialbyparkplaceid(parkplaceid)
            return result.ok(list)
        except Exception as e:
            print(e)
            return result.error("获取报表失败！")

    def listallfinancial(self):
        """返回所有报表"""
        result = ParkResult.ParkResult()
        try:
            list = FinancialDaoImpl().listallfinancial()
            return result.ok(list)
        except Exception as e:
            print(e)
            return result.errror("获取报表失败！")

    def listmonthsumbyyear(self, year):
        """
        获取某年的已发生的每个月的金额和，将数据库中没有收入的月份收入置为0
        :param year: 年份，输入格式为 '2018'
        :return: 返回元素为字典类型的列表
        """

        # 月份
        months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        result = ParkResult.ParkResult()
        # 获取当前时间
        localtime = time.localtime(time.time())
        tempyear = localtime.tm_year
        if tempyear == year:
            # 取月份
            temp = localtime.tm_mon
            if temp < 10:
                nowmonth = '0{0}'.format(temp)
            else:
                nowmonth = str(temp)
            print(temp)

            pastmonths = []
            for i in months:
                if i <= nowmonth:
                    pastmonths.append(i)
        else:
            pastmonths = months
        try:
            ymresult = FinancialDaoImpl().listsumeachmonthbyyear(year)
            ymouth = []
            for i in ymresult:
                ymouth.append((i['ymdatetime']))
            for i in pastmonths:
                if i in ymouth:
                    pass
                else:
                    ymresult.append({'totalmoney': 0, 'ymdatetime': i})
            print(ymresult)
            sortedym = sorted(ymresult, key=lambda e: e.__getitem__('ymdatetime'))
            print(sortedym)
            return result.ok(sortedym)
        except Exception as e:
            print(e)
            return result.error("发生意外！")

    def listdaysumbymonth(self, year_month):
        """
        获取某月已反生的每天的收入和
        :param year_month: 月份 输入格式为'2018-06'
        :return: 将数据库中没有的时间段添加到列表中，收入设置为零返回字典列表
        """
        result = ParkResult.ParkResult()

        # 分割字符串 将年份和月份分离出来
        tempyearmonth = year_month.split('-')
        print(tempyearmonth)
        # 转换为int 类型
        year = int(tempyearmonth[0])
        month = int(tempyearmonth[1])

        # 利用日历模块求某月天数
        monthdays = calendar.monthrange(year, month)[1]
        print(monthdays)

        # 获取当前日期
        nowtime = time.localtime(time.time())
        # 获取当前
        nowyear = nowtime.tm_year
        nowmonth = nowtime.tm_mon
        nowday = nowtime.tm_mday
        # 如果所检索月份为当前月，则要考虑只显示当前天之前的信息，不显示剩下没有发生的天数的信息
        if year == nowyear and month == nowmonth:
            monthdaysrange = nowday
        else:
            monthdaysrange = monthdays
        days = []
        for i in range(1, monthdaysrange + 1):
            day = str(i)
            day = day.zfill(2)
            print(day)
            days.append(day)
        print(days)
        try:
            dmresult = FinancialDaoImpl().listsumeachdaybymonth(year_month)
            print(dmresult)
            daysresult = []

            for i in dmresult:
                daysresult.append(i['mddatetime'])
            for day in days:
                if day in daysresult:
                    pass
                else:
                    dmresult.append({'totalmoney': 0, 'mddatetime': day})
            print(dmresult)
            # sortedym = sorted(dmresult, key=lambda e: e.__getitem__('mddatetime'))
            sorteddmresult = sorted(dmresult, key=lambda e: e.__getitem__('mddatetime'))
            # print(sortedym)
            print(sorteddmresult)
            return result.ok(sorteddmresult)
        except Exception as e:
            print(e)
            return result.error("发生意外！")

    def listhoursumbyday(self, year_month_day):
        """
        获取某天的每个时间段的数据
        :param year_month_day:
        :return:
        """
        result = ParkResult.ParkResult()
        # 分割字符串 将年份和月份分离出来
        tempyearmonthday = year_month_day.split('-')
        # print(tempyearmonthday)
        # 转换为int 类型
        year = int(tempyearmonthday[0])
        month = int(tempyearmonthday[1])
        day = int(tempyearmonthday[2])

        # 获取当前时间 年月日
        nowtime = time.localtime(time.time())
        nowyear = nowtime.tm_year
        nowmonth = nowtime.tm_mon
        nowday = nowtime.tm_mday
        nowhour = nowtime.tm_hour

        # 判断所选天是否为当前日期，如果为当前日期则考虑只显示当前hour之前的数据
        # 如果非当前天，则可以显示一整天的数据
        if year == nowyear and month == nowmonth and day == nowday:
            hourrange = nowhour
        else:
            hourrange = 23
        hours = []
        # 如果小于两位则填充前置0
        for i in range(hourrange + 1):
            hour = str(i).zfill(2)
            hours.append(hour)
        # print(hours)
        try:
            dhrs= FinancialDaoImpl().listsumeachhourbyday(year_month_day)
            rshour = []
            #获取数据库中取得的小时列表
            for i in dhrs:
                rshour.append(i['dhdatetime'])
            # print(rshour)
            #遍历 将没有出现在rshour 中的添加进dhrs
            for hour in hours:
                if hour in rshour:
                    pass
                else:
                    dhrs.append({'totalmoney':0,'dhdatetime':hour})
            sorteddhrs = sorted(dhrs,key=lambda e: e.__getitem__('dhdatetime'))
            # print(dhrs)
            # print(sorteddhrs)
            return result.ok(sorteddhrs)
        except Exception as e:
            print(e)
            return result.error("发生意外！")


if __name__ == '__main__':
    # FinancialService().listmonthsumbyyear(2015)
    # FinancialService().listdaybymonth('2018-06')
    FinancialService().listhoursumbyday('2018-06-20')