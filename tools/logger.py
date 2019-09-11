# -*- coding: utf-8 -*-
import logging
import time


class Logger(object):
    def __init__(self,logger):
        """
        将日志保存到指定的路径文件中
        指定日志的级别，以及调用文件
        """

        # 创建logger文件
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        # 创建一个handle，用来写入日志文件
        log_path = "./result/logs/"
        log_time = time.strftime("%Y-%m-%d_%H-%M-%S")
        log_name = log_path + log_time + '.log'

        filehandle = logging.FileHandler(log_name,encoding="utf-8")
        filehandle.setLevel(logging.INFO)

        # 创建一个handle，用来输入日志到控制台
        controlhandle = logging.StreamHandler()
        controlhandle.setLevel(logging.INFO)

        # 将输出的hangdle格式进行转换
        formatter = logging.Formatter('%(asctime)s  - %(levelname)s - %(message)s')
        filehandle.setFormatter(formatter)
        controlhandle.setFormatter(formatter)

        # 给logger添加handle
        self.logger.addHandler(filehandle)
        self.logger.addHandler(controlhandle)

    def getlog(self):
        return self.logger
