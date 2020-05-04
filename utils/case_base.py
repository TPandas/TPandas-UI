# encoding:utf-8
# Motto：good good study, day day up. why you so lazy ？？？
from utils.handle_requests import MyRequests


class TestCaseBase(object):
    url = "http://111.231.133.146:38080/app/mock/2/manage/testdata"

    api_search = MyRequests()

    def get_data(self):
        search_data = {"project_id": 1, "page_name": str(self.__class__.__name__)}

        res = TestCaseBase.api_search("get", TestCaseBase.url, data=search_data)
        return res.json().get("data")


if __name__ == '__main__':
    print(TestCaseBase().get_data())
