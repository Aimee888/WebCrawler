#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : test -> ImgVerify.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2022/11/18 8:12
@Desc    :
================================================="""
from PIL import Image
import requests
from lxml import html
etree = html.etree


def base64_api(uname, pwd, img):  # 打码平台解析工具
    import base64
    from io import BytesIO
    from sys import version_info
    import json
    img = img.convert('RGB')
    buffered = BytesIO()
    img.save(buffered, format="JPEG")
    # result = None
    if version_info.major >= 3:
        b64 = str(base64.b64encode(buffered.getvalue()), encoding='utf-8')

    else:
        b64 = str(base64.b64encode(buffered.getvalue()))
    data = {"username": uname, "password": pwd, "image": b64}
    result = json.loads(requests.post("http://api.ttshitu.com/base64", json=data).text)

    if result['success']:
        return result["data"]["result"]
    else:
        return result["message"]


def test_way3():
    img_path = "./pic1/6d72_3.jpg"
    # img_path = "./captcha1.jpg"
    img = Image.open(img_path)
    # 这里用自己的用户名和密码
    result = base64_api(uname='', pwd='', img=img)
    print("真正解析出来的值是：", result)


def main():
    test_way3()


if __name__ == '__main__':
    main()



