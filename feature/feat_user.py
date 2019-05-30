# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @DATE    : 4/18/2019
# @Author  : xiaotong niu
# @File    : feat_user.py
# @Project : JData-UCS
# @Github  ：https://github.com/isNxt
# @Describ : ...
import os
import pandas as pd
from datetime import datetime
from datetime import timedelta
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters

# %% 配置
# 输出设置
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)
register_matplotlib_converters()
plt.style.use('seaborn')
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
cache_path = '../cache/user'


# TODO: (user_id,action_time) pkey
# GR: 依赖系列
# 行为
def feat_action(start_date, end_date):
    print('action_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    if start_date == datetime.strptime(data_start_date, '%Y-%m-%d') \
            and end_date == datetime.strptime(data_end_date, '%Y-%m-%d'):
        feat = pd.read_csv(action_path, parse_dates=['action_time'], na_filter=False, skip_blank_lines=True)
    else:
        dump_path = cache_path + '/%s/action_%s_%s.csv' % (
            end_date.strftime('%y%m%d'), start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
        if os.path.exists(dump_path):
            feat = pd.read_csv(dump_path, parse_dates=['action_time'], na_filter=False, skip_blank_lines=True)
        else:
            action = pd.read_csv(action_path, parse_dates=['action_time'], na_filter=False, skip_blank_lines=True)
            feat = action[
                (start_date <= action['action_time']) & (action['action_time'] < end_date + timedelta(days=1))]
            feat.to_csv(dump_path, index=False)
    return feat


# 浏览行为
def feat_view(start_date, end_date):
    print('view_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/view_%s_%s.csv' % (
        end_date.strftime('%y%m%d'), start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, parse_dates=['action_time'], na_filter=False, skip_blank_lines=True)
    else:
        feat = feat_action(start_date, end_date)
        feat = feat[feat['type'] == 1]
        feat.to_csv(dump_path, index=False)
    return feat


# 购买行为
def feat_buy(start_date, end_date):
    print('buy_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/buy_%s_%s.csv' % (
        end_date.strftime('%y%m%d'), start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, parse_dates=['action_time'], na_filter=False, skip_blank_lines=True)
    else:
        feat = feat_action(start_date, end_date)
        feat = feat[feat['type'] == 2]
        feat.to_csv(dump_path, index=False)
    return feat


# 关注行为
def feat_follow(start_date, end_date):
    print('follow_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/follow_%s_%s.csv' % (
        end_date.strftime('%y%m%d'), start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, parse_dates=['action_time'], na_filter=False, skip_blank_lines=True)
    else:
        feat = feat_action(start_date, end_date)
        feat = feat[feat['type'] == 3]
        feat.to_csv(dump_path, index=False)
    return feat


# 评论行为
def feat_remark(start_date, end_date):
    print('remark_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/remark_%s_%s.csv' % (
        end_date.strftime('%y%m%d'), start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, parse_dates=['action_time'], na_filter=False, skip_blank_lines=True)
    else:
        feat = feat_action(start_date, end_date)
        feat = feat[feat['type'] == 4]
    feat.to_csv(dump_path, index=False)
    return feat


# 购物车行为
def feat_cart(start_date, end_date):
    print('cart_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/cart_%s_%s.csv' % (
        end_date.strftime('%y%m%d'), start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, parse_dates=['action_time'], na_filter=False, skip_blank_lines=True)
    else:
        feat = feat_action(start_date, end_date)
        feat = feat[feat['type'] == 5]
        feat.to_csv(dump_path, index=False)
    return feat


# TODO: (user_id) pkey
# 用户信息
def feat_user():
    print('user.csv')
    feat = pd.read_csv(user_path, na_filter=False)
    return feat


# GR: 是否系列
# 用户是否行为
def feat_user_if_action(start_date, end_date):
    print('user_if_action_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/user_if_action_%s_%s.csv' % (
        end_date.strftime('%y%m%d'), start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        feat = feat_user_action_amt(start_date, end_date)
        feat.ix[feat['user_action_amt'] > 0, 'user_action_amt'] = 1
        feat.rename(columns={'user_action_amt': 'user_if_action'}, inplace=True)
        feat = feat.astype(int)
        feat.to_csv(dump_path, index=False)
    return feat


# 用户是否浏览
def feat_user_if_view(start_date, end_date):
    print('user_if_view_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/user_if_view_%s_%s.csv' % (
        end_date.strftime('%y%m%d'), start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        feat = feat_user_view_amt(start_date, end_date)
        feat.ix[feat['user_view_amt'] > 0, 'user_view_amt'] = 1
        feat.rename(columns={'user_view_amt': 'user_if_view'}, inplace=True)
        feat = feat.astype(int)
        feat.to_csv(dump_path, index=False)
    return feat


# 用户是否购买
def feat_user_if_buy(start_date, end_date):
    print('user_if_buy_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/user_if_buy_%s_%s.csv' % (
        end_date.strftime('%y%m%d'), start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        feat = feat_user_buy_amt(start_date, end_date)
        feat.ix[feat['user_buy_amt'] > 0, 'user_buy_amt'] = 1
        feat.rename(columns={'user_buy_amt': 'user_if_buy'}, inplace=True)
        feat = feat.astype(int)
        feat.to_csv(dump_path, index=False)
    return feat


# 用户是否关注
def feat_user_if_follow(start_date, end_date):
    print('user_if_follow_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/user_if_follow_%s_%s.csv' % (
        end_date.strftime('%y%m%d'), start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        feat = feat_user_follow_amt(start_date, end_date)
        feat.ix[feat['user_follow_amt'] > 0, 'user_follow_amt'] = 1
        feat.rename(columns={'user_follow_amt': 'user_if_follow'}, inplace=True)
        feat = feat.astype(int)
        feat.to_csv(dump_path, index=False)
    return feat


# 用户是否评论
def feat_user_if_remark(start_date, end_date):
    print('user_if_remark_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/user_if_remark_%s_%s.csv' % (
        end_date.strftime('%y%m%d'), start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        feat = feat_user_remark_amt(start_date, end_date)
        feat.ix[feat['user_remark_amt'] > 0, 'user_remark_amt'] = 1
        feat.rename(columns={'user_remark_amt': 'user_if_remark'}, inplace=True)
        feat = feat.astype(int)
        feat.to_csv(dump_path, index=False)
    return feat


# 用户是否购物车
def feat_user_if_cart(start_date, end_date):
    print('user_if_cart_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/user_if_cart_%s_%s.csv' % (
        end_date.strftime('%y%m%d'), start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        feat = feat_user_cart_amt(start_date, end_date)
        feat.ix[feat['user_cart_amt'] > 0, 'user_cart_amt'] = 1
        feat.rename(columns={'user_cart_amt': 'user_if_cart'}, inplace=True)
        feat = feat.astype(int)
        feat.to_csv(dump_path, index=False)
    return feat


# GR: 数量系列
# 用户行为数量
def feat_user_action_amt(start_date, end_date):
    print('user_action_amt_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/user_action_amt_%s_%s.csv' % (
        end_date.strftime('%y%m%d'), start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        action = feat_action(start_date, end_date)
        feat = action.groupby('user_id').size().reset_index(name='user_action_amt')
        feat = feat.astype(int)
        feat.to_csv(dump_path, index=False)
    return feat


# 用户浏览数量
def feat_user_view_amt(start_date, end_date):
    print('user_view_amt_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/user_view_amt_%s_%s.csv' % (
        end_date.strftime('%y%m%d'), start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        action = feat_view(start_date, end_date)
        feat = action.groupby('user_id').size().reset_index(name='user_view_amt')
        feat = feat.astype(int)
        feat.to_csv(dump_path, index=False)
    return feat


# 用户购买数量
def feat_user_buy_amt(start_date, end_date):
    print('user_buy_amt_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/user_buy_amt_%s_%s.csv' % (
        end_date.strftime('%y%m%d'), start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        action = feat_buy(start_date, end_date)
        feat = action.groupby('user_id').size().reset_index(name='user_buy_amt')
        feat = feat.astype(int)
        feat.to_csv(dump_path, index=False)
    return feat


# 用户关注数量
def feat_user_follow_amt(start_date, end_date):
    print('user_follow_amt_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/user_follow_amt_%s_%s.csv' % (
        end_date.strftime('%y%m%d'), start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        action = feat_follow(start_date, end_date)
        feat = action.groupby('user_id').size().reset_index(name='user_follow_amt')
        feat = feat.astype(int)
        feat.to_csv(dump_path, index=False)
    return feat


# 用户评论数量
def feat_user_remark_amt(start_date, end_date):
    print('user_remark_amt_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/user_remark_amt_%s_%s.csv' % (
        end_date.strftime('%y%m%d'), start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        action = feat_remark(start_date, end_date)
        feat = action.groupby('user_id').size().reset_index(name='user_remark_amt')
        feat = feat.astype(int)
        feat.to_csv(dump_path, index=False)
    return feat


# 用户购物车数量
def feat_user_cart_amt(start_date, end_date):
    print('user_cart_amt_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/user_cart_amt_%s_%s.csv' % (
        end_date.strftime('%y%m%d'), start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        action = feat_cart(start_date, end_date)
        feat = action.groupby('user_id').size().reset_index(name='user_cart_amt')
        feat = feat.astype(int)
        feat.to_csv(dump_path, index=False)
    return feat


# GR: 天数
# 用户行为天数
def feat_user_action_day(start_date, end_date):
    print('user_action_day_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/user_action_day_%s_%s.csv' % (end_date.strftime('%y%m%d'),
                                                                start_date.strftime('%y%m%d'),
                                                                end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        action = feat_action(start_date, end_date)[['user_id', 'action_time']]
        action.sort_values(['user_id', 'action_time'], inplace=True)
        action['action_time'] = action['action_time'].values.astype('datetime64[D]')
        action = action.drop_duplicates(['user_id', 'action_time'])
        feat = action.groupby('user_id').size().reset_index(name='user_action_day')
        feat = feat.astype(int)
        feat.to_csv(dump_path, index=False)
    return feat


# 用户浏览天数
def feat_user_view_day(start_date, end_date):
    print('user_view_day_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/user_view_day_%s_%s.csv' % (end_date.strftime('%y%m%d'),
                                                              start_date.strftime('%y%m%d'),
                                                              end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        view = feat_view(start_date, end_date)[['user_id', 'action_time']]
        view.sort_values(['user_id', 'action_time'], inplace=True)
        view['action_time'] = view['action_time'].values.astype('datetime64[D]')
        view = view.drop_duplicates(['user_id', 'action_time'])
        feat = view.groupby('user_id').size().reset_index(name='user_view_day')
        feat = feat.astype(int)
        feat.to_csv(dump_path, index=False)
    return feat


# 用户购买天数
def feat_user_buy_day(start_date, end_date):
    print('user_buy_day_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/user_buy_day_%s_%s.csv' % (end_date.strftime('%y%m%d'),
                                                             start_date.strftime('%y%m%d'),
                                                             end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        buy = feat_buy(start_date, end_date)[['user_id', 'action_time']]
        buy.sort_values(['user_id', 'action_time'], inplace=True)
        buy['action_time'] = buy['action_time'].values.astype('datetime64[D]')
        buy = buy.drop_duplicates(['user_id', 'action_time'])
        feat = buy.groupby('user_id').size().reset_index(name='user_buy_day')
        feat = feat.astype(int)
        feat.to_csv(dump_path, index=False)
    return feat


# 用户关注天数
def feat_user_follow_day(start_date, end_date):
    print('user_follow_day_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/user_follow_day_%s_%s.csv' % (end_date.strftime('%y%m%d'),
                                                                start_date.strftime('%y%m%d'),
                                                                end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        follow = feat_follow(start_date, end_date)[['user_id', 'action_time']]
        follow.sort_values(['user_id', 'action_time'], inplace=True)
        follow['action_time'] = follow['action_time'].values.astype('datetime64[D]')
        follow = follow.drop_duplicates(['user_id', 'action_time'])
        feat = follow.groupby('user_id').size().reset_index(name='user_follow_day')
        feat = feat.astype(int)
        feat.to_csv(dump_path, index=False)
    return feat


# 用户评论天数
def feat_user_remark_day(start_date, end_date):
    print('user_remark_day_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/user_remark_day_%s_%s.csv' % (end_date.strftime('%y%m%d'),
                                                                start_date.strftime('%y%m%d'),
                                                                end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        remark = feat_remark(start_date, end_date)[['user_id', 'action_time']]
        remark.sort_values(['user_id', 'action_time'], inplace=True)
        remark['action_time'] = remark['action_time'].values.astype('datetime64[D]')
        remark = remark.drop_duplicates(['user_id', 'action_time'])
        feat = remark.groupby('user_id').size().reset_index(name='user_remark_day')
        feat = feat.astype(int)
        feat.to_csv(dump_path, index=False)
    return feat


# 用户购物车天数
def feat_user_cart_day(start_date, end_date):
    print('user_cart_day_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/user_cart_day_%s_%s.csv' % (end_date.strftime('%y%m%d'),
                                                              start_date.strftime('%y%m%d'),
                                                              end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        cart = feat_cart(start_date, end_date)[['user_id', 'action_time']]
        cart.sort_values(['user_id', 'action_time'], inplace=True)
        cart['action_time'] = cart['action_time'].values.astype('datetime64[D]')
        cart = cart.drop_duplicates(['user_id', 'action_time'])
        feat = cart.groupby('user_id').size().reset_index(name='user_cart_day')
        feat = feat.astype(int)
        feat.to_csv(dump_path, index=False)
    return feat


# GR: 其他
# 用户行为比例
def feat_user_action_ratio(start_date, end_date):
    print('user_action_ratio_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/user_action_ratio_%s_%s.csv' % (
        end_date.strftime('%y%m%d'), start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        feat = pd.read_csv(user_path, na_filter=False, skip_blank_lines=True, usecols=['user_id'])
        feat = pd.merge(feat, feat_user_action_amt(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_view_amt(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_buy_amt(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_follow_amt(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_remark_amt(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_cart_amt(start_date, end_date), on='user_id', how='left')
        feat.fillna(0, inplace=True)
        feat.ix[feat['user_action_amt'] == 0, 'user_action_amt'] = -1
        feat['user_view_ratio'] = feat['user_view_amt'] / (feat['user_action_amt']) * 100
        feat['user_buy_ratio'] = feat['user_buy_amt'] / (feat['user_action_amt']) * 100
        feat['user_follow_ratio'] = feat['user_follow_amt'] / (feat['user_action_amt']) * 100
        feat['user_remark_ratio'] = feat['user_remark_amt'] / (feat['user_action_amt']) * 100
        feat['user_cart_ratio'] = feat['user_cart_amt'] / (feat['user_action_amt']) * 100
        feat = feat[['user_id', 'user_view_ratio', 'user_buy_ratio', 'user_follow_ratio', 'user_remark_ratio',
                     'user_cart_ratio']]
        feat = feat.astype(int)
        feat.to_csv(dump_path, index=False)

    return feat


# 用户购买转换率
def feat_user_buy_rate(start_date, end_date):
    print('user_buy_rate_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/user_buy_rate_%s_%s.csv' % (
        end_date.strftime('%y%m%d'), start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        feat = pd.read_csv(user_path, na_filter=False, skip_blank_lines=True, usecols=['user_id'])
        feat = pd.merge(feat, feat_user_view_amt(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_buy_amt(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_follow_amt(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_remark_amt(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_cart_amt(start_date, end_date), on='user_id', how='left')
        feat.fillna(0, inplace=True)
        feat.ix[feat['user_follow_amt'] == 0, 'user_follow_amt'] = -1
        feat['user_buy/follow'] = feat['user_buy_amt'] / (feat['user_follow_amt']) * 100
        feat.ix[feat['user_remark_amt'] == 0, 'user_remark_amt'] = -1
        feat['user_buy/remark'] = feat['user_buy_amt'] / (feat['user_remark_amt']) * 100
        feat.ix[feat['user_cart_amt'] == 0, 'user_cart_amt'] = -1
        feat['user_buy/cart'] = feat['user_buy_amt'] / (feat['user_cart_amt']) * 100
        feat.ix[feat['user_view_amt'] == 0, 'user_view_amt'] = -1
        feat['user_buy/view'] = feat['user_buy_amt'] / (feat['user_view_amt']) * 100
        feat = feat[['user_id', 'user_buy/view', 'user_buy/follow', 'user_buy/remark', 'user_buy/cart']]
        feat = feat.astype(int)
        feat.to_csv(dump_path, index=False)

    return feat


# 用户最早行为时差(小时)
def feat_user_first_hour(start_date, end_date):
    print('user_first_hour_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/user_first_hour_%s_%s.csv' % (end_date.strftime('%y%m%d'),
                                                                start_date.strftime('%y%m%d'),
                                                                end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        action = feat_action(start_date, end_date)[['user_id', 'action_time']]
        action.sort_values(['user_id', 'action_time'], inplace=True)
        feat = action.groupby('user_id').max().reset_index()
        feat['user_first_hour'] = [((end_date - i).total_seconds()) // 3600 for i in feat['action_time']]
        feat.drop('action_time', axis=1, inplace=True)
        feat = feat.astype(int)
        feat.to_csv(dump_path, index=False)
    return feat


# 用户最晚行为时差(小时)
def feat_user_last_hour(start_date, end_date):
    print('user_last_hour_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/user_last_hour_%s_%s.csv' % (end_date.strftime('%y%m%d'),
                                                               start_date.strftime('%y%m%d'),
                                                               end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        action = feat_action(start_date, end_date)[['user_id', 'action_time']]
        action.sort_values(['user_id', 'action_time'], inplace=True)
        feat = action.groupby('user_id').min().reset_index()
        feat['user_last_hour'] = [((end_date - i).total_seconds()) // 3600 for i in feat['action_time']]
        feat.drop('action_time', axis=1, inplace=True)
        feat = feat.astype(int)
        feat.to_csv(dump_path, index=False)
    return feat


# 用户最晚行为次数(天)
def feat_user_last_amt(start_date, end_date):
    print('user_last_amt_%s_%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/%s/user_last_amt_%s_%s.csv' % (end_date.strftime('%y%m%d'),
                                                              start_date.strftime('%y%m%d'),
                                                              end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        action = feat_action(start_date, end_date)[['user_id', 'action_time']]
        action.sort_values(['user_id', 'action_time'], inplace=True)
        action['action_time'] = action['action_time'].values.astype('datetime64[D]')
        sub_action = action.groupby('user_id').first().reset_index()
        action = pd.merge(sub_action, action, on=['user_id', 'action_time'], how='left')
        feat = action.groupby('user_id').size().reset_index(name='user_last_amt')
        feat = feat.astype(int)
        feat.to_csv(dump_path, index=False)
    return feat


if __name__ == "__main__":
    end_date = datetime.strptime(train_end_date, '%Y-%m-%d')
    start_date = datetime.strptime(train_start_date, '%Y-%m-%d')
