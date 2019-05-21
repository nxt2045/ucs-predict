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

# 读取
print('> reading')
product = pd.read_csv(fill_path + "/jdata_product.csv", na_filter=False)
user = pd.read_csv(fill_path + "/jdata_user.csv", na_filter=False)
action = pd.read_csv(fill_path + "/jdata_action.csv", na_filter=False, parse_dates=['action_time'])
comment = pd.read_csv(fill_path + "/jdata_comment.csv", na_filter=False)
shop = pd.read_csv(fill_path + "/jdata_shop.csv", na_filter=False)
# 总hist
'''
print("> histing")
plt.rcParams['figure.figsize'] = (15, 10)
product.hist(bins=20)
plt.savefig('./plot/product_hist.png', dpi=300)
user.hist(bins=20)
plt.savefig('./plot/user_hist.png', dpi=300)
action.hist(bins=20)
plt.savefig('./plot/action_hist.png', dpi=300)
comment.hist(bins=20)
plt.savefig('./plot/comment_hist.png', dpi=300)
shop.hist(bins=20)
plt.savefig('./plot/shop_hist.png', dpi=300)
'''
# 每人行为
print('> per action plus')
groups = action.groupby(action['user_id'])
for group in groups:
    user_id = group[0]
    df = pd.merge(group[1], product, on='sku_id')
    df.to_csv('./csv/%s.csv'%(str(user_id)))
