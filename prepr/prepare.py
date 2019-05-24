# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @DATE    : 5/9/2019
# @Author  : xiaotong niu
# @File    : prepare.py
# @Project : JData-Predict
# @Github  ：https://github.com/isNxt
# @Describ : ...


import os
import shutil
import time
from datetime import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters

# %% 配置
# 输出设置
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)
register_matplotlib_converters()
plt.style.use('seaborn')
plt.rcParams['figure.figsize'] = (12, 8)

# 时间划分
data_start_date = "2018-02-01"
data_end_date = "2018-04-15"
train_start_date = "2018-02-23"
train_end_date = "2018-04-15"
sub_start_date = "2018-04-16"
sub_end_date = "2018-04-22"

# 文件列表
ori_list = ['jdata_action.csv', 'jdata_user.csv', 'jdata_product.csv', 'jdata_shop.csv', 'jdata_comment.csv']
clean_list = ['action.csv', 'user.csv', 'product.csv', 'shop.csv', 'comment.csv']

# 路径
data_path = "../data"
ori_path = "../data/ori"
clean_path = "../data/clean"
fill_path = "../data/fill"
user_path = clean_path + "/user.csv"
action_path = clean_path + "/action.csv"
product_path = clean_path + "/product.csv"
shop_path = clean_path + "/shop.csv"
submit_path = '../submit'
cache_path = '../cache'


# %% step 1 填充空值 输出到/data/fill

def fill_NaN():
    print('>> 开始替换数据')
    for file_name in ori_list:
        in_file = ori_path + "/" + file_name
        out_file = fill_path + "/" + file_name
        if file_name == 'jdata_user.csv':
            print("> Null in ", file_name)
            df = pd.read_csv(in_file, dtype=object)
            print(df[df.isnull().values].head())
            print("> filling", file_name)
            print('读取完成！')
            df.fillna(-1, inplace=True)
            df.to_csv(out_file, index=False)
            print('保存完成！')
        elif file_name == 'jdata_shop.csv':
            print("> Null in ", file_name)
            df = pd.read_csv(in_file, dtype=object)
            print(df[df.isnull().values].head())
            print("> filling", file_name)
            df.ix[df['shop_reg_tm'].isnull(), 'shop_reg_tm'] = '2018-04-16 00:00:00.0'
            df.fillna(-1, inplace=True)
            df.to_csv(out_file, index=False)
            print('保存完成！')
        else:
            print("> copying", file_name)
            shutil.copyfile(in_file, out_file)
            print('复制完成！')
    print('<< 数据替换完成！')


# %% step 2 删除无效 输出到/data/clean
def clean_data():
    print('>> 开始处理数据')
    clean_action()  # 必须先action
    clean_user()
    clean_product()
    clean_comment()
    clean_shop()
    print('<< 数据处理完成!')

def map_day(x):
    if x < datetime.strptime(sub_start_date, '%Y-%m-%d'):
        d = datetime.strptime(sub_start_date, '%Y-%m-%d') - x
        d = d.days
    else:
        d = -1
    return d

def map_month(x):
    if x < datetime.strptime(sub_start_date, '%Y-%m-%d'):
        d = datetime.strptime(sub_start_date, '%Y-%m-%d') - x
        d = d.days // 30
    else:
        d = -1
    return d

def map_year(x):
    if x < datetime.strptime(sub_start_date, '%Y-%m-%d'):
        d = datetime.strptime(sub_start_date, '%Y-%m-%d') - x
        d = d.days // 365
    else:
        d = -1
    return d
def map_cate(d):
    if d < 0:
        d = -1
    elif 0 <= d <= 3:
        d = 1
    elif 3 < d <= 6:
        d = 2
    elif 6 < d <= 12:
        d = 3
    elif 12 < d <= 24:
        d = 4
    elif 24 < d <= 48:
        d = 5
    else:
        d = 6
    return d


def clean_user():
    # all column: 'user_id', 'age', 'sex', 'user_reg_tm', 'user_lv_cd', 'city_level', 'province', 'city', 'county'
    print('> cleaning user')
    user = pd.read_csv(fill_path + "/jdata_user.csv", parse_dates=['user_reg_tm'], na_filter=False)
    print('before:', user.shape)
    action = pd.read_csv(clean_path + "/action.csv", usecols=['user_id'])
    user = user[user['user_id'].isin(action['user_id'])]
    user = user.drop_duplicates('user_id')
    user['user_reg_day'] = user['user_reg_tm'].apply(map_day)
    user['user_reg_month'] = user['user_reg_tm'].apply(map_month)
    user['user_reg_cate'] = user['user_reg_month'].apply(map_cate)
    user['user_reg_year'] = user['user_reg_tm'].apply(map_year)
    user = user.sort_values('user_id')
    user = user.drop('user_reg_tm', axis=1)
    print('after:', user.shape)
    user.to_csv(clean_path + "/user.csv", index=False)


def clean_product():
    # all column: 'sku_id', 'brand', 'shop_id', 'cate', 'market_time'
    print('> cleaning product')
    product = pd.read_csv(fill_path + "/jdata_product.csv", parse_dates=['market_time'], na_filter=False)
    print('before:', product.shape)

    action = pd.read_csv(clean_path + "/action.csv", usecols=['sku_id'])
    product = product[product['sku_id'].isin(action['sku_id'])]

    product = product.drop_duplicates('sku_id')
    product['product_reg_month'] = product['market_time'].apply(map_month)

    product['product_reg_cate'] = product['product_reg_month'].apply(map_cate)
    product = product.drop('market_time', axis=1)

    product = product.sort_values(by=['shop_id', 'cate', 'brand', 'product_reg_cate'])
    print('after:', product.shape)
    product.to_csv(clean_path + "/product.csv", index=False)


def clean_shop():
    # all column: 'vender_id', 'shop_id', 'fans_num', 'vip_num', 'shop_reg_tm','cate', 'shop_score'
    print('> cleaning shop')
    shop = pd.read_csv(fill_path + "/jdata_shop.csv", parse_dates=['shop_reg_tm'], na_filter=False)
    print('before:', shop.shape)

    product = pd.read_csv(clean_path + "/product.csv", usecols=['shop_id'])
    shop = shop[shop['shop_id'].isin(product['shop_id'])]
    shop = shop.drop_duplicates('shop_id')
    shop.rename(columns={'cate': 'shop_cate'}, inplace=True)

    shop['shop_reg_month'] = shop['shop_reg_tm'].apply(map_month)
    shop['shop_reg_cate'] = shop['shop_reg_month'].apply(map_cate)
    shop = shop.drop('shop_reg_tm', axis=1)

    print('after:', shop.shape)
    shop = shop.sort_values(by=['shop_reg_month'])
    shop.to_csv(clean_path + "/shop.csv", index=False)


def clean_comment():
    print('> cleaning comment')
    # all column: 'dt', 'sku_id', 'comments', 'good_comments', 'bad_comments'
    comment = pd.read_csv(fill_path + "/jdata_comment.csv", parse_dates=['dt'], na_filter=False)
    print('before:', comment.shape)

    product = pd.read_csv(clean_path + "/product.csv", usecols=['sku_id'])

    comment = comment[comment['sku_id'].isin(product['sku_id'])]
    comment = comment.sort_values(by=['sku_id', 'dt'])
    print('after:', comment.shape)
    comment.to_csv(clean_path + "/comment.csv", index=False)


def clean_action():
    print('> cleaning action')

    product = pd.read_csv(fill_path + "/jdata_product.csv", usecols=['sku_id'], na_filter=False)
    user = pd.read_csv(fill_path + "/jdata_user.csv", usecols=['user_id'], na_filter=False)
    # all column: 'user_id', 'sku_id', 'action_time', 'module_id', 'type' 1浏览 2下单 3关注 4评论 5加购物车
    action = pd.read_csv(fill_path + "/jdata_action.csv", parse_dates=['action_time'],
                         na_filter=False)
    print('before:', action.shape)
    print('读取完成！')
    print('before sku_id:', action.shape)
    action = action[action['sku_id'].isin(product['sku_id'])]
    print('before user_id:', action.shape)
    action = action[action['user_id'].isin(user['user_id'])]
    print('after:', action.shape)
    action = action.sort_values(by=['user_id', 'action_time'])
    print('排序完成！')
    action.to_csv(clean_path + "/action.csv", index=False)
    print('保存完成！')


if __name__ == "__main__":
    # fill_NaN()
    # clean_shop()
    clean_user()

"""log
D:\Program\Miniconda3\envs\env_jdata\python.exe D:/Project/JData-UCS/prepr/prepare.py
>> 开始处理数据
> cleaning action
before: (37214269, 5)
读取完成！
before sku_id: (37214269, 5)
before user_id: (36858846, 5)
after: (36858846, 5)
排序完成！
保存完成！
> cleaning user
before: (1608707, 9)
after: (1602150, 10)
> cleaning product
before: (352539, 5)
after: (352539, 6)
> cleaning comment
before: (1774233, 5)
after: (1710752, 5)
> cleaning shop
before: (10399, 7)
after: (10296, 7)
<< 数据处理完成!

Process finished with exit code 0

"""
