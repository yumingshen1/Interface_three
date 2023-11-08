# -*- coding:utf-8 -*-
# @Time : 2023/5/8 11:23
# Auther : shenyuming
# @File : login_cookies_2.py
# @Software : PyCharm
import requests

HOST = 'http://124.223.33.41:7081'
NAME_PASSWORD = {'username':'auto','password':'sdfsdfsdf'}
def login(inData):
    url = f'{HOST}/api/mgr/loginReq'
    payload = inData
    resp = requests.post(url,data=payload)
    return resp.cookies

class Lesson:
    def __init__(self,inCookie):
        self.cookies = inCookie

    def list_lesson(self,inData):
        url = f'{HOST}/api/mgr/sq_mgr/'
        payload = inData
        re = requests.get(url,params=payload,cookies=self.cookies)
        re.encoding = 'unicode_escape'
        return re.text

if __name__ == '__main__':
    cookies = login(NAME_PASSWORD)
    result = Lesson(cookies).list_lesson({"action":"list_course","pagenum":1,"pagesize":20})
    print(result)