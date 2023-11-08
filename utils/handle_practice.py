# -*- coding:utf-8 -*-
# @Time : 2023/8/6 21:33
# Auther : shenyuming
# @File : handle_practice.py
# @Software : PyCharm
'''
    生成二维码
'''

import qrcode
import os

data = "https://g99kujhtfuwb.xyz:36999/vod/detail.html?id=554877&type_id=725"

img = qrcode.make(data)

img.save("output.png")
