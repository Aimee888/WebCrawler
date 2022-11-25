#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : 20221123 -> train.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2022/11/25 15:18
@Desc    :
================================================="""
from torch.utils.data import DataLoader
from CNNTraning import my_dataset
from torch import nn
from torch.optim import Adam
from VKModel import vkmodel
from torch.utils.tensorboard import SummaryWriter
import torch


def main():
    test_dataset = my_dataset("./datasets/test/")
    test_dataloader = DataLoader(test_dataset, batch_size=40, shuffle=True)

    train_dataset = my_dataset("./datasets/train/")
    train_dataloader = DataLoader(train_dataset, batch_size=40, shuffle=True)
    # vk_model = vkmodel()  # CPU
    vk_model = vkmodel().cuda()  # GPU
    # loss_fn = nn.MultiLabelSoftMarginLoss()  # CPU
    loss_fn = nn.MultiLabelSoftMarginLoss().cuda()  # GPU
    optim = Adam(vk_model.parameters(),lr=0.001)
    w = SummaryWriter("logs")
    total_step = 0
    for epoch in range(10):
        print("外层训练次数{}".format(epoch))
        for i, (images,labels) in enumerate(train_dataloader):
            images = images.cuda()  # GPU
            labels = labels.cuda()  # GPU
            vk_model.train()
            outputs = vk_model(images)
            loss = loss_fn(outputs,labels)
            optim.zero_grad()
            loss.backward()
            optim.step()
            total_step += 1
            if i%100 == 0:
                print("训练次数{},损失率{}".format(i,loss.item()))
                w.add_scalar("loss",loss,total_step)
    torch.save(vk_model, "model.pth")


if __name__ == '__main__':
    main()
