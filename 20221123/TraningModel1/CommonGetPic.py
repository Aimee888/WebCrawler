#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : 20221123 -> CommonGetPic.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2022/11/28 13:22
@Desc    :获取样本集，训练集存放在train文件夹中20000张，测试集存放在test文件夹中100张
================================================="""
from captcha.image import ImageCaptcha
import random
import time


captcha_array = list("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
captcha_size = 4


def getTrainPic():
    for i in range(20000):
        image = ImageCaptcha()
        image_text = "".join(random.sample(captcha_array,captcha_size))
        image_path = "./datasets/train/{}_{}.png".format(image_text, int(time.time()))
        image.write(image_text, image_path)


def getTestPic():
    for i in range(100):
        image = ImageCaptcha()
        image_text = "".join(random.sample(captcha_array,captcha_size))
        image_path = "./datasets/test/{}_{}.png".format(image_text, int(time.time()))
        image.write(image_text, image_path)


def main():
    # getTestPic()
    getTrainPic()


if __name__ == '__main__':
    main()
