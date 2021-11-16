#!/user/bin/env python
# -*- coding:utf-8 -*-
import configparser

'''
    配置管理类
'''
class configRead():
    # 获取DEFAULT下的url路径
    # 定义无惨方法需用@staticmethod 把它标识为一个静态方法
    # 静态方法可不用传self参数
    @staticmethod
    def get_url():
        return configRead.read_url(section='DEFAULT', option='url')

    # 读取配置文件
    def read_url(section, option):
        # 实例化ConfigParser
        cf = configparser.ConfigParser()
        # 读取config.ini文件
        cf.read('../config_manager/config.ini')
        # print(cf.get(section=section, option=option))
        # 返回url
        return cf.get(section=section, option=option)

if __name__ == '__main__':
    configRead.get_url()