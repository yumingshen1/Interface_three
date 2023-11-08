# -*- coding:utf-8 -*-
# @Time : 2023/4/7 15:02
# Auther : shenyuming
# @File : login.py
# @Software : PyCharm
import copy
import requests
from has_md5 import get_md5_demo

HOST = 'http://121.41.14.39:8082/'
NAME_PASSWORD = {'username':'zo0385','password':'44982'}  #ka0518,xintian

def login(inData,getToken=False):
    #url
    url = f'{HOST}account/sLogin?'
    #data
    inData = copy.copy(inData)  # copy参数
    inData['password'] = get_md5_demo(inData['password']) #MD5加密
    pyloads = inData
    #request
    res = requests.post(url,pyloads)
    print('响应头:',res.headers)
    print('请求头：',res.request.headers)
    print('cookies:',res.cookies)   #后续接口只需要原生态的cookies对象，直接cookies


    if getToken == False:
        return res.json()
    else:
        return res.json()['data']['token']

    #return
    # return res.text


if __name__ == '__main__':
    res_test = login(NAME_PASSWORD,getToken=False)
    print(res_test)