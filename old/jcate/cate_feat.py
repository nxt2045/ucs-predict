# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @DATE    : 5/14/2019
# @Author  : xiaotong niu
# @File    : cate_feat.py
# @Project : JData-Predict
# @Github  ：https://github.com/isNxt
# @Describ : ...

from user_feat import feat_view, feat_buy, feat_cart, feat_follow, feat_remark
import os
import pandas as pd
from datetime import timedelta
from datetime import datetime

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
# 浏览行为+商品
def feat_view_plus(_start_date, _end_date):
    dump_path = cache_path + '/view_plus_%s_%s.csv' % (_start_date.strftime('%y%m%d'), _end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        feat = feat_view(_start_date, _end_date)
        product = pd.read_csv(product_path, na_filter=False)
        shop = pd.read_csv(shop_path, na_filter=False)
        feat = pd.merge(feat, product, on='sku_id', how='left')
        feat = pd.merge(feat, shop, on='shop_id', how='left')
        # feat.to_csv(dump_path, index=False)
    return feat


# 购买行为+商品
def feat_buy_plus(_start_date, _end_date):
    dump_path = cache_path + '/buy_plus_%s_%s.csv' % (_start_date.strftime('%y%m%d'), _end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        feat = feat_buy(_start_date, _end_date)
        product = pd.read_csv(product_path, na_filter=False)
        shop = pd.read_csv(shop_path, na_filter=False)
        feat = pd.merge(feat, product, on='sku_id', how='left')
        feat = pd.merge(feat, shop, on='shop_id', how='left')
        # feat.to_csv(dump_path, index=False)
    return feat


# 关注行为+商品
def feat_follow_plus(_start_date, _end_date):
    dump_path = cache_path + '/follow_plus_%s_%s.csv' % (_start_date.strftime('%y%m%d'), _end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        feat = feat_follow(_start_date, _end_date)
        product = pd.read_csv(product_path, na_filter=False)
        shop = pd.read_csv(shop_path, na_filter=False)
        feat = pd.merge(feat, product, on='sku_id', how='left')
        feat = pd.merge(feat, shop, on='shop_id', how='left')
        # feat.to_csv(dump_path, index=False)
    return feat


# 评论行为+商品
def feat_remark_plus(_start_date, _end_date):
    dump_path = cache_path + '/remark_plus_%s_%s.csv' % (_start_date.strftime('%y%m%d'), _end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        feat = feat_remark(_start_date, _end_date)
        product = pd.read_csv(product_path, na_filter=False)
        shop = pd.read_csv(shop_path, na_filter=False)
        feat = pd.merge(feat, product, on='sku_id', how='left')
        feat = pd.merge(feat, shop, on='shop_id', how='left')
        # feat.to_csv(dump_path, index=False)
    return feat


# 购物车行为+商品
def feat_cart_plus(_start_date, _end_date):
    dump_path = cache_path + '/cart_plus_%s_%s.csv' % (_start_date.strftime('%y%m%d'), _end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        feat = feat_cart(_start_date, _end_date)
        product = pd.read_csv(product_path, na_filter=False)
        shop = pd.read_csv(shop_path, na_filter=False)
        feat = pd.merge(feat, product, on='sku_id', how='left')
        feat = pd.merge(feat, shop, on='shop_id', how='left')
        # feat.to_csv(dump_path, index=False)
    return feat


# TODO: (user_id,cate) pkey

# 用户品类是否购买
def feat_user_cate_if_buy(start_date, end_date):
    print('\tuser_cate_if_buy_%s_%s.csv' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/user_cate_if_buy_%s_%s.csv' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        feat = feat_user_cate_buy_amt(start_date, end_date)
        feat.ix[feat['user_cate_buy_amt'] > 0, ['user_cate_buy_amt']] = 1
        feat.rename(columns={'user_cate_buy_amt': 'user_cate_if_buy'}, inplace=True)
        # feat.to_csv(dump_path, index=False)
    return feat


# 用户品类浏览量
def feat_user_cate_view_amt(start_date, end_date):
    print('\tuser_cate_view_amt_%s_%s.csv' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/user_cate_view_amt_%s_%s.csv' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        action = feat_view_plus(start_date, end_date)
        feat = action.groupby(['user_id', 'cate']).size().reset_index(name='user_cate_view_amt')
        # feat.to_csv(dump_path, index=False)
    return feat


# 用户品类购买量
def feat_user_cate_buy_amt(start_date, end_date):
    print('\tuser_cate_buy_amt_%s_%s.csv' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/user_cate_buy_amt_%s_%s.csv' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        action = feat_buy_plus(start_date, end_date)
        feat = action.groupby(['user_id', 'cate']).size().reset_index(name='user_cate_buy_amt')
        # feat.to_csv(dump_path, index=False)
    return feat


# 用户品类关注量
def feat_user_cate_follow_amt(start_date, end_date):
    print('\tuser_cate_follow_amt_%s_%s.csv' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/user_cate_follow_amt_%s_%s.csv' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        action = feat_follow_plus(start_date, end_date)
        feat = action.groupby(['user_id', 'cate']).size().reset_index(name='user_cate_follow_amt')
        # feat.to_csv(dump_path, index=False)
    return feat


# 用户品类评论量
def feat_user_cate_remark_amt(start_date, end_date):
    print('\tuser_cate_remark_amt_%s_%s.csv' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/user_cate_remark_amt_%s_%s.csv' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        action = feat_remark_plus(start_date, end_date)
        feat = action.groupby(['user_id', 'cate']).size().reset_index(name='user_cate_remark_amt')
        # feat.to_csv(dump_path, index=False)
    return feat


# 用户品类购物车量
def feat_user_cate_cart_amt(start_date, end_date):
    print('\tuser_cate_cart_amt_%s_%s.csv' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/user_cate_cart_amt_%s_%s.csv' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        action = feat_cart_plus(start_date, end_date)
        feat = action.groupby(['user_id', 'cate']).size().reset_index(name='user_cate_cart_amt')
        # feat.to_csv(dump_path, index=False)
    return feat


if __name__ == "__main__":
    end_date = datetime.strptime('2018-4-8', '%Y-%m-%d')
    start_date = end_date - timedelta(days=7 - 1)
    action = feat_buy_plus(start_date, end_date)
    action = action[['user_id', 'cate']]
    action = action.drop_duplicates()
    print(action)
    action = pd.concat([action, pd.DataFrame({'shop_id': [3230] * action.shape[0]})], axis=1)
    action = action.astype(int)
    action.to_csv("2.csv", index=False)
