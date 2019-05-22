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
user_path = clean_path + "/user.csv"
action_path = clean_path + "/action.csv"
product_path = clean_path + "/product.csv"
shop_path = clean_path + "/shop.csv"
submit_path = '../submit'
cache_path = '../cache'

# %% 读取数据
print('> 读取数据')
product = pd.read_csv(fill_path + "/jdata_product.csv", na_filter=False)
user = pd.read_csv(fill_path + "/jdata_user.csv", na_filter=False)
action = pd.read_csv(fill_path + "/jdata_action.csv", na_filter=False, parse_dates=['action_time'])
comment = pd.read_csv(fill_path + "/jdata_comment.csv", na_filter=False)
shop = pd.read_csv(fill_path + "/jdata_shop.csv", na_filter=False)


# %% 原hist
def fill_hist():
    print("> 原频率分布直方图")
    plt.rcParams['figure.figsize'] = (15, 10)
    product.hist()
    plt.savefig('./plot/product_hist.png', dpi=300)
    user.hist()
    plt.savefig('./plot/user_hist.png', dpi=300)
    action.hist()
    plt.savefig('./plot/action_hist.png', dpi=300)
    shop.hist()
    plt.savefig('./plot/shop_hist.png', dpi=300)


# %% 每日购买折线
def daily_buy_line():
    print("> 每日购买折线图")
    buy = action[action['type'] == 2]
    buy = pd.concat([buy, pd.DataFrame({'action_date':buy['action_time'].values.astype('datetime64[D]')})],axis=1)
    buy_user = buy[['action_date','user_id']].drop_duplicates()
    buy_user_amt = buy_user.groupby('action_date').size().reset_index(name='user_amt')
    plt.rcParams['figure.figsize'] = (15, 10)
    plt.plot(buy_user_amt['action_date'],buy_user_amt['user_amt'])
    plt.savefig('./plot/daily_buy_line.png', dpi=300)



# %% 购买用户数量
def buy_user_amt():
    """
    全部的用户数量： 1608707 买过的用户数量： 1608707
    """
    print('> 每个购买过的用户行为详情')
    buy = action[action['type'] == 2]
    buy_user = user[user['user_id'].isin(buy['user_id'])]
    print('全部的用户数量：', user.shape[0], '买过的用户数量：', buy_user.shape[0], )


# %% 每人行为
def per_action_plus():
    print('> 每个用户行为详情')
    groups = action.groupby(action['user_id'])
    for group in groups:
        print(group[0])
        user_id = group[0]
        df = pd.merge(group[1], product, on='sku_id')
        df = df.sort_values(by=['action_time'])
        df.to_csv('./csv/每个用户行为详情/用户_%s.csv' % (str(user_id)), index=False)


if __name__ == "__main__":
    fill_hist()
