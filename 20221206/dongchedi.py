#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : 20221206 -> dongchedi.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2022/12/22 18:36
@Desc    :
================================================="""
import requests


# 热销轿车榜
def getRankingListCarOfWuHan():
    url = "https://www.dongchedi.com/motor/pc/car/rank_data?city_name=%E6%AD%A6%E6%B1%89&count=10&offset=0&month=&new_energy_type=&rank_data_type=1&brand_id=&price=&manufacturer=&outter_detail_type=0%2C1%2C2%2C3%2C4%2C5&nation=0"
    response = requests.get(url)
    content = response.json()['data']['list']
    print(content)
    print("排名","车类","车名","价格","日均关注度")
    for one in content:
        print(one['rank'],end='\t')
        print(one['brand_name'],end='\t')
        print(one['series_name'],end='\t')
        print(one['dealer_price'],end='\t')
        print(one['count'])


# 武汉热销榜
def getRankingListOfWuHan():
    url = "https://www.dongchedi.com/motor/pc/car/rank_data?city_name=%E6%AD%A6%E6%B1%89&count=10&offset=0&month=&new_energy_type=&rank_data_type=64&brand_id=&price=&manufacturer=&outter_detail_type=&nation=0"
    response = requests.get(url)
    content = response.json()['data']['list']
    print(content)
    print("排名", "车类", "车名", "价格", "销量")
    for one in content:
        print(one['rank'],end='\t')
        print(one['brand_name'],end='\t')
        print(one['series_name'],end='\t')
        print(one['dealer_price'],end='\t')
        print(one['count'])


def main():
    # getRankingListOfWuHan()
    getRankingListCarOfWuHan()


if __name__ == '__main__':
    main()
