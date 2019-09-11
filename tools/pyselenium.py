# -*- coding: utf-8 -*-
from selenium.webdriver import ActionChains
from tools.browser import Browser
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from tools.logger import Logger

logger = Logger(logger='KeyWord').getlog()


class KeyWord(Browser):

    def __init__(self):
        """初始化并打开浏览器"""
        self.browser = self.open_browser()

    def close_browser(self):
        """关闭浏览器"""
        self.browser.quit()
        logger.info('浏览器执行关闭操作成功')

    def back(self):
        """浏览器返回"""
        self.browser.back()
        logger.info('浏览器执行返回操作成功')

    def forward(self):
        """浏览器前进"""
        self.browser.forward()
        logger.info('浏览器执行前进操作成功')

    def refresh(self):
        """刷新浏览器"""
        self.browser.refresh()
        logger.info('浏览器执行刷新操作成功')

    def set_window_size(self, num, numb):
        """设置浏览器大小"""
        self.browser.set_window_size(num, numb)
        logger.info('浏览器设置指定大小成功，高度为：{0}，宽度为：{1}'.format(num, numb))

    def into_new_handle(self):
        """关闭旧窗口，切换新窗口"""
        try:
            handles = self.browser.window_handles  # 获取所有窗口
            self.sleep(1)
            self.browser.close()  # 关闭就窗口
            self.browser.switch_to.window(handles[-1])  # 切换新窗口
            logger.info('执行窗口切换成功')
        except:
            logger.error('执行窗口切换失败！！！')
            raise ('执行窗口切换失败！！！')

    def sleep(self, s):
        """强制等待时间，调试时使用"""
        time.sleep(s)
        logger.info('正在执行线程等待，等待时间为{}秒'.format(s))

    def wait(self, s):
        """隐示等待时间"""
        self.browser.implicitly_wait(s)
        logger.info('执行隐式等待，等待时长为{}秒'.format(s))

    def into_frame(self, locator):
        """
        进入frame框架
        :param value: frame id 或者 name
        :return:
        """
        try:
            WebDriverWait(self.browser,10).until(EC.frame_to_be_available_and_switch_to_it(locator))
            logger.info('进入frame框架成功，定位into_frame的元素为：', locator)
        except:
            self.get_shot()
            logger.error('进入frame框架失败，', locator, '元素无法找到！！！')
            raise ('进入frame框架失败，', locator, '元素无法找到！！！')

    def out_frame(self):
        """
        退出frame框架
        :return:
        """
        try:
            self.browser.switch_to_default_content()
            logger.info('已退出frame框架')
        except:
            self.get_shot()
            logger.error('退出frame框架失败！！！')
            raise ('退出frame框架失败！！！')

    def mouse_hover(self, locator):
        """
        鼠标移动至某个元素，并停留
        :param locator: 定位方法
        :return:
        """
        try:
            element = self.browser.find_element_by_xpath(locator)
            ActionChains(self.browser).move_to_element(element).perform()
            logger.info('执行鼠标悬停成功，定位方法以及元素为：{}'.format(locator))
        except:
            self.get_shot()
            logger.error('执行鼠标悬停失败！！！，定位方法以及元素为：{} '.format(locator))
            raise ('执行鼠标悬停失败！！！，定位方法以及元素为：{} '.format(locator))

    def js_execute(self, js):
        """执行JS操作"""
        try:
            self.browser.execute_script(js)
            logger.info('执行JS操作元素成功，JS脚本为：', js)
        except :
            logger.error('JS脚本运行出错，请检查后重新运行！！！，JS脚本为：', js)
            raise ('JS脚本运行出错，请检查后重新运行！！！')

    def js_scroll_top(self):
        """滚动到浏览器顶部"""
        js = "window.scrollTo(0,0)"
        self.browser.execute_script(js)

    def js_scroll_end(self):
        """滚动到浏览器底部"""
        js = "window.scrollTo(0,document.body.scrollHeight)"
        self.browser.execute_script(js)

    def select_by_index(self, locator, value, index):
        """通过索引,index是索引第几个，从0开始"""
        element = self.browser.find_element(locator, value)
        Select(element).select_by_index(index)

    def select_by_value(self, locator, value, values):
        """通过value属性"""
        element = self.browser.find_element(locator, value)
        Select(element).select_by_value(values)

    def select_by_text(self, locator, value, text):
        """通过文本值定位"""
        element = self.browser.find_element(locator, value)
        Select(element).select_by_value(text)

    def element_until_click(self, locator):
        """
        等待元素出现，并进行点击操作
        :param locator: 定位方法
        :return:
        """
        element = WebDriverWait(self.browser, 10).until(lambda x: x.find_element(*locator))
        element.click()

    def element_until_send_keys(self, locator, text):
        """
        等待元素出现，并进行输入操作
        :param locator: 定位方法
        :param text: 输入的值
        :return:
        """
        element = WebDriverWait(self.browser, 10).until(lambda x: x.find_element(*locator))
        element.clear()
        element.send_keys(text)

    def element_until_visibility_click(self, locator):
        '''
        等待元素出现，并进行点击操作
        :param locator: 定位方法
        :return:
        '''
        element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(locator))
        element.click()
        logger.info('执行元素等待出现并进行点击操作成功，元素值为：', locator)

    def element_until_visibility_send_keys(self, locator, text):
        '''
        等待元素出现，并进入输入操做
        :param locator: 定位方法
        :param text: 输入的内容
        :return:
        '''
        element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def element_until_presence_click(self, locator):
        '''
        等待元素出现，并进行点击操作
        :param locator:  定位方法
        :return:
        '''
        element = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(locator))
        element.click()
        logger.info('执行元素等待出现并进行点击操作成功，元素值为：', locator)

    def element_until_presence_send_keys(self, locator, text):
        '''
        等待元素出现，并进入输入操做
        :param locator: 定位方法
        :param text: 输入的内容
        :return:
        '''
        element = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_shot(self):
        """
        运行异常进行截图操作
        :return:
        """
        picture_path = "./result/SCRshot/"
        picture_time = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
        try:
            self.browser.get_screenshot_as_file(picture_path + picture_time + '.png')
            logger.info('错误信息已截图，截图地址为：{}'.format(picture_path + picture_time + '.png'))
        except :
            logger.error("执行截图操作失败！！！")
            raise ("执行截图操作失败！！！")

    def get_title(self):
        """获取浏览器title信息"""
        logger.info('执行获取title信息成功，当前title为：{}'.format(self.browser.title))
        return self.browser.title

    def get_url(self):
        """获取浏览器URL地址"""
        logger.info('执行获取当前URL信息成功，当前URL为：{}'.format(self.browser.current_url))
        return self.browser.current_url

    def get_text(self, value):
        """
        根据传入的定位方法获取该路径的文本值
        :param value:   定位元素
        :return:
        """
        try:
            text = self.browser.find_element(*value).text
            logger.info('成功获取文本值，定位元素的方法以及值为：{}，获取的文本值为：{}'.format(value, text))
            return text
        except :
            self.get_shot()
            logger.error('获取文本值失败！！！定位元素的方法以及值为：{}，获取的文本值为：{}'.format(value, text))
            raise ('获取文本值失败！！！定位元素的方法以及值为：{}，获取的文本值为：{}'.format(value, text))

    def get_alert_text(self):
        """获取弹窗的文本内容"""
        alert = self.browser.switch_to_alert()
        rel = alert.text
        logger.info('获取alert弹窗文本值内容成功，内容值为：{}'.format(rel))
        return rel

    def close_alter(self):
        """关闭alter弹窗"""
        alter = self.browser.switch_to.alert
        # alter.accept()  # 确认并关闭弹窗
        alter.dismiss()  # 取消并关闭弹窗
        logger.info('alter弹窗执行关闭操作成功')
