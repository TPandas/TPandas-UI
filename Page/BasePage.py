import os

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.support.wait import WebDriverWait

from settings import ROOT_PATH
from utils.handle_requests import MyRequests


class Base:
    mock_url = "http://111.231.133.146:38080/app/mock/2/manage/element"

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10
        self.api_search = MyRequests()

    def wait_element_be_click(self, locator) -> bool:
        wait = WebDriverWait(self.driver, self.timeout)
        ele = wait.until(Ec.element_to_be_clickable(locator))
        return ele if ele else False

    def wait_element_be_presence(self, locator):
        wait = WebDriverWait(self.driver, self.timeout)

        try:
            ele = wait.until(Ec.presence_of_element_located(locator))
        except (TimeoutException, NoSuchElementException) as e:
            ele = None
            # log
        return ele

    def visit_url(self, url):
        return self.driver.get(url)

    def click(self, locator):
        try:
            ele = self.find_element(locator)
            ele.click()
        except (NoSuchElementException, TimeoutError)as e:
            # self.logger.error(e + "{}".format('元素不可点击'))
            raise e

    def find_element(self, locator) -> WebElement:
        """获取一个元素对象"""
        ele = self.wait_element_be_presence(locator)
        if ele:
            return ele

        # log元素没找到

    def find_elements(self, locator) -> list:
        """获取一组元素对象"""
        wait = WebDriverWait(driver=self.driver, timeout=self.timeout)
        try:
            ele = wait.until(Ec.presence_of_all_elements_located(locator))
        except (TimeoutError, NoSuchElementException) as e:
            # self.logger.error(f"获取一组元素对象失败，失败原因为{e}")
            raise e
        else:
            return ele

    def send_keys(self, location, value) -> None:
        """
        input the value to input box of element
        :param location: //*[@by="location"]
        :param value: 输入的数据
        :return: None
        """
        try:
            element = self.find_element(location)
            element.clear()
            element.send_keys(value)
        except (NoSuchElementException, TimeoutException) as e:
            # self.logger.error("输入框:{}, 输入数据{}失败:{}".format(location, value, e))
            # self.save_screen_shot("send_keys")
            raise e

    def get_element_text(self, locator):
        ele = self.find_element(locator)
        try:
            value = ele.text
        except AttributeError:
            value = ele.get_attribute('value')
            # self.logger.error('获取元素对象文本失败')
        return value

    def _get_project_name(self):
        """
        根据系统获取项目名
        :return:
        """
        project_name = None
        if not os.name == "nt":
            project_name = ROOT_PATH.split(r'/')[-1]

        return project_name

    def get_po_libs(self):
        """
        从接口获取PO页的对象库
        :return:
        """

        # {
        #     "success": true,
        #     "ui_elements": {
        #         "user": "[ID,\"reader_email]",
        #         "passwd": "[ID,\"reader_email]",
        #         "login_button": "[XPATH,\"//input[@name='commit']\"]"
        #     }
        # }
        search_data = {"project_name": self._get_project_name(), "page_name": str(self.__class__.__name__)}
        res = self.api_search(method="GET", url=Base.mock_url, data=search_data)
        eles = res.json().get("ui_elements")
        for name, value in eles.items():
            setattr(self, name, tuple(value.split(",")))

    def get_attr(self, attr: str):
        self.get_po_libs()
        if hasattr(self, attr):
            return self.__getattribute__(attr)


if __name__ == '__main__':
    from selenium import webdriver

    By.ID
    driver = webdriver.Chrome()
    Base(driver).get_po_libs()
