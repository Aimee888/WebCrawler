#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : test -> BaiduAipVerify.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2022/11/18 16:54
@Desc    :https://www.baidu.com/link?url=MhUIH_SbTAorRgGZbw4EuOA3ldjZK25a1_k7HJ7mQcxWPmhvktKH665zCpE3nNra&wd=&eqid=cde3a4db000250d3000000066388670b
================================================="""
from aip import AipOcr
import codecs  # pip install baidu-aip
import os

# 读取图片函数
def ocr(path):
    with open(path, 'rb') as f:
        return f.read()


def test_way4():
    # app_id = '*********'
    app_id = '18640801'
    # api_key = '********************'
    api_key = 'SUCoWqGniSB3Ng5uoHzDvn6h'
    # secret_key = '*******************************'
    secret_key = 'CRh6EoG4SpGTWQboVKFSA4FIzlFI45KD'
    pic_list = os.listdir("./pic")
    print(pic_list)
    a = 0
    for i, pic_one in enumerate(pic_list):
        text_o = pic_one.split("_")[0]
        pic_one_path = "./pic/" + pic_one
        filename = pic_one_path
        client = AipOcr(app_id, api_key, secret_key)
        # 读取图片
        image = ocr(filename)
        # 进程ocr识别
        dict1 = client.general(image)
        print(dict1)
        try:
            text = dict1["words_result"][0]["words"]
        except:
            text = ""
            pass
        if text_o == text:
            a = a + 1
            print("实际值为：{}, 测试值为：{}".format(text_o, text))
    print("通过率为：", a/10)


def main():
    test_way4()


if __name__ == '__main__':
    main()
