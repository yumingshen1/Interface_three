# -*- coding:utf-8 -*-
# @Time : 2023/4/7 16:00
# Auther : shenyuming
# @File : has_md5.py
# @Software : PyCharm

'''
    md5加密 函数
'''
import hashlib

def get_md5_demo(data:str):
    md5= hashlib.md5(data.encode(encoding='utf-8')) #创建md5对象
    return md5.hexdigest()

