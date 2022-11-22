# 验证码识别   
开发语言：python 3.9  
开发平台：Win11 22H2  
开发工具：PyCharm 2017.3.2   
实现功能：从网页中获取验证码图片样本10张，使用ddddocr库识别样本中的验证码  

## 获取验证码图片样本  
 参考链接：https://blog.51cto.com/aiyc/5153929  
 - 安装captcha  
 ~~~
 pip install captcha
 ~~~  
 - 写获取Image的程序GetImgSample.py  
 ![](./res/1.png)  
 可以看到验证码已经成功下载下来，并且命名方式就是验证码字符加上随机数  

 ## 识别验证码  
 参考链接：https://www.cnblogs.com/hahaa/p/16411939.html  
 - 安装ddddocr  
 ~~~
 pip install ddddocr
 ~~~  
 - 写识别验证码的程序recognition_veryfycode.py  
 可以看到用GetImgSample获取到的样本图片./pic/*.jpg识别率只有2/10 = 20%，识别率非常低。  
 但是用这个程序识别从另一个网页中得到的样本./pic1/*.jpg的识别率是10/10 = 100%，识别率非常高。  
 ./pic1/*jpg样式如下：  
 ![](./res/2.png)  
 所以说ddddocr这个开源库适合的是./pic1文件夹中的验证码样式。  

 ## 问题清单  
 1. 验证码链接是同一个URL，但是验证码在变，requests如何通过验证码验证？  
 解答：  
 参考链接：https://zhuanlan.zhihu.com/p/492952092  
 在获取网页的时候，请求验证码，以及提交验证码的时候，对方服务器肯定通过了某种手段验证我之前获取的验证码和最后提交的验证码是同一个验证码，那这个手段是什么手段呢？很明显，就是通过cookie来实现的，所以对应的，在请求页面，请求验证码，提交验证码的到时候需要保证cookie的一致性，对此可以使用requests.session来解决。  
 ~~~python
 session = requests.session()
 session.headers = {
    'User-Agent': '',
 }
 url_verfyimg = ""
 img_data = session.get(url_verfyimg).content
 url_login = ""
 session.headers.update({"Content-Type":"application/json;charset=UTF-8"})
 post_data = {
            "password": "",
            "verifyCode": "",
            "username": "",
        }
 data_json = json.dumps(post_data)
 response = session.post(url_login, data_json)
 ~~~
