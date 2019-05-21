# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @DATE    : 5/14/2019
# @Author  : xiaotong niu
# @File    : merg_uc.py
# @Project : JData-Predict
# @Github  ：https://github.com/isNxt
# @Describ : ...

import os, time, sys, shutil
import numpy as np
import pandas as pd
from datetime import datetime
from datetime import timedelta
from cate_feat import *
from user_feat import feat_user

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


# %% 特征融合
def gen_feat(end_date_set, time_gap, mark):
    """
    遍历获取每个结束时间对应的特征
    并拼接
    """
    time_0 = time.clock()
    feat_concat = []
    for end_date in end_date_set:
        print('> end_date', end_date)
        end_date = datetime.strptime(end_date, '%Y-%m-%d')
        dump_path = cache_path + '/jcate_feat_%s.csv' % (end_date.strftime('%y%m%d'))
        if os.path.exists(dump_path):
            feat = pd.read_csv(dump_path)
            feat_concat.append(feat)
            print("\tfeat", feat.shape)
            print("\tcols", feat.columns)
            print("\thead", feat.head())
            print("\ttail", feat.tail())
            print('\t加载特征%s，用时%ss' % (str(feat.shape), str(time.clock() - time_0)))
        else:
            feat = extract_feat(end_date, time_gap, mark)
            feat_concat.append(feat)
            print("\tfeat", feat.shape)
            print("\tcols", feat.columns)
            print("\thead", feat.head())
            print("\ttail", feat.tail())
            print('\t生成特征%s，用时%ss' % (str(feat.shape), str(time.clock() - time_0)))
            if mark != 'submit':
                feat.to_csv(dump_path, index=False)
    feat = pd.concat(feat_concat, axis=0, sort=False)
    return feat


def extract_feat(end_date, time_gap, mark):
    """生成某一结束时间对应的特征
    1. user信息
    2. action对应信息
    """
    # 添加label
    recovr_subset()
    label = get_label(end_date, mark)
    gen_subset(label)
    pkey = label.drop('label', axis=1)
    feat_concat = [label]
    for gap in time_gap:
        print('gap', gap)
        start_date = end_date - timedelta(days=gap - 1)
        # 初始化feat
        feat = pkey
        # TODO 开始：与time_gap相关的feat
        feat = pd.merge(feat, feat_user_cate_if_buy(start_date, end_date), on=['user_id', 'cate'], how='left')
        feat = pd.merge(feat, feat_user_cate_view_amt(start_date, end_date), on=['user_id', 'cate'], how='left')
        feat = pd.merge(feat, feat_user_cate_buy_amt(start_date, end_date), on=['user_id', 'cate'], how='left')
        feat = pd.merge(feat, feat_user_cate_follow_amt(start_date, end_date), on=['user_id', 'cate'], how='left')
        feat = pd.merge(feat, feat_user_cate_remark_amt(start_date, end_date), on=['user_id', 'cate'], how='left')
        feat = pd.merge(feat, feat_user_cate_cart_amt(start_date, end_date), on=['user_id', 'cate'], how='left')
        # TODO 结束：与time_gap相关的feat
        # 最后调整
        feat = feat.drop(['user_id', 'cate'], axis=1)
        feat = feat.add_prefix(str(gap) + '_')  # 列名加上gap标签前缀
        feat_concat.append(feat)
    feat = pd.concat(feat_concat, axis=1)
    # TODO 开始：与time_gap无关的feat
    print('global')
    gl_start_date = datetime.strptime(train_start_date, '%Y-%m-%d')
    gl_end_date = datetime.strptime(train_end_date, '%Y-%m-%d')
    feat = pd.merge(feat, feat_user(), on='user_id', how='left')
    feat = pd.merge(feat, feat_user_cate_view_amt(gl_start_date, gl_end_date), on=['user_id', 'cate'], how='left')
    feat = pd.merge(feat, feat_user_cate_buy_amt(gl_start_date, gl_end_date), on=['user_id', 'cate'], how='left')
    feat = pd.merge(feat, feat_user_cate_follow_amt(gl_start_date, gl_end_date), on=['user_id', 'cate'], how='left')
    feat = pd.merge(feat, feat_user_cate_remark_amt(gl_start_date, gl_end_date), on=['user_id', 'cate'], how='left')
    feat = pd.merge(feat, feat_user_cate_cart_amt(gl_start_date, gl_end_date), on=['user_id', 'cate'], how='left')
    feat.fillna(0, inplace=True)
    feat = feat.astype(int)
    recovr_subset()
    # TODO 结束：与time_gap无关的feat
    return feat


def get_label(end_date, mark):
    """生成某一结束时间对应的特征label
    label：预测label,提交集=-1
    """
    print('label')
    _time_0 = time.clock()
    dump_path = cache_path + '/label_%s.csv' % (end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        label = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        # label：预测label,提交集=-1
        if mark == 'submit':
            buy_user = pd.read_csv(sub_path + "/user.csv", na_filter=False, skip_blank_lines=True, usecols=['user_id'])
            # 可能购买(每个用户可能购买所有类别)
            cate = pd.DataFrame({'cate': list(range(1, 82)), 'key': [1] * 81})
            list_user = buy_user['user_id'].values
            user_cate = pd.merge(pd.DataFrame({'user_id': list_user, 'key': [1] * len(list_user)}), cate, how='left',
                                 on='key')
            user_cate = user_cate.drop_duplicates()
            user_cate = user_cate.drop(['key'], axis=1)
            print('\t可能购买', user_cate.shape)
            pkey = user_cate
            # 添加标签
            label = pd.concat([pkey.reset_index(), pd.DataFrame({'label': [-1] * pkey.shape[0]})], axis=1)
            label = label.drop(['index'], axis=1)
            label['label'] = label['label'].astype('int')
            label = label.sort_values('user_id')
        else:
            pred_end_date = end_date + timedelta(days=7)
            pred_start_date = end_date + timedelta(days=1)
            # 真实购买
            buy_plus = feat_buy_plus(pred_start_date, pred_end_date)
            buy_user_cate = buy_plus[['user_id', 'cate']]
            buy_user_cate = buy_user_cate.drop_duplicates()
            print('\t真实购买', buy_user_cate.shape)
            buy_user = buy_user_cate[['user_id']]
            buy_user = buy_user.drop_duplicates()
            # 可能购买(每个用户可能购买所有类别)
            cate = pd.DataFrame({'cate': list(range(1, 82)), 'key': [1] * 81})
            list_user = buy_user['user_id'].values
            user_cate = pd.merge(pd.DataFrame({'user_id': list_user, 'key': [1] * len(list_user)}), cate, how='left',
                                 on='key')
            user_cate = user_cate.drop_duplicates()
            print('\t可能购买', user_cate.shape)
            # 可能购买采样(每个用户可能购买随机的0.01个类别)
            groups = user_cate.groupby('user_id', as_index=False).apply(lambda x: x.sample(n=2, replace=True))
            user_cate = groups.reset_index()
            user_cate = user_cate.drop(['level_0', 'level_1', 'key'], axis=1)
            print('\t采样后可能购买', user_cate.shape)
            # 合并购买(防止采样后可能购买不含真实购买的类别)
            user_cate = pd.concat([buy_user_cate, user_cate], sort=False, axis=0)
            user_cate = user_cate.drop_duplicates()
            print('\t合并购买', user_cate.shape)
            pkey = user_cate
            # 添加标签
            label_1 = pd.concat([buy_user_cate.reset_index(), pd.DataFrame({'label': [1] * buy_user_cate.shape[0]})], axis=1)
            label_1 = label_1.drop(['index'], axis=1)
            label = pd.merge(pkey, label_1, on=['user_id', 'cate'], how='left')
            label.fillna(0, inplace=True)
            label['label'] = label['label'].astype('int')
            label = label.sort_values('user_id')
        label.to_csv(dump_path, index=False)
    print("\tlabel", label.shape)
    print("\tcols", label.columns)
    print("\thead", label.head())
    print("\ttail", label.tail())
    print('\t生成标签', label.shape)
    return label


def gen_subset(label):
    print('gen sebset:')

    action = pd.read_csv(action_path, na_filter=False, skip_blank_lines=True)
    shop = pd.read_csv(shop_path, na_filter=False, skip_blank_lines=True)
    product = pd.read_csv(product_path, na_filter=False, skip_blank_lines=True)
    user = pd.read_csv(user_path, na_filter=False, skip_blank_lines=True)

    print('\tbefore user:', user.shape)
    user = user[user['user_id'].isin(label['user_id'])]
    print('\tafter user:', user.shape)

    print('\tbefore action:', action.shape)
    action = action[action['user_id'].isin(label['user_id'])]
    print('\tafter action:', action.shape)

    print('\tbefore product:', product.shape)
    product = product[product['sku_id'].isin(action['sku_id'])]
    print('\tafter product:', product.shape)

    print('\tbefore shop:', shop.shape)
    shop = shop[shop['shop_id'].isin(product['shop_id'])]
    print('\tafter shop:', shop.shape)

    user.to_csv(user_path, index=False)
    shop.to_csv(shop_path, index=False)
    product.to_csv(product_path, index=False)
    action.to_csv(action_path, index=False)
    print('finish gen sebset')


def recovr_subset():
    print('recover sebset:')

    shutil.copyfile('../data/clean_ori/user.csv', user_path)
    shutil.copyfile('../data/clean_ori/shop.csv', shop_path)
    shutil.copyfile('../data/clean_ori/product.csv', product_path)
    shutil.copyfile('../data/clean_ori/action.csv', action_path)
