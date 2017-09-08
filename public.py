# -*- coding=UTF-8 -*-
#登录
def login(driver,username,password):
    driver.find_element_by_name("telphone").clear()
    driver.find_element_by_name("telphone").send_keys(username)
    driver.find_element_by_name("password").clear()
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_id("loginBtn").click()