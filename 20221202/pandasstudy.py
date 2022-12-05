#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : 20221202 -> pandasstudy.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2022/12/2 15:18
@Desc    :https://www.w3cschool.cn/hyspo/hyspo-m7je3723.html
================================================="""
import pandas as pd
import numpy as np


"""
用值列表生成Series
"""
def test1():
    s = pd.Series([1, 3, 5, np.nan, 6, 8])
    print(s)


"""
用含日期时间索引与标签的 NumPy 数组生成 DataFrame
"""
def test2():
    dates = pd.date_range('20130101', periods=6)
    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
    print(df)


"""
用 Series 字典对象生成 DataFrame
"""
def test3():
    df2 = pd.DataFrame({'A': 1.,
                        'B': pd.Timestamp('20130102'),
                        'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                        'D': np.array([3] * 4, dtype='int32'),
                        'E': pd.Categorical(["test", "train", "test", "train"]),
                        'F': 'foo'})

    print(df2)
    print(df2.dtypes)


def test4():
    x1 = pd.ExcelFile(r"E:\gitplay\python\VerifyCodeTraning\tmp.xls")
    dfs = x1.parse(x1.sheet_names[0])
    print(dfs)
    dfs = dfs[dfs['Miss Rate'].str.strip("%").astype(float) > 0]
    dfs.to_excel("1.xlsx", sheet_name='sheet1', index=False)


def main():
    # test1()
    # test2()
    # test3()
    test4()


if __name__ == '__main__':
    main()
