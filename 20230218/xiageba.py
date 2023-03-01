#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : 20230218 -> xiageba.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2023/2/18 9:10
@Desc    :https://music.y444.cn/#/
================================================="""
import requests
from urllib import parse
import json


def main():
    name_song = "黎明前的黑暗"
    url = "https://music.y444.cn/api/v1/search/v3/?keyword={}&page=1&size=10&src=kw".format(name_song)
    url = parse.quote(url)
    url = url.replace("%3F", "?")
    url = url.replace("%3D", "=")
    url = url.replace("%26", "&")
    url = url.replace("%3A", ":")
    response = requests.get(url)
    r = response.text
    response_dict = json.loads(r)
    print(response_dict)
    song_list = response_dict["data"]
    # print(song_list)


if __name__ == '__main__':
    main()
