#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : 20221123 -> predict.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2022/11/28 10:20
@Desc    :
================================================="""
from PIL import Image
from torch.utils.data import DataLoader
from datasets_my import my_dataset,vec2Text
from CommonGetPic import captcha_array, captcha_size
import torch
from torchvision import transforms


def test_onepic(path):
    img = Image.open(path)
    trans = transforms.Compose(
        [
            transforms.Resize((60, 160)),
            transforms.Grayscale(),
            transforms.ToTensor()
        ]
    )
    img_tensor = trans(img).cuda()
    img_tensor = img_tensor.reshape(1,1,60,160)
    print(img_tensor.shape)
    m = torch.load("model.pth").cuda()
    m.eval()
    output = m(img_tensor)
    output = output.view(-1, captcha_array.__len__())
    output_label = vec2Text(output)
    print(output_label)


def main():
    test_dataset = my_dataset("./datasets/test/")
    test_dataloader = DataLoader(test_dataset, batch_size=1, shuffle=True)
    m = torch.load("model.pth").cuda()
    m.eval()
    correct = 0
    test_len = test_dataset.__len__()
    print(test_len)
    # print(m)
    for i,(images,labels) in enumerate(test_dataloader):
        images = images.cuda()
        labels = labels.cuda()
        # print(labels.shape) #[4, 62]
        labels = labels.view(-1, captcha_array.__len__())
        # print(labels.shape)
        # print(vec2Text(labels))
        label_text = vec2Text(labels)
        output = m(images)
        output = output.view(-1, captcha_array.__len__())
        output_test = vec2Text(output)
        # print(label_text, output_test)
        if label_text == output_test:
            correct += 1
            print("正确值: {}, 预测值: {}".format(label_text, output_test))
    print("正确率: {}".format(correct / test_len * 100))


if __name__ == '__main__':
    main()
    # test_onepic(r"E:\gitplay\python\VerifyCodeTraning\pic\2.jpg")
