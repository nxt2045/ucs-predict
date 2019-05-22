# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @DATE    : 5/14/2019
# @Author  : xiaotong niu
# @File    : cate_feat.py
# @Project : JData-Predict
# @Github  ：https://github.com/isNxt
# @Describ : ...

from juser.user_feat import feat_view, feat_buy, feat_cart, feat_follow, feat_remark
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


# %% 特征提取
# TODO: (user_id,action_time) pkey
# 浏览行为+商品
def feat_view_plus(start_date, end_date):
    print('view_plus_%s_%s.csv' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/view_plus_%s_%s.csv' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        feat = feat_view(start_date, end_date)
        product = pd.read_csv(product_path, na_filter=False)
        shop = pd.read_csv(shop_path, na_filter=False)
        feat = pd.merge(feat, product, on='sku_id', how='left')
        feat = pd.merge(feat, shop, on='shop_id', how='left')
        # feat.to_csv(dump_path, index=False)
    return feat


# 购买行为+商品
def feat_buy_plus(start_date, end_date):
    print('buy_plus_%s_%s.csv' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/buy_plus_%s_%s.csv' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        feat = feat_buy(start_date, end_date)
        product = pd.read_csv(product_path, na_filter=False)
        shop = pd.read_csv(shop_path, na_filter=False)
        feat = pd.merge(feat, product, on='sku_id', how='left')
        feat = pd.merge(feat, shop, on='shop_id', how='left')
        # feat.to_csv(dump_path, index=False)
    return feat


# 关注行为+商品
def feat_follow_plus(start_date, end_date):
    print('follow_plus_%s_%s.csv' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/follow_plus_%s_%s.csv' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        feat = feat_follow(start_date, end_date)
        product = pd.read_csv(product_path, na_filter=False)
        shop = pd.read_csv(shop_path, na_filter=False)
        feat = pd.merge(feat, product, on='sku_id', how='left')
        feat = pd.merge(feat, shop, on='shop_id', how='left')
        # feat.to_csv(dump_path, index=False)
    return feat


# 评论行为+商品
def feat_remark_plus(start_date, end_date):
    print('remark_plus_%s_%s.csv' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/remark_plus_%s_%s.csv' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        feat = feat_remark(start_date, end_date)
        product = pd.read_csv(product_path, na_filter=False)
        shop = pd.read_csv(shop_path, na_filter=False)
        feat = pd.merge(feat, product, on='sku_id', how='left')
        feat = pd.merge(feat, shop, on='shop_id', how='left')
        # feat.to_csv(dump_path, index=False)
    return feat


# 购物车行为+商品
def feat_cart_plus(start_date, end_date):
    print('cart_plus_%s_%s.csv' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
    dump_path = cache_path + '/cart_plus_%s_%s.csv' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        feat = feat_cart(start_date, end_date)
        product = pd.read_csv(product_path, na_filter=False)
        shop = pd.read_csv(shop_path, na_filter=False)
        feat = pd.merge(feat, product, on='sku_id', how='left')
        feat = pd.merge(feat, shop, on='shop_id', how='left')
        # feat.to_csv(dump_path, index=False)
    return feat


# TODO: (user_id,cate) pkey

# 用户品类浏览量
def feat_user_cate_view_amt(start_date, end_date):
    print('user_cate_view_amt_%s_%s.csv' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
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
    print('user_cate_buy_amt_%s_%s.csv' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
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
    print('user_cate_follow_amt_%s_%s.csv' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
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
    print('user_cate_remark_amt_%s_%s.csv' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
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
    print('user_cate_cart_amt_%s_%s.csv' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
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
