# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @DATE    : 5/9/2019
# @Author  : xiaotong niu
# @File    : user_feat.py
# @Project : JData-Predict
# @Github  ：https://github.com/isNxt
# @Describ : ...
import os
import pandas as pd
from datetime import datetime
from sklearn.preprocessing import LabelEncoder

# %% 目录配置
# 时间划分
data_start_date = "2018-02-01"
data_end_date = "2018-04-15"
train_start_date = "2018-02-23"
train_end_date = "2018-04-15"
sub_start_date = "2018-04-16"
sub_end_date = "2018-04-22"
# 数据路径
clean_path = "../data/clean"
user_path = clean_path + "/user.csv"
action_path = clean_path + "/action.csv"
product_path = clean_path + "/product.csv"
shop_path = clean_path + "/shop.csv"
# 提交路径
sub_path = '../submit'
# 输出路径
out_path = './output'
# 缓存路径
cache_path = './cache'


# %% 特征提取

# TODO: (user_id,action_time) pkey
# 行为
def feat_action(start_date, end_date):
    if start_date == datetime.strptime(train_start_date, '%Y-%m-%d') \
            and end_date == datetime.strptime(train_end_date, '%Y-%m-%d'):
        feat = pd.read_csv(action_path, parse_dates=['action_time'], na_filter=False, skip_blank_lines=True)
    else:
        dump_path = cache_path + '/user_action_%s_%s.csv' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
        if os.path.exists(dump_path):
            feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
        else:
            df_action = pd.read_csv(action_path, parse_dates=['action_time'], na_filter=False, skip_blank_lines=True)
            feat = df_action[
                (start_date <= df_action['action_time']) & (df_action['action_time'] <= end_date)]
            # feat.to_csv(dump_path, index=False)
    return feat


# 浏览行为
def feat_view(start_date, end_date):
    dump_path = cache_path + '/view_%s_%s.csv' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        feat = feat_action(start_date, end_date)
        feat = feat[feat['type'] == 1]
        # feat.to_csv(dump_path, index=False)
    return feat


# 购买行为
def feat_buy(start_date, end_date):
    dump_path = cache_path + '/buy_%s_%s.csv' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        feat = feat_action(start_date, end_date)
        feat = feat[feat['type'] == 2]
        # feat.to_csv(dump_path, index=False)
    return feat


# 关注行为
def feat_follow(start_date, end_date):
    dump_path = cache_path + '/follow_%s_%s.csv' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        feat = feat_action(start_date, end_date)
        feat = feat[feat['type'] == 3]
        # feat.to_csv(dump_path, index=False)
    return feat


# 评论行为
def feat_remark(start_date, end_date):
    dump_path = cache_path + '/remark_%s_%s.csv' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        feat = feat_action(start_date, end_date)
        feat = feat[feat['type'] == 4]
    # feat.to_csv(dump_path, index=False)
    return feat


# 购物车行为
def feat_cart(start_date, end_date):
    dump_path = cache_path + '/cart_%s_%s.csv' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        feat = feat_action(start_date, end_date)
        feat = feat[feat['type'] == 5]
        # feat.to_csv(dump_path, index=False)
    return feat


# TODO: (user_id) pkey
# 用户信息
def feat_user():
    print('\tuser.csv')
    feat = pd.read_csv(user_path, na_filter=False, skip_blank_lines=True)
    return feat


# 用户是否购买
def feat_user_if_buy(start_date, end_date):
    print('\tuser_if_buy_%s_%s.csv' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/user_if_buy_%s_%s.csv' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        feat = feat_user_buy_amt(start_date, end_date)
        feat.ix[feat['user_buy_amt'] > 0, ['user_buy_amt']] = 1
        feat = feat.rename(columns={'user_buy_amt': 'user_if_buy'})
        # feat.to_csv(dump_path, index=False)
    return feat


# 用户浏览量
def feat_user_view_amt(start_date, end_date):
    print('\tuser_view_amt_%s_%s.csv' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/user_view_amt_%s_%s.csv' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        action = feat_view(start_date, end_date)
        feat = action.groupby('user_id').size().reset_index(name='user_view_amt')
        # feat.to_csv(dump_path, index=False)
    return feat


# 用户购买量
def feat_user_buy_amt(start_date, end_date):
    print('\tuser_buy_amt_%s_%s.csv' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/user_buy_amt_%s_%s.csv' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        action = feat_buy(start_date, end_date)
        feat = action.groupby('user_id').size().reset_index(name='user_buy_amt')
        # feat.to_csv(dump_path, index=False)
    return feat


# 用户关注量
def feat_user_follow_amt(start_date, end_date):
    print('\tuser_follow_amt_%s_%s.csv' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/user_follow_amt_%s_%s.csv' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        action = feat_follow(start_date, end_date)
        feat = action.groupby('user_id').size().reset_index(name='user_follow_amt')
        # feat.to_csv(dump_path, index=False)
    return feat


# 用户评论量
def feat_user_remark_amt(start_date, end_date):
    print('\tuser_remark_amt_%s_%s.csv' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/user_remark_amt_%s_%s.csv' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        action = feat_remark(start_date, end_date)
        feat = action.groupby('user_id').size().reset_index(name='user_remark_amt')
        # feat.to_csv(dump_path, index=False)
    return feat


# 用户购物车量
def feat_user_cart_amt(start_date, end_date):
    print('\tuser_cart_amt_%s_%s.csv' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/user_cart_amt_%s_%s.csv' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        action = feat_cart(start_date, end_date)
        feat = action.groupby('user_id').size().reset_index(name='user_cart_amt')
        # feat.to_csv(dump_path, index=False)
    return feat


# 用户行为转化率
def feat_user_action_ratio(start_date, end_date):
    print('\tuser_action_ratio_%s_%s.csv' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/user_action_ratio_%s_%s.csv' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
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
        class_le = LabelEncoder()
        feat['user_buy/view'] = feat['user_buy_amt'] / feat['user_view_amt']
        feat['user_buy/view'] = class_le.fit_transform(feat['user_buy/view'])
        feat['user_buy/follow'] = feat['user_buy_amt'] / feat['user_follow_amt']
        feat['user_buy/follow'] = class_le.fit_transform(feat['user_buy/follow'])
        feat['user_buy/remark'] = feat['user_buy_amt'] / feat['user_remark_amt']
        feat['user_buy/remark'] = class_le.fit_transform(feat['user_buy/remark'])
        feat['user_buy/cart'] = feat['user_buy_amt'] / feat['user_cart_amt']
        feat['user_buy/cart'] = class_le.fit_transform(feat['user_buy/cart'])
        feat = feat[['user_id', 'user_buy/view', 'user_buy/follow', 'user_buy/remark', 'user_buy/cart']]
        # feat.to_csv(dump_path, index=False)
    return feat


if __name__ == "__main__":
    end_date = datetime.strptime(train_end_date, '%Y-%m-%d')
    start_date = datetime.strptime(train_start_date, '%Y-%m-%d')
    feat_user_view_amt(start_date, end_date)
