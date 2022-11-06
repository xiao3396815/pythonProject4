# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author: 沙陌 微信：Matongxue_2
# @Time: 2022-02-19 15:18
# @Copyright：北京码同学

import requests

session = requests.session()


# 对于一个接口，url和请求方式一定是需要的，
# 但是注意headers、请求参数这些不一定有，所以我们使用**kwargs来表示不确定的参数
def send(url, method, **kwargs):
    resp = session.request(url=url, method=method, **kwargs)
    return resp
