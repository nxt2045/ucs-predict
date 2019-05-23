# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @DATE    : 5/14/2019
# @Author  : xiaotong niu
# @File    : merg_user.py
# @Project : JData-Predict
# @Github  ：https://github.com/isNxt
# @Describ : ...

import time
import logging
from datetime import timedelta
from datetime import datetime
from user_feat import *
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters

# %% 配置
# 输出设置

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)
register_matplotlib_converters()
plt.style.use('seaborn')
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


# %% 特征融合
def gen_feat(end_date, time_gap, mark):
    """
    遍历获取每个结束时间对应的特征
    并拼接
    """
    print(datetime.now())
    print('>> 开始生成特征X,y')
    print('end_date', end_date)
    end_date = datetime.strptime(end_date, '%Y-%m-%d')
    dump_path = cache_path + '/feat_user_%s.csv' % (end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path)
    else:
        feat = extract_feat(end_date, time_gap, mark)
        # feat.to_csv(dump_path, index=False)
    # print("feat", feat.shape)
    # print("cols", feat.columns)
    # print("head")
    # print(feat.head())
    # print("tail")
    # print(feat.tail())
    print('生成特征%s' % (str(feat.shape)))
    return feat


def extract_feat(end_date, time_gap, mark):
    """生成某一结束时间对应的特征
    1. user信息
    2. action对应信息
    """
    # 添加label
    label = get_label(end_date, mark)
    pkey = label.drop('label', axis=1)
    feat_concat = [label]
    for gap in time_gap:
        print(datetime.now())
        print('> 开始生成特征 gap=%s' % (str(gap)))
        start_date = end_date - timedelta(days=gap - 1)
        # 初始化feat
        feat = pkey
        # user
        feat = pd.merge(feat, feat_user_view_amt(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_buy_amt(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_follow_amt(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_remark_amt(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_cart_amt(start_date, end_date), on='user_id', how='left')
        # 最后调整
        feat.drop(['user_id'], axis=1, inplace=True)
        feat.fillna(0, inplace=True)
        feat = feat.astype(int)
        feat = feat.add_prefix(str(gap) + '_')  # 列名加上gap标签前缀
        print(feat.head())
        feat_concat.append(feat)
    feat = pd.concat(feat_concat, axis=1)
    # TODO 开始：与time_gap无关的feat
    print(datetime.now())
    print('> 生成全局特征')
    start_date = end_date - timedelta(30 - 1)
    # user
    feat = pd.merge(feat, feat_user(), on='user_id', how='left')
    feat = pd.merge(feat, feat_user_view_amt(start_date, end_date), on='user_id', how='left')
    feat = pd.merge(feat, feat_user_buy_amt(start_date, end_date), on='user_id', how='left')
    feat = pd.merge(feat, feat_user_follow_amt(start_date, end_date), on='user_id', how='left')
    feat = pd.merge(feat, feat_user_remark_amt(start_date, end_date), on='user_id', how='left')
    feat = pd.merge(feat, feat_user_cart_amt(start_date, end_date), on='user_id', how='left')
    feat.fillna(0, inplace=True)
    feat = feat.astype(int)
    feat = pd.merge(feat, feat_user_action_ratio(start_date, end_date), on='user_id', how='left')
    print(feat.head())
    # TODO 结束：与time_gap无关的feat
    return feat


def get_label(end_date, mark):
    """生成某一结束时间对应的特征label
    label：预测label,提交集=-1
    """
    print(datetime.now())
    print('> 开始生成标签')
    if mark == 'submit':
        label = pd.read_csv(clean_path + '/user.csv', na_filter=False, usecols=['user_id'])
    else:
        # 可能购买
        pkey = pd.read_csv(clean_path + '/user.csv', na_filter=False, usecols=['user_id'])
        # 真实购买
        user_buy_amt = feat_user_buy_amt(end_date + timedelta(days=1), end_date + timedelta(days=7))
        user_buy = user_buy_amt[user_buy_amt['user_buy_amt'] > 0]
        label_1 = pd.concat([user_buy['user_id'], pd.DataFrame({'label': [1] * user_buy.shape[0]})], axis=1)
        label = pd.merge(pkey, label_1, on=['user_id'], how='left')
        print('真实购买', user_buy.shape)
    # 最后调整
    label.fillna(0, inplace=True)
    label = label.astype('int')
    print("shape", label.shape)
    print("cols", label.columns)
    print("head")
    print(label.head())
    print("tail")
    print(label.tail())
    return label



