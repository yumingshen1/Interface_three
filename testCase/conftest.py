# -*- coding:utf-8 -*-
# @Time : 2023/6/2 17:43
# Auther : shenyuming
# @File : conftest.py
# @Software : PyCharm
import pytest
from libs.login import Login
from configs.config import NAMEPASS
from libs.shop import Shop

pytest.fixture(scope='session',autouse=True)
def start_running():
    print('项目开始执行')
    yield
    print('数据清除')


#登录初始化
@pytest.fixture(scope='session')
def login_init():
    _token = Login().login(NAMEPASS,getToken=True)
    yield _token
    print('登录完成')

#店铺实例
@pytest.fixture(scope='class')
def shop_init(login_init):  #login_init 使用有返回值的fixtrue
    shopObject = Shop(login_init)
    yield shopObject  #返回店铺实例

