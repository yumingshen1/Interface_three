# -*- coding:utf-8 -*-
# @Time : 2023/8/8 22:46
# Auther : shenyuming
# @File : handle_mysql.py
# @Software : PyCharm

import pymysql

connect = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='Sym123456',
    database='ceshi'
)
cursor = connect.cursor()
sql1='select * from biaodan'
sql2 = 'SELECT * from biaodan ORDER BY id DESC LIMIT 10'
sql3 = 'insert into biaodan(name,age,classname,school,city,county)values("吧啦",223,"python写入","清华源","巴黎","法国")'
cursor.execute(sql3)
connect.commit()
cursor.execute(sql2)
data = cursor.fetchmany(2) #返回N条数据
for one in data:
    print(one)
cursor.close()
connect.close()
