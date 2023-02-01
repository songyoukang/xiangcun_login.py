# -*- coding:utf-8 -*-
# datetime:2022/10/28 17:25
# software: PyCharm
class HomeLoc:
    welcome_loc = '//*[@class="s-userName"]'

    def __getattr__(self, item):
        return item
