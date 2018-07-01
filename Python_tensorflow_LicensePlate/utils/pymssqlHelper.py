# coding=utf-8
import pymysql

'''
	python的对SQLserver数据库的操作
'''


class PymssqlHelper:

    # 定义一个连接sqlserver数据库的函数
    def getConnection(self):
        try:
            conn = pymssql.connect(server="localhost", port=1433, user="root", password="root",
                                   database="company_parking_system")
            return conn
        except pymssql.Error as e:
            print("pymssql Error:%s" % e)

    # 定义一个利用sql带参数获取所有结果记录
    def selectAllByParam(self, sql, params):
        try:
            conn = self.getConnection()
            cur = conn.cursor()
            count = cur.execute(sql, params=params)
            result = cur.fetchall()
            return result
        except pymssql.Error as e:
            print("pymssql Error:%s" % e)
        finally:
            cur.close()
            conn.close()

    # 定义一个根据参数值的sql选择单行数据记录
    def selectOneByParam(self, sql, params):
        try:
            conn = self.getConnection()
            cur = conn.cursor()
            count = cur.execute(sql, params=params)
            result = cur.fetchone()
            return result
        except pymssql.Error as e:
            print("pymssql Error:%s" % e)
        finally:
            cur.close()
            conn.close()

    # 没有参数的单行选择数据记录
    def selectOne(self, sql):
        try:
            conn = self.getConnection()
            cur = conn.cursor()
            count = cur.execute(sql)
            result = cur.fetchone()
            return result
        except pymssql.Error as e:
            print("pymssql Error:%s" % e)
        finally:
            cur.close()
            conn.close()

    # 定义一个利用sql获取所有结果记录
    def selectALL(self, sql):
        try:
            conn = self.getConnection()
            cur = conn.cursor()
            count = cur.execute(sql)
            result = cur.fetchall()
            return result
        except pymssql.Error as e:
            print("pymssql Error:%s" % e)
        finally:
            cur.close()
            conn.close()

    # 带参数的更新方法eg:sql='insert into pythontest values(%s,%s,%s,now())',
    # params=(6,'C#','good book')
    def updateByParam(self, sql, params):
        try:
            conn = self.getConnection()
            cur = conn.cursor()
            count = cur.execute(sql, params)
            conn.commit()
            return count
        except pymssql.Error as e:
            conn.rollback()
            print("pymssql Error:%s" % e)
        finally:
            cur.close()
            conn.close()

    # 不带参数的更新方法
    def update(self, sql):
        try:
            conn = self.getConnection()
            cur = conn.cursor()
            count = cur.execute(sql)
            conn.commit()
            return count
        except pymssql.Error as e:
            conn.rollback()
            print("pymssql Error:%s" % e)
        finally:
            cur.close()
            conn.close()
