#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : 20221122 -> recognition_veryfycode.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2022/11/22 13:47
@Desc    :
================================================="""
import ddddocr
import re


def main():
    ocr = ddddocr.DdddOcr()
    with open('./pic1/ynna_5.jpg', 'rb') as f:
        img_bytes = f.read()
        result = ocr.classification(img_bytes)
        # print(result)
        result1 = ''.join(re.findall(r'[A-Za-z0-9]', result))
        print(result1)


if __name__ == '__main__':
    main()
