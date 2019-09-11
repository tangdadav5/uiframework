# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


class Baidu_search():
    hover = (By.XPATH, '//*[@id="u1"]/a[9]')     # 更多产品
    hover1 = ('//*[@id="u1"]/a[9]')              # 更多产品
    send_keys = (By.ID, 'kw')                    # 输入框
    click = (By.XPATH, '//*[@id="su"]')          # 百度一下
    text = (By.XPATH, '//a[text()="官网"]')


