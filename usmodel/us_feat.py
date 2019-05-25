# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @DATE    : 5/14/2019
# @Author  : xiaotong niu
# @File    : cate_feat.py
# @Project : JData-Predict
# @Github  ：https://github.com/isNxt
# @Describ : ...

from u_feat import *
from s_feat import *
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
submit_path = '../submit'
cache_path = '../cache/us'


# %% 特征提取
# TODO: (user_id,sku_id) pkey


# GR: 是否系列
# 用户商品是否行为
def feat_user_sku_if_action(start_date, end_date):
    print('user_sku_if_action_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/user_sku_if_action_%s_%s.csv' % (
        end_date.strftime('%y%m%d'), start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        feat = feat_user_sku_action_amt(start_date, end_date)
        feat.ix[feat['user_sku_action_amt'] > 0, 'user_sku_action_amt'] = 1
        feat.rename(columns={'user_sku_action_amt': 'user_sku_if_action'}, inplace=True)
        feat = feat.astype(int)
        feat.to_csv(dump_path, index=False)
    return feat


# 用户商品是否浏览
def feat_user_sku_if_view(start_date, end_date):
    print('user_sku_if_view_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/user_sku_if_view_%s_%s.csv' % (
        end_date.strftime('%y%m%d'), start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        feat = feat_user_sku_view_amt(start_date, end_date)
        feat.ix[feat['user_sku_view_amt'] > 0, 'user_sku_view_amt'] = 1
        feat.rename(columns={'user_sku_view_amt': 'user_sku_if_view'}, inplace=True)
        feat = feat.astype(int)
        feat.to_csv(dump_path, index=False)
    return feat


# 用户商品是否购买
def feat_user_sku_if_buy(start_date, end_date):
    print('user_sku_if_buy_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/user_sku_if_buy_%s_%s.csv' % (
        end_date.strftime('%y%m%d'), start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        feat = feat_user_sku_buy_amt(start_date, end_date)
        feat.ix[feat['user_sku_buy_amt'] > 0, 'user_sku_buy_amt'] = 1
        feat.rename(columns={'user_sku_buy_amt': 'user_sku_if_buy'}, inplace=True)
        feat = feat.astype(int)
        feat.to_csv(dump_path, index=False)
    return feat


# 用户商品是否关注
def feat_user_sku_if_follow(start_date, end_date):
    print('user_sku_if_follow_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/user_sku_if_follow_%s_%s.csv' % (
        end_date.strftime('%y%m%d'), start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        feat = feat_user_sku_follow_amt(start_date, end_date)
        feat.ix[feat['user_sku_follow_amt'] > 0, 'user_sku_follow_amt'] = 1
        feat.rename(columns={'user_sku_follow_amt': 'user_sku_if_follow'}, inplace=True)
        feat = feat.astype(int)
        feat.to_csv(dump_path, index=False)
    return feat


# 用户商品是否评论
def feat_user_sku_if_remark(start_date, end_date):
    print('user_sku_if_remark_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/user_sku_if_remark_%s_%s.csv' % (
        end_date.strftime('%y%m%d'), start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        feat = feat_user_sku_remark_amt(start_date, end_date)
        feat.ix[feat['user_sku_remark_amt'] > 0, 'user_sku_remark_amt'] = 1
        feat.rename(columns={'user_sku_remark_amt': 'user_sku_if_remark'}, inplace=True)
        feat = feat.astype(int)
        feat.to_csv(dump_path, index=False)
    return feat


# 用户商品是否购物车
def feat_user_sku_if_cart(start_date, end_date):
    print('user_sku_if_cart_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/user_sku_if_cart_%s_%s.csv' % (
        end_date.strftime('%y%m%d'), start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        feat = feat_user_sku_cart_amt(start_date, end_date)
        feat.ix[feat['user_sku_cart_amt'] > 0, 'user_sku_cart_amt'] = 1
        feat.rename(columns={'user_sku_cart_amt': 'user_sku_if_cart'}, inplace=True)
        feat = feat.astype(int)
        feat.to_csv(dump_path, index=False)
    return feat


# GR: 数量系列
# 用户商品行为数量
def feat_user_sku_action_amt(start_date, end_date):
    print('user_sku_action_amt_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/user_sku_action_amt_%s_%s.csv' % (
        end_date.strftime('%y%m%d'), start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        action = feat_action(start_date, end_date)
        feat = action.groupby(['user_id', 'sku_id']).size().reset_index(name='user_sku_action_amt')
        feat = feat.astype(int)
        feat.to_csv(dump_path, index=False)
    return feat


# 用户商品浏览数量
def feat_user_sku_view_amt(start_date, end_date):
    print('user_sku_view_amt_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/user_sku_view_amt_%s_%s.csv' % (
        end_date.strftime('%y%m%d'), start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        action = feat_view(start_date, end_date)
        feat = action.groupby(['user_id', 'sku_id']).size().reset_index(name='user_sku_view_amt')
        feat = feat.astype(int)
        feat.to_csv(dump_path, index=False)
    return feat


# 用户商品购买数量
def feat_user_sku_buy_amt(start_date, end_date):
    print('user_sku_buy_amt_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/user_sku_buy_amt_%s_%s.csv' % (
        end_date.strftime('%y%m%d'), start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        action = feat_buy(start_date, end_date)
        feat = action.groupby(['user_id', 'sku_id']).size().reset_index(name='user_sku_buy_amt')
        feat = feat.astype(int)
        feat.to_csv(dump_path, index=False)
    return feat


# 用户商品关注数量
def feat_user_sku_follow_amt(start_date, end_date):
    print('user_sku_follow_amt_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/user_sku_follow_amt_%s_%s.csv' % (
        end_date.strftime('%y%m%d'), start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        action = feat_follow(start_date, end_date)
        feat = action.groupby(['user_id', 'sku_id']).size().reset_index(name='user_sku_follow_amt')
        feat = feat.astype(int)
        feat.to_csv(dump_path, index=False)
    return feat


# 用户商品评论数量
def feat_user_sku_remark_amt(start_date, end_date):
    print('user_sku_remark_amt_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/user_sku_remark_amt_%s_%s.csv' % (
        end_date.strftime('%y%m%d'), start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        action = feat_remark(start_date, end_date)
        feat = action.groupby(['user_id', 'sku_id']).size().reset_index(name='user_sku_remark_amt')
        feat = feat.astype(int)
        feat.to_csv(dump_path, index=False)
    return feat


# 用户商品购物车数量
def feat_user_sku_cart_amt(start_date, end_date):
    print('user_sku_cart_amt_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/user_sku_cart_amt_%s_%s.csv' % (
        end_date.strftime('%y%m%d'), start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        action = feat_cart(start_date, end_date)
        feat = action.groupby(['user_id', 'sku_id']).size().reset_index(name='user_sku_cart_amt')
        feat = feat.astype(int)
        feat.to_csv(dump_path, index=False)
    return feat


# GR: 其他
# 用户商品行为比例
def feat_user_sku_action_ratio(start_date, end_date):
    print('user_sku_action_ratio_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/user_sku_action_ratio_%s_%s.csv' % (
        end_date.strftime('%y%m%d'), start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        action = feat_action(start_date, end_date)[['user_id', 'sku_id']]
        feat = action.drop_duplicates(['user_id', 'sku_id'])
        feat = pd.merge(feat, feat_user_sku_action_amt(start_date, end_date), on=['user_id', 'sku_id'], how='left')
        feat = pd.merge(feat, feat_user_sku_view_amt(start_date, end_date), on=['user_id', 'sku_id'], how='left')
        feat = pd.merge(feat, feat_user_sku_buy_amt(start_date, end_date), on=['user_id', 'sku_id'], how='left')
        feat = pd.merge(feat, feat_user_sku_follow_amt(start_date, end_date), on=['user_id', 'sku_id'], how='left')
        feat = pd.merge(feat, feat_user_sku_remark_amt(start_date, end_date), on=['user_id', 'sku_id'], how='left')
        feat = pd.merge(feat, feat_user_sku_cart_amt(start_date, end_date), on=['user_id', 'sku_id'], how='left')
        feat.fillna(0, inplace=True)
        feat.ix[feat['user_sku_action_amt'] == 0, 'user_sku_action_amt'] = -1
        feat['user_sku_view_ratio'] = feat['user_sku_view_amt'] / (feat['user_sku_action_amt']) * 100
        feat['user_sku_buy_ratio'] = feat['user_sku_buy_amt'] / (feat['user_sku_action_amt']) * 100
        feat['user_sku_follow_ratio'] = feat['user_sku_follow_amt'] / (feat['user_sku_action_amt']) * 100
        feat['user_sku_remark_ratio'] = feat['user_sku_remark_amt'] / (feat['user_sku_action_amt']) * 100
        feat['user_sku_cart_ratio'] = feat['user_sku_cart_amt'] / (feat['user_sku_action_amt']) * 100
        feat = feat[
            ['user_id', 'sku_id', 'user_sku_view_ratio', 'user_sku_buy_ratio', 'user_sku_follow_ratio',
             'user_sku_remark_ratio',
             'user_sku_cart_ratio']]
        feat = feat.astype(int)
        feat.to_csv(dump_path, index=False)

    return feat


# 用户商品用户行为比例
def feat_user_sku_user_action_ratio(start_date, end_date):
    print('user_sku_user_action_ratio_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/user_sku_user_action_ratio_%s_%s.csv' % (
        end_date.strftime('%y%m%d'), start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        action = feat_action(start_date, end_date)[['user_id', 'sku_id']]
        feat = action.drop_duplicates(['user_id', 'sku_id'])

        feat = pd.merge(feat, feat_user_action_amt(start_date, end_date), on=['user_id'], how='left')
        feat = pd.merge(feat, feat_user_view_amt(start_date, end_date), on=['user_id'], how='left')
        feat = pd.merge(feat, feat_user_buy_amt(start_date, end_date), on=['user_id'], how='left')
        feat = pd.merge(feat, feat_user_follow_amt(start_date, end_date), on=['user_id'], how='left')
        feat = pd.merge(feat, feat_user_remark_amt(start_date, end_date), on=['user_id'], how='left')
        feat = pd.merge(feat, feat_user_cart_amt(start_date, end_date), on=['user_id'], how='left')

        feat = pd.merge(feat, feat_user_sku_action_amt(start_date, end_date), on=['user_id', 'sku_id'], how='left')
        feat = pd.merge(feat, feat_user_sku_view_amt(start_date, end_date), on=['user_id', 'sku_id'], how='left')
        feat = pd.merge(feat, feat_user_sku_buy_amt(start_date, end_date), on=['user_id', 'sku_id'], how='left')
        feat = pd.merge(feat, feat_user_sku_follow_amt(start_date, end_date), on=['user_id', 'sku_id'], how='left')
        feat = pd.merge(feat, feat_user_sku_remark_amt(start_date, end_date), on=['user_id', 'sku_id'], how='left')
        feat = pd.merge(feat, feat_user_sku_cart_amt(start_date, end_date), on=['user_id', 'sku_id'], how='left')
        feat.fillna(0, inplace=True)

        feat.ix[feat['user_action_amt'] == 0, 'user_action_amt'] = -1
        feat['user_sku_user_action_ratio'] = feat['user_sku_action_amt'] / (feat['user_action_amt']) * 100

        feat.ix[feat['user_view_amt'] == 0, 'user_view_amt'] = -1
        feat['user_sku_user_view_ratio'] = feat['user_sku_view_amt'] / (feat['user_view_amt']) * 100

        feat.ix[feat['user_buy_amt'] == 0, 'user_buy_amt'] = -1
        feat['user_sku_user_buy_ratio'] = feat['user_sku_buy_amt'] / (feat['user_buy_amt']) * 100

        feat.ix[feat['user_follow_amt'] == 0, 'user_follow_amt'] = -1
        feat['user_sku_user_follow_ratio'] = feat['user_sku_follow_amt'] / (feat['user_follow_amt']) * 100

        feat.ix[feat['user_remark_amt'] == 0, 'user_remark_amt'] = -1
        feat['user_sku_user_remark_ratio'] = feat['user_sku_remark_amt'] / (feat['user_remark_amt']) * 100

        feat.ix[feat['user_cart_amt'] == 0, 'user_cart_amt'] = -1
        feat['user_sku_user_cart_ratio'] = feat['user_sku_cart_amt'] / (feat['user_cart_amt']) * 100

        feat = feat[
            ['user_id', 'sku_id', 'user_sku_user_action_ratio', 'user_sku_user_view_ratio', 'user_sku_user_buy_ratio',
             'user_sku_user_follow_ratio', 'user_sku_user_remark_ratio', 'user_sku_user_cart_ratio']]
        feat = feat.astype(int)
        feat.to_csv(dump_path, index=False)

    return feat


# 用户商品最早行为时差(小时)
def feat_user_sku_first_hour(start_date, end_date):
    print('user_sku_first_hour_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/user_sku_first_hour_%s_%s.csv' % (end_date.strftime('%y%m%d'),
                                                                    start_date.strftime('%y%m%d'),
                                                                    end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        action = feat_action(start_date, end_date)[['user_id', 'sku_id', 'action_time']]
        action.sort_values(['user_id', 'sku_id', 'action_time'], inplace=True)
        feat = action.groupby(['user_id', 'sku_id']).max().reset_index()
        feat['user_sku_first_hour'] = [((end_date - i).total_seconds()) // 3600 for i in feat['action_time']]
        feat.drop('action_time', axis=1, inplace=True)
        feat = feat.astype(int)
        feat.to_csv(dump_path, index=False)
    return feat


# 用户商品最晚行为时差(小时)
def feat_user_sku_last_hour(start_date, end_date):
    print('user_sku_last_hour_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/user_sku_last_hour_%s_%s.csv' % (end_date.strftime('%y%m%d'),
                                                                   start_date.strftime('%y%m%d'),
                                                                   end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        action = feat_action(start_date, end_date)[['user_id', 'sku_id', 'action_time']]
        action.sort_values(['user_id', 'sku_id', 'action_time'], inplace=True)
        feat = action.groupby(['user_id', 'sku_id']).min().reset_index()
        feat['user_sku_last_hour'] = [((end_date - i).total_seconds()) // 3600 for i in feat['action_time']]
        feat.drop('action_time', axis=1, inplace=True)
        feat = feat.astype(int)
        feat.to_csv(dump_path, index=False)
    return feat


# 用户商品最晚行为次数(天)
def feat_user_sku_last_amt(start_date, end_date):
    print('user_sku_last_amt_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/user_sku_last_amt_%s_%s.csv' % (end_date.strftime('%y%m%d'),
                                                                  start_date.strftime('%y%m%d'),
                                                                  end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        action = feat_action(start_date, end_date)[['user_id', 'sku_id', 'action_time']]
        action.sort_values(['user_id', 'sku_id', 'action_time'], inplace=True)
        action['action_time'] = action['action_time'].values.astype('datetime64[D]')
        sub_action = action.groupby(['user_id', 'sku_id']).first().reset_index()
        action = pd.merge(sub_action, action, on=['user_id', 'sku_id', 'action_time'], how='left')
        feat = action.groupby(['user_id', 'sku_id']).size().reset_index(name='user_sku_last_amt')
        feat = feat.astype(int)
        feat.to_csv(dump_path, index=False)
    return feat


# GR: 天数
# 用户商品行为天数
def feat_user_sku_action_day(start_date, end_date):
    print('user_sku_action_day_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/user_sku_action_day_%s_%s.csv' % (end_date.strftime('%y%m%d'),
                                                                    start_date.strftime('%y%m%d'),
                                                                    end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        action = feat_action(start_date, end_date)[['user_id', 'sku_id', 'action_time']]
        action.sort_values(['user_id', 'sku_id', 'action_time'], inplace=True)
        action['action_time'] = action['action_time'].values.astype('datetime64[D]')
        action = action.drop_duplicates(['user_id', 'sku_id', 'action_time'])
        feat = action.groupby(['user_id', 'sku_id']).size().reset_index(name='user_sku_action_day')
        feat = feat.astype(int)
        feat.to_csv(dump_path, index=False)
    return feat


# 用户商品浏览天数
def feat_user_sku_view_day(start_date, end_date):
    print('user_sku_view_day_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/user_sku_view_day_%s_%s.csv' % (end_date.strftime('%y%m%d'),
                                                                  start_date.strftime('%y%m%d'),
                                                                  end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        view = feat_view(start_date, end_date)[['user_id', 'sku_id', 'action_time']]
        view.sort_values(['user_id', 'sku_id', 'action_time'], inplace=True)
        view['action_time'] = view['action_time'].values.astype('datetime64[D]')
        view = view.drop_duplicates(['user_id', 'sku_id', 'action_time'])
        feat = view.groupby(['user_id', 'sku_id']).size().reset_index(name='user_sku_view_day')
        feat = feat.astype(int)
        feat.to_csv(dump_path, index=False)
    return feat


# 用户商品购买天数
def feat_user_sku_buy_day(start_date, end_date):
    print('user_sku_buy_day_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/user_sku_buy_day_%s_%s.csv' % (end_date.strftime('%y%m%d'),
                                                                 start_date.strftime('%y%m%d'),
                                                                 end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        buy = feat_buy(start_date, end_date)[['user_id', 'sku_id', 'action_time']]
        buy.sort_values(['user_id', 'sku_id', 'action_time'], inplace=True)
        buy['action_time'] = buy['action_time'].values.astype('datetime64[D]')
        buy = buy.drop_duplicates(['user_id', 'sku_id', 'action_time'])
        feat = buy.groupby(['user_id', 'sku_id']).size().reset_index(name='user_sku_buy_day')
        feat = feat.astype(int)
        feat.to_csv(dump_path, index=False)
    return feat


# 用户商品关注天数
def feat_user_sku_follow_day(start_date, end_date):
    print('user_sku_follow_day_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/user_sku_follow_day_%s_%s.csv' % (end_date.strftime('%y%m%d'),
                                                                    start_date.strftime('%y%m%d'),
                                                                    end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        follow = feat_follow(start_date, end_date)[['user_id', 'sku_id', 'action_time']]
        follow.sort_values(['user_id', 'sku_id', 'action_time'], inplace=True)
        follow['action_time'] = follow['action_time'].values.astype('datetime64[D]')
        follow = follow.drop_duplicates(['user_id', 'sku_id', 'action_time'])
        feat = follow.groupby(['user_id', 'sku_id']).size().reset_index(name='user_sku_follow_day')
        feat = feat.astype(int)
        feat.to_csv(dump_path, index=False)
    return feat


# 用户商品评论天数
def feat_user_sku_remark_day(start_date, end_date):
    print('user_sku_remark_day_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/user_sku_remark_day_%s_%s.csv' % (end_date.strftime('%y%m%d'),
                                                                    start_date.strftime('%y%m%d'),
                                                                    end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        remark = feat_remark(start_date, end_date)[['user_id', 'sku_id', 'action_time']]
        remark.sort_values(['user_id', 'sku_id', 'action_time'], inplace=True)
        remark['action_time'] = remark['action_time'].values.astype('datetime64[D]')
        remark = remark.drop_duplicates(['user_id', 'sku_id', 'action_time'])
        feat = remark.groupby(['user_id', 'sku_id']).size().reset_index(name='user_sku_remark_day')
        feat = feat.astype(int)
        feat.to_csv(dump_path, index=False)
    return feat


# 用户商品购物车天数
def feat_user_sku_cart_day(start_date, end_date):
    print('user_sku_cart_day_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/user_sku_cart_day_%s_%s.csv' % (end_date.strftime('%y%m%d'),
                                                                  start_date.strftime('%y%m%d'),
                                                                  end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        cart = feat_cart(start_date, end_date)[['user_id', 'sku_id', 'action_time']]
        cart.sort_values(['user_id', 'sku_id', 'action_time'], inplace=True)
        cart['action_time'] = cart['action_time'].values.astype('datetime64[D]')
        cart = cart.drop_duplicates(['user_id', 'sku_id', 'action_time'])
        feat = cart.groupby(['user_id', 'sku_id']).size().reset_index(name='user_sku_cart_day')
        feat = feat.astype(int)
        feat.to_csv(dump_path, index=False)
    return feat
