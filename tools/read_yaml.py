# -*- coding: utf-8 -*-
import yaml
# from tools.config_path import yaml_path

class ReadYaml():

    def read_yaml(self):
        # """读取yaml配置文件"""
        yaml_path = "./config/data.yaml"
        # yaml_path = r"D:\PythonCode\uiframework\config\data.yaml"
        with open(yaml_path, 'r', encoding="UTF-8") as yamlfile:
            cfg = yaml.load(yamlfile, Loader=yaml.FullLoader)
            # url = cfg['url']
            # browser_type = cfg['browser']['type']
            # browser_mode = cfg['browser']['mode']
            # print(url, browser_type, browser_mode)
            return cfg


if __name__ == '__main__':
    yaml = ReadYaml()
    yaml.read_yaml()
