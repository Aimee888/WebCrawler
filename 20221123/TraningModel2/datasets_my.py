#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : 20221123 -> datasets.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2022/11/28 13:27
@Desc    :
================================================="""
from torch.utils.data import Dataset
import os
from torchvision import transforms
from PIL import Image
from torch import zeros, argmax
from _CommonGetPic import captcha_array,captcha_size
from torch.utils.data import DataLoader


def text2Vec(text):
    vec = zeros(captcha_size,len(captcha_array))
    # print(vec)
    for i in range(len(text)):
        # print(captcha_array.index(text[i]))
        vec[i, captcha_array.index(text[i])] = 1
    return vec


def vec2Text(vec):
    vec = argmax(vec, dim=1)
    # print(vec)
    text = ""
    for i in vec:
        text += captcha_array[i]
    return text


class my_dataset(Dataset):
    def __init__(self, root_dir):
        super(my_dataset, self)
        self.image_path = [os.path.join(root_dir,image_name) for image_name in os.listdir(root_dir)]
        # Resize那里是图片的像素大小，可右键图片查看
        self.transfroms = transforms.Compose(
            [
                transforms.ToTensor(),
                transforms.Resize((50, 300)),
                transforms.Grayscale(),
            ]
        )
        print(self.image_path)

    def __len__(self):
        return self.image_path.__len__()

    def __getitem__(self, index):
        image_path = self.image_path[index]
        # 将图片灰度化
        image = self.transfroms(Image.open(image_path))
        # image = Image.open(image_path)
        # image.show()
        label = image_path.split("/")[-1]
        # 取出验证码的字符
        label = label.split("_")[0]
        # print(label)
        label_tensor = text2Vec(label)
        label_tensor = label_tensor.view(1,-1)[0]
        return image,label_tensor


def main():
    test_dataset = my_dataset("./datasets/test/")
    test_dataloader = DataLoader(test_dataset, batch_size=4,shuffle=True)
    for i,(images,labels) in enumerate(test_dataloader):
        print(labels)
        # print(i)
        print(images.shape)
        print(labels.shape)


if __name__ == '__main__':
    main()
