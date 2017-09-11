# -*- coding: UTF-8 -*-
#我的收入提现功能
import os,time
from appium import webdriver
from selenium import webdriver
#-------------------------------------------------------------------------------------------start
# device='8ac7d424'                                     #此处设备号
# pack='com.yiyaotong.flashhunter'                      #此处是app的package名称
# #pack="com.tencent.mobileqq"
# activity='com.yiyaotong.flashhunter.ui.MainActivity'  #此处是app的主activity
# #activity='com.tencent.mobileqq.troop.MainActivity'
# PATH=lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))
# #定义驱动参数
# desired_caps={}
# desired_caps['device'] = 'android'
# desired_caps['platformName']='Android'
# desired_caps['browserName']=''
# desired_caps['Version']='4.4.4'
# desired_caps['deviceName']=device
# #desired_caps['app']=PATH('D:\\jr.apk')
# desired_caps['appPackage'] = pack
# desired_caps['appActivity'] = activity
# desired_caps['unicodeKeyboard'] = True
# desired_caps['resetKeyboard'] = True
# driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
# driver.implicitly_wait(3)
#
#
# el = driver.find_elements_by_id('tv_tab')
# el[3].click()
# time.sleep(3)
# layouts=driver.find_elements_by_id('layout1')
# layouts[1].click()
# #获取当前会员可用积分
# keyong=driver.find_element_by_id('tv_integral').text
# print(u"会员当前可用积分为:%s" %keyong)
# #获取当前会员待用积分
# daiyong=driver.find_element_by_id('tv_integral1').text
# print(u"会员当前待用积分为:%s" %daiyong)
# #获取当前会员提现积分
# tixian=driver.find_element_by_id('tv_integral2').text
# print(u"会员当前提现积分为:%s" %tixian)
#
# driver.find_element_by_id('tv_extract').click()     #点击提现
# driver.find_element_by_id('edit_integral').send_keys('100')
# driver.find_element_by_id('btm_extract').click()
# tv_names=driver.find_elements_by_id('tv_name')
# i=0
# while i<6:
#    tv_names[i].click()
#    i=i+1
# print(u"输入密码成功")
# title=driver.find_element_by_id('titlebar_text').text
# if title==u"我的积分":
#     print(u'提现申请成功')
# time.sleep(6)

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
frames.switch_to.frame(frames[-1])
time.sleep(3)
driverWeb.find_element_by_id('example_last').click()
ids=driverWeb.find_elements_by_class_name('ids')
ids[-1].click()




