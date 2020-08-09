# -*- coding: utf-8 -*-
# @author : 刘捷
# @time   : 2020-08-06 21:47

import os
import yaml


def get_yaml_data(yaml_path):
    """获取yaml文件数据"""
    f = open(yaml_path, "r", encoding="utf-8")
    yamldata = f.read()
    # print(yamlpath)

    # 把yaml文件数据转字典
    d = yaml.load(yamldata)
    f.close()
    # print(d['test_info_params'])
    return d


if __name__ == '__main__':
    # read_yaml.py 和 yml文件在一个文件夹，可以直接读取到
    # read_yaml.py 和 yml文件 不在一个文件夹用绝对路径
    cur_path = os.path.dirname(os.path.realpath(__file__))
    print(cur_path)  # F:\PythonProject\pytest_web\common
    print(os.path.dirname(cur_path))  # F:\PythonProject\pytest_web
    yaml_path = os.path.join(os.path.dirname(cur_path), "test_data",
                             "data_demo.yml")  # F:\PythonProject\pytest_web\test_data\data_demo.yml
    print(yaml_path)
    a = get_yaml_data(yaml_path)
    print(a["test_add_canshuhua"])
