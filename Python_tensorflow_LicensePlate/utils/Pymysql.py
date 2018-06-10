# user/bin/python
# coding=utf-8
import pymysql
'''
CREATE TABLE `users` (
    `id` INT(11) NOT NULL AUTO_INCREMENT,
    `email` VARCHAR(255) NOT NULL,
    `password` VARCHAR(255) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=INNODB DEFAULT CHARSET=utf8
AUTO_INCREMENT=1 ;
'''
'''
    python的对MySQL数据库的操作
'''


class PyMySQLHelper:
    # 定义一个连接mysql的函数
    def getConnection(self):
        try:
            conn = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='company_parking_system')
        except pymysql.Error as e:
            print("pymysql Connection Error:%s" % e)
        return conn
    # 定义一个利用sql带参数获取所有结果记录
    def selectAllByParam(self, sql, params):
        try:
            conn = self.getConnection()
            cur = conn.cursor()
            count = cur.execute(sql, params=params)
            result = cur.fetchall()
            return result
        except pymysql.Error as e:
            print("pymysql Error:%s" % e)
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
        except pymysql.Error as e:
            print("pymysql Error:%s" % e)
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
        except pymysql.Error as e:
            print("pymysql Error:%s" % e)
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
        except pymysql.Error as e:
            print("pymysql Error:%s" % e)
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
        except pymysql.Error as e:
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
        except pymysql.Error as e:
            conn.rollback()
            print("pymysql Error:%s" % e)
        finally:
            cur.close()
            conn.close()

    def selectalldictcursor(self,sql):
        """返回所有查找记录列表，且单条记录为字典类型"""
        try:
            conn = self.getConnection()
            cur = conn.cursor(cursor = pymysql.cursors.DictCursor)
            count = cur.execute(sql)
            result = cur.fetchall()
            return result
        except pymysql.Error as e:
            print("pymysql Error:%s" % e)
        finally:
            cur.close()
            conn.close()

    def selectOnedictcursor(self, sql):
        """返回单行记录，且记录的类型为字典类型"""
        try:
            conn = self.getConnection()
            cur = conn.cursor(cursor = pymysql.cursors.DictCursor)
            count = cur.execute(sql)
            result = cur.fetchone()
            return result
        except pymysql.Error as e:
            print("pymysql Error:%s" % e)
        finally:
            cur.close()
            conn.close()