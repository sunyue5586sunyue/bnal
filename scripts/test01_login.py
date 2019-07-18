import sys
import os
sys.path.append(os.getcwd())
import allure
import pytest
from page.page_in import PageIn
from tool.get_driver import GetDriver
from tool.get_data_list import get_data_list


def get_data():
    data = get_data_list("data_login.yaml")
    data_list = []
    for i in data.values():
            data_list.append(tuple(i.values()))
    return data_list


class TestLogin:

    @allure.step(title= '初始化操作')
    def setup_class(self):
        # 初始化PageLogin
        self.login = PageIn().page_login_in()
        # 点击 我
        self.login.page_click_me()
        # 点击 已有账号，去登录
        self.login.page_account_link()

    @allure.step(title='收尾操作')
    def teardown_class(self):
        # 关闭driver
        GetDriver().quit_driver()

    @allure.step(title='登录测试方法')
    @pytest.mark.parametrize(("username, pwd, nickname, expect_toast"), get_data())
    def test_login(self, username, pwd, nickname, expect_toast):
        # 调用登录业务方法
        self.login.page_login(username, pwd)
        # 正向
        if nickname:
            try:
                # 断言 昵称
                assert nickname == self.login.page_get_nickname()
            except:
                # 截图
                self.login.page_get_image()
                # 将失败截图写入报告
                self.login.base_file_write_allure()
                raise
            finally:
                # 退出登录
                self.login.page_logout()
                # 点击 我
                self.login.page_click_me()
                # 点击 已有账号，去登录
                self.login.page_account_link()

        # 逆向
        else:
            try:
                # 断言  toast
                assert expect_toast in self.login.page_get_err_info(expect_toast)
            except:
                # 截图
                self.login.page_get_image()
                # 将失败截图写入报告
                self.login.base_file_write_allure()
                raise
