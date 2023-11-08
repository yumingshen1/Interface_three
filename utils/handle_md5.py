# -*- coding:utf-8 -*-
# @Time : 2023/5/8 15:48
# Auther : shenyuming
# @File : handle_md5.py
# @Software : PyCharm

'''
    md5加密
'''
import hashlib

def get_data_md5(data:str):
    md5 = hashlib.md5(data.encode(encoding='utf-8'))
    return md5.hexdigest()