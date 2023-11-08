# -*- coding:utf-8 -*-
# @Time : 2023/8/6 23:33
# Auther : shenyuming
# @File : handle_mock.py
# @Software : PyCharm
'''
    mock测试，
    启动：
        mock的jira包和json文件（放入入参、出参）放在一起，
        建立sh文件，写入进入启动命令"java -jar moco-runner-1.1.0-standalone.jar http -p 9999 -c test.json"
        -jar:jira包名
        -p : 端口
        -c ： json文件
        启动文件，
        然后浏览器访问ip+uri。  或者代码访问
    代码：
        建立HOST, 创建请求
'''
import requests

HOST = 'http://127.0.0.1:9999'
#无参
def M_test1():
    res = requests.get(url=f'{HOST}/sq4')
    print(res.text)

#querise--->params
def M_test2():
    payload = {"key1":"abc","key2":"123"}
    res = requests.get(url=f'{HOST}/sym',params=payload)
    print(res.text)

#forms--->data
def M_test3():
    payload = {"key1":"abc"}
    res = requests.get(url=f'{HOST}/sq2',data=payload)
    print(res.text)

#json---->json
def M_test4():
    # payload = {"key1":"value1","key2":"value2"}
    payload = {"user_id":"sq123456","goods_id":"20200815","num":1,"amount":200.6}
    res = requests.post(url=f'{HOST}/api/order/create/',json=payload)
    print(res.text)

if __name__ == '__main__':
    # M_test1()
    # M_test2()
    # M_test3()
    M_test4()