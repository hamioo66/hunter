# -*- coding=UTF-8 -*-
#读取excel文件
# import xlrd
# data=xlrd.open_workbook('text\readMe.xls')
# #获取一个工作表
# table=data.sheets()[0]#通过索引顺序获取
# table1=data.sheet_by_index(0)
# table2=data.sheet_by_name(u'sheet')
# #获取整行和整列的值（数组）
# table.row_values(i)
# table.col_values(j)
# #获取行数和列数
# nrows=table.nrows
# ncols=table.ncols
# #循环行列表数据
# for i in range(nrows):
#     print table.row_values(i)

import xdrlib,sys
import xlrd
def open_excel(file='text/readMe.xls'):
    try:
        data=xlrd.open_workbook(file)
        return data
    except Exception,e:
        print str(e)
# 根据索引获取Excel表格中的数据，参数：file:Excel文件路径  colnameindex:表头列名所在行的索引，by_index:表的索引
def excel_table_byindex(file='text/readMe.xls',colnameindex=0,by_index=0):
    data=open_excel(file)
    table=data.sheets()[by_index]
    nrows=table.nrows
    ncols=table.ncols
    colnames=table.row_values(colnameindex)
    list=[]
    for rownum in range(1,nrows):
        row=table.row_values(rownum)
        if row:
            app={}
            for i in range(len(colnames)):
                app[colnames[i]]=row[i]
            list.append(app)
    return list
#根据名称获取excel表格中的数据，参数：file：Excel文件 路径  colnameindex：表头列名所在行的索引，by_name:sheet1名称

def excel_table_byname(file='text/readMe.xls',colnameindex=0,by_name=u'sheet1'):
    data=open_excel(file)
    table=data.sheet_by_name(by_name)
    nrows=table.nrows
    colnames=table.row_values(colnameindex)
    list=[]
    for rownum in range(1,nrows):
        row=table.row_values(rownum)
        if row:
            app={}
            for i in range(len(colnames)):
                app[colnames[i]]=row(i)
            list.append(app)
    return list
def main():
    tables=excel_table_byindex()
    for row in tables:
        print row
    tables=excel_table_byname()
    for row in tables:
        print row
if __name__=="__main__":
    main()