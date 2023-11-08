# -*- coding:utf-8 -*-
# @Time : 2023/5/6 13:03
# Auther : shenyuming
# @File : login_cookies.py
# @Software : PyCharm

'''
    关联cookie
'''
import requests

HOST = 'http://124.223.33.41:7081'
NAME_PASSWORD = {'username':'auto','password':'sdfsdfsdf'}
def login(inData):
    url = f'{HOST}/api/mgr/loginReq'
    payload = inData
    resp = requests.post(url,data=payload)
    return resp.cookies

#业务类
class Lesson:
    def __init__(self,inCookies):
        self.cookies = inCookies

    def list_lesson(self,inData):
        url = f'{HOST}/api/mgr/sq_mgr/'
        payload = inData
        resp = requests.get(url,params=payload,cookies=self.cookies)
        #相应编码处理
        resp.encoding = 'unicode_escape'
        return resp.text

if __name__ == '__main__':
    cookie = login(NAME_PASSWORD)
    print(cookie)
    res=Lesson(cookie).list_lesson({"action":"list_course","pagenum":1,"pagesize":20})
    print(res)