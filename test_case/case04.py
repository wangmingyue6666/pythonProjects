import json

import unittest

from api_key.api import ApiDemo

from ddt import ddt, file_data


'''
    优化项:类实例化的优化
'''

@ddt
class CaseDemo(unittest.TestCase):
    # 第一步(新增)
    @classmethod
    def setUpClass(cls) -> None:
        cls.ad = ApiDemo()

    @file_data('../data/user1.yaml')
    def test01_login(self, data, txt):
        # 第二步(删除)
        # ad = ApiDemo()
        # 单接口请求
        url = 'http://58.247.87.190:8002/songbaisys/sys/sys_login_new'
        header = {
            'Content-Type': 'application/json'
        }
        # 调用已经封装的post方法
        # json.dumps()
        # 第三步(修改用法,增加self.)
        res = self.ad.do_post(url=url, data=json.dumps(data), headers=header)
        # 输出响应结果
        print(res.text)

        # 断言校验本次测试是否成功:将实际的结果与预期结果进行对比,校验本次测试是否正确
        # 注意:字段的大小写
        # assert res.json()['MSG'] == 'success', '断言失败'
        # 使用unitest中的方法进行比较
        self.assertEqual(txt, res.json()['MSG'], '断言失败')

if __name__ == '__main__':
    unittest.main()