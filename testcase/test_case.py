# -*- coding: utf-8 -*-
import unittest


class TestCase1(unittest.TestCase):

    def setUp(self):
        print('TestCaseLogin1-测试开始')

    def test_case1(self):
        print('TestCaseLogin1-case1')

    def test_case2(self):
        print('TestCaseLogin1-case2')

    def test_case3(self):
        print('TestCaseLogin1-case3')

    def tearDown(self):
        print('TestCaseLogin1-测试结束')


class TestCase2(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print('TestCaseLogin2-测试开始')

    def test_case1(self):
        print('TestCaseLogin2-case1')

    def test_case2(self):
        print('TestCaseLogin2-case2')

    def test_case3(self):
        print('TestCaseLogin2-case3')

    @classmethod
    def tearDownClass(self):
        print('TestCaseLogin2-测试结束')


if __name__=="__main__":
    unittest.main()