# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @DATE    : 5/20/2019
# @Author  : xiaotong
# @File    : draw
# @Project : PyCharm
# @Github  ：https://github.com/isNxt
# @Describ : ...
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import skewnorm
import os, time
import numpy as np
import pandas as pd
import matplotlib.dates as mdates
from pandas.plotting import register_matplotlib_converters

# 配置
# 输出设置
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)
register_matplotlib_converters()
plt.style.use('seaborn')
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
user_path = clean_path + "/user.csv"
action_path = clean_path + "/action.csv"
product_path = clean_path + "/product.csv"
shop_path = clean_path + "/shop.csv"
submit_path = '../submit'
cache_path = '../cache'


# 总数据bar
def total_bar():
    print('> 读取数据')
    product = pd.read_csv(product_path, na_filter=False, usecols=['cate'])
    user = pd.read_csv(user_path, na_filter=False,
                       usecols=['age', 'sex', 'user_reg_month', 'user_reg_cate', 'user_lv_cd', 'city_level',
                                'province'])
    action = pd.read_csv(action_path, na_filter=False, usecols=['type'])
    shop = pd.read_csv(shop_path, na_filter=False, usecols=['shop_cate'])
    print("> user数据bar图")
    plt.figure(figsize=(8, 6))
    user['age'].value_counts().plot.bar()
    plt.savefig('./plot/总数据bar/user_%s.png' % 'age', dpi=200, bbox_inches='tight')

    plt.figure(figsize=(5, 5))
    user['sex'].value_counts().plot.bar()
    plt.savefig('./plot/总数据bar/user_%s.png' % 'sex', dpi=200, bbox_inches='tight')

    plt.figure(figsize=(45, 6))
    user['user_reg_month'].value_counts().plot.bar()
    plt.savefig('./plot/总数据bar/user_%s.png' % 'reg_month', dpi=200, bbox_inches='tight')

    plt.figure(figsize=(8, 6))
    user['user_reg_cate'].value_counts().plot.bar()
    plt.savefig('./plot/总数据bar/user_%s.png' % 'reg_cate', dpi=200, bbox_inches='tight')

    plt.figure(figsize=(8, 6))
    user['user_lv_cd'].value_counts().plot.bar()
    plt.savefig('./plot/总数据bar/user_%s.png' % 'lv_cd', dpi=200, bbox_inches='tight')

    plt.figure(figsize=(8, 6))
    user['city_level'].value_counts().plot.bar()
    plt.savefig('./plot/总数据bar/user_%s.png' % 'city_level', dpi=200, bbox_inches='tight')

    plt.figure(figsize=(20, 6))
    user['province'].value_counts().plot.bar()
    plt.savefig('./plot/总数据bar/user_%s.png' % 'province', dpi=200, bbox_inches='tight')

    print("> product数据bar图")
    plt.figure(figsize=(20, 6))
    product['cate'].value_counts().plot.bar()
    plt.savefig('./plot/总数据bar/product_cate.png', dpi=200, bbox_inches='tight')

    print("> action数据bar图")
    plt.figure(figsize=(6, 6))
    action['type'].value_counts().plot.bar()
    plt.savefig('./plot/总数据bar/action_type.png', dpi=200, bbox_inches='tight')

    print("> shop数据bar图")
    plt.figure(figsize=(20, 6))
    shop['shop_cate'].value_counts().plot.bar()
    plt.savefig('./plot/总数据bar/shop_%s.png' % 'cate', dpi=200, bbox_inches='tight')


# 购买品类bar
def buy_cate_bar():
    print('> 读取数据')
    product = pd.read_csv(fill_path + "/jdata_product.csv", na_filter=False)
    buy = pd.read_csv("./csv/buy.csv", na_filter=False, parse_dates=['action_time'])
    buy_plus = pd.merge(buy, product, on='sku_id')
    print("> 购买品类bar")
    plt.figure(figsize=(20, 6))
    buy_plus['cate'].value_counts().plot.bar()
    plt.savefig('./plot/buy_cate_bar.png', dpi=200, bbox_inches='tight')
    print("> 购买品类/商品品类")
    plt.figure(figsize=(20, 6))
    buy_plus = buy_plus.sort_values(by=['cate'])
    product = product.sort_values(by=['cate'])
    (buy_plus['cate'].value_counts()/product['cate'].value_counts()).plot.bar()
    plt.savefig('./plot/buy_cate_ratio_bar.png', dpi=200, bbox_inches='tight')


# 每日购买折线
def daily_buy_line():
    print('> 读取数据')
    buy = pd.read_csv("./csv/buy.csv", na_filter=False, parse_dates=['action_time'])

    print("> 每日购买折线图")
    buy = pd.concat(
        [buy, pd.DataFrame({'action_date': buy['action_time'].values.astype('datetime64[D]')})],
        axis=1)
    buy_user = buy[['action_date', 'user_id']].drop_duplicates()
    buy_user_amt = buy_user.groupby('action_date').size().reset_index(name='user_amt')
    buy_user_amt.to_csv('./csv/daily_buy_user_amt.csv', index=False)
    plt.figure(figsize=(20, 6))
    plt.xticks(rotation=90)
    ax = plt.gca()
    ax.plot_date(buy_user_amt['action_date'].values, buy_user_amt['user_amt'].values, linestyle="-", marker="o")
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator())
    # 日期的排列根据图像的大小自适应
    # fig.autofmt_xdate()
    plt.savefig('./plot/daily_buy_line.png', dpi=200, bbox_inches='tight')


# 购买用户数量
def buy_user_amt():
    """
    全部的用户数量： 1608707 买过的用户数量： 1608707
    """
    print('> 读取数据')
    user = pd.read_csv(fill_path + "/jdata_user.csv", na_filter=False)
    buy = pd.read_csv("./csv/buy.csv", na_filter=False, parse_dates=['action_time'])
    print('> 每个购买过的用户行为详情')
    buy_user = user[user['user_id'].isin(buy['user_id'])]
    print('全部的用户数量：', user.shape[0], '买过的用户数量：', buy_user.shape[0], )


# 每人行为
def per_action_plus():
    print('> 读取数据')
    product = pd.read_csv(fill_path + "/jdata_product.csv", na_filter=False)
    action = pd.read_csv(fill_path + "/jdata_action.csv", na_filter=False, parse_dates=['action_time'])

    print('> 每个用户行为详情')
    groups = action.groupby(action['user_id'])
    for group in groups:
        print(group[0])
        user_id = group[0]
        df = pd.merge(group[1], product, on='sku_id')
        df = df.sort_values(by=['action_time'])
        df.to_csv('./csv/每个用户行为详情/用户_%s.csv' % (str(user_id)), index=False)


# 分离行为
def split_action_type():
    action = pd.read_csv(fill_path + "/jdata_action.csv", na_filter=False)
    buy = action[action['type'] == 2]
    buy.to_csv('./csv/buy.csv', index=False)


# 特征标签bar
def feat_bar(f_path):
    feat = pd.read_csv(f_path)
    file_name = f_path.split('/')[-1]
    for col in feat.columns:
        sns.countplot(x="label", hue=col, data=feat)
        plt.savefig('./%s_bar/%s_label.png' % (file_name, col))


if __name__ == "__main__":
    # total_bar()
    # buy_cate_bar()
    daily_buy_line()
