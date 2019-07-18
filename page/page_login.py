import allure

import page
from base.base import Base


class PageLogin(Base):


    @allure.step(title='点击 我 操作')
    # 点击 我
    def page_click_me(self):
        self.base_click(page.login_me)

    @allure.step(title='点击 已有账号，去登陆 操作')
    # 点击 已有账号，去登陆
    def page_account_link(self):
        self.base_click(page.login_account_link)

    @allure.step(title='输入用户名操作')
    # 输入用户名
    def page_input_username(self, username):
        allure.attach("用户名:", username)
        self.base_input(page.login_username, username)

    @allure.step(title='输入密码操作')
    # 输入密码
    def page_input_password(self,pwd):
        allure.attach("密码:", pwd)
        self.base_input(page.login_pwd,pwd)

    @allure.step(title='点击登录按钮操作')
    # 点击登录按钮
    def page_click_login_btn(self):
        self.base_click(page.login_btn)

    @allure.step(title='点击设置按钮操作')
    # 点击设置按钮
    def page_set_btn(self):
        self.base_click(page.login_set_btn)

    @allure.step(title='拖拽操作')
    # 拖拽  消息推送-->修改密码
    def page_drag_and_drop(self):
        self.base_drag_and_drop(page.login_set_notification, page.login_set_modify_pwd)

    @allure.step(title='点击退出按钮操作')
    # 点击退出
    def page_click_logout(self):
        self.base_click(page.login_set_logout_btn)

    @allure.step(title='点击确定退出按钮操作')
    def page_right_ok(self):
        self.base_click(page.login_set_right_ok)

    @allure.step(title='获取昵称操作')
    # 获取 昵称
    def page_get_nickname(self):
        return self.base_get_text(page.login_nickname)

    @allure.step(title='获取 错误提示消息操作')
    # 获取 错误提示消息
    def page_get_err_info(self, msg):
        return self.base_get_toast(msg)

    @allure.step(title='截图操作')
    # 截图
    def page_get_image(self):
        self.driver.get_screenshot_as_file("./image/file.png")

    # 点击—设置_新增地址管理
    def page_set_address_manage(self):
        self.base_click(page.set_address_manage)

    @allure.step(title='组合业务方法--登录操作')
    # 组合业务方法--登录
    def page_login(self, username, pwd):
        self.page_input_username(username)
        self.page_input_password(pwd)
        self.page_click_login_btn()

    @allure.step(title='退出登录组合业务方法操作')
    # 退出登录组合业务方法
    def page_logout(self):
        self.page_set_btn()
        self.page_drag_and_drop()
        self.page_click_logout()
        self.page_right_ok()

    # 组合业务方法--地址依赖登录
    def page_address_login(self, username, pwd):
        self.page_click_me()
        self.page_account_link()
        self.page_input_username(username)
        self.page_input_password(pwd)
        self.page_click_login_btn()
        self.page_set_btn()
        self.page_set_address_manage()
