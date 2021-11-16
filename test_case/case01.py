import json

import unittest

from api_key.api import ApiDemo

'''
    优化项:封装api方法的调用
    使用到的类:api_key包下的api.py文件
'''
class CaseDemo(unittest.TestCase):
    def test01_login(self):
        ad = ApiDemo()
        # 单接口请求
        url = 'http://58.247.87.190:8002/songbaisys/sys/sys_login_new'
        data = {
            'USER_NAME': '汪明月123',
            'PASSWORD': 'Wang@123'
        }
        header = {
            'Content-Type': 'application/json'
        }
        # 调用已经封装的post方法
        # json.dumps()
        res = ad.do_post(url=url, data=json.dumps(data), headers=header)
        # 输出响应结果
        print(res.text)

        # 断言校验本次测试是否成功:将实际的结果与预期结果进行对比,校验本次测试是否正确
        # 注意:字段的大小写
        # assert res.json()['MSG'] == 'success', '断言失败'
        # 使用unitest中的方法进行比较
        self.assertEqual('success', res.json()['MSG'], '断言失败')

if __name__ == '__main__':
    unittest.main()