import allure
from appium import webdriver


class GetDriver:
    driver = None


    @classmethod
    @allure.step(title='初始化driver操作')
    def get_driver(cls):
        if not cls.driver:
            desired_caps = {}
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '5.1'
            desired_caps['deviceName'] = '192.168.56.101:5555'
            # app信息
            desired_caps['appPackage'] = 'com.yunmall.lc'
            desired_caps['appActivity'] = 'com.yunmall.ymctoc.ui.activity.MainActivity'
            # 中文
            desired_caps['unicodeKeyboard'] = True
            desired_caps['resetKeyboard'] = True
            # toast信息
            desired_caps['automationName'] = 'Uiautomator2'
            # 获取driver
            cls.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        return cls.driver


    @classmethod
    @allure.step(title='关闭driver操作')
    def quit_driver(cls):
        if cls.driver:
            cls.driver.quit()
            cls.driver = None
