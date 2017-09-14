# -*- coding: UTF-8 -*-
#我的收入提现功能
import os,time
import logging
from appium import webdriver

#-------------------------------------------------------------------------------------------start
device='8ac7d424'                                     #此处设备号
pack='com.yiyaotong.flashhunter'                      #此处是app的package名称
#pack="com.tencent.mobileqq"
activity='com.yiyaotong.flashhunter.ui.MainActivity'  #此处是app的主activity
#activity='com.tencent.mobileqq.troop.MainActivity'
PATH=lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))
#定义驱动参数
desired_caps={}
desired_caps['device'] = 'android'
desired_caps['platformName']='Android'
desired_caps['browserName']=''
desired_caps['Version']='4.4.4'
desired_caps['deviceName']=device
#desired_caps['app']=PATH('D:\\jr.apk')
desired_caps['appPackage'] = pack
desired_caps['appActivity'] = activity
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True
driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.implicitly_wait(3)


logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='myapp.log',
                filemode='w')

#################################################################################################
#定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)


#swipe方法（app）
def get_size():
    x=driver.get_window_size()['width']
    y=driver.get_window_size()['height']
    return(x,y)
#下滑
def swipe_down(t):
    screen = get_size()
    driver.swipe(screen[0] * 0.5, screen[1] * 0.25, screen[0] * 0.5, screen[1] * 0.75, t)
#切换我的
def mine():
    el = driver.find_elements_by_id('tv_tab')
    el[3].click()
    time.sleep(3)

def Login(username,password):
    driver.find_element_by_name('账号密码登录').click()
    driver.find_element_by_id('edit_phone').send_keys(username)
    driver.find_element_by_id('edit_pw').send_keys(password)
    driver.find_element_by_id('btm_login').click()
def Logout():
    driver.find_element_by_id('logout').click()
mine()              #切换到我的
driver.find_element_by_id('memberAvatarIV').click()  # 点击头像
if driver.find_element_by_id('titlebar_text').text == u'登录':
    Login('17300286293', '123456')
elif driver.find_element_by_id('titlebar_text').text == u'个人信息':
    Logout()
    # swipe_down(1000)
    driver.find_element_by_id('memberAvatarIV').click()
    Login('17300286293', '123456')
else:
    driver.quit()
mine()              #切换到我的
layouts=driver.find_elements_by_id('layout1')
layouts[1].click()
#获取当前会员可用积分
keyong=driver.find_element_by_id('tv_integral').text
logging.info(u"会员当前可用积分为:%s" %keyong)
#获取当前会员待用积分
daiyong=driver.find_element_by_id('tv_integral1').text
logging.info(u"会员当前待用积分为:%s" %daiyong)
#获取当前会员提现积分
tixian=driver.find_element_by_id('tv_integral2').text
logging.info(u"会员当前提现积分为:%s" %tixian)

driver.find_element_by_id('tv_extract').click()     #点击提现
driver.find_element_by_id('edit_integral').send_keys('100')
jifen=driver.find_element_by_id('edit_integral').text
logging.info(u"当前提现积分为:%s" %jifen)
driver.find_element_by_id('btm_extract').click()
tv_names=driver.find_elements_by_id('tv_name')
i=0
while i<6:
   tv_names[i].click()
   i=i+1
logging.info(u"输入密码成功")
#提现申请后获取当前会员可用积分
keyong1=driver.find_element_by_id('tv_integral').text
logging.info(u"提现后会员当前可用积分为:%s" %keyong1)
title=driver.find_element_by_id('titlebar_text').text
#print type(float(keyong))
#print type(float(keyong1))
#print float(keyong)==float(keyong1)+100.0
if title==u"我的积分" and float(keyong)==float(keyong1)+100.0 :
    logging.info(u'提现申请成功')
    time.sleep(6)
    #后台验证
    from selenium import webdriver
    driverWeb=webdriver.Firefox()
    driverWeb.get('http://123.206.57.62:7000')
    driverWeb.maximize_window()
    driverWeb.find_element_by_name("telphone").clear()
    driverWeb.find_element_by_name("telphone").send_keys('15086769552')
    driverWeb.find_element_by_name("password").clear()
    driverWeb.find_element_by_name("password").send_keys('123456')
    driverWeb.find_element_by_id("loginBtn").click()
    time.sleep(6)
    driverWeb.find_element_by_xpath("//*[@id='accordion_a']/li[6]/div").click()
    time.sleep(6)
    driverWeb.find_element_by_xpath("//*[@id='accordion_a']/li[6]/dl/dd[5]/a").click()
    time.sleep(6)
    frames = driverWeb.find_elements_by_tag_name('iframe')
    driverWeb.switch_to.frame(frames[-1])
    time.sleep(3)
    driverWeb.find_element_by_id('example_last').click()
    time.sleep(3)
    ids=driverWeb.find_elements_by_class_name('ids')
    ids[-1].click()
    driverWeb.find_element_by_class_name('js_auditNo').click()    #积分提现运营审核不通过
    driverWeb.find_element_by_class_name('layui-layer-btn0').click()
    time.sleep(3)
    driverWeb.find_element_by_class_name('layui-layer-btn0').click()
    time.sleep(6)
else:
    logging.info(u'提现异常')
#提现申请审核不通过
swipe_down(1000)
keyong2=driver.find_element_by_id('tv_integral').text
logging.info(u"审核不通过，会员当前可用积分为:%s" %keyong2)
#获取当前会员待用积分
daiyong=driver.find_element_by_id('tv_integral1').text
logging.info(u"审核不通过，会员当前待用积分为:%s" %daiyong)
#获取当前会员提现积分
tixian=driver.find_element_by_id('tv_integral2').text
logging.info(u"审核不通过，会员当前提现积分为:%s" %tixian)

title=driver.find_element_by_id('titlebar_text').text
if title==u"我的积分" and float(keyong)==float(keyong1)+100.0 :
    logging.info(u'积分退回成功')
else:
    logging.info(u'提现异常')
time.sleep(6)








