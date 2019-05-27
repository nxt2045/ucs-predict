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
import seaborn as sns
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
cache_path = '../cache'


# %% 特征融合
def gen_feat(end_date, time_gap, mark):
    """ 主调用
    调用 label-extract-map
    """
    print(datetime.now())
    print('\n>> 开始生成特征(X,y)')
    print('end_date', end_date)
    end_date = datetime.strptime(end_date, '%Y-%m-%d')
    dump_path = cache_path + '/feat_user_%s.csv' % (end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path):
        feat = pd.read_csv(dump_path)
    else:
        label = get_label(end_date, mark)
        feat = extract_feat(end_date, time_gap, label)
        # feat.to_csv(dump_path, index=False)
    # TODO: 分箱数据 [结果变差]
    # feat = map_feat(feat)
    print("feat", feat.shape)
    print("cols", feat.columns)
    print("head")
    print(feat.head())
    print("tail")
    print(feat.tail())
    print('生成特征%s' % (str(feat.shape)))
    return feat


def extract_feat(end_date, time_gap, label):
    """生成某一结束时间对应的特征
    1. user信息
    2. action对应信息
    """
    pkey = label.drop('label', axis=1)
    feat_concat = [label]
    for gap in time_gap:
        print(datetime.now())
        print('> 开始生成特征 gap=%s' % (str(gap)))
        start_date = end_date - timedelta(days=gap - 1)
        # 初始化feat
        feat = pkey
        # user
        feat = pd.merge(feat, feat_user_action_amt(start_date, end_date), on='user_id', how='left')
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
    feat = pd.merge(feat, feat_user_action_amt(start_date, end_date), on='user_id', how='left')
    feat = pd.merge(feat, feat_user_view_amt(start_date, end_date), on='user_id', how='left')
    feat = pd.merge(feat, feat_user_buy_amt(start_date, end_date), on='user_id', how='left')
    feat = pd.merge(feat, feat_user_follow_amt(start_date, end_date), on='user_id', how='left')
    feat = pd.merge(feat, feat_user_remark_amt(start_date, end_date), on='user_id', how='left')
    feat = pd.merge(feat, feat_user_cart_amt(start_date, end_date), on='user_id', how='left')
    feat = pd.merge(feat, feat_user_buy_rate(start_date, end_date), on='user_id', how='left')
    feat = pd.merge(feat, feat_user_first_hour(start_date, end_date), on='user_id', how='left')
    feat = pd.merge(feat, feat_user_last_hour(start_date, end_date), on='user_id', how='left')
    feat = pd.merge(feat, feat_user_last_amt(start_date, end_date), on='user_id', how='left')
    feat.fillna(0, inplace=True)
    feat = feat.astype(int)
    # TODO 结束：与time_gap无关的feat
    return feat


def get_label(end_date, mark):
    """生成某一结束时间对应的特征label
    label：预测label,提交集=-1
    """
    print(datetime.now())
    print('> 开始生成标签')
    if mark == 'submit':
        pkey = pd.read_csv(clean_path + '/user.csv', na_filter=False, usecols=['user_id'])
        label = pd.concat([pkey, pd.DataFrame({'label': [-1] * pkey.shape[0]})], axis=1)
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


def map_feat(feat):
    """ 分箱数据
    可执行 qcut 分析
    :param feat:
    :return:
    """
    # qcut_feat(feat)
    # TODO: 自定义函数
    dicts = {
        '2_user_view_amt': [min(0, min(feat['2_user_view_amt'].values)) - 1,
                            1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13, 17, 23,
                            max(342, max(feat['2_user_view_amt'].values)) + 1],
        '3_user_view_amt': [min(0, min(feat['3_user_view_amt'].values)) - 1,
                            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15, 20,
                            29, max(679, max(feat['3_user_view_amt'].values)) + 1],
        '7_user_view_amt': [min(0, min(feat['7_user_view_amt'].values)) - 1,
                            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 17,
                            20, 26, 40, max(1648, max(feat['7_user_view_amt'].values)) + 1],
        '7_user_follow_amt': [min(0, min(feat['7_user_follow_amt'].values)) - 1,
                              1, 3, 4, 5, 7,
                              max(175, max(feat['7_user_follow_amt'].values)) + 1],
        '14_user_view_amt': [min(0, min(feat['14_user_view_amt'].values)) - 1,
                             1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 18, 21, 25,
                             33, 51, max(2411, max(feat['14_user_view_amt'].values)) + 1],
        '14_user_buy_amt': [min(0, min(feat['14_user_buy_amt'].values)) - 1,
                            1, 2, 3,
                            max(38, max(feat['14_user_buy_amt'].values)) + 1],
        '14_user_follow_amt': [min(0, min(feat['14_user_follow_amt'].values)) - 1,
                               1, 2, 3, 4, 5, 8,
                               max(215, max(feat['14_user_follow_amt'].values)) + 1],
        '14_user_remark_amt': [min(0, min(feat['14_user_remark_amt'].values)) - 1,
                               1, 2, 3, 4, 5,
                               max(67, max(feat['14_user_remark_amt'].values)) + 1],
        'user_reg_month': [min(0, min(feat['user_reg_month'].values)) - 1,
                           1, 2, 4, 6, 8, 12, 18, 24, 36, 48, 60,
                           max(180, max(feat['user_reg_month'].values)) + 1],
        'user_view_amt': [min(0, min(feat['user_view_amt'].values)) - 1,
                          1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 14, 16, 18, 21, 24, 29, 35, 44, 59, 94,
                          max(11644, max(feat['user_view_amt'].values)) + 1],
        'user_buy_amt': [min(0, min(feat['user_buy_amt'].values)) - 1,
                         1, 2, 3, 4, 5, 6, 8,
                         max(237, max(feat['user_buy_amt'].values)) + 1],
        'user_follow_amt': [min(0, min(feat['user_follow_amt'].values)) - 1,
                            1, 2, 3, 4, 5, 6, 8, 12,
                            max(559, max(feat['user_follow_amt'].values)) + 1],
        'user_remark_amt': [min(0, min(feat['user_remark_amt'].values)) - 1,
                            1, 2, 3, 4, 5, 6, 8,
                            max(125, max(feat['user_remark_amt'].values)) + 1],
        'user_cart_amt': [min(0, min(feat['user_cart_amt'].values)) - 1,
                          1, 2, 3, 4, 5, 6, 8, 10, 14,
                          max(319, max(feat['user_cart_amt'].values)) + 1],
        'user_buy/view': [min(-13800, min(feat['user_buy/view'].values)) - 1,
                          -200, -100, 0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 16, 20, 25, 28, 33, 50, 100,
                          max(1666, max(feat['user_buy/view'].values)) + 1],
        'user_buy/follow': [min(-23700, min(feat['user_buy/follow'].values)) - 1,
                            -600, -500, -400, -300, -200, -100, 0, 1, 27, 33, 50, 66, 100, 157, 200, 300,
                            max(9180, max(feat['user_buy/follow'].values)) + 1],
        'user_buy/remark': [min(-23700, min(feat['user_buy/remark'].values)) - 1,
                            -500, -400, -300, -200, -100, 0, 1, 11, 25, 33, 37, 50, 66, 100, 150, 200,
                            max(7400, max(feat['user_buy/remark'].values)) + 1],
        'user_buy/cart': [min(-13800, min(feat['user_buy/cart'].values)) - 1,
                          -600, -400, -300, -200, -100, 0, 6, 16, 25, 33, 50, 66, 100, 166, 200, 300,
                          max(17700, max(feat['user_buy/cart'].values)) + 1],
    }
    for col, bins in dicts.items():
        print(col, bins)
        labels = [str(i) for i in range(len(bins) - 1)]
        feat.loc[:, col] = pd.cut(feat[col], bins=bins, labels=labels)
        print(feat[col].value_counts(sort=False))
    return feat


def qcut_feat(feat):
    """等频分箱
    与"label"无关
    不适用<数值无意义>类别 (city province)
    :param feat:
    :return:
    """
    print(datetime.now())
    print('> 开始映射特征')
    feat = feat.drop(['user_id'], axis=1)
    for col in feat.columns:
        counts = feat[col].value_counts().values
        if len(counts) == 1:
            print('\n无效特征列：', col)
        elif col != 'label' and len(counts) > 30:
            cuts = int(50.0 * feat.shape[0] / (feat.shape[0] - counts[0]))
            print('\n开始划分：%s(%s)' % (col, str(cuts)))
            print('min：%s' % (str(min(feat[col].values))))
            print('max：%s' % (str(max(feat[col].values))))
            cutted = pd.qcut(feat[col], cuts, duplicates='drop')
            if len(cutted.value_counts()) > 30:
                cutted = pd.qcut(feat[col], 100, duplicates='drop')
                if len(cutted.value_counts()) > 30:
                    cutted = pd.qcut(feat[col], 50, duplicates='drop')
                    if len(cutted.value_counts()) > 30:
                        cutted = pd.qcut(feat[col], 30, duplicates='drop')
            feat.loc[:, col] = cutted
            print(feat[col].value_counts(sort=False))