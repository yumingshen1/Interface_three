# -*- coding:utf-8 -*-
# @Time : 2023/5/5 20:02
# Auther : shenyuming
# @File : python_test01.py
# @Software : PyCharm

# def cale(opr):
#     if opr == '+':
#         return lambda a,b:(a+b)
#     else:
#         return lambda a,b:(a-b)
# f1 = cale('+')
# f2 = cale('-')
# print("10+5=[0]".format(f1(10,5)))

#普通函数
def add(x,y):
    return x+y
print(add(2, 3))
# lambda函数
add = lambda x,y:x+y
print(add(3, 4))

t = lambda x : x-3
print(t(5))

# 关于string的 'replace' 不会改变原str的内容
str1 = 'I LOVE PYTHON'
print(str1.replace('LOVE', 'ENJOY').split())
print(str1)

# list--append  : append么有返回值，赋值给workdays后是None 可以:print(workdays.append('zhou'))
workdays = ['周四','周五']
workdays = workdays.append('周六')
print('append没返回值，是None:',workdays)

# 翻转字符串 , .join(reversed())
st = 'python'
st = "".join(reversed(st))
print(st)
 # [::-1]
st1 = st[::-1]
print(st1)

## 四个数字组合多少个不同的三位数
def tm001():
    arr = []
    for i in range(1,5):
        for j in range(1,5):
            for k in range(1,5):
                num = 100*i + 10*j +k
                if i!=j and i!=k and j!=k and num not in arr:
                    arr.append(num)
    print(len(arr),arr)
tm001()


a=b=[3]
print(a,b)
a+=b
print(a,b)


def f(n):
    return n*2 if n<10 else n/2
print(f(f(9)),f(f(12)))

def f(n):
    if n < 10:
        return n*2
    else:
        n / 2


a = [1,2,3,4]
a.insert(1,a.pop(2))
print(a)
