# -*- coding: utf-8 -*-
from tools.pyselenium import KeyWord
from pagas.baidu_page import Baidu_search
import unittest


class TestCaseBaidu(unittest.TestCase,KeyWord):
    """百度搜索测试"""
    @classmethod
    def setUpClass(self):
        """打开浏览器"""
        self.dr = KeyWord()
        self.dr.wait(10)

    def test_case1(self):
        """搜索123"""
        self.dr.mouse_hover(Baidu_search.hover) # 悬停失败
        self.dr.element_until_send_keys(Baidu_search.send_keys,'123')
        self.dr.element_until_click(Baidu_search.click)
        self.dr.get_text(Baidu_search.text)

    def test_case2(self):
        """搜索好123"""
        self.dr.element_until_presence_send_keys(Baidu_search.send_keys,'hao123')
        self.dr.element_until_presence_click(Baidu_search.click)
        self.dr.get_text(Baidu_search.text)

    def test_case3(self):
        """搜索好123"""
        self.dr.element_until_visibility_send_keys(Baidu_search.send_keys,'hao123')
        self.dr.element_until_visibility_click(Baidu_search.click)
        self.dr.get_text(Baidu_search.text)

    @classmethod
    def tearDownClass(self):
        """关闭浏览器"""
        self.dr.close_browser()


if __name__ == "__main__":
    unittest.main()
