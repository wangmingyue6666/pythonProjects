# 导入requests库
import json

import requests
# 单接口请求
url = 'http://58.247.87.190:8002/songbaisys/sys/sys_login_new'
data = {
    'USER_NAME': '汪明月123',
    'PASSWORD': 'Wang@123'
}
header = {
    'Content-Type': 'application/json'
    # 'charset': 'utf-8'
}
# 调用post请求
res = requests.post(url=url, data=json.dumps(data), headers=header)
print(data)
# print(json.dumps(data))
print(res.text)
