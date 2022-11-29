#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : 20221123 -> VKModel.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2022/11/25 14:59
@Desc    :
================================================="""
import torch
from torch import nn


# captcha_array = list("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
captcha_array = list("0123456789abcdefghijklmnopqrstuvwxyz")
captcha_size = 4


class vkmodel(nn.Module):
    def __init__(self):
        super(vkmodel, self).__init__()
        self.layer1 = nn.Sequential(
            nn.Conv2d(in_channels=1, out_channels=64, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2)
        )
        self.layer2 = nn.Sequential(
            nn.Conv2d(in_channels=64, out_channels=128, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2)
        )
        self.layer3 = nn.Sequential(
            nn.Conv2d(in_channels=128, out_channels=256, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2)
        )
        self.layer4 = nn.Sequential(
            nn.Conv2d(in_channels=256, out_channels=512, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2)
        )
        self.layer5 = nn.Sequential(
            nn.Flatten(),
            nn.Linear(in_features=15360,out_features=4096),
            nn.Dropout(0.2),
            nn.ReLU(),
            nn.Linear(in_features=4096, out_features=captcha_size*captcha_array.__len__())
        )

    def forward(self, x):
        x = self.layer1(x)
        x = self.layer2(x)
        x = self.layer3(x)
        x = self.layer4(x)
        x = self.layer5(x)
        return x


def main():
    data = torch.ones(1,1,60,160)
    m = vkmodel()
    x = m(data)
    print(x.shape)


if __name__ == '__main__':
    main()
