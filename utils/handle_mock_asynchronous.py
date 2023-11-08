# -*- coding:utf-8 -*-
# @Time : 2023/8/7 16:55
# Auther : shenyuming
# @File : handle_mock_asynchronous.py
# @Software : PyCharm

'''
    mock和异步
'''
import time
import threading
import requests

HOST = 'http://127.0.0.1:9999'

#创建订单
def commit_order(inData):
    url = '/api/order/create/'
    payload = inData
    res = requests.post(url=f'{HOST}{url}',json = payload)
    return res.json()

#查询订单 ， 加上轮循时间和超时时间 ,
def get_orderresult(order_id,queryTime=2,outTime=15):
    url = '/api/order/get_result1/'
    payload = order_id

    starttime = time.time()
    endtime = starttime + outTime
    cnt = 1
    try:
        while time.time() < endtime:
            res = requests.get(url=f'{HOST}{url}',params=payload)
            if res.text:
                print(f'第{cnt}次查询，有结果，查询结束')
                break
            else:
                print(f'第{cnt}次查询，无结果，继续查询')
            time.sleep(queryTime)
            cnt += 1
        return res.json()
    except Exception as e:
        print('未查询出结果',e)




if __name__ == '__main__':
    inData = {"user_id": "sq123456",
			    "goods_id": "20200815",
				"num":1,
				"amount":200.6
              }
    #整体开始时间
    startime = time.time()

    result = commit_order(inData)
    orderid = result['order_id']
    print(result)
    print(orderid)
    # result2 = get_orderresult(result)
    # print(result2)
    # print(get_orderresult(result))

    '''
        使用多线程，合理利用时间  threading.thread()
        main中的函数都是主线程， 
        thread中的函数是子线程
        target: 传入函数名，不带括号
        args* :函数需要的参数，是元组格式
        设置线程守护后(setDaemon)主线程停止后，子线程也停止
    '''
    thread_fun = threading.Thread(target=get_orderresult,args=(result,))
    thread_fun.setDaemon(True) #设置线程守护
    thread_fun.start()
    # thread_fun.join()    #线程阻塞，要等该线程执行完，在执行其他的

    #创建多个线程
    # thread_list = []
    # for one in range(10):
    #     thread_list.append(threading.Thread(target=get_orderresult,args=(result,)))
    # for t in thread_list:
    #     t.setDaemon(True)
    #     t.start()

    #其他业务
    for i in range(10):
        print('我执行下其他的功能')
        time.sleep(1)

    #整体结束时间
    endtime = time.time()
    print('整体的测试时间：',endtime-startime)