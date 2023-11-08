# -*- coding:utf-8 -*-
# @Time : 2023/5/8 13:26
# Auther : shenyuming
# @File : handle_apiConfig_yml.py
# @Software : PyCharm

'''
    读取yml文件数据
'''
import yaml

def get_data_yml(fileDir):
    with open(fileDir,encoding='utf-8') as fo:
        return yaml.safe_load(fo.read())

##获取yml用例函数 , 最终处理结果格式[(),(),()]
def get_yml_caseData(fileDir):
    resList = [] #存放数据[(描述，参数，结果),(描述，参数，结果)]
    res = get_data_yml(fileDir)
    for i in res:
        resList.append((i['detail'],i['data'],i['resp']))
    return resList

if __name__ == '__main__':
    print(get_data_yml('../data/loginCase.yml'))
    print(get_yml_caseData('../data/loginCase.yml'))