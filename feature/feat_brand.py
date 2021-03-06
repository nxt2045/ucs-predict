# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @DATE    : 5/1/2019
# @Author  : xiaotong niu
# @File    : feat_brand.py
# @Project : JData-UCS
# @Github  ：https://github.com/isNxt
# @Describ : ...

from feature.feat_user import *
from feature.feat_sku import *

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
submit_path = '../submit'
cache_path = '../cache/brand'


# %% 特征提取
# TODO: (user_id,action_time) pkey

# 品牌系列

# GR: 数量系列t

# 品牌浏览数量
def feat_brand_view_amt(start_date, end_date):
    print('brand_view_amt_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/brand_view_amt_%s_%s.csv' % (
        end_date.strftime('%y%m%d'), start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        action = feat_view_plus(start_date, end_date)[['brand', 'action_time']]
        feat = action.groupby('brand').size().reset_index(name='brand_view_amt')
        feat = feat.astype(int)
        feat.to_csv(dump_path, index=False)
    return feat


# 品牌购买数量
def feat_brand_buy_amt(start_date, end_date):
    print('brand_buy_amt_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/brand_buy_amt_%s_%s.csv' % (
        end_date.strftime('%y%m%d'), start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        action = feat_buy_plus(start_date, end_date)
        feat = action.groupby('brand').size().reset_index(name='brand_buy_amt')
        feat = feat.astype(int)
        feat.to_csv(dump_path, index=False)
    return feat


# 品牌关注数量
def feat_brand_follow_amt(start_date, end_date):
    print('brand_follow_amt_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/brand_follow_amt_%s_%s.csv' % (
        end_date.strftime('%y%m%d'), start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        action = feat_follow_plus(start_date, end_date)
        feat = action.groupby('brand').size().reset_index(name='brand_follow_amt')
        feat = feat.astype(int)
        feat.to_csv(dump_path, index=False)
    return feat


# 品牌评论数量
def feat_brand_remark_amt(start_date, end_date):
    print('brand_remark_amt_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/brand_remark_amt_%s_%s.csv' % (
        end_date.strftime('%y%m%d'), start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        action = feat_remark_plus(start_date, end_date)
        feat = action.groupby('brand').size().reset_index(name='brand_remark_amt')
        feat = feat.astype(int)
        feat.to_csv(dump_path, index=False)
    return feat


# 品牌购物车数量
def feat_brand_cart_amt(start_date, end_date):
    print('brand_cart_amt_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/brand_cart_amt_%s_%s.csv' % (
        end_date.strftime('%y%m%d'), start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        action = feat_cart_plus(start_date, end_date)
        feat = action.groupby('brand').size().reset_index(name='brand_cart_amt')
        feat = feat.astype(int)
        feat.to_csv(dump_path, index=False)
    return feat



# GR: 天数


# 品牌浏览天数
def feat_brand_view_day(start_date, end_date):
    print('brand_view_day_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/brand_view_day_%s_%s.csv' % (end_date.strftime('%y%m%d'),
                                                             start_date.strftime('%y%m%d'),
                                                             end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        view = feat_view_plus(start_date, end_date)[['brand', 'action_time']]
        view.sort_values(['brand', 'action_time'], inplace=True)
        view['action_time'] = view['action_time'].values.astype('datetime64[D]')
        view = view.drop_duplicates(['brand', 'action_time'])
        feat = view.groupby('brand').size().reset_index(name='brand_view_day')
        feat = feat.astype(int)
        feat.to_csv(dump_path, index=False)
    return feat


# 品牌购买天数
def feat_brand_buy_day(start_date, end_date):
    print('brand_buy_day_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/brand_buy_day_%s_%s.csv' % (end_date.strftime('%y%m%d'),
                                                            start_date.strftime('%y%m%d'),
                                                            end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        buy = feat_buy_plus(start_date, end_date)[['brand', 'action_time']]
        buy.sort_values(['brand', 'action_time'], inplace=True)
        buy['action_time'] = buy['action_time'].values.astype('datetime64[D]')
        buy = buy.drop_duplicates(['brand', 'action_time'])
        feat = buy.groupby('brand').size().reset_index(name='brand_buy_day')
        feat = feat.astype(int)
        feat.to_csv(dump_path, index=False)
    return feat


# 品牌关注天数
def feat_brand_follow_day(start_date, end_date):
    print('brand_follow_day_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/brand_follow_day_%s_%s.csv' % (end_date.strftime('%y%m%d'),
                                                               start_date.strftime('%y%m%d'),
                                                               end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        follow = feat_follow_plus(start_date, end_date)[['brand', 'action_time']]
        follow.sort_values(['brand', 'action_time'], inplace=True)
        follow['action_time'] = follow['action_time'].values.astype('datetime64[D]')
        follow = follow.drop_duplicates(['brand', 'action_time'])
        feat = follow.groupby('brand').size().reset_index(name='brand_follow_day')
        feat = feat.astype(int)
        feat.to_csv(dump_path, index=False)
    return feat


# 品牌评论天数
def feat_brand_remark_day(start_date, end_date):
    print('brand_remark_day_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/brand_remark_day_%s_%s.csv' % (end_date.strftime('%y%m%d'),
                                                               start_date.strftime('%y%m%d'),
                                                               end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        remark = feat_remark_plus(start_date, end_date)[['brand', 'action_time']]
        remark.sort_values(['brand', 'action_time'], inplace=True)
        remark['action_time'] = remark['action_time'].values.astype('datetime64[D]')
        remark = remark.drop_duplicates(['brand', 'action_time'])
        feat = remark.groupby('brand').size().reset_index(name='brand_remark_day')
        feat = feat.astype(int)
        feat.to_csv(dump_path, index=False)
    return feat


# 品牌购物车天数
def feat_brand_cart_day(start_date, end_date):
    print('brand_cart_day_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/brand_cart_day_%s_%s.csv' % (end_date.strftime('%y%m%d'),
                                                             start_date.strftime('%y%m%d'),
                                                             end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        cart = feat_cart_plus(start_date, end_date)[['brand', 'action_time']]
        cart.sort_values(['brand', 'action_time'], inplace=True)
        cart['action_time'] = cart['action_time'].values.astype('datetime64[D]')
        cart = cart.drop_duplicates(['brand', 'action_time'])
        feat = cart.groupby('brand').size().reset_index(name='brand_cart_day')
        feat = feat.astype(int)
        feat.to_csv(dump_path, index=False)
    return feat


# TODO: (user_id,brand) pkey


# GR: 数量系列
# 用户品牌浏览量
def feat_user_brand_view_amt(start_date, end_date):
    print('user_brand_view_amt_%s_%s.csv' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/user_brand_view_amt_%s_%s.csv' % (
        end_date.strftime('%y%m%d'), start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        action = feat_view_plus(start_date, end_date)
        feat = action.groupby(['user_id', 'brand']).size().reset_index(name='user_brand_view_amt')
        feat.to_csv(dump_path, index=False)
    return feat


# 用户品牌购买量
def feat_user_brand_buy_amt(start_date, end_date):
    print('user_brand_buy_amt_%s_%s.csv' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/user_brand_buy_amt_%s_%s.csv' % (
        end_date.strftime('%y%m%d'), start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        action = feat_buy_plus(start_date, end_date)
        feat = action.groupby(['user_id', 'brand']).size().reset_index(name='user_brand_buy_amt')
        feat.to_csv(dump_path, index=False)
    return feat


# 用户品牌关注量
def feat_user_brand_follow_amt(start_date, end_date):
    print('user_brand_follow_amt_%s_%s.csv' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/user_brand_follow_amt_%s_%s.csv' % (
        end_date.strftime('%y%m%d'), start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        action = feat_follow_plus(start_date, end_date)
        feat = action.groupby(['user_id', 'brand']).size().reset_index(name='user_brand_follow_amt')
        feat.to_csv(dump_path, index=False)
    return feat


# 用户品牌评论量
def feat_user_brand_remark_amt(start_date, end_date):
    print('user_brand_remark_amt_%s_%s.csv' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/user_brand_remark_amt_%s_%s.csv' % (
        end_date.strftime('%y%m%d'), start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        action = feat_remark_plus(start_date, end_date)
        feat = action.groupby(['user_id', 'brand']).size().reset_index(name='user_brand_remark_amt')
        feat.to_csv(dump_path, index=False)
    return feat


# 用户品牌购物车量
def feat_user_brand_cart_amt(start_date, end_date):
    print('user_brand_cart_amt_%s_%s.csv' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/user_brand_cart_amt_%s_%s.csv' % (
        end_date.strftime('%y%m%d'), start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        action = feat_cart_plus(start_date, end_date)
        feat = action.groupby(['user_id', 'brand']).size().reset_index(name='user_brand_cart_amt')
        feat.to_csv(dump_path, index=False)
    return feat

# GR: 其他
# 用户品牌用户行为比例
def feat_user_brand_user_action_ratio(start_date, end_date):
    print('user_brand_user_action_ratio_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/user_brand_user_action_ratio_%s_%s.csv' % (
        end_date.strftime('%y%m%d'), start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        action = feat_action(start_date, end_date)[['user_id', 'sku_id']]
        feat = action.drop_duplicates(['user_id', 'sku_id'])
        product = pd.read_csv(product_path, na_filter=False,usecols=['sku_id','brand'])
        feat = pd.merge(feat, product, on='sku_id', how='left')

        feat = pd.merge(feat, feat_user_view_amt(start_date, end_date), on=['user_id'], how='left')
        feat = pd.merge(feat, feat_user_buy_amt(start_date, end_date), on=['user_id'], how='left')
        feat = pd.merge(feat, feat_user_follow_amt(start_date, end_date), on=['user_id'], how='left')
        feat = pd.merge(feat, feat_user_remark_amt(start_date, end_date), on=['user_id'], how='left')
        feat = pd.merge(feat, feat_user_cart_amt(start_date, end_date), on=['user_id'], how='left')

        feat = pd.merge(feat, feat_user_brand_view_amt(start_date, end_date), on=['user_id', 'brand'], how='left')
        feat = pd.merge(feat, feat_user_brand_buy_amt(start_date, end_date), on=['user_id', 'brand'], how='left')
        feat = pd.merge(feat, feat_user_brand_follow_amt(start_date, end_date), on=['user_id', 'brand'], how='left')
        feat = pd.merge(feat, feat_user_brand_remark_amt(start_date, end_date), on=['user_id', 'brand'], how='left')
        feat = pd.merge(feat, feat_user_brand_cart_amt(start_date, end_date), on=['user_id', 'brand'], how='left')
        feat.fillna(0, inplace=True)

        feat.ix[feat['user_view_amt'] == 0, 'user_view_amt'] = -1
        feat['user_brand_user_view_ratio'] = feat['user_brand_view_amt'] / (feat['user_view_amt']) * 100

        feat.ix[feat['user_buy_amt'] == 0, 'user_buy_amt'] = -1
        feat['user_brand_user_buy_ratio'] = feat['user_brand_buy_amt'] / (feat['user_buy_amt']) * 100

        feat.ix[feat['user_follow_amt'] == 0, 'user_follow_amt'] = -1
        feat['user_brand_user_follow_ratio'] = feat['user_brand_follow_amt'] / (feat['user_follow_amt']) * 100

        feat.ix[feat['user_remark_amt'] == 0, 'user_remark_amt'] = -1
        feat['user_brand_user_remark_ratio'] = feat['user_brand_remark_amt'] / (feat['user_remark_amt']) * 100

        feat.ix[feat['user_cart_amt'] == 0, 'user_cart_amt'] = -1
        feat['user_brand_user_cart_ratio'] = feat['user_brand_cart_amt'] / (feat['user_cart_amt']) * 100

        feat = feat[
            ['user_id', 'brand', 'user_brand_user_view_ratio', 'user_brand_user_buy_ratio',
             'user_brand_user_follow_ratio', 'user_brand_user_remark_ratio', 'user_brand_user_cart_ratio']]
        feat = feat.astype(int)
        feat.to_csv(dump_path, index=False)

    return feat
