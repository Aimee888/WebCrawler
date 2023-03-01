#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : 20230218 -> sliderverification2.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2023/3/1 19:23
@Desc    :https://bm.cltt.org/
================================================="""
import ddddocr


def main():
    det = ddddocr.DdddOcr(det=False, ocr=False)

    with open('./vryimg/sli.png', 'rb') as f:
        target_bytes = f.read()

    with open('./vryimg/sli.png', 'rb') as f:
        background_bytes = f.read()

    res = det.slide_match(target_bytes, background_bytes)

    print(res)


if __name__ == '__main__':
    main()
