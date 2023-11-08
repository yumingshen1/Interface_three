# -*- coding:utf-8 -*-
# @Time : 2023/8/9 16:24
# Auther : shenyuming
# @File : handle_mongo_connect.py
# @Software : PyCharm

'''
    mongo数据库封装
'''

import pymongo

class DBMongoConnect():
    def __init__(self,ip='localhost',port=27017,usernam='xx',pwd='pwd',db='xx'):
        self.client = pymongo.MongoClient(f"mongodb://{usernam}:{pwd}@{ip}:{port}/")
        dblist = self.client.list_database_names() #获得所有已存在的库
        if db in dblist:
            self.connect =  self.client[db]   #链接库
        else:
            print(f'mongo的{db}库不存在')

    #增加方法 ,集合，查询字典，
    def insert(self,collection,query,many=True):
        mycol = self.connect[collection]
        if many:
            mycol.insert_many(query)
        else:
            mycol.insert_one(query)


    #查询方法
    def query(self,collection,query,many=True):
        mycol = self.connect[collection]
        if many:
            return [i for i in mycol.find(query)]
            # result = mycol.find(query)
            # for i in result:
            #     return i
        else:
            return mycol.find_one(query)

    #修改 ， 集合，查询字典，修改的值，
    def update(self,collection,query,newquery,many=True):
        mycol = self.connect[collection]
        if many:
            mycol.update_many(query,{"$set":newquery})
        else:
            mycol.update_one(query,{"$set":newquery})

    #删除
    def delete(self,collection,query,many=True):
        mycol = self.connect[collection]
        if many:
            mycol.delete_many(query)
        else:
            mycol.delete_one(query)

if __name__ == '__main__':
    db = DBMongoConnect(db='xxx')
    res = db.query('集合',{'name':'啦啦啦'},many=True)
    print(res)