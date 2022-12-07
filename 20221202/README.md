# Pandas操纵表格   
开发语言：python 3.9  
开发平台：Win11 22H2  
开发工具：PyCharm 2017.3.2   
实现功能：使用pandas读取表格内容，并将表格内容通过outlook发送出去  

## Python library下载  
1. pip install pandas
2. pip install pypiwin32


## pandas读取表格  
- 读取单个sheet的内容
    ~~~python
    # 读取1.xlsx表格的sheet1的内容
    df = pd.read_excel(open('1.xlsx', 'rb'), sheet_name='sheet1')
    ~~~  
- 打印列标题名称  
    ~~~python
    # df.columns是列标题的名称，类型是<class 'pandas.core.indexes.base.Index'>
    for one_col in df.columns:
        print(one_col)
    ~~~  
- 获取表格全部数据（不包含列标题）  
    ~~~python
    # 获取表格全部数据，得到的是一个二维数组
    data = df.values
    # print(data)
    for tr_list in data:  # 获取每一行的值
        for td_list in tr_list:  # 获取每一列的值
            # 得到一个单元格的值，由于在一行内，所以间隔用tab
            print(td_list, end="\t")  
        # 打印完一行的值就换行
        print("")
    ~~~  
- 直接打印某一个单元格的值  
    ~~~python
    # 读取第1行第0列的数据
    print(df.iat[1,0])
    ~~~

## win32com发送outlook邮件   
win32com只支持windows平台  
- 获取Outlook对象  
    ~~~python
    # 这里需要注意的是，如果你此时outlook是打开状态，那么这句话执行时就会报错
    outlook = win32.Dispatch('Outlook.Application')
    ~~~
    如果想要在打开outlook的状态下使用，最好用try catch处理一下
    ~~~python
    try:
        outlook = win32.Dispatch('Outlook.Application')
    except:
        outlook.Quit
    ~~~
- 新建一封mail  
    ~~~python
    mail = outlook.CreateItem(0)
    ~~~
- 设置mail的一些基本参数：收件人，抄送人，密抄收件人，主题，附件  
    ~~~python
    mail.To = 'XXXX'  # 收件人
    mail.CC = 'XXXX'  # 抄送人
    mail.Bcc= 'XXXX'  # 密抄收件人
    mail.Subject = 'test1'  # 邮件主题
    mail.Attachments.Add('绝对路径')  # 添加附件
    mail.Importance = 2  # 设置邮件重要性为高
    ~~~
- 设置mail主题内容  
    ~~~python
    mail.Body = '这是一封测试邮件'  # 邮件正文
    ~~~
    如果是要把excel粘贴到邮件正文，那么需要用html的Body格式  
    ~~~python
    body_html = ""
    body_html = body_html + '<body>Hi all:<br/>以下是XXXXX项目今天的测试情况:<br/><br/>明天的测试计划:<br/><br/>目前的bug:'
    body_html = body_html + '<table width="1" border="1" cellspacing="1" cellpadding="1" height="100">'
    # 中间部分将表格数据以html的格式加到body_html中,此部分为表格里面的内容，省略。。。
    body_html = body_html + '</table>'
    body_html = body_html + "</body>"
    mail.HtmlBody = body_html
    ~~~

