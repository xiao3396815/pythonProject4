# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author: 沙陌 微信：Matongxue_2
# @Time: 2022-02-19 15:51
# @Copyright：北京码同学

# 使用pytest的参数化方式来实现excel数据的执行
import pytest

from excel_load import read_excel
from requests_client import send

test_data = read_excel('shop.xlsx', 'Sheet2')


# 参数化时，需要有变量去接收你的测试数据
@pytest.mark.parametrize('casename,url,method,headers,params,expect_status,expect_busi_code,expect_msg', test_data)
def test_case(casename, url, method, headers, params, expect_status, expect_busi_code, expect_msg):
    headers = eval(headers)
    params = eval(params)
    resp = send(url=url, method=method, headers=headers, **params)
    actual_status = resp.status_code
    actual_busi_code = resp.json()['code']
    actual_msg = resp.json()['msg']
    # 断言，多断言使用pytest-assume这个插件来完成
    pytest.assume(expect_status == actual_status)
    pytest.assume(expect_busi_code == actual_busi_code)
    pytest.assume(expect_msg == actual_msg)
