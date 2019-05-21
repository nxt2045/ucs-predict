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
fill_list = ['jdata_user.csv', 'jdata_shop.csv']
clean_list = ['action.csv', 'user.csv', 'product.csv', 'shop.csv', 'comment.csv']

# 路径
data_path = "../data"
ori_path = "../data/ori"
clean_path = "../data/clean"
fill_path = "../data/fill"
stats_path = "../data/stats"
plot_path = "../data/plot"
user_path = clean_path + "/user.csv"
action_path = clean_path + "/action.csv"
product_path = clean_path + "/product.csv"
shop_path = clean_path + "/shop.csv"
submit_path = '../submit'
output_path = '../output'
cache_path = '../cache'


# %% step 1 填充空值 输出到/data/fill

def fill_NaN():
    _time_0 = time.clock()
    print('\n>> 开始替换数据')
    for file_name in ori_list:
        in_file = ori_path + "/" + file_name
        out_file = fill_path + "/" + file_name
        if file_name in fill_list:
            print("> Null in ", file_name)
            df = pd.read_csv(in_file, dtype=object)
            print(df[df.isnull().values == True].head())
            print("> filling", file_name)
            print('\t读取完成！用时', time.clock() - _time_0, 's')
            df.fillna(-1, inplace=True)
            df.to_csv(out_file, index=False)
            print('\t保存完成！用时', time.clock() - _time_0, 's')
        else:
            print("> copying", file_name)
            shutil.copyfile(in_file, out_file)
            print('\t复制完成！用时', time.clock() - _time_0, 's')
    print('<< 数据替换完成！用时', time.clock() - _time_0, 's')


# %% step 2 删除无效 输出到/data/clean
def clean_data():
    time_0 = time.clock()
    print('\n>> 开始处理数据')
    clean_action()  # 必须先action
    clean_user()
    clean_product()
    clean_comment()
    clean_shop()
    print('<< 数据处理完成！用时', time.clock() - time_0, 's')


def map_month(x):
    if x < datetime.strptime(sub_start_date, '%Y-%m-%d'):
        d = datetime.strptime(sub_start_date, '%Y-%m-%d') - x
        d = d.days // 30
    else:
        d = -1
    return d


def cate_reg(d):
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
    dtype_user = {'age': 'category', 'sex': 'category', 'user_lv_cd': 'category', 'city_level': 'category',
                  'province': 'category', 'city': 'category', 'county': 'category'}
    user = pd.read_csv(fill_path + "/jdata_user.csv", parse_dates=['user_reg_tm'], na_filter=False)
    print('\tbefore:', user.shape)
    action = pd.read_csv(clean_path + "/action.csv", usecols=['user_id'])
    user = user[user['user_id'].isin(action['user_id'])]
    user = user.drop_duplicates('user_id')
    user['user_reg_month'] = user['user_reg_tm'].apply(map_month)
    user['user_reg_cate'] = user['user_reg_month'].apply(cate_reg)
    user = user.sort_values('user_id')
    user = user.drop('user_reg_tm', axis=1)
    print('\tafter:', user.shape)
    user.to_csv(clean_path + "/user.csv", index=False)


def clean_product():
    # all column: 'sku_id', 'brand', 'shop_id', 'cate', 'market_time'
    print('> cleaning product')
    dtype_product = {'cate': 'category'}
    product = pd.read_csv(fill_path + "/jdata_product.csv", parse_dates=['market_time'], na_filter=False)
    print('\tbefore:', product.shape)

    action = pd.read_csv(clean_path + "/action.csv", usecols=['sku_id'])
    product = product[product['sku_id'].isin(action['sku_id'])]

    product = product.drop_duplicates('sku_id')
    product['product_month'] = product['market_time'].apply(map_month)
    product['product_cate'] = product['product_month'].apply(cate_reg)
    product = product.drop('product_month', axis=1)

    product = product.sort_values(by=['shop_id', 'cate', 'brand', 'product_cate'])
    print('\tafter:', product.shape)
    product.to_csv(clean_path + "/product.csv", index=False)


def clean_shop():
    # all column: 'vender_id', 'shop_id', 'fans_num', 'vip_num', 'shop_reg_tm','cate', 'shop_score'
    print('> cleaning shop')
    shop = pd.read_csv(fill_path + "/jdata_shop.csv", parse_dates=['shop_reg_tm'], na_filter=False)
    print('\tbefore:', shop.shape)

    product = pd.read_csv(clean_path + "/product.csv", usecols=['shop_id'])
    shop = shop[shop['shop_id'].isin(product['shop_id'])]
    shop = shop.drop_duplicates('shop_id')
    shop.rename(columns={'cate': 'shop_cate'}, inplace=True)
    print('\tafter:', shop.shape)
    shop = shop.sort_values(by=['shop_id'])
    shop.to_csv(clean_path + "/shop.csv", index=False)


def clean_comment():
    print('> cleaning comment')
    # all column: 'dt', 'sku_id', 'comments', 'good_comments', 'bad_comments'
    comment = pd.read_csv(fill_path + "/jdata_comment.csv", parse_dates=['dt'], na_filter=False)
    print('\tbefore:', comment.shape)

    product = pd.read_csv(clean_path + "/product.csv", usecols=['sku_id'])

    comment = comment[comment['sku_id'].isin(product['sku_id'])]
    comment = comment.sort_values(by=['sku_id', 'dt'])
    print('\tafter:', comment.shape)
    comment.to_csv(clean_path + "/comment.csv", index=False)


def clean_action():
    print('> cleaning action')
    _time_0 = time.clock()
    product = pd.read_csv(fill_path + "/jdata_product.csv", usecols=['sku_id'], na_filter=False)
    user = pd.read_csv(fill_path + "/jdata_user.csv", usecols=['user_id'], na_filter=False)
    # all column: 'user_id', 'sku_id', 'action_time', 'module_id', 'type' 1浏览 2下单 3关注 4评论 5加购物车
    action = pd.read_csv(fill_path + "/jdata_action.csv", parse_dates=['action_time'],
                         na_filter=False)
    print('\tbefore:', action.shape)
    print('\t读取完成！用时', time.clock() - _time_0, 's')
    # # action.csv每个人都至少购买了一次
    # action_type = pd.concat([action[['user_id']], pd.get_dummies(action['type'], prefix='type')], axis=1)
    # user_action_type_amt = (action_type.groupby('user_id').sum().reset_index()).astype(int)
    # user_buy = user_action_type_amt[user_action_type_amt['type_2'] > 0]
    # print('\tbefore user_buy:', action.shape)
    # action = action[action['user_id'].isin(user_buy['user_id'])]
    print('\tbefore sku_id:', action.shape)
    action = action[action['sku_id'].isin(product['sku_id'])]
    print('\tbefore user_id:', action.shape)
    action = action[action['user_id'].isin(user['user_id'])]
    print('\tafter:', action.shape)
    action = action.sort_values(by=['user_id', 'action_time'])
    print('\t排序完成！用时', time.clock() - _time_0, 's')
    action.to_csv(clean_path + "/action.csv", index=False)
    print('\t保存完成！用时', time.clock() - _time_0, 's')


if __name__ == "__main__":
    clean_data()
