import allure

from page.page_address import PageAddress
from page.page_login import PageLogin
from tool.get_driver import GetDriver


class PageIn:
    def __init__(self):
    # 获取driver
        self.driver = GetDriver().get_driver()

    @allure.step(title='获取PageLogin对象操作')
    def page_login_in(self):

        return PageLogin(self.driver)

    def page_in_address(self):
        # 获取driver
        return PageAddress(self.driver)
