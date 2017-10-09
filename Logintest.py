# -*- coding=UTF-8 -*-
from selenium import webdriver
import MySQLdb
import public,time,random
#读取user_info.txt文件


#链接数据库
db=MySQLdb.connect("123.206.66.110","dev-test","123456","orion_test")
cursor=db.cursor()
cursor.execute("SELECT MAX(sort) FROM lt_news_classify")      #查找数据库中资讯分类排序号最大的值
maxSort=cursor.fetchone()
db.commit()
print maxSort[0]
db.close()


def login():
    global driver1
    driver1= webdriver.Firefox()
    user_file=open('text/user_info.txt','r')
    values=user_file.readlines()
    user_file.close()
    i=[]
    for search in values:
        i.append(search)
        #获取驱动打开网站
    base_url = 'http://123.206.57.62:7000'
    driver1.get(base_url)
    driver1.maximize_window()
    username=i[3].split(',')[0]
    password=i[3].split(',')[1]
    print("用户名是:%s" %username)
    print("密码是:%s" %password)
    #调用登陆方法
    public.login(driver1,username,password)
    driver1.implicitly_wait(10)
    #driver1.close()


# 资讯管理添加资讯
def addNews():
    driver1.find_element_by_xpath("//*[@id='accordion_a']/li[2]/div").click()
    time.sleep(3)
    driver1.find_element_by_xpath("//*[@id='accordion_a']/li[2]/dl/dd/a").click()
    time.sleep(3)
    #iframe = driver1.find_element_by_class_name('iframeBox')
    frames=driver1.find_elements_by_tag_name('iframe')
    driver1.switch_to.frame(frames[-1])
    time.sleep(3)
    driver1.find_element_by_class_name('js_addLabour').click()
    time.sleep(3)
    driver1.switch_to.frame(driver1.find_element_by_id('layui-layer-iframe1'))
    driver1.find_element_by_id('title0').send_keys(u"测试title"+str(random.randint(0,100)))
    driver1.find_element_by_class_name('dropdown-toggle').click()
    driver1.find_element_by_class_name("dropdown-menu")
    text1 = driver1.find_elements_by_class_name("text")
    #print random.randint(2,8)
    text1[random.randint(2,8)].click()
    time.sleep(3)
    editFrame=driver1.find_element_by_class_name('ke-edit-iframe')
    driver1.switch_to.frame(editFrame)
    driver1.find_element_by_class_name('ke-content').click()
    driver1.find_element_by_class_name('ke-content').send_keys(u"如果说你是海上的烟火我是浪花的泡沫某一刻你的光照亮了我如果说你是遥远的星河耀眼得让人想哭我是追逐着你的眼眸总在孤单时候眺望夜空我可以跟在你身后像影子追着光梦游我可以等在这路口")
    time.sleep(3)
    driver1.switch_to.parent_frame()
    #用google浏览器驱动解决不下滑查找元素
    target=driver1.find_element_by_class_name('submit')
    driver1.execute_script("argument[0].scrolltoView();",target)
    #火狐驱动直接找到元素
    driver1.find_element_by_class_name('submit').click()
    time.sleep(3)
    driver1.find_element_by_id('layui-layer1')
    driver1.find_element_by_class_name('layui-layer-btn-c').click()


#系统管理（添加资讯分类）
def addNewsType():
    driver1.find_element_by_xpath("//*[@id='accordion_a']/li[8]/div").click()
    time.sleep(6)
    driver1.find_element_by_xpath("//*[@id='accordion_a']/li[8]/dl/dd[2]/a").click()
    time.sleep(6)
    frames=driver1.find_elements_by_tag_name('iframe')
    driver1.switch_to.frame(frames[-1])
    time.sleep(3)
    driver1.find_element_by_class_name('js_addLabour').click()
    time.sleep(6)
    driver1.find_element_by_id('editClassifyName').send_keys(u'测试'+str(random.randint(0,100)))
    time.sleep(3)
    driver1.find_element_by_id('editSort').send_keys(int(maxSort[0])+1)
    time.sleep(3)
    driver1.find_element_by_id('isActive').click()
    time.sleep(3)
    driver1.find_element_by_class_name('layui-layer-btn0').click()
    time.sleep(3)
    driver1.find_element_by_class_name('layui-layer-btn0').click()

def main():
    #调用登录方法
    login()
    time.sleep(6)
    #调用添加资讯分类
    #addNewsType()
    #添加资讯
    addNews()
    time.sleep(6)

#main()