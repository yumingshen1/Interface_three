# -*- coding:utf-8 -*-
# @Time : 2023/6/2 17:12
# Auther : shenyuming
# @File : test_shop.py
# @Software : PyCharm
import pytest,allure
from utils.handle_excel import get_excel_data
from common.baseApi import ApiAssert

class TestShop:
    @pytest.mark.parametrize('title,inData,expData',get_excel_data('我的商铺','listshopping','标题','请求参数','响应预期结果'))
    @allure.title("{title}")
    def test_shop_list(self,title,inData,expData,shop_init):
        res = shop_init.query(inData)
        ApiAssert.defassert_api(res['code'],'==',expData['code'])

    def test_shop_update(self):
        pass



if __name__ == '__main__':
    pytest.main(['test_shop.py','-sv'])