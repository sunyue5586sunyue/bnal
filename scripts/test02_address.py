import os
import sys
sys.path.append(os.getcwd())
import pytest
from tool.get_data_list import get_data_list
from page.page_in import PageIn
from tool.get_driver import GetDriver


def get_data(ty):

    data = get_data_list("data_address.yaml")
    data_list = []
    if ty == "post":
        data_list.append(tuple(data.get("post_address").values()))
    else:
        data_list.append(tuple(data.get("put_address").values()))
    return data_list



class TestAddress:
    # 初始化
    def setup_class(self):
        # 获取Pagelogin 并调用 登录方法
        self.page_longin_in = PageIn().page_login_in().page_address_login("17624227027", "199402115586")
        # 获取PageAddress
        self.page_address = PageIn().page_in_address()

    # 结束
    def teardown(self):
        # 关闭driver
        GetDriver().quit_driver()

    # 测试方法
    # 新增地址
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("name, phone, pro, city, dis, info, code", get_data("post"))
    def test_post_address(self, name, phone, pro, city, dis, info, code):
        self.page_address.page_address(name, phone, pro, city, dis, info, code)
        try:
            # 断言 收件人及电话
            result_list = self.page_address.page_get_receipt_list()
            expect = name + "  " + phone
            assert expect in result_list
        except:
            # 截图
            self.page_longin_in.page_get_image()
            # 将失败截图写入报告
            self.page_longin_in.base_file_write_allure()
            raise
        try:
            # 断言 地址
            address_list = self.page_address.page_get_address_list()
            expect_address = pro + city + dis + info
            assert expect_address in address_list
        except:
            # 截图
            self.page_longin_in.page_get_image()
            # 将失败截图写入报告
            self.page_longin_in.base_file_write_allure()
            raise

    # 地址管理--编辑地址
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("name2, phone2, pro2, city2, dis2, info2, code2, expect2", get_data("put"))
    def test_address_compile(self, name2, phone2, pro2, city2, dis2, info2, code2, expect2):
        self.page_address.page_address_compile(name2, phone2, pro2, city2, dis2, info2, code2)
        # 断言 toast
        try:
            assert expect2 == self.page_address.page_get_toast(expect2)

            # 断言 收件人及电话
            result_list = self.page_address.page_get_receipt_list()
            expect = name2 + "  " + phone2
            assert expect in result_list

            # 断言 地址
            address_list = self.page_address.page_get_address_list()
            expect_address = pro2 + city2 + dis2 + info2
            assert expect_address in address_list
        except:
            # 截图
            self.page_longin_in.page_get_image()
            # 将失败截图写入报告
            # self.page_longin_in.base_file_write_allure()
            raise

    # 地址管理--删除地址
    # 删除--单个
    # def test_address_delete_one(self):
    #     self.page_address.page_delete_one()

    # 删除--所有
    @pytest.mark.run(order=3)
    def test_address_delete_all(self):
        self.page_address.page_delete_all()
        try:
            # 断言是否还有地址信息
            assert self.page_address.page_if_address_exists()
        except:
            # 截图
            self.page_longin_in.page_get_image()
            # 将失败截图写入报告
            self.page_longin_in.base_file_write_allure()
            raise
