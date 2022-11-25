# DataSet数据加载  
开发语言：python 3.9  
开发平台：Win11 22H2  
开发工具：PyCharm 2017.3.2   
实现功能：先生成20000张图片放到Datasets/train的文件夹中，用train对齐进行训练，然后生成100张测试图片到Datasets/test文件夹中。  


## 安装库  
pip install torch  
pip install torchvision  
pip install tensorboard  

## 参考链接  
1. https://www.bilibili.com/video/BV1BP4y1b7Er/?p=3&spm_id_from=pageDriver&vd_source=92d090d4c3dbc39b2a328af71c01284b  



## 问题  
1. 执行tensorboard --logdir==logs报错Fatal error in launcher: Unable to create process using  
解决方法：https://blog.csdn.net/sinat_38316070/article/details/105418480  
python -m tensorboard.main --logdir=logs  
2. 执行GPU运行train.py时报错Torch not compiled with CUDA enabled  
解决办法：https://blog.csdn.net/moyong1572/article/details/119438286  
pip install torch==1.12.0+cu113 torchvision==0.13.0+cu113 torchaudio==0.12.0 --extra-index-url https://download.pytorch.org/whl/cu113  




