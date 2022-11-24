#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : 20221123 -> ChangePic.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2022/11/23 16:55
@Desc    :
================================================="""
from PIL import Image
import pytesseract


def handler(grays, threshold=160):
    """
    对灰度图片进行二值化处理，默认阈值是160，可根据实际情况调整
    二值化处理其实是根据阈值调整原图的像素值，将大于阈值的像素点改为白色，小于阈值的像素点改为黑色
    :param grays:
    :param threshold:
    :return:
    """
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    anti = grays.point(table, '1')
    return anti


def main():
    img_path = "./pic/DBxJ_9.jpg"
    # 图片灰度处理
    gray = Image.open(img_path).convert('L')
    # gray.show()
    # 二值化处理
    image = handler(gray)
    image.show()
    text = pytesseract.image_to_string(image)
    print(text)


if __name__ == '__main__':
    main()
