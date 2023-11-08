# -*- coding:utf-8 -*-
# @Time : 2023/8/7 20:35
# Auther : shenyuming
# @File : handle_threading.py
# @Software : PyCharm
import threading
import time

# def read():
#     for i in range(5):
#         print(f'在%s时间时，在听音乐'% time.ctime())
#         time.sleep(2)
#
# def write():
#     for j in range(5):
#         print(f'在%s时间时，在看影片'% time.ctime())
#         time.sleep(2)
#
# def other():
#     for i in range(5):
#         print('在执行其他的任务')
#         time.sleep(1)
#
# def mon():
#     music_list = []
#     tv_list = []
#     for i in range(3):
#         music_thread = threading.Thread(target=read)
#         music_list.append(music_thread)
#     for j in range(3):
#         tv_thread = threading.Thread(target=write)
#         tv_list.append(tv_thread)
#
#     for n in range(0,3):
#         music_list[n].start()
#         tv_list[n].start()
#
#     other()
#
#
# if __name__ == '__main__':
#     mon()
    # other()


# count = 0
# class MyThread(threading.Thread):
#     def __init__(self,threadNmae):
#         super(MyThread,self).__init__(name=MyThread)
#     def run(self) -> None:
#         global count
#         for i in range(10):
#             count += 1
#             time.sleep(1)
#             print(self.getName(),count)
# for i in range(2):
#     MyThread('MyThreadName:'+str(i)).start()


# exfilg = 0
# class MyThread(threading.Thread):
#     def __init__(self,threadID,name,delay):
#         threading.Thread.__init__(self)
#         self.threadId = threadID
#         self.name = name
#         self.delay = delay
#     def run(self):
#         print('开始线程：',self.name)
#         lock.acquire()  #获得锁
#         print_time(self.name,self.delay,5)
#         lock.release() #释放锁
#         print('结束线程：',self.name)
#
# def print_time(threadName,delay,count):
#     while count:
#         if exfilg:
#             threadName.exit()
#         time.sleep(delay)
#         print('%s:%s'% (threadName,time.ctime(time.time())))
#         count-=1
# #线程锁创建
# lock = threading.Lock()
# #存放线程list
# threadlist = []
#
# thread1 = MyThread(1,'thread-1',1)
# thread2 = MyThread(2,'thread-2',2)
#
# threadlist.append(thread1)
# threadlist.append(thread2)
#
# thread1.start()
# thread2.start()
# for i in threadlist:
#     i.join()
# print('退出主线程')



# def job1():
#     time.sleep(3)
#     print(f'the number of T1 is %s' % threading.current_thread())
#
# def job2():
#     print('T2 start')
#     for i in range(5):
#         time.sleep(1)
#         print(i)
#     print('T2 finsh')
#
# def run():
#     job2_thread = threading.Thread(target=job2,name='T2')
#     job2_thread.start()
#     job2_thread.join()  ## 执行完毕 job2_thread线程后在执行之后的
#     print('ALL CODE！！！')
#     print(job2_thread.getName())  #获得线程名
# if __name__ == '__main__':
#     # new_thread = threading.Thread(target=job1,name='T1')
#     # new_thread.setDaemon(True)
#     # new_thread.start()
#     # print(f'返回正在运行的数量：',threading.active_count())
#     # print(f'返回一个包含正在运行的线程的list:',threading.enumerate())
#     # print(f'返回当前的线程变量：',threading.current_thread())
#     run()


# class lianxi:
#     def A_thread(self):
#         lock.acquire()
#         for i in range(10):
#             print(f'我是A方法')
#             time.sleep(0.8)
#         lock.release()
#
#     def B_thread(self):
#         lock.acquire()
#         for i in range(10):
#             print(f'我是B方法')
#             time.sleep(0.5)
#         lock.release()
#
#     def run(self):
#         A_t = threading.Thread(target=lianxi().A_thread)
#         B_t = threading.Thread(target=lianxi().B_thread)
#         A_t.setDaemon(True)
#         B_t.setDaemon(True)
#         A_t.start()
#         B_t.start()
#
#         # 其他方法
#         c = 1
#         for i in range(15):
#             print(f'执行主线程任务-->',c)
#             time.sleep(1)
#             c+=1
# #创建锁
# lock = threading.Lock()
#
#
# if __name__ == '__main__':
#     lianxi().run()



class MyThread(threading.Thread):
    def __init__(self,a):
        threading.Thread.__init__(self)
        self.a = a
    def run(self):
        print(f'线程开始')
        A_Thred(self.a)
        # B_Thred(self)
        print(f'线程结束')

        c = 1
        for i in range(10):
            print(f'正在执行任务',c)
            time.sleep(1)
            c+=1

def A_Thred(a):
    lock.acquire()
    for i in range(a):
        print(f'A执行')
        time.sleep(2)
    lock.release()
lock = threading.Lock()

if __name__ == '__main__':
    t1 = MyThread(7)
    t1.start()
