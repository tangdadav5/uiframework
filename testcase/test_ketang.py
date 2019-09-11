# -*- coding: utf-8 -*-
from tools.pyselenium import KeyWord
from pagas.ketang_page import KeTang_login
import unittest
import time


class TestCaseKeTang(unittest.TestCase,KeyWord):
    """腾讯课堂iframe测试"""
    @classmethod
    def setUpClass(self):
        """打开浏览器"""
        self.dr = KeyWord()
        self.dr.wait(10)

    def test_case(self):
        """点击登录1"""
        self.dr.mouse_hover(KeTang_login.hover) # 悬浮分类按钮
        self.dr.element_until_presence_click(KeTang_login.click_login)  # 点击登录
        self.dr.element_until_presence_click(KeTang_login.click_qq_login)   # 点击QQ登录
        self.dr.into_frame(KeTang_login.login_frame)
        self.dr.element_until_presence_click(KeTang_login.username_login)   # 点击账号密码登录
        time.sleep(1)

    def test_case(self):
        """点击登录2"""
        self.dr.mouse_hover(KeTang_login.hover)  # 悬浮分类按钮
        self.dr.element_until_presence_click(KeTang_login.click_login)  # 点击登录
        self.dr.element_until_presence_click(KeTang_login.click_qq_login)  # 点击QQ登录
        self.dr.into_frame(KeTang_login.login_frame)
        self.dr.element_until_presence_click(KeTang_login.username_login)  # 点击账号密码登录
        time.sleep(1)

    @classmethod
    def tearDownClass(self):
        """关闭浏览器"""
        self.dr.close_browser()


if __name__ == "__main__":
    unittest.main()
