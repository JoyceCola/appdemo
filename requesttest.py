# -*- coding: utf-8 -*-


import requests
import pytest
import allure

@allure.feature("登录模块")
class TestLogin():

    @allure.story("这是一个故事")
    @allure.title("这是一个标题1")
    def test_1(self):
        a = "hello"
        assert a in "hello world"

    @allure.title("这是一个标题2")
    @allure.testcase("这里是功能测试用例地址https://www.juhe.cn/box/index/id/479")
    def test_2(self):
        a = "hello"
        assert a in "hi world"

    @allure.title("这是一个标题3")
    def test_3(self):
        a = "hello"
        assert a in "hello friends"
