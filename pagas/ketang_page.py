# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


class KeTang_login():
    hover = ('//*[@id="js_main_nav"]/div/div[1]/div[1]/a')
    click_login = (By.XPATH,'//*[@id="js-mod-entry-index"]/a')
    click_qq_login = (By.XPATH,"//*[@class='icon-font i-qq']")
    login_frame = ('login_frame_qq')
    username_login = (By.XPATH,'//*[@id="switcher_plogin"]')
