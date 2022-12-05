#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : 20221202 -> sendoutlookmail.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2022/12/3 10:32
@Desc    :
================================================="""
import win32com.client as win32
import xlwings


def get_excel_date(filename):
    '''
    获得excel里的所有内容，返回list
    :param filename:  excel路径
    :return: list[list[]]
    '''
    app = xlwings.App(visible=False, add_book=True)
    app.display_alerts = False
    app.screen_updating = False
    wb = app.books.open(filename)
    sht = wb.sheets[0]
    rng = sht.range('A1')
    # 把excel里的数据读取成 年-月-日 时:分:秒的格式
    my_date_handler = lambda year, month, day, hour, minute, second, **kwargs: "%04i-%02i-%02i %02i:%02i:%02i" % (
    year, month, day, hour, minute, second)
    # 取出所有内容,这里用ig这个变量，是为了庆祝I.G获得LOL S8赛季总冠军
    ig = rng.current_region.options(index=False, numbers=int, empty='N/A', dates=my_date_handler)
    result = ig.value
    wb.close()
    app.quit()
    return result


def main():
    # 如果outlook打开的话，执行程序会报错，所以用try catch防止此类错误
    try:
        outlook = win32.Dispatch('Outlook.Application')
    except:
        outlook.Quit
    mail = outlook.CreateItem(0)
    mail.To = '12345678@qq.com'  # 收件人
    # mail.CC = '12345678@qq.com'  # 抄送人
    # mail.Bcc='12345678@qq.com' #密抄收件人
    mail.Subject = 'test1'  # 邮件主题
    mail.Body = '这是一封测试邮件'  # 邮件正文
    # mail.Importance = 2  # 设置重要性为高
    mail.Attachments.Add('1.xlsx')  # 添加附件
    body_html = ""
    body_html = body_html + '<body>Hi all:<br/>以下是XXXXX项目今天的测试情况:<br/><br/>明天的测试计划:<br/><br/>目前的bug:'
    body_html = body_html + '<table width="1" border="1" cellspacing="1" cellpadding="1" height="100">'
    # 这里用rng 是因为这一次rng止步8强！
    rng_list = get_excel_date('1.xlsx')
    # 表头
    for tr_list in rng_list[:1]:
        body_html = body_html + "<tr>"
        for td_list in tr_list:
            # 这里也是奇葩需求，因为要求表头不能换行，所以用了nowrap
            body_html = body_html + '<th bgcolor="#C3C3C3" nowrap="nowrap">' + td_list + '</th>'
        body_html = body_html + "</tr>"
    # 表内容
    for tr_list in rng_list[1:]:
        body_html = body_html + "<tr>"
        for td_list in tr_list:
            body_html = body_html + "<td>" + str(td_list) + "</td>"
        body_html = body_html + "</tr>"
    body_html = body_html + '</table>'
    body_html = body_html + "</body>"
    mail.HtmlBody = body_html
    mail.Send()  # 发送


if __name__ == '__main__':
    main()
