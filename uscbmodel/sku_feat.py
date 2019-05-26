# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @DATE    : 5/14/2019
# @Author  : xiaotong niu
# @File    : cate_feat.py
# @Project : JData-Predict
# @Github  ：https://github.com/isNxt
# @Describ : ...

from user_feat import *
import os
import pandas as pd
from datetime import timedelta
from datetime import datetime
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
train_start_date = "2018-03-10"
train_end_date = "2018-04-08"
sub_start_date = "2018-04-17"
sub_end_date = "2018-04-15"

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
comment_path = clean_path + "/comment.csv"
submit_path = '../submit'
cache_path = '../cache/sku'


# %% 特征提取
# TODO: (user_id,action_time) pkey
# GR: 依赖系列
# 浏览行为+商品
def feat_view_plus(start_date, end_date):
    print('view_plus_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/view_plus_%s_%s.csv' % (
        end_date.strftime('%y%m%d'), start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        feat = feat_view(start_date, end_date)
        product = pd.read_csv(product_path, na_filter=False)
        shop = pd.read_csv(shop_path, na_filter=False)
        feat = pd.merge(feat, product, on='sku_id', how='left')
        feat = pd.merge(feat, shop, on='shop_id', how='left')
        feat.to_csv(dump_path, index=False)
    return feat


# 购买行为+商品
def feat_buy_plus(start_date, end_date):
    print('buy_plus_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/buy_plus_%s_%s.csv' % (
        end_date.strftime('%y%m%d'), start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        feat = feat_buy(start_date, end_date)
        product = pd.read_csv(product_path, na_filter=False)
        shop = pd.read_csv(shop_path, na_filter=False)
        feat = pd.merge(feat, product, on='sku_id', how='left')
        feat = pd.merge(feat, shop, on='shop_id', how='left')
        feat.to_csv(dump_path, index=False)
    return feat


# 关注行为+商品
def feat_follow_plus(start_date, end_date):
    print('follow_plus_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/follow_plus_%s_%s.csv' % (
        end_date.strftime('%y%m%d'), start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        feat = feat_follow(start_date, end_date)
        product = pd.read_csv(product_path, na_filter=False)
        shop = pd.read_csv(shop_path, na_filter=False)
        feat = pd.merge(feat, product, on='sku_id', how='left')
        feat = pd.merge(feat, shop, on='shop_id', how='left')
        feat.to_csv(dump_path, index=False)
    return feat


# 评论行为+商品
def feat_remark_plus(start_date, end_date):
    print('remark_plus_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/remark_plus_%s_%s.csv' % (
        end_date.strftime('%y%m%d'), start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        feat = feat_remark(start_date, end_date)
        product = pd.read_csv(product_path, na_filter=False)
        shop = pd.read_csv(shop_path, na_filter=False)
        feat = pd.merge(feat, product, on='sku_id', how='left')
        feat = pd.merge(feat, shop, on='shop_id', how='left')
        feat.to_csv(dump_path, index=False)
    return feat


# 购物车行为+商品
def feat_cart_plus(start_date, end_date):
    print('cart_plus_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/cart_plus_%s_%s.csv' % (
        end_date.strftime('%y%m%d'), start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        feat = feat_cart(start_date, end_date)
        product = pd.read_csv(product_path, na_filter=False)
        shop = pd.read_csv(shop_path, na_filter=False)
        feat = pd.merge(feat, product, on='sku_id', how='left')
        feat = pd.merge(feat, shop, on='shop_id', how='left')
        feat.to_csv(dump_path, index=False)
    return feat


# TODO: (sku_id) pkey
# 商品信息
def feat_sku():
    print('product.csv')
    feat = pd.read_csv(product_path, na_filter=False, usecols=['sku_id', 'cate', 'brand', 'shop_id'])
    return feat


def feat_sku_plus():
    print('sku_plus')
    dump_path = cache_path + '/sku_plus.csv'
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        product = pd.read_csv(product_path, na_filter=False)
        shop = pd.read_csv(shop_path, na_filter=False)
        feat = pd.merge(product, shop, on='shop_id', how='left')
        feat = feat.drop(['vender_id'], axis=1)
        feat.to_csv(dump_path, index=False)
    return feat


# 品类系列


# GR: 是否系列
# 商品是否行为
def feat_sku_if_action(start_date, end_date):
    print('sku_if_action_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/sku_if_action_%s_%s.csv' % (
        end_date.strftime('%y%m%d'), start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        feat = feat_sku_action_amt(start_date, end_date)
        feat.ix[feat['sku_action_amt'] > 0, 'sku_action_amt'] = 1
        feat.rename(columns={'sku_action_amt': 'sku_if_action'}, inplace=True)
        feat = feat.astype(int)
        feat.to_csv(dump_path, index=False)
    return feat


# 商品是否浏览
def feat_sku_if_view(start_date, end_date):
    print('sku_if_view_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/sku_if_view_%s_%s.csv' % (
        end_date.strftime('%y%m%d'), start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        feat = feat_sku_view_amt(start_date, end_date)
        feat.ix[feat['sku_view_amt'] > 0, 'sku_view_amt'] = 1
        feat.rename(columns={'sku_view_amt': 'sku_if_view'}, inplace=True)
        feat = feat.astype(int)
        feat.to_csv(dump_path, index=False)
    return feat


# 商品是否购买
def feat_sku_if_buy(start_date, end_date):
    print('sku_if_buy_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/sku_if_buy_%s_%s.csv' % (
        end_date.strftime('%y%m%d'), start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        feat = feat_sku_buy_amt(start_date, end_date)
        feat.ix[feat['sku_buy_amt'] > 0, 'sku_buy_amt'] = 1
        feat.rename(columns={'sku_buy_amt': 'sku_if_buy'}, inplace=True)
        feat = feat.astype(int)
        feat.to_csv(dump_path, index=False)
    return feat


# 商品是否关注
def feat_sku_if_follow(start_date, end_date):
    print('sku_if_follow_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/sku_if_follow_%s_%s.csv' % (
        end_date.strftime('%y%m%d'), start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        feat = feat_sku_follow_amt(start_date, end_date)
        feat.ix[feat['sku_follow_amt'] > 0, 'sku_follow_amt'] = 1
        feat.rename(columns={'sku_follow_amt': 'sku_if_follow'}, inplace=True)
        feat = feat.astype(int)
        feat.to_csv(dump_path, index=False)
    return feat


# 商品是否评论
def feat_sku_if_remark(start_date, end_date):
    print('sku_if_remark_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/sku_if_remark_%s_%s.csv' % (
        end_date.strftime('%y%m%d'), start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        feat = feat_sku_remark_amt(start_date, end_date)
        feat.ix[feat['sku_remark_amt'] > 0, 'sku_remark_amt'] = 1
        feat.rename(columns={'sku_remark_amt': 'sku_if_remark'}, inplace=True)
        feat = feat.astype(int)
        feat.to_csv(dump_path, index=False)
    return feat


# 商品是否购物车
def feat_sku_if_cart(start_date, end_date):
    print('sku_if_cart_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/sku_if_cart_%s_%s.csv' % (
        end_date.strftime('%y%m%d'), start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        feat = feat_sku_cart_amt(start_date, end_date)
        feat.ix[feat['sku_cart_amt'] > 0, 'sku_cart_amt'] = 1
        feat.rename(columns={'sku_cart_amt': 'sku_if_cart'}, inplace=True)
        feat = feat.astype(int)
        feat.to_csv(dump_path, index=False)
    return feat


# GR: 数量系列
# 商品行为数量
def feat_sku_action_amt(start_date, end_date):
    print('sku_action_amt_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/sku_action_amt_%s_%s.csv' % (
        end_date.strftime('%y%m%d'), start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        action = feat_action(start_date, end_date)
        feat = action.groupby('sku_id').size().reset_index(name='sku_action_amt')
        feat = feat.astype(int)
        feat.to_csv(dump_path, index=False)
    return feat


# 商品浏览数量
def feat_sku_view_amt(start_date, end_date):
    print('sku_view_amt_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/sku_view_amt_%s_%s.csv' % (
        end_date.strftime('%y%m%d'), start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        action = feat_view(start_date, end_date)
        feat = action.groupby('sku_id').size().reset_index(name='sku_view_amt')
        feat = feat.astype(int)
        feat.to_csv(dump_path, index=False)
    return feat


# 商品购买数量
def feat_sku_buy_amt(start_date, end_date):
    print('sku_buy_amt_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/sku_buy_amt_%s_%s.csv' % (
        end_date.strftime('%y%m%d'), start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        action = feat_buy(start_date, end_date)
        feat = action.groupby('sku_id').size().reset_index(name='sku_buy_amt')
        feat = feat.astype(int)
        feat.to_csv(dump_path, index=False)
    return feat


# 商品关注数量
def feat_sku_follow_amt(start_date, end_date):
    print('sku_follow_amt_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/sku_follow_amt_%s_%s.csv' % (
        end_date.strftime('%y%m%d'), start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        action = feat_follow(start_date, end_date)
        feat = action.groupby('sku_id').size().reset_index(name='sku_follow_amt')
        feat = feat.astype(int)
        feat.to_csv(dump_path, index=False)
    return feat


# 商品评论数量
def feat_sku_remark_amt(start_date, end_date):
    print('sku_remark_amt_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/sku_remark_amt_%s_%s.csv' % (
        end_date.strftime('%y%m%d'), start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        action = feat_remark(start_date, end_date)
        feat = action.groupby('sku_id').size().reset_index(name='sku_remark_amt')
        feat = feat.astype(int)
        feat.to_csv(dump_path, index=False)
    return feat


# 商品购物车数量
def feat_sku_cart_amt(start_date, end_date):
    print('sku_cart_amt_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/sku_cart_amt_%s_%s.csv' % (
        end_date.strftime('%y%m%d'), start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        action = feat_cart(start_date, end_date)
        feat = action.groupby('sku_id').size().reset_index(name='sku_cart_amt')
        feat = feat.astype(int)
        feat.to_csv(dump_path, index=False)
    return feat


# 商品历史评论数量(含比例)
def feat_sku_comment_amt(start_date, end_date):
    print('sku_comment_amt_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/sku_comment_amt_%s_%s.csv' % (
        end_date.strftime('%y%m%d'), start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        comment = pd.read_csv(comment_path, na_filter=False, parse_dates=['dt'], skip_blank_lines=True)
        comment = comment[
            (start_date <= comment['dt']) & (comment['dt'] <= end_date)]
        feat = comment.groupby('sku_id').sum().reset_index()
        feat.fillna(0, inplace=True)
        feat.ix[feat['comments'] == 0, 'comments'] = -1
        feat['bad/all'] = feat['bad_comments'] / feat['comments'] * 100
        feat['good/all'] = feat['good_comments'] / feat['comments'] * 100
        feat = feat.astype(int)
        feat.to_csv(dump_path, index=False)
    return feat


# GR: 其他
# 商品行为比例
def feat_sku_action_ratio(start_date, end_date):
    print('sku_action_ratio_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/sku_action_ratio_%s_%s.csv' % (
        end_date.strftime('%y%m%d'), start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        feat = pd.read_csv(product_path, na_filter=False, skip_blank_lines=True, usecols=['sku_id'])
        feat = pd.merge(feat, feat_sku_action_amt(start_date, end_date), on='sku_id', how='left')
        feat = pd.merge(feat, feat_sku_view_amt(start_date, end_date), on='sku_id', how='left')
        feat = pd.merge(feat, feat_sku_buy_amt(start_date, end_date), on='sku_id', how='left')
        feat = pd.merge(feat, feat_sku_follow_amt(start_date, end_date), on='sku_id', how='left')
        feat = pd.merge(feat, feat_sku_remark_amt(start_date, end_date), on='sku_id', how='left')
        feat = pd.merge(feat, feat_sku_cart_amt(start_date, end_date), on='sku_id', how='left')
        feat.fillna(0, inplace=True)
        feat.ix[feat['sku_action_amt'] == 0, 'sku_action_amt'] = -1
        feat['sku_view_ratio'] = feat['sku_view_amt'] / (feat['sku_action_amt']) * 100
        feat['sku_buy_ratio'] = feat['sku_buy_amt'] / (feat['sku_action_amt']) * 100
        feat['sku_follow_ratio'] = feat['sku_follow_amt'] / (feat['sku_action_amt']) * 100
        feat['sku_remark_ratio'] = feat['sku_remark_amt'] / (feat['sku_action_amt']) * 100
        feat['sku_cart_ratio'] = feat['sku_cart_amt'] / (feat['sku_action_amt']) * 100
        feat = feat[['sku_id', 'sku_view_ratio', 'sku_buy_ratio', 'sku_follow_ratio', 'sku_remark_ratio',
                     'sku_cart_ratio']]
        feat = feat.astype(int)
        feat.to_csv(dump_path, index=False)

    return feat


# 商品购买转换率
def feat_sku_buy_rate(start_date, end_date):
    print('sku_buy_rate_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/sku_buy_rate_%s_%s.csv' % (
        end_date.strftime('%y%m%d'), start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        feat = pd.read_csv(product_path, na_filter=False, skip_blank_lines=True, usecols=['sku_id'])
        feat = pd.merge(feat, feat_sku_view_amt(start_date, end_date), on='sku_id', how='left')
        feat = pd.merge(feat, feat_sku_buy_amt(start_date, end_date), on='sku_id', how='left')
        feat = pd.merge(feat, feat_sku_follow_amt(start_date, end_date), on='sku_id', how='left')
        feat = pd.merge(feat, feat_sku_remark_amt(start_date, end_date), on='sku_id', how='left')
        feat = pd.merge(feat, feat_sku_cart_amt(start_date, end_date), on='sku_id', how='left')
        feat.fillna(0, inplace=True)
        feat.ix[feat['sku_follow_amt'] == 0, 'sku_follow_amt'] = -1
        feat['sku_buy/follow'] = feat['sku_buy_amt'] / (feat['sku_follow_amt']) * 100
        feat.ix[feat['sku_remark_amt'] == 0, 'sku_remark_amt'] = -1
        feat['sku_buy/remark'] = feat['sku_buy_amt'] / (feat['sku_remark_amt']) * 100
        feat.ix[feat['sku_cart_amt'] == 0, 'sku_cart_amt'] = -1
        feat['sku_buy/cart'] = feat['sku_buy_amt'] / (feat['sku_cart_amt']) * 100
        feat.ix[feat['sku_view_amt'] == 0, 'sku_view_amt'] = -1
        feat['sku_buy/view'] = feat['sku_buy_amt'] / (feat['sku_view_amt']) * 100
        feat = feat[['sku_id', 'sku_buy/view', 'sku_buy/follow', 'sku_buy/remark', 'sku_buy/cart']]
        feat = feat.astype(int)
        feat.to_csv(dump_path, index=False)

    return feat


# 商品最早行为时差(小时)
def feat_sku_first_hour(start_date, end_date):
    print('sku_first_hour_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/sku_first_hour_%s_%s.csv' % (end_date.strftime('%y%m%d'),
                                                               start_date.strftime('%y%m%d'),
                                                               end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        action = feat_action(start_date, end_date)[['sku_id', 'action_time']]
        action.sort_values(['sku_id', 'action_time'], inplace=True)
        feat = action.groupby('sku_id').max().reset_index()
        feat['sku_first_hour'] = [((end_date - i).total_seconds()) // 3600 for i in feat['action_time']]
        feat.drop('action_time', axis=1, inplace=True)
        feat = feat.astype(int)
        feat.to_csv(dump_path, index=False)
    return feat


# 商品最晚行为时差(小时)
def feat_sku_last_hour(start_date, end_date):
    print('sku_last_hour_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/sku_last_hour_%s_%s.csv' % (end_date.strftime('%y%m%d'),
                                                              start_date.strftime('%y%m%d'),
                                                              end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        action = feat_action(start_date, end_date)[['sku_id', 'action_time']]
        action.sort_values(['sku_id', 'action_time'], inplace=True)
        feat = action.groupby('sku_id').min().reset_index()
        feat['sku_last_hour'] = [((end_date - i).total_seconds()) // 3600 for i in feat['action_time']]
        feat.drop('action_time', axis=1, inplace=True)
        feat = feat.astype(int)
        feat.to_csv(dump_path, index=False)
    return feat


# 商品最晚行为次数(天)
def feat_sku_last_amt(start_date, end_date):
    print('sku_last_amt_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/sku_last_amt_%s_%s.csv' % (end_date.strftime('%y%m%d'),
                                                             start_date.strftime('%y%m%d'),
                                                             end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        action = feat_action(start_date, end_date)[['sku_id', 'action_time']]
        action.sort_values(['sku_id', 'action_time'], inplace=True)
        action['action_time'] = action['action_time'].values.astype('datetime64[D]')
        sub_action = action.groupby('sku_id').first().reset_index()
        action = pd.merge(sub_action, action, on=['sku_id', 'action_time'], how='left')
        feat = action.groupby('sku_id').size().reset_index(name='sku_last_amt')
        feat = feat.astype(int)
        feat.to_csv(dump_path, index=False)
    return feat


# GR: 天数
# 商品行为天数
def feat_sku_action_day(start_date, end_date):
    print('sku_action_day_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/sku_action_day_%s_%s.csv' % (end_date.strftime('%y%m%d'),
                                                               start_date.strftime('%y%m%d'),
                                                               end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        action = feat_action(start_date, end_date)[['sku_id', 'action_time']]
        action.sort_values(['sku_id', 'action_time'], inplace=True)
        action['action_time'] = action['action_time'].values.astype('datetime64[D]')
        action = action.drop_duplicates(['sku_id', 'action_time'])
        feat = action.groupby('sku_id').size().reset_index(name='sku_action_day')
        feat = feat.astype(int)
        feat.to_csv(dump_path, index=False)
    return feat


# 商品浏览天数
def feat_sku_view_day(start_date, end_date):
    print('sku_view_day_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/sku_view_day_%s_%s.csv' % (end_date.strftime('%y%m%d'),
                                                             start_date.strftime('%y%m%d'),
                                                             end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        view = feat_view(start_date, end_date)[['sku_id', 'action_time']]
        view.sort_values(['sku_id', 'action_time'], inplace=True)
        view['action_time'] = view['action_time'].values.astype('datetime64[D]')
        view = view.drop_duplicates(['sku_id', 'action_time'])
        feat = view.groupby('sku_id').size().reset_index(name='sku_view_day')
        feat = feat.astype(int)
        feat.to_csv(dump_path, index=False)
    return feat


# 商品购买天数
def feat_sku_buy_day(start_date, end_date):
    print('sku_buy_day_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/sku_buy_day_%s_%s.csv' % (end_date.strftime('%y%m%d'),
                                                            start_date.strftime('%y%m%d'),
                                                            end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        buy = feat_buy(start_date, end_date)[['sku_id', 'action_time']]
        buy.sort_values(['sku_id', 'action_time'], inplace=True)
        buy['action_time'] = buy['action_time'].values.astype('datetime64[D]')
        buy = buy.drop_duplicates(['sku_id', 'action_time'])
        feat = buy.groupby('sku_id').size().reset_index(name='sku_buy_day')
        feat = feat.astype(int)
        feat.to_csv(dump_path, index=False)
    return feat


# 商品关注天数
def feat_sku_follow_day(start_date, end_date):
    print('sku_follow_day_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/sku_follow_day_%s_%s.csv' % (end_date.strftime('%y%m%d'),
                                                               start_date.strftime('%y%m%d'),
                                                               end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        follow = feat_follow(start_date, end_date)[['sku_id', 'action_time']]
        follow.sort_values(['sku_id', 'action_time'], inplace=True)
        follow['action_time'] = follow['action_time'].values.astype('datetime64[D]')
        follow = follow.drop_duplicates(['sku_id', 'action_time'])
        feat = follow.groupby('sku_id').size().reset_index(name='sku_follow_day')
        feat = feat.astype(int)
        feat.to_csv(dump_path, index=False)
    return feat


# 商品评论天数
def feat_sku_remark_day(start_date, end_date):
    print('sku_remark_day_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/sku_remark_day_%s_%s.csv' % (end_date.strftime('%y%m%d'),
                                                               start_date.strftime('%y%m%d'),
                                                               end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        remark = feat_remark(start_date, end_date)[['sku_id', 'action_time']]
        remark.sort_values(['sku_id', 'action_time'], inplace=True)
        remark['action_time'] = remark['action_time'].values.astype('datetime64[D]')
        remark = remark.drop_duplicates(['sku_id', 'action_time'])
        feat = remark.groupby('sku_id').size().reset_index(name='sku_remark_day')
        feat = feat.astype(int)
        feat.to_csv(dump_path, index=False)
    return feat


# 商品购物车天数
def feat_sku_cart_day(start_date, end_date):
    print('sku_cart_day_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/sku_cart_day_%s_%s.csv' % (end_date.strftime('%y%m%d'),
                                                             start_date.strftime('%y%m%d'),
                                                             end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        cart = feat_cart(start_date, end_date)[['sku_id', 'action_time']]
        cart.sort_values(['sku_id', 'action_time'], inplace=True)
        cart['action_time'] = cart['action_time'].values.astype('datetime64[D]')
        cart = cart.drop_duplicates(['sku_id', 'action_time'])
        feat = cart.groupby('sku_id').size().reset_index(name='sku_cart_day')
        feat = feat.astype(int)
        feat.to_csv(dump_path, index=False)
    return feat


# GR: 特殊系列
# 重复购买率
def feat_sku_rebuy_rate(start_date, end_date):
    print('sku_rebuy_rate_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/sku_rebuy_rate_%s_%s.csv' % (end_date.strftime('%y%m%d'),
                                                               start_date.strftime('%y%m%d'),
                                                               end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        buy = feat_buy(start_date, end_date)[['user_id', 'sku_id']]
        df1 = buy.groupby(['user_id', 'sku_id']).size().reset_index(name='user_buy_amt')
        df2 = df1[df1['user_buy_amt'] > 1]
        df1 = df1.drop('user_buy_amt', axis=1)
        df2 = df2.drop('user_buy_amt', axis=1)
        df1 = df1.groupby('sku_id', as_index=False).size().reset_index(name='all_user_amt')
        df2 = df2.groupby('sku_id', as_index=False).size().reset_index(name='all_rebuy_user_amt')
        feat = pd.read_csv(product_path, na_filter=False, skip_blank_lines=True)[['sku_id']]
        feat = pd.merge(feat, df1, on='sku_id', how='left')
        feat = pd.merge(feat, df2, on='sku_id', how='left')
        feat.fillna(0, inplace=True)
        feat.ix[feat['all_user_amt'] == 0, 'all_user_amt'] = -1
        feat['sku_rebuy_rate'] = (feat['all_rebuy_user_amt'] / feat['all_user_amt']) * 100
        feat = feat[['sku_id', 'sku_rebuy_rate']]
        feat = feat.astype(int)
        feat.to_csv(dump_path, index=False)
    return feat


if __name__ == "__main__":
    end_date = datetime.strptime(train_end_date, '%Y-%m-%d')
    start_date = datetime.strptime(train_start_date, '%Y-%m-%d')
    action = feat_sku_comment_amt(start_date, end_date)
