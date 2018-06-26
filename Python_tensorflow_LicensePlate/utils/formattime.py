import time
import datetime
def totime(dt):
    # 转换成时间数组
    timeArray = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
    # 转换成时间戳
    timestamp = time.mktime(timeArray)
    return timestamp

def calc_time(end, start):
    if end != None:
        start_datatime = totime(start)
        end_datatime = totime(end)
        s = datetime.datetime.fromtimestamp(start_datatime)
        e = datetime.datetime.fromtimestamp(end_datatime)
        return '%.2f'% (((e-s).seconds) / 3600)
    return None
