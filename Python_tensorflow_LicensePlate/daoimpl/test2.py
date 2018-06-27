from Python_tensorflow_LicensePlate.utils.Pymysql import PyMySQLHelper

sql = 'SELECT COUNT(parkPlaceType) FROM parkplace WHERE parkPlaceType = 1'

rs = PyMySQLHelper().selectOnedictcursor(sql)
count = rs['COUNT(parkPlaceType)']
print(count)