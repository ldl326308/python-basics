# -*- coding:utf-8 -*-
from selenium import webdriver
import time


def login():
    # 谷歌浏览器驱动
    dr = webdriver.Chrome()

    # 打开登陆163邮箱的网页
    dr.get('http://mail.163.com/')

    # 将浏览器窗口最大化
    # dr.maximize_window()

    # 休息五秒钟等待网页加载完毕
    time.sleep(5)

    # 找到邮箱账号登录框对应的iframe
    # //*[@id="x-URS-iframe1554714954574.2969"]
    # dr.switch_to.frame('x-URS-iframe')

    # 找到邮箱账号输入框
    email = dr.find_element_by_name('email')
    # email = dr.find_element_by_css_selector("[name='email']")
    print('email元素：', email)

    # 将自己的邮箱地址输入到邮箱账号框中
    email.send_keys('liu_di_lin')

    # 找到密码输入框
    password = dr.find_element_by_name('password')

    # 输入自己的邮箱密码
    password.send_keys('kebi24lc07.')

    # 找到登陆按钮
    login_btn = dr.find_element_by_id('dologin')

    # 点击登陆按钮
    login_btn.click()

    # 等待10秒看是否登陆成功
    time.sleep(10)


if __name__ == '__main__':
    login()
