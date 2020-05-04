# encoding:utf-8
# Motto：good good study, day day up. why you so lazy ？？？

import pytest

from Page.LoginPage import Login

# @pytest.mark.skip
from utils.case_base import TestCaseBase


class TestLogin(TestCaseBase):
    """登录首页"""
    LoginData = TestCaseBase().get_data()

    @pytest.fixture(scope='function', autouse=True)
    def start(self, driver):
        self.login_page = Login(driver)

    #     self.login_page.F5()

    # @pytest.mark.base_case
    @pytest.mark.parametrize('user, pwd, expect', [value.values() for value in LoginData.get("test_login_success")])
    def test_login_success(self, user, pwd, expect):
        """测试登录成功"""
        self.login_page.login(username=user, password=pwd)

        # assert self.login_page.assert_text_in_source(expect)


if __name__ == '__main__':
    pytest.main(['-s'])
