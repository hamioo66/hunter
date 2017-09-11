# -*- coding: UTF-8 -*-
import os
from appium import webdriver
#TouchAction方法时appium自己定义的新方法
# *短按(press)  *释放(release) * 移动到(moveTo) *点击(tap) *等待(wait) *长按(longPress) *执行(perform)
from appium.webdriver.common.touch_action import TouchAction
import MySQLdb#,Logintest
import time,random

#----------调用后台添加资讯分类----------
#Logintest.main()
#time.sleep(10)

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

#-------------------------------------------------------------------------------------------end
#链接数据库
db=MySQLdb.connect("123.206.66.110","dev-test","123456","orion_test",charset="utf8")
cursor=db.cursor()
cursor.execute("SELECT sort,classifyName FROM lt_news_classify ORDER BY sort DESC limit 1")      #查找数据库中资讯分类排序号最大的值
data=cursor.fetchone()
db.commit()
print data[0],data[1]
db.close()




#-------------------------------------------------------------------------------------------start
el = driver.find_elements_by_id('tv_tab')
# 获取首页【猎眼】
def news():
    el[0].click()
    driver.implicitly_wait(10)
# 获取首页【猎头】
def hunter():
    el[1].click()
    driver.implicitly_wait(10)
# 获取首页【购物车】
def cart():
    el[2].click()
    driver.implicitly_wait(10)
# 获取首页【我的】
def mine():
    el[3].click()
    time.sleep(3)
    driver.find_element_by_id('memberAvatarIV').click()  # 点击头像
    time.sleep(3)
#-------------------------------------------------------------------------------------------end

#-------------------------------------------------------------------------------------------start
#swipe方法（app）
def get_size():
    x=driver.get_window_size()['width']
    y=driver.get_window_size()['height']
    return(x,y)
#上滑
def swipe_up(t):
    screen=get_size()
    driver.swipe(screen[0] * 0.5, screen[1] * 0.75, screen[0] * 0.5, screen[1] * 0.25, t)
#下滑
def swipe_down(t):
    screen = get_size()
    driver.swipe(screen[0] * 0.5, screen[1] * 0.25, screen[0] * 0.5, screen[1] * 0.75, t)
#左滑
def swipe_left(t):
    screen = get_size()
    driver.swipe(screen[0] * 0.75, screen[1] * 0.5, screen[0] * 0.25, screen[1] * 0.5, t)
#右滑
def swipe_right(t):
    screen = get_size()
    driver.swipe(screen[0] * 0.25, screen[1] * 0.5, screen[0] * 0.75, screen[1] * 0.5, t)

#-------------------------------------------------------------------------------------------end
#s随机生成手机号
def randomPhoneNum():
    i = '13'
    j = str(random.randrange(4, 10)) + ''.join(str(random.choice(range(10))) for j in range(8))
    phoneNum = i + j
    print phoneNum


#登录（参数是用户名和验证码）
def Login(username,password):
    driver.find_element_by_id('edit_phone').send_keys(username)      #手机号
    driver.find_element_by_id('yzm_edit').send_keys(password)        #手机验证码
    #driver.find_element_by_id('send_yzm').click()
    #driver.find_element_by_id('checkbox').click()
    driver.find_element_by_id('btm_login').click()                   #点击登录

#通过用户名和密码登录
def fs(username,password):
    driver.find_element_by_name('账号密码登录').click()
    driver.find_element_by_id('edit_phone').send_keys(username)
    driver.find_element_by_id('edit_pw').send_keys(password)
    driver.find_element_by_id('btm_login').click()

#退出
def Logout():
    driver.find_element_by_id('logout').click()                    #点击退出登录

#判断是否登录
def isOrnotLogin():
    mine()
    if driver.find_element_by_id('titlebar_text').text==u'登录':
        Login('15599155289','666666')
    elif driver.find_element_by_id('titlebar_text').text==u'个人信息':
        Logout()
        #swipe_down(1000)
        driver.find_element_by_id('memberAvatarIV').click()
        Login('15599155289', '666666')
    else:
        driver.quit()

#添加商品
def addProduct():
    driver.find_element_by_id('goToHunterCenterTV').click()
    driver.find_element_by_id('rl_product_manage').click()
    driver.find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.TextView[contains(@text,"添加商品")]')

#查看验证资讯分类排序
def checkNewsType():
    driver.find_element_by_id('open_layout').click()
    texts=driver.find_elements_by_class_name('android.widget.TextView')
    if texts[-1].text==data[1]:
        print "新增资讯分类排序正确"
    else:
        print "新增资讯分类排序不对"
    texts[-1].click()
    #print len(texts)

#聊天
def communication():
    driver.find_element_by_id('searchBarLayout').click()
    time.sleep(3)
    driver.find_element_by_id('et_search').send_keys(u'周海蜜测试')
    driver.find_element_by_id('tv_search').click()
    #获取猎头tab页
    texts=driver.find_elements_by_class_name('android.widget.TextView')
    texts[3].click()
    #遍历卡片，找到第一个
    cards=driver.find_elements_by_id('headIV')
    cards[1].click()
    driver.find_element_by_id('callBT').click()

    #点击发送语音
    driver.find_element_by_id('rc_voice_toggle').click()
    action=TouchAction(driver)
    #长按发送语音
    action.long_press(driver.find_element_by_id('rc_audio_input_toggle'),duration=6000).perform().release()
    print "语音发送成功"
    #切换回输入法
    driver.find_element_by_id('rc_voice_toggle').click()
    driver.find_element_by_id('rc_edit_text').send_keys(u'测试发送消息11111')
    driver.find_element_by_id('rc_send_toggle').click()
    print "测试信息发送成功"

    #发送图片及文件
    driver.find_element_by_id('rc_plugin_toggle').click()
    driver.find_element_by_id('rc_ext_plugin_icon').click()
    driver.find_element_by_id('mask').click()
    driver.find_element_by_id('send').click()
    print "图片发送成功"
    driver.find_element_by_id('rc_voice_toggle').click()

    global sends,sendTime
    sends=driver.find_elements_by_id('rc_time')
    sendTime=sends[-1].text
    print(u"消息发送时间：%s" %sendTime)
    #assert u"测试发送消息11111" in driver.page_source
    # print "测试信息发送成功"#, driver.page_source



#重置app
#driver.reset()

# 校验猎头分类排序
def checkNews():
    checkNewsType()

def checkContact():
    #校验聊天
    isOrnotLogin()
    news()
    communication()
    driver.implicitly_wait(10)
    i=0
    while i < 4:
        driver.keyevent(4)
        i=i+1
        time.sleep(3)

    print "回到猎眼页面成功"
    mine()
    membername = driver.find_element_by_id('info').text
    print u"当前用户是：",membername
    Logout()
    swipe_down(1000)
    driver.find_element_by_id('memberAvatarIV').click()  # 点击头像
    Login('17300286293','666666')
    driver.find_element_by_id('goToHunterCenterTV').click()
    huntername = driver.find_element_by_id('tv_hunte_name').text
    print u"当前用户是：", huntername
    driver.find_element_by_id('messages').click()
    driver.find_element_by_name(membername).click()
    receives=driver.find_elements_by_id('rc_time')
    receiveTime=receives[-1].text
    print(u"消息接收时间：%s" % receiveTime)
    if sendTime==receiveTime:
        print u'消息发送成功并能正常接收'

#执行方法
checkContact()
#checkNews()










