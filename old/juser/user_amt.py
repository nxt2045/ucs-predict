# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @DATE    : 5/9/2019
# @Author  : xiaotong niu
# @File    : user_amt.py
# @Project : JData-Predict
# @Github  ：https://github.com/isNxt
# @Describ : ...


import time
from datetime import timedelta,datetime
from user_feat import feat_user_if_buy
import os
import pandas as pd


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


# %% 用户数量
def get_amt():
    time_0 = time.clock()
    print('\n>> 开始计算人数')
    last_date = datetime.strptime(data_end_date, '%Y-%m-%d')
    first_date = datetime.strptime(data_start_date, '%Y-%m-%d')
    time_gap = [7]
    for gap in time_gap:
        times = int((last_date - first_date).days / gap)
        feat_concat = []
        for i in range(times):
            end_date = last_date - timedelta(days=gap * i)
            start_date = end_date - timedelta(days=gap - 1)
            feat = feat_user_if_buy(start_date, end_date)
            feat = feat['if_buy'].sum()
            feat_concat.append({'start_date': start_date, 'end_date': end_date, 'amt': feat})
        feat = pd.DataFrame(feat_concat)
        feat.to_csv(out_path + '/user_amt_' + str(gap) + '.csv', index=False)
    print('<< 结果预测完成, 用时', time.clock() - time_0, 's')


if __name__ == "__main__":
    get_amt()
