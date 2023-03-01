#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : 20230218 -> getMicrosoftStoreApp.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2023/2/18 9:15
@Desc    :
================================================="""
import requests
import json
from urllib import parse
import base64


def main():
    num = 0
    while num < 100000:
        a = "o={}&b=".format(num)
        a = base64.b64encode(a.encode("utf-8")).decode("utf-8")
        b = "会议"
        url = "https://apps.microsoft.com/store/api/Products/GetFilteredSearch?hl=zh-cn&gl=CN&FilteredCategories=AllProducts&Cursor={}&Query={}".format(a,b)
        url = parse.quote(url)
        url = url.replace("%3F","?")
        url = url.replace("%3D","=")
        url = url.replace("%26","&")
        url = url.replace("%3A",":")
        response = requests.get(url)
        r = response.text
        response_dict = json.loads(r)
        ptdic = response_dict["productsList"]
        if len(ptdic) > 0:
            for i,product in enumerate(ptdic):
                print(num+i+1, end="\t")
                print(product["title"])
            num = num + 20
        else:
            break


if __name__ == '__main__':
    main()
