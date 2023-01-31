#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : 20230130 -> playaudio.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2023/1/30 9:40
@Desc    :https://www.cnpython.com/qa/346808
================================================="""
from win32com.client import Dispatch
import win32com
import time


def main():
    # mp = win32com.client.gencache.EnsureDispatch("WMPlayer.OCX")
    # print(mp.currentMedia)
    mp = Dispatch("WMPlayer.OCX")
    tune = mp.newMedia(r"E:\gitplay\test\audio\music.wav")
    # tune = mp.newMedia(r"E:\Case\development\2023\2023规划.mp4")
    mp.currentPlaylist.appendItem(tune)
    mp.controls.play()
    time.sleep(1)
    mp.controls.playItem(tune)
    # print(mp.controls.currentItem)
    # print(mp.currentMedia)
    print(mp.currentMedia.name)
    time.sleep(int(tune.duration))
    mp.controls.stop()



if __name__ == '__main__':
    main()
