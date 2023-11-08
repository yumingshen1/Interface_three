# -*- coding:utf-8 -*-
# @Time : 2023/5/8 12:27
# Auther : shenyuming
# @File : baseApi.py
# @Software : PyCharm
'''
基类封装思路：
    加入异常机制+log
    截图操作--ui自动化
    增删改查方法，请求发送方法
'''
import inspect
import requests,os
from utils.handle_apiConfig_yml import get_data_yml
from utils.handle_path import apiconfig_yml_path
from configs.config import HOST

class baseApi:
    def __init__(self,inToken=None):
        #业务层需要token
        if inToken:
            self.header = {'Authorization':inToken}
        else:
            self.header = None
        # 提取url地址数据并获取类名
        self.data = get_data_yml(os.path.join(apiconfig_yml_path,'apiConfig.yml'))[self.__class__.__name__]

    def request_send(self,data=None,json=None,params=None,files=None,id=''):
        try:
            dataname = inspect.stack()[1][3]  #获得调用request_send方法的方法名
            method,path = self.data[dataname].values() # 获得字典的值
            resp = requests.request(method=method,url=f'{HOST}{path}{id}',data=data,json=json,
                                    params=params,files=files,headers=self.header)
            return resp.json()  #返回数据
        except:
            pass


    #新增接口
    def add(self):
        pass
    def delete(self):
        pass
    def update(self,inData):
        return self.request_send(params=inData)
    def query(self,inData):
        return self.request_send(params=inData)

    #图片上传 ， 固定的参数  d:/22.png
    def file_upload(self,fileDir:str):
        fileName = fileDir.split('/')[-1]
        fileType = fileDir.split('.')[-1]
        userFile = {'file':(fileName,open(fileDir,mode='rb'),fileType)}
        return self.request_send(files=userFile)


class ApiAssert:
    @classmethod
    def defassert_api(self,result,conditon,expResult):
        try:
            if conditon == '==':
                assert result == expResult
            elif conditon == 'in':
                assert expResult in result
        except Exception as error:
            raise error
