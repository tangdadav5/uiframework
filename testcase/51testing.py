# -*- coding:utf-8 -*-
from selenium import webdriver
import unittest
import time


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("http://bbs.51testing.com/forum.php")
        driver.find_element_by_id("ls_username").click()
        driver.find_element_by_id("ls_username").clear()
        driver.find_element_by_id("ls_username").send_keys("皂滑弄人")
        driver.find_element_by_id("ls_password").click()
        driver.find_element_by_id("ls_password").clear()
        driver.find_element_by_id("ls_password").send_keys("zxc3465132?")
        driver.find_element_by_xpath("//button[@type='submit']/em").click()
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
