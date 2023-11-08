# -*- coding:utf-8 -*-
# @Time : 2023/5/12 15:29
# Auther : shenyuming
# @File : handle_excel.py
# @Software : PyCharm
'''
读取excel
'''
import xlrd,os,json
from utils.handle_path import casedata_path
def get_excel_data(sheetName,caseName,*args,runCase=['all'],execlDir=None):
    """
    :param execlDir: 地址 ,做缺省值，在pytest调用时省事 /  或不缺省在py直接传地址， / 或者写入配置文件，从配置文件读取
    :param sheetName: sheetname页
    :param caseName: 用例名称
    :param *args: 选择用例哪几列
    :param runCase: 用例编码筛选
    :return:[(),()]
    """
    execlDir = os.path.join(casedata_path,'test_devolop.xls')
    #数据处理后存放
    resList = []

    workbook = xlrd.open_workbook(execlDir,formatting_info=True)

    #获得所有模块名
    #sheetnames = workbook.sheet_names()

    #读取某一模块 第一列
    sheetname = workbook.sheet_by_name(sheetName)
    worksheetcol = sheetname.col_values(0)

    #第一行
    worksheetrow = sheetname.row_values(0)

    #获取单元格
    worksheetcell = sheetname.cell_value(0,1)
    worksheetcell2 = sheetname.cell(0,1).value

    #处理传入的用例列名称对应的下标
    colIndexLIst = []
    for i in args:
        colIndexLIst.append(sheetname.row_values(0).index(i))
    # print(colIndexLIst)

    #用例筛选,[001],[001-003],[all]
    runList = []
    if 'all' in runCase:  #all运行全部
        runList = sheetname.col_values(0)
    else:
        for i in runCase:  #一段 01--03
            if '-' in i:
                start,end = i.split('-')
                for j in range(int(start),int(end)+1):
                    runList.append(caseName+f'{j:0>3}')
            else:
                runList.append(caseName+f'{i:0>3}')

    #处理字符传数据--》字典格式
    def is_json(inData):
        try:
            json.loads(inData)
            return True
        except:
            return False

    #初始行,  循环读取每行对应的列数据
    rowNum = 0
    for one in sheetname.col_values(0):
        if caseName in one and one in runList:
            # resBody = sheetname.cell_value(rowNum,9)
            # resData = sheetname.cell_value(rowNum,11)
            getcoldata =[]
            for num in colIndexLIst:
                tmp = sheetname.cell_value(rowNum,num)
                if is_json(tmp): #判断是否是json
                    tmp = json.loads(tmp)
                getcoldata.append(tmp)
            resList.append(list(getcoldata))
        rowNum+=1
    for i in resList:
        print(i)
    return resList

if __name__ == '__main__':
    get_excel_data('登录模块','Login','请求参数','预期结果',runCase=['1','3-5','6'],execlDir=os.path.join(casedata_path,'test_devolop.xls'))