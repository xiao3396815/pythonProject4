# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author: 沙陌 微信：Matongxue_2
# @Time: 2022-02-19 14:55
# @Copyright：北京码同学

import requests

session = requests.session()  # 使用该对象发起接口调用，可以自动关联cookie
# requests库是帮我们进行接口调用的，可以拿到接口的响应信息
url = 'http://121.42.15.146:9090/mtx/index.php?s=/index/user/login.html'

headers = {
    "X-Requested-With": "XMLHttpRequest"
}

data = {
    "accounts": "shamotest1",
    "pwd": "123456"
}
# 根据接口基本信息发起调用，并得到服务器响应resp，包含了响应headers,响应状态码，响应body体
resp = session.request(url=url, method='post', headers=headers, data=data)
print(resp.status_code)  # 获取响应状态码
print(resp.json())  # 获取响应body体的json格式数据

# 接下来调用提交订单的接口，但是提交订单需要登录接口所产生的cookie信息
url = 'http://121.42.15.146:9090/mtx/index.php?s=/index/buy/add.html'
data = {
    "goods_id": 8,
    "stock": 1,
    "buy_type": "goods",
    "address_id": 1651,
    "payment_id": 1,
    "spec": "[]",
    "user_note": ""
}

resp = session.request(url=url, method='post', headers=headers, data=data)
print(resp.status_code)  # 获取响应状态码
print(resp.json())  # 获取响应body体的json格式数据
