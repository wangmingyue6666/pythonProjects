import configparser
import json

import unittest

from api_key.api import ApiDemo

from ddt import ddt, file_data


'''
    读取ini文件的数据
    文件:config.ini
'''

@ddt
class CaseDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.ad = ApiDemo()
        # 第一步:定义jsessionId变量,赋值为None
        cls.SESSION_ID = None

        # 实例化configparser
        cf = configparser.ConfigParser()
        # 读取文件
        cf.read('../data/config.ini')
        # 获取数据
        CaseDemo.url = cf.get('DEFAULT', 'url')

    # 登录接口
    @file_data('../data/user1.yaml')
    def test01_login(self, data, txt):
        # 单接口请求
        url = CaseDemo.url + '/songbaisys/sys/sys_login_new'
        header = {
            'Content-Type': 'application/json'
        }
        # 调用已经封装的post方法
        # json.dumps()
        # 第三步(修改用法,增加self.)
        res = self.ad.do_post(url=url, data=json.dumps(data), headers=header)
        # 获取token并赋值给jsessionId
        CaseDemo.SESSION_ID = res.json()['PD']['SESSION_ID']
        # 输出响应结果
        print(1, res.text)

        # 断言校验本次测试是否成功:将实际的结果与预期结果进行对比,校验本次测试是否正确
        # 注意:字段的大小写
        # assert res.json()['MSG'] == 'success', '断言失败'
        # 使用unitest中的方法进行比较
        self.assertEqual(txt, res.json()['MSG'], '断言失败')

    # 分页查询供应商列表
    def test02_querySupplierListByPage(self):
        # 单接口请求
        url = CaseDemo.url + '/songbaisys/supplier/query_supplier_column'
        data = {
            "selectList": [{
                "culumnName": "COUNT_ID",
                "param": "",
                "selectType": "1002001"}],
            "OFFSET": 0,
            "SIZE": 8
        }
        header = {
            'Content-Type': 'application/json',
            'Cookie': 'JSESSIONID=' + self.SESSION_ID
        }
        # 调用已经封装的post方法
        # json.dumps()
        # 第三步(修改用法,增加self.)
        res = self.ad.do_post(url=url, data=json.dumps(data), headers=header)
        # 输出响应结果
        print(2, res.text)

        # 断言校验本次测试是否成功:将实际的结果与预期结果进行对比,校验本次测试是否正确
        # 注意:字段的大小写
        assert res.json()['MSG'] == 'success', '断言失败'

if __name__ == '__main__':
    unittest.main()