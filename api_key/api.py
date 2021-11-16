import requests

'''
    接口的关键字驱动封装
    将常用的请求方法进行函数的封装
'''

class ApiDemo:
    # post封装
    def do_post(self, url, params=None, headers=None, **kwargs):
        return requests.post(url=url, params=params, headers=headers, **kwargs)

    # get封装
    def do_get(self, url, params=None, headers=None, **kwargs):
        return  requests.get(url=url, params=params, headers=headers, **kwargs)