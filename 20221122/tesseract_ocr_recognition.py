#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : 20221122 -> tesseract_ocr_recognition.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2022/12/5 15:39
@Desc    :
================================================="""
import cv2 as cv
import pytesseract
from PIL import Image

def recognize_text2(image):
    dst = cv.pyrMeanShiftFiltering(image, sp=10, sr=150)  # 边缘保留滤波  去噪
    gray = cv.cvtColor(dst, cv.COLOR_BGR2GRAY)  # 灰度图像
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)  # 二值化
    erode = cv.erode(binary, None, iterations=2)  # 形态学操作   腐蚀  膨胀
    dilate = cv.dilate(erode, None, iterations=1)
    cv.imshow('dilate', dilate)
    cv.bitwise_not(dilate, dilate)  # 逻辑运算，背景设为白色，字体为黑，便于识别
    cv.imshow('binary-image', dilate)
    test_message = Image.fromarray(dilate)  # 识别
    text = pytesseract.image_to_string(test_message)
    print(f'识别结果：{text}')


def test_way2():
    src = cv.imread(r'./pic/DBxJ_9.jpg')
    cv.imshow('input image', src)
    recognize_text2(src)
    # cv.waitKey(0) #这一行的意思是等待输入
    cv.destroyAllWindows()


def main():
    test_way2()


if __name__ == '__main__':
    main()
