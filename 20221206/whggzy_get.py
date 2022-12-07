#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : 20221206 -> whggzy_get.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2022/12/6 18:51
@Desc    :网站地址：http://www.whggzy.com/PoliciesAndRegulations/index.html?utm=sites_group_font.4dd516b0
================================================="""
import requests


def main():

    headers = {
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Accept': '*/*',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
        'Content-Type': 'application/json',
        'Origin': 'http://www.whggzy.com',
        'Referer': 'http://www.whggzy.com/PoliciesAndRegulations/index.html?utm=sites_group_font.4dd516b0',
        'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    }

    json_data = {
        'utm': 'sites_group_font.4dd516b0',
        'categoryCode': 'GovernmentProcurement',
        'pageSize': 15,
        'pageNo': 1,
    }

    response = requests.post(
        'http://www.whggzy.com/front/search/category',
        headers=headers,
        json=json_data,
        verify=False,
    )
    print(response.text)


if __name__ == '__main__':
    main()
