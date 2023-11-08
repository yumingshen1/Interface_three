# -*- coding:utf-8 -*-
# @Time : 2023/5/8 12:46
# Auther : shenyuming
# @File : login.py
# @Software : PyCharm
import copy
from common.baseApi import baseApi
from utils.handle_md5 import get_data_md5
from configs.config import NAMEPASS

class Login(baseApi):
    def login(self,inData,getToken=False):
        payload = copy.copy(inData)
        payload['password'] = get_data_md5(payload['password']) #调用加密
        resp = self.request_send(data=payload)
        if getToken == False:   #判断是否取token
            return resp
        else:
            return resp['data']['token']

if __name__ == '__main__':
    print(Login().login(NAMEPASS,getToken=True))

