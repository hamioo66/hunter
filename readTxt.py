# -*- coding=UTF-8 -*-
#读取user_info.txt文件
def readtxt():
    user_file=open('text\user_info.txt','r')
    values=user_file.readlines()
    user_file.close()
    i = []
    for search in values:
        i.append(search)
        print i
    username=i[2].split(',')[0]
    password=i[2].split(',')[1]
    ass=i[2].split(',')[2]
    print username
    print password
    print ass

readtxt()