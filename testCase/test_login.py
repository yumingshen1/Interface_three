# -*- coding:utf-8 -*-
# @Time : 2023/5/12 15:17
# Auther : shenyuming
# @File : test_login.py
# @Software : PyCharm
'''
    业务层代码封装完
    测试用例-数据驱动
    加测试报告
'''
import pytest,allure
import os
from libs.login import Login
from utils.handle_apiConfig_yml import get_yml_caseData
from utils.handle_excel import get_excel_data
from utils.handle_path import report_path,casedata_path
from common.baseApi import ApiAssert
@allure.epic('测试项目登录接口')
@allure.story('登录')
class TestLogin:
    @pytest.mark.parametrize('title,inData,expData',get_yml_caseData(os.path.join(casedata_path,'loginCase.yml')))#yml用例
    @pytest.mark.parametrize('title,inData,expData',get_excel_data('登录模块','Login','标题','请求参数','响应预期结果'))#excel用例
    @allure.title("{title}")
    def test_login(self,title,inData,expData):
        res = Login().login(inData)
        # assert res['msg'] == expData['msg']
        ApiAssert.defassert_api(res['msg'],'==',expData['msg'])

if __name__ == '__main__':
    pytest.main([__file__,'-sv','--alluredir',f'{report_path}','--clean-alluredir'])
    os.system(f'allure serve {report_path}')