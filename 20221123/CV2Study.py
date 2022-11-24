#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : 20221123 -> CV2Study.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2022/11/24 10:04
@Desc    :
================================================="""
import cv2


def main():
    img = cv2.imread("./pic/DBxJ_9.jpg")

    # 灰度处理
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)  # 数字2的前后分别是转换前和转换后的色彩空间

    # # 转换为三通道图
    # img = cv2.cvtColor(gray, cv2.COLOR_RGB2BGR)
    # print(img.shape)

    # # 获取局部区域（roi）
    # roi = img[0:80, 85:170]
    # # 保存roi到roi1.jpg
    # cv2.imwrite("roi1.jpg", roi)

    # 二值化处理
    ret, thresh1 = cv2.threshold(gray, 160, 255, cv2.THRESH_BINARY)
    cv2.imshow("thresh1", thresh1)
    cv2.waitKey()  # 等待键盘输入，输入任意键返回
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
