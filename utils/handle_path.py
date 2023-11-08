# -*- coding:utf-8 -*-
# @Time : 2023/5/8 14:11
# Auther : shenyuming
# @File : handle_path.py
# @Software : PyCharm
'''
获取系统路径 ,  os.path.abspath处理反斜杠
'''
import copy
import os

#工程路径
project_path = os.path.dirname(os.path.dirname(__file__))

#apiconfig.yml文件路径
apiconfig_yml_path = os.path.join(project_path,'configs')

#casedata_path
casedata_path = os.path.join(project_path,'data')

#report_path
report_path = os.path.join(project_path,'outFiles/report')

#logs_path
logs_path = os.path.join(project_path,'outFiles/logs')

#config_path
config_path = os.path.join(project_path,'configs/loguru.ini')

#erweima
erweima = os.path.join(project_path,'outFiles/logs/erweima')
