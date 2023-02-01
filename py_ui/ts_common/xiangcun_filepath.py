# -*- coding:utf-8 -*-
# author: fangql
# datetime:2022/10/28 17:50
# software: PyCharm
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # 获取当前base路径
CHROME_DIRVER = os.path.join(BASE_DIR, "chromedriver.exe")
PROJECT_DIR = os.path.join(BASE_DIR,"shuzixiangcun")
LC_DIR = os.path.join(PROJECT_DIR, "xiangcun_img")
LC_FILE_PATH =os.path.join(LC_DIR, "img.png")

print(LC_FILE_PATH)

