# -*- coding:utf-8 -*-
# @Time : 2023/5/16 18:44
# Auther : shenyuming
# @File : shop.py
# @Software : PyCharm
from common.baseApi import baseApi
from libs.login import Login
from configs.config import NAMEPASS
from utils.handle_path import casedata_path
import os
class Shop(baseApi):
    #列出

    #更新
    '''
    店铺更新，读取用例
    id,需要更新
    图片，需要传入
    '''
    def update(self,inData,shopID,fileInfo):
        # 约定什么样id不更新店铺
        if inData['id'] == 'id不存在':
            inData['id'] == '000'
        else:
            #更新店铺id
            inData['id'] = shopID
        #更新文件信息
        inData['image_path'] = fileInfo
        inData['image'] = f'/file/getImgStream?fileName={fileInfo}'
        return super(Shop,self).update(inData) #调用父类的update



if __name__ == '__main__':
    token=Login().login(NAMEPASS,getToken=True)
    #查询店铺
    shop = Shop(token)
    testData={'page':1,'limit':20}
    res = shop.query(testData)

    #获取店铺id
    shopid = res['data']['records'][0]['id']
    print('获取店铺id>>>',shopid)

    #文件上传
    res_foto = shop.file_upload(os.path.join(casedata_path,'xingguan.jpg'))
    print(res_foto)

    #获取图片信息
    shopimage = res['data']['realFileName']
    print('获取店铺图片>>>',shopimage)

    #测试数据
    shopData = {
            "name": "星巴克新建店",
            "address": "上海市静安区秣陵路303号",
            "id": "3269",
            "Phone": "13176876632",
            "rating": "6.0",
            "recent_order_num":100,
            "category": "快餐便当/简餐",
            "description": "满30减5，满60减8",
            "image_path": "b8be9abc-a85f-4b5b-ab13-52f48538f96c.png",
            "image": "http://121.41.14.39:8082/file/getImgStream?fileName=b8be9abc-a85f-4b5b-ab13-52f48538f96c.png"
        }
    #修改店铺
    res3 = shop.query(shopData,shopid,shopimage)
    print(res3)