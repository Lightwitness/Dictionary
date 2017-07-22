#!E:\Python python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/22 11:50
# @Author  : Lightwitness
# @File    : testSelenium1.py
# @Software: PyCharm

from selenium import webdriver
import time
def dict(word):
    driver = webdriver.Chrome()

    driver.get("http://fanyi.youdao.com/")
    # assert u"百度一下，你就知道 " in driver.title

    elem = driver.find_element_by_id("inputText")
    elem.clear()
    elem.send_keys(word)
    driver.find_element_by_id("translateBtn").click()
    time.sleep(2)
    driver.close()
if __name__ == '__main__':
    print '请输入英语：'
    word = raw_input()

    while(word != "byebye"):
        dict(word)
        print '请继续输入英语，退出请输入“byebye”'
        word = raw_input()