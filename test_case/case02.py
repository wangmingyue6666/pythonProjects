import json

import unittest

from api_key.api import ApiDemo

from ddt import ddt, file_data


'''
    优化项:数据驱动(使用yaml文件进行参数化)
    使用到的文件:user.yaml
'''

@ddt
class CaseDemo(unittest.TestCase):
    @file_data('../data/user.yaml')
    def test01_login(self, data):
        ad = ApiDemo()
        # 单接口请求
        url = 'http://58.247.87.190:8002/songbaisys/sys/sys_login_new'
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