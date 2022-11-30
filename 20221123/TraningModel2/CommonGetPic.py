#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : test -> getImg.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2022/11/18 8:04
@Desc    :
================================================="""
import requests
import time


headers = {
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
    }


def save_data(img, title):
    # img_url = "http:" + img
    img_url = img
    img_data = requests.get(img_url, headers=headers).content

    img_path = "./datasets/train/{}_{}.jpg".format(title, int(time.time()))
    print("正在下载：", str(img))
    with open(img_path, "wb") as f:
        f.write(img_data)
    print(str(img.split("/")[-1]) + "下载完毕")


def main():
    for i in range(20000):
        img_url = ""
        save_data(img_url, str(i))


if __name__ == '__main__':
    main()
