import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    # 初始化
    def __init__(self, driver):
        # 获取driver
        self.driver = driver

    @allure.step(title='查找元素操作')
    # 查找元素方法
    def base_find(self, loc, timeout=30, poll=0.5):
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # 查一组找元素方法
    def base_finds(self, loc, timeout=30, poll=0.5):
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_elements(*loc))

    @allure.step(title='点击方法操作')
    # 点击方法
    def base_click(self, loc):
        self.base_find(loc).click()

    @allure.step(title='输入方法操作')
    # 输入方法
    def base_input(self, loc, value):
        # 获取元素
        el = self.base_find(loc)
        # 清空
        el.clear()
        # 输入数据
        el.send_keys(value)

    @allure.step(title='获取文本信息操作')
    # 获取文本信息
    def base_get_text(self, loc):
        return self.base_find(loc).text

    @allure.step(title='获取toast消息操作')
    # 获取toast消息
    def base_get_toast(self, msg):
        loc = By.XPATH, "//*[contains(@text，'{}')]".format(msg)
        return self.base_find(loc, timeout=5, poll=0.2).text

    @allure.step(title='拖拽操作')
    # 拖拽
    def base_drag_and_drop(self, start_loc, end_loc):
        start_el = self.base_find(start_loc)
        end_el = self.base_find(end_loc)
        self.driver.drag_and_drop(start_el, end_el)

    @allure.step(title='将失败截图写入报告操作')
    # 将失败截图写入报告
    def base_file_write_allure(self):
        with open("./image/file.png", "rb")as f:
            allure.attach("断言失败原因：", f.read(), allure.attach_type.PNG)

    # 通过传入的文本信息点击
    def base_text_click(self, text):
        loc = By.XPATH, "//*[contains(@text, '{}')]".format(text)
        self.base_find(loc).click()

