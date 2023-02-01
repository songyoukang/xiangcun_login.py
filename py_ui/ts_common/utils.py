from time import sleep
from selenium import webdriver
from py_ui.ts_common.xiangcun_filepath import *
class Driverutile(object):
    """浏览器管理"""
    driver=None
    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            cls.driver = webdriver.Chrome(CHROME_DIRVER)
            cls.driver.get("https://digitalvillagecs.szrcbank.com/")
            cls.driver.maximize_window()
            cls.driver.implicitly_wait(10)
        return cls.driver
    @classmethod
    def quit_driver(cls):
        """退出浏览器"""
        if cls.driver:
            sleep(3)
            cls.driver.quit()
            cls.driver=None
if __name__ == '__main__':
    Driverutile.get_driver()
    Driverutile.quit_driver()
