#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : 20221123 -> CNNTraning.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2022/11/25 9:32
@Desc    :
pip install torch: torch-1.13.0-cp39-cp39-win_amd64.whl
================================================="""
from torch.utils.data import Dataset
import os
from PIL import Image
from torchvision import transforms
from torch.utils.tensorboard import SummaryWriter


class my_dataset(Dataset):
    def __init__(self, root_dir):
        super(my_dataset, self)
        self.image_path = [os.path.join(root_dir,image_name) for image_name in os.listdir(root_dir)]
        # Resize那里是图片的像素大小，可右键图片查看
        self.transfroms = transforms.Compose(
            [
                transforms.ToTensor(),
                transforms.Resize((80, 170)),
                transforms.Grayscale()
            ]
        )
        print(self.image_path)

    def __len__(self):
        return self.image_path.__len__()

    def __getitem__(self, index):
        image_path = self.image_path[index]
        image = self.transfroms(Image.open(image_path))
        # image = Image.open(image_path)
        # image.show()
        label = image_path.split("/")[-1]
        label = label.split("_")[0]
        return image,label


def main():
    writer = SummaryWriter("logs")
    train_data = my_dataset("./pic/")
    img,label = train_data[0]
    print(img.shape,label)
    writer.add_image("img", img, 1)
    writer.close()


if __name__ == '__main__':
    main()
