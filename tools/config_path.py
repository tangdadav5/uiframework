# -*- coding: utf-8 -*-
import os
base_path = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]

# yaml文件路径
yaml_path = os.path.join(base_path,'config', 'data.yaml')

# 截图路径
picture_path = os.path.join(base_path, 'result/SCRshot/')

# 日志路径
log_path = os.path.join(base_path, 'result/logs/')

# 报告路径
report_path = os.path.join(base_path, 'result/report/')

