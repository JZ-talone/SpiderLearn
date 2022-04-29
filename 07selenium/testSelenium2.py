# https://chromedriver.storage.googleapis.com/index.html 驱动地址
# 驱动程序和浏览器版本映射关系
import time

from lxml import etree
from selenium import webdriver

bro = webdriver.Chrome()

bro.get('https://ourcoders.com/user/login/')
#找元素
name_input = bro.find_element(by='id',value='name')
# name_input = bro.find_element_by_id('name')
#输入框赋值
name_input.send_keys('talone')
name_input = bro.find_element_by_id('password')
name_input.send_keys('qwerasdf1234')
submit=bro.find_element_by_id('submit')
#点击
submit.click()
time.sleep(2)
#执行浏览器脚本
bro.execute_script('window.scrollTo(0,document.body.scrollHeight)')
time.sleep(2)
bro.get('https://www.taobao.com/')

name_input = bro.find_element(by='id',value='q')
time.sleep(2)
name_input.send_keys('手机')
time.sleep(2)
name_input = bro.find_element_by_class_name('btn-search')
name_input.click()
time.sleep(2)
#前进后退
bro.back()
time.sleep(2)
bro.forward()
time.sleep(2)

bro.quit()
