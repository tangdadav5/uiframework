# -*- coding: utf-8 -*-
import unittest
import time
from tools.HTMLTestRunner import HTMLTestRunner


def run():
    '''第一步：创建一个test suite实例'''
    testcases = unittest.TestSuite()

    '''第二步：用例集添加用例'''
    # 第一种，增加单个用例
    # testcases.addTest(TestCase1('test_case3'))
    # 第二种，增加多个用例
    # testcases.addTests([TestCase1('test_case3'),TestCase2('test_case3')])
    # 第三种，增加一个类的到用例集里，用TestLoader
    # testcases.addTests(unittest.TestLoader().loadTestsFromTestCase(TestCase1))
    # testcases.addTests(unittest.TestLoader().loadTestsFromName('class_note.class18_report.TestCase1'))
    # testcases.addTests(unittest.TestLoader().loadTestsFromNames(['testcase.test_case.TestCase1', 'testcase.test_case.TestCase2']))

    testcases.addTests(unittest.TestLoader().loadTestsFromName('testcase.test_baidu.TestCaseBaidu'))

    '''第三步：TestTestRunner类里面的run方法执行'''
    # unittest.TextTestRunner().run(testcases)
    '''集成报告后的第三步'''
    report_path = "./result/report/"
    report_name = "UI自动化测试报告"
    report_time = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
    dir = report_path + report_name + report_time + ".html"
    file_path = open(dir, 'wb')
    runner = HTMLTestRunner(stream=file_path, title="UI自动化测试报告", description='百度搜索模块用例', verbosity=2)
    runner.run(testcases)

# def run():
#     test_dir = './testcase'
#     suite = unittest.defaultTestLoader.discover(start_dir=test_dir,pattern='test*.py')
#
#     report_time = time.strftime('%Y-%m-%d_%H_%M_%S')
#     report_name = 'UI自动化测试报告'
#     report_path = './report/'
#     reportname = report_path + report_name + report_time + '.html'
#     with open(reportname,'wb') as f:
#         runner = HTMLTestRunner(
#             stream=f,
#             title='测试报告',
#             description='Test the import testcase'
#         )
#         runner.run(suite)
#     # # 发送邮件
#     # sendmail()


if __name__ == '__main__':
    run()