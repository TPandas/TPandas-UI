# encoding:utf-8
# Motto：good good study, day day up. why you so lazy ？？？


# -*-conding:utf-8
# @Time:2019-05-30 6:23
# @auther:grassroadsZ
# @file:handle_requests.py


import json
import requests


class MyRequests(object):
    """
    对request请求进行封装
    """

    def __init__(self):
        """"创建请求会话"""
        self.my_session = requests.Session()

    def __call__(self, method, url, data=None, is_json=False, **kwargs):
        method = method.lower()
        if isinstance(data, str):
            try:
                data = json.loads(data)
            except Exception as e:
                print(e)
                data = eval(data)

        if method == "get":
            res = self.my_session.request(method, url, params=data, **kwargs)
        elif method == "post":
            if is_json:
                res = self.my_session.request(method, url, json=data, **kwargs)
            else:
                res = self.my_session.request(method, url, data=data, **kwargs)
        else:
            res = None
            print("不支持{}的请求方法".format(method))
        return res

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.my_session.close()
