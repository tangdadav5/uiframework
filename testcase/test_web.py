# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
import time
'''两个用例分别打开两次浏览器'''


class UntitledTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("http://127.0.0.1:5000/")

    def test_click(self):
        dr = self.driver
        dr.find_element_by_xpath('//*[@id="testid"]').click()
        time.sleep(1)
        dr.switch_to.alert.accept()
        time.sleep(1)

    def test_login(self):
        self.driver.find_element_by_xpath('/html/body/a').click()
        self.driver.find_element_by_name('username').send_keys('123')
        self.driver.find_element_by_name('password').send_keys('456')
        self.driver.find_element_by_xpath('/html/body/form/p[3]/button')
        time.sleep(1)

    def tearDown(self):
        self.driver.quit()

class TestCaseLogin(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("http://127.0.0.1:5000/")

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def test_click(self):
        self.driver.find_element_by_xpath('//*[@id="testid"]').click()
        time.sleep(1)
        self.driver.switch_to.alert.dismiss()
        time.sleep(1)

    def test_login(self):
        self.driver.find_element_by_xpath('/html/body/a').click()
        self.driver.find_element_by_name('username').send_keys('123')
        self.driver.find_element_by_name('password').send_keys('456')
        self.driver.find_element_by_xpath('/html/body/form/p[3]/button')
        time.sleep(1)


if __name__ == "__main__":
    unittest.main()
