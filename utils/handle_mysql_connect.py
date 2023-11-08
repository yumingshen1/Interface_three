# -*- coding:utf-8 -*-
# @Time : 2023/8/8 23:41
# Auther : shenyuming
# @File : handle_mysql_connect.py
# @Software : PyCharm

'''
    链接mysql,封装方法
'''
import pymysql

class DBMySqlConnect():
    def __init__(self,host='127.0.0.1',port=3306,user='root',password='Sym123456',database='ceshi'):
        self.connect = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connect.cursor()

    #查询操作
    def select(self,sql,many=True):
        self.cursor.execute(sql)
        if many:
            result = self.cursor.fetchall()
        else:
            result = self.cursor.fetchone()
        return result


    #增删改提取相同操作
    def do(self,sql):
        try:
            self.cursor.execute(sql)
        except Exception as error:
            self.connect.rollback() #出错后回滚
            print(f'MySQLDB error: {error}')
            raise error
        self.connect.commit()

    #增加
    def inisert(self,sql):
        self.do(sql)
    #删除
    def delete(self,sql):
        self.do(sql)
    #修改
    def update(self,sql):
        self.do(sql)

    #关闭游标和数据库连接
    def exit(self):
        self.cursor.close()
        self.connect.close()


if __name__ == '__main__':
    sql = 'SELECT * from biaodan ORDER BY id DESC LIMIT 2'
    data = DBMySqlConnect().select(sql=sql)
    print(data)
