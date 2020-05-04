# encoding:utf-8
# Motto：good good study, day day up. why you so lazy ？？？


from Page.BasePage import Base
from settings import base_url


class Login(Base):
    """登录页"""

    def login(self, username: str, password: str):
        """登录流程"""

        self.visit_url(base_url)
        self.input_username(username)
        self.input_password(password)
        self.click_login_button

    def input_username(self, username):
        return self.send_keys(self.get_attr("user"), username)

    def input_password(self, password):
        return self.send_keys(self.get_attr("passwd"), password)

    @property
    def click_login_button(self):
        return self.click(self.get_attr("login_button"))


if __name__ == '__main__':
    from selenium import webdriver

    driver = webdriver.Chrome()
    l = Login(driver)
    l.login("username", "password", )
