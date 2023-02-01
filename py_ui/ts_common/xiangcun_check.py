# -*- coding:utf-8 -*-
# author: fangql
# datetime:2022/10/28 17:29
# software: PyCharm
from selenium.webdriver.common.by import By


def check_element_exists(driver, element, condition):
    try:

        if condition == 'class':
            driver.find_element(by=By.CLASS_NAME, value=element)
        elif condition == 'id':
            driver.find_element(by=By.ID, value=element)
        elif condition == 'xpath':
            driver.find_element(by=By.XPATH, value=element)
            print(True)
        return True
    except Exception as e:
        print(False)
        return False

    # '/Users/fangql/Documents/my_code/youkang_web/venv/lib/python3.9/site-packages/pytesseract
# '