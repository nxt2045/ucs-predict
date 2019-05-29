# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @DATE    : 5/14/2019
# @Author  : xiaotong niu
# @File    : merg.py
# @Project : JData-Predict
# @Github  ：https://github.com/isNxt
# @Describ : ...

import time
import gc
import logging
from datetime import timedelta
from datetime import datetime
from feature.feat_user import *
from feature.feat_cate import *
from feature.feat_shop import *
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

# %% 配置
# 输出设置

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 20)
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
cache_path = '../cache'

if_plot = False
if_save_gap = True


# %% 特征融合
def gen_feat(end_date, label_gap, mark):
    """ 主调用
    调用 label-extract-map
    """
    print(datetime.now())
    print('\n>> 开始生成特征(X,y)')
    print('end_date', end_date)
    end_date = datetime.strptime(end_date, '%Y-%m-%d')
    dump_path = cache_path + '/feat_uscb_%s_%s_%s.csv' % (str(label_gap), mark, end_date.strftime('%y%m%d'))
    if os.path.exists(dump_path) and not if_plot:
        feat = pd.read_csv(dump_path)
    else:
        label = gen_label(end_date, label_gap, mark)
        feat_concat = [label]
        feat_concat.append(gen_feat_1(end_date, label))
        feat_concat.append(gen_feat_2(end_date, label))
        feat_concat.append(gen_feat_3(end_date, label))
        feat_concat.append(gen_feat_7(end_date, label))
        feat_concat.append(gen_feat_14(end_date, label))
        feat_concat.append(gen_feat_30(end_date, label))
        feat = pd.concat(feat_concat, axis=1)
        feat.to_csv(dump_path, index=False)
    print('>> 完成生成特征%s' % (str(feat.shape)))
    return feat


def gen_feat_1(end_date, label):
    """生成某一结束时间对应的特征
    特征缓存：pd.merge(feat,...) 换成 pd.merge(pkey,...)

    """

    gap = 1
    print(datetime.now())
    print('> 遍历特征 gap=%s' % (str(gap)))
    start_date = end_date - timedelta(days=gap - 1)
    dump_path = '%s/feat/%s_%s.csv' % (cache_path, end_date.strftime('%y%m%d'), str(gap))
    if os.path.exists(dump_path) and not if_plot:
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        # 初始化feat
        feat = label
        # GR: 用户
        # 用户是否
        feat = pd.merge(feat, feat_user_if_view(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_if_buy(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_if_follow(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_if_remark(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_if_cart(start_date, end_date), on='user_id', how='left')
        feat.fillna(0, inplace=True)
        feat = feat.astype(int)
        if if_plot:
            print('>> 开始绘制特征%s' % (str(feat.shape)))
            for col in feat.columns:
                counts = feat[col].value_counts()
                plot_path = './vc/%s_%s/%s %s-%s.png' % (end_date.strftime('%y%m%d'), str(gap), col.replace('/', '#'),
                                                         start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
                if col not in ['user_id', 'cate', 'shop_id', 'label'] and len(counts) > 2 \
                        and if_plot and not os.path.exists(plot_path):
                    print('ploting: ', col)
                    fig, [ax1, ax2] = plt.subplots(2, 1, figsize=(8, 8))
                    sns.boxplot(x=col, y="label", orient='h', data=feat, ax=ax1)
                    ax1.set_title('%s-%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
                    sns.violinplot(x=col, y="label", orient='h', data=feat, ax=ax2)
                    plt.subplots_adjust(hspace=0.2)
                    # 指定子图的标题
                    plt.savefig(plot_path, dpi=300, bbox_inches='tight')
            del feat
            print('gc: ', gc.collect())
            feat = label

        # 用户数量
        feat = pd.merge(feat, feat_user_action_amt(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_view_amt(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_buy_amt(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_follow_amt(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_remark_amt(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_cart_amt(start_date, end_date), on='user_id', how='left')
        feat.fillna(0, inplace=True)
        feat = feat.astype(int)
        if if_plot:
            print('>> 开始绘制特征%s' % (str(feat.shape)))
            for col in feat.columns:
                counts = feat[col].value_counts()
                plot_path = './vc/%s_%s/%s %s-%s.png' % (end_date.strftime('%y%m%d'), str(gap), col.replace('/', '#'),
                                                         start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
                if col not in ['user_id', 'cate', 'shop_id', 'label'] and len(counts) > 2 \
                        and if_plot and not os.path.exists(plot_path):
                    print('ploting: ', col)
                    fig, [ax1, ax2] = plt.subplots(2, 1, figsize=(8, 8))
                    sns.boxplot(x=col, y="label", orient='h', data=feat, ax=ax1)
                    ax1.set_title('%s-%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
                    sns.violinplot(x=col, y="label", orient='h', data=feat, ax=ax2)
                    plt.subplots_adjust(hspace=0.2)
                    # 指定子图的标题
                    plt.savefig(plot_path, dpi=300, bbox_inches='tight')
            del feat
            print('gc: ', gc.collect())
            feat = label

        # 用户天数
        feat = pd.merge(feat, feat_user_action_day(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_view_day(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_buy_day(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_follow_day(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_remark_day(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_cart_day(start_date, end_date), on='user_id', how='left')
        feat.fillna(0, inplace=True)
        feat = feat.astype(int)
        if if_plot:
            print('>> 开始绘制特征%s' % (str(feat.shape)))
            for col in feat.columns:
                counts = feat[col].value_counts()
                plot_path = './vc/%s_%s/%s %s-%s.png' % (end_date.strftime('%y%m%d'), str(gap), col.replace('/', '#'),
                                                         start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
                if col not in ['user_id', 'cate', 'shop_id', 'label'] and len(counts) > 2 \
                        and if_plot and not os.path.exists(plot_path):
                    print('ploting: ', col)
                    fig, [ax1, ax2] = plt.subplots(2, 1, figsize=(8, 8))
                    sns.boxplot(x=col, y="label", orient='h', data=feat, ax=ax1)
                    ax1.set_title('%s-%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
                    sns.violinplot(x=col, y="label", orient='h', data=feat, ax=ax2)
                    plt.subplots_adjust(hspace=0.2)
                    # 指定子图的标题
                    plt.savefig(plot_path, dpi=300, bbox_inches='tight')
            del feat
            print('gc: ', gc.collect())
            feat = label

        # 用户其他
        feat = pd.merge(feat, feat_user_action_ratio(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_buy_rate(start_date, end_date), on='user_id', how='left')
        feat.fillna(0, inplace=True)
        feat = feat.astype(int)
        if if_plot:
            print('>> 开始绘制特征%s' % (str(feat.shape)))
            for col in feat.columns:
                counts = feat[col].value_counts()
                plot_path = './vc/%s_%s/%s %s-%s.png' % (end_date.strftime('%y%m%d'), str(gap), col.replace('/', '#'),
                                                         start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
                if col not in ['user_id', 'cate', 'shop_id', 'label'] and len(counts) > 2 \
                        and if_plot and not os.path.exists(plot_path):
                    print('ploting: ', col)
                    fig, [ax1, ax2] = plt.subplots(2, 1, figsize=(8, 8))
                    sns.boxplot(x=col, y="label", orient='h', data=feat, ax=ax1)
                    ax1.set_title('%s-%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
                    sns.violinplot(x=col, y="label", orient='h', data=feat, ax=ax2)
                    plt.subplots_adjust(hspace=0.2)
                    # 指定子图的标题
                    plt.savefig(plot_path, dpi=300, bbox_inches='tight')
            del feat
            print('gc: ', gc.collect())
            feat = label

        # GR: 用户品类
        # 用户品类数量
        feat = pd.merge(feat, feat_user_cate_view_amt(start_date, end_date), on=['user_id', 'cate'], how='left')
        feat = pd.merge(feat, feat_user_cate_buy_amt(start_date, end_date), on=['user_id', 'cate'], how='left')
        feat = pd.merge(feat, feat_user_cate_follow_amt(start_date, end_date), on=['user_id', 'cate'], how='left')
        feat = pd.merge(feat, feat_user_cate_remark_amt(start_date, end_date), on=['user_id', 'cate'], how='left')
        feat = pd.merge(feat, feat_user_cate_cart_amt(start_date, end_date), on=['user_id', 'cate'], how='left')
        feat.fillna(0, inplace=True)
        feat = feat.astype(int)
        if if_plot:
            print('>> 开始绘制特征%s' % (str(feat.shape)))
            for col in feat.columns:
                counts = feat[col].value_counts()
                plot_path = './vc/%s_%s/%s %s-%s.png' % (end_date.strftime('%y%m%d'), str(gap), col.replace('/', '#'),
                                                         start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
                if col not in ['user_id', 'cate', 'shop_id', 'label'] and len(counts) > 2 \
                        and if_plot and not os.path.exists(plot_path):
                    print('ploting: ', col)
                    fig, [ax1, ax2] = plt.subplots(2, 1, figsize=(8, 8))
                    sns.boxplot(x=col, y="label", orient='h', data=feat, ax=ax1)
                    ax1.set_title('%s-%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
                    sns.violinplot(x=col, y="label", orient='h', data=feat, ax=ax2)
                    plt.subplots_adjust(hspace=0.2)
                    # 指定子图的标题
                    plt.savefig(plot_path, dpi=300, bbox_inches='tight')
            del feat
            print('gc: ', gc.collect())
            feat = label

        # 用户品类其他

        feat = pd.merge(feat, feat_user_cate_action_ratio(start_date, end_date), on=['user_id', 'cate'], how='left')
        feat = pd.merge(feat, feat_user_cate_user_action_ratio(start_date, end_date), on=['user_id', 'cate'],
                        how='left')
        feat.fillna(0, inplace=True)
        feat = feat.astype(int)
        if if_plot:
            print('>> 开始绘制特征%s' % (str(feat.shape)))
            for col in feat.columns:
                counts = feat[col].value_counts()
                plot_path = './vc/%s_%s/%s %s-%s.png' % (end_date.strftime('%y%m%d'), str(gap), col.replace('/', '#'),
                                                         start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
                if col not in ['user_id', 'cate', 'shop_id', 'label'] and len(counts) > 2 \
                        and if_plot and not os.path.exists(plot_path):
                    print('ploting: ', col)
                    fig, [ax1, ax2] = plt.subplots(2, 1, figsize=(8, 8))
                    sns.boxplot(x=col, y="label", orient='h', data=feat, ax=ax1)
                    ax1.set_title('%s-%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
                    sns.violinplot(x=col, y="label", orient='h', data=feat, ax=ax2)
                    plt.subplots_adjust(hspace=0.2)
                    # 指定子图的标题
                    plt.savefig(plot_path, dpi=300, bbox_inches='tight')
            del feat
            print('gc: ', gc.collect())
            feat = label

        # GR: 用户店铺

        # 用户店铺数量
        feat = pd.merge(feat, feat_user_shop_view_amt(start_date, end_date), on=['user_id', 'shop_id'], how='left')
        feat = pd.merge(feat, feat_user_shop_buy_amt(start_date, end_date), on=['user_id', 'shop_id'], how='left')
        feat = pd.merge(feat, feat_user_shop_follow_amt(start_date, end_date), on=['user_id', 'shop_id'], how='left')
        feat = pd.merge(feat, feat_user_shop_remark_amt(start_date, end_date), on=['user_id', 'shop_id'], how='left')
        feat = pd.merge(feat, feat_user_shop_cart_amt(start_date, end_date), on=['user_id', 'shop_id'], how='left')
        feat.fillna(0, inplace=True)
        feat = feat.astype(int)
        if if_plot:
            print('>> 开始绘制特征%s' % (str(feat.shape)))
            for col in feat.columns:
                counts = feat[col].value_counts()
                plot_path = './vc/%s_%s/%s %s-%s.png' % (end_date.strftime('%y%m%d'), str(gap), col.replace('/', '#'),
                                                         start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
                if col not in ['user_id', 'cate', 'shop_id', 'label'] and len(counts) > 2 \
                        and if_plot and not os.path.exists(plot_path):
                    print('ploting: ', col)
                    fig, [ax1, ax2] = plt.subplots(2, 1, figsize=(8, 8))
                    sns.boxplot(x=col, y="label", orient='h', data=feat, ax=ax1)
                    ax1.set_title('%s-%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
                    sns.violinplot(x=col, y="label", orient='h', data=feat, ax=ax2)
                    plt.subplots_adjust(hspace=0.2)
                    # 指定子图的标题
                    plt.savefig(plot_path, dpi=300, bbox_inches='tight')
            del feat
            print('gc: ', gc.collect())
            feat = label

        # 用户店铺其他
        feat = pd.merge(feat, feat_user_shop_action_ratio(start_date, end_date), on=['user_id', 'shop_id'], how='left')
        feat = pd.merge(feat, feat_user_shop_user_action_ratio(start_date, end_date), on=['user_id', 'shop_id'],
                        how='left')
        feat.fillna(0, inplace=True)
        feat = feat.astype(int)
        if if_plot:
            print('>> 开始绘制特征%s' % (str(feat.shape)))
            for col in feat.columns:
                counts = feat[col].value_counts()
                plot_path = './vc/%s_%s/%s %s-%s.png' % (end_date.strftime('%y%m%d'), str(gap), col.replace('/', '#'),
                                                         start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
                if col not in ['user_id', 'cate', 'shop_id', 'label'] and len(counts) > 2 \
                        and if_plot and not os.path.exists(plot_path):
                    print('ploting: ', col)
                    fig, [ax1, ax2] = plt.subplots(2, 1, figsize=(8, 8))
                    sns.boxplot(x=col, y="label", orient='h', data=feat, ax=ax1)
                    ax1.set_title('%s-%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
                    sns.violinplot(x=col, y="label", orient='h', data=feat, ax=ax2)
                    plt.subplots_adjust(hspace=0.2)
                    # 指定子图的标题
                    plt.savefig(plot_path, dpi=300, bbox_inches='tight')
            del feat
            print('gc: ', gc.collect())
            feat = label

        # 计算vc
        print(datetime.now())
        f = open(
            './vc/%s_%s/%s_%s.txt' % (end_date.strftime('%y%m%d'), str(gap), end_date.strftime('%y%m%d'), str(gap)),
            'w')
        for col in feat.columns:
            if col not in ['user_id', 'cate', 'shop_id', 'label']:
                counts = feat[col].value_counts()
                print('> 1_%s: %s' % (col, str(len(counts))))
                f.write(col + ': ' + str(counts.to_json()))
                f.write('\n')
        f.close()

        # 最后调整
        feat = feat.drop(['user_id', 'cate', 'shop_id', 'label'], axis=1)
        feat = feat.add_prefix(str(gap) + '_')  # 列名加上gap标签前缀
        if if_save_gap and not if_plot: feat.to_csv(dump_path, index=False)
    return feat


def gen_feat_2(end_date, label):
    """生成某一结束时间对应的特征
    特征缓存：pd.merge(feat,...) 换成 pd.merge(pkey,...)
    """
    gap = 2
    print(datetime.now())
    print('> 遍历特征 gap=%s' % (str(gap)))
    start_date = end_date - timedelta(days=gap - 1)
    dump_path = '%s/feat/%s_%s.csv' % (cache_path, end_date.strftime('%y%m%d'), str(gap))
    if os.path.exists(dump_path) and not if_plot:
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        # 初始化feat
        feat = label
        # GR: 用户
        # 用户是否
        feat = pd.merge(feat, feat_user_if_view(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_if_buy(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_if_follow(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_if_remark(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_if_cart(start_date, end_date), on='user_id', how='left')
        feat.fillna(0, inplace=True)
        feat = feat.astype(int)
        if if_plot:
            print('>> 开始绘制特征%s' % (str(feat.shape)))
            for col in feat.columns:
                counts = feat[col].value_counts()
                plot_path = './vc/%s_%s/%s %s-%s.png' % (end_date.strftime('%y%m%d'), str(gap), col.replace('/', '#'),
                                                         start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
                if col not in ['user_id', 'cate', 'shop_id', 'label'] and len(counts) > 2 \
                        and if_plot and not os.path.exists(plot_path):
                    print('ploting: ', col)
                    fig, [ax1, ax2] = plt.subplots(2, 1, figsize=(8, 8))
                    sns.boxplot(x=col, y="label", orient='h', data=feat, ax=ax1)
                    ax1.set_title('%s-%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
                    sns.violinplot(x=col, y="label", orient='h', data=feat, ax=ax2)
                    plt.subplots_adjust(hspace=0.2)
                    # 指定子图的标题
                    plt.savefig(plot_path, dpi=300, bbox_inches='tight')
            del feat
            print('gc: ', gc.collect())
            feat = label

        # 用户数量
        feat = pd.merge(feat, feat_user_action_amt(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_view_amt(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_buy_amt(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_follow_amt(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_remark_amt(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_cart_amt(start_date, end_date), on='user_id', how='left')
        feat.fillna(0, inplace=True)
        feat = feat.astype(int)
        if if_plot:
            print('>> 开始绘制特征%s' % (str(feat.shape)))
            for col in feat.columns:
                counts = feat[col].value_counts()
                plot_path = './vc/%s_%s/%s %s-%s.png' % (end_date.strftime('%y%m%d'), str(gap), col.replace('/', '#'),
                                                         start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
                if col not in ['user_id', 'cate', 'shop_id', 'label'] and len(counts) > 2 \
                        and if_plot and not os.path.exists(plot_path):
                    print('ploting: ', col)
                    fig, [ax1, ax2] = plt.subplots(2, 1, figsize=(8, 8))
                    sns.boxplot(x=col, y="label", orient='h', data=feat, ax=ax1)
                    ax1.set_title('%s-%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
                    sns.violinplot(x=col, y="label", orient='h', data=feat, ax=ax2)
                    plt.subplots_adjust(hspace=0.2)
                    # 指定子图的标题
                    plt.savefig(plot_path, dpi=300, bbox_inches='tight')
            del feat
            print('gc: ', gc.collect())
            feat = label

        # 用户天数
        feat = pd.merge(feat, feat_user_action_day(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_view_day(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_buy_day(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_follow_day(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_remark_day(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_cart_day(start_date, end_date), on='user_id', how='left')
        feat.fillna(0, inplace=True)
        feat = feat.astype(int)
        if if_plot:
            print('>> 开始绘制特征%s' % (str(feat.shape)))
            for col in feat.columns:
                counts = feat[col].value_counts()
                plot_path = './vc/%s_%s/%s %s-%s.png' % (end_date.strftime('%y%m%d'), str(gap), col.replace('/', '#'),
                                                         start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
                if col not in ['user_id', 'cate', 'shop_id', 'label'] and len(counts) > 2 \
                        and if_plot and not os.path.exists(plot_path):
                    print('ploting: ', col)
                    fig, [ax1, ax2] = plt.subplots(2, 1, figsize=(8, 8))
                    sns.boxplot(x=col, y="label", orient='h', data=feat, ax=ax1)
                    ax1.set_title('%s-%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
                    sns.violinplot(x=col, y="label", orient='h', data=feat, ax=ax2)
                    plt.subplots_adjust(hspace=0.2)
                    # 指定子图的标题
                    plt.savefig(plot_path, dpi=300, bbox_inches='tight')
            del feat
            print('gc: ', gc.collect())
            feat = label

        # 用户其他
        feat = pd.merge(feat, feat_user_action_ratio(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_buy_rate(start_date, end_date), on='user_id', how='left')
        feat.fillna(0, inplace=True)
        feat = feat.astype(int)
        if if_plot:
            print('>> 开始绘制特征%s' % (str(feat.shape)))
            for col in feat.columns:
                counts = feat[col].value_counts()
                plot_path = './vc/%s_%s/%s %s-%s.png' % (end_date.strftime('%y%m%d'), str(gap), col.replace('/', '#'),
                                                         start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
                if col not in ['user_id', 'cate', 'shop_id', 'label'] and len(counts) > 2 \
                        and if_plot and not os.path.exists(plot_path):
                    print('ploting: ', col)
                    fig, [ax1, ax2] = plt.subplots(2, 1, figsize=(8, 8))
                    sns.boxplot(x=col, y="label", orient='h', data=feat, ax=ax1)
                    ax1.set_title('%s-%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
                    sns.violinplot(x=col, y="label", orient='h', data=feat, ax=ax2)
                    plt.subplots_adjust(hspace=0.2)
                    # 指定子图的标题
                    plt.savefig(plot_path, dpi=300, bbox_inches='tight')
            del feat
            print('gc: ', gc.collect())
            feat = label

        # GR: 用户品类
        # 用户品类数量
        feat = pd.merge(feat, feat_user_cate_view_amt(start_date, end_date), on=['user_id', 'cate'], how='left')
        feat = pd.merge(feat, feat_user_cate_buy_amt(start_date, end_date), on=['user_id', 'cate'], how='left')
        feat = pd.merge(feat, feat_user_cate_follow_amt(start_date, end_date), on=['user_id', 'cate'], how='left')
        feat = pd.merge(feat, feat_user_cate_remark_amt(start_date, end_date), on=['user_id', 'cate'], how='left')
        feat = pd.merge(feat, feat_user_cate_cart_amt(start_date, end_date), on=['user_id', 'cate'], how='left')
        feat.fillna(0, inplace=True)
        feat = feat.astype(int)
        if if_plot:
            print('>> 开始绘制特征%s' % (str(feat.shape)))
            for col in feat.columns:
                counts = feat[col].value_counts()
                plot_path = './vc/%s_%s/%s %s-%s.png' % (end_date.strftime('%y%m%d'), str(gap), col.replace('/', '#'),
                                                         start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
                if col not in ['user_id', 'cate', 'shop_id', 'label'] and len(counts) > 2 \
                        and if_plot and not os.path.exists(plot_path):
                    print('ploting: ', col)
                    fig, [ax1, ax2] = plt.subplots(2, 1, figsize=(8, 8))
                    sns.boxplot(x=col, y="label", orient='h', data=feat, ax=ax1)
                    ax1.set_title('%s-%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
                    sns.violinplot(x=col, y="label", orient='h', data=feat, ax=ax2)
                    plt.subplots_adjust(hspace=0.2)
                    # 指定子图的标题
                    plt.savefig(plot_path, dpi=300, bbox_inches='tight')
            del feat
            print('gc: ', gc.collect())
            feat = label

        # 用户品类其他

        feat = pd.merge(feat, feat_user_cate_action_ratio(start_date, end_date), on=['user_id', 'cate'], how='left')
        feat = pd.merge(feat, feat_user_cate_user_action_ratio(start_date, end_date), on=['user_id', 'cate'],
                        how='left')
        feat.fillna(0, inplace=True)
        feat = feat.astype(int)
        if if_plot:
            print('>> 开始绘制特征%s' % (str(feat.shape)))
            for col in feat.columns:
                counts = feat[col].value_counts()
                plot_path = './vc/%s_%s/%s %s-%s.png' % (end_date.strftime('%y%m%d'), str(gap), col.replace('/', '#'),
                                                         start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
                if col not in ['user_id', 'cate', 'shop_id', 'label'] and len(counts) > 2 \
                        and if_plot and not os.path.exists(plot_path):
                    print('ploting: ', col)
                    fig, [ax1, ax2] = plt.subplots(2, 1, figsize=(8, 8))
                    sns.boxplot(x=col, y="label", orient='h', data=feat, ax=ax1)
                    ax1.set_title('%s-%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
                    sns.violinplot(x=col, y="label", orient='h', data=feat, ax=ax2)
                    plt.subplots_adjust(hspace=0.2)
                    # 指定子图的标题
                    plt.savefig(plot_path, dpi=300, bbox_inches='tight')
            del feat
            print('gc: ', gc.collect())
            feat = label

        # GR: 用户店铺

        # 用户店铺数量
        feat = pd.merge(feat, feat_user_shop_view_amt(start_date, end_date), on=['user_id', 'shop_id'], how='left')
        feat = pd.merge(feat, feat_user_shop_buy_amt(start_date, end_date), on=['user_id', 'shop_id'], how='left')
        feat = pd.merge(feat, feat_user_shop_follow_amt(start_date, end_date), on=['user_id', 'shop_id'], how='left')
        feat = pd.merge(feat, feat_user_shop_remark_amt(start_date, end_date), on=['user_id', 'shop_id'], how='left')
        feat = pd.merge(feat, feat_user_shop_cart_amt(start_date, end_date), on=['user_id', 'shop_id'], how='left')
        feat.fillna(0, inplace=True)
        feat = feat.astype(int)
        if if_plot:
            print('>> 开始绘制特征%s' % (str(feat.shape)))
            for col in feat.columns:
                counts = feat[col].value_counts()
                plot_path = './vc/%s_%s/%s %s-%s.png' % (end_date.strftime('%y%m%d'), str(gap), col.replace('/', '#'),
                                                         start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
                if col not in ['user_id', 'cate', 'shop_id', 'label'] and len(counts) > 2 \
                        and if_plot and not os.path.exists(plot_path):
                    print('ploting: ', col)
                    fig, [ax1, ax2] = plt.subplots(2, 1, figsize=(8, 8))
                    sns.boxplot(x=col, y="label", orient='h', data=feat, ax=ax1)
                    ax1.set_title('%s-%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
                    sns.violinplot(x=col, y="label", orient='h', data=feat, ax=ax2)
                    plt.subplots_adjust(hspace=0.2)
                    # 指定子图的标题
                    plt.savefig(plot_path, dpi=300, bbox_inches='tight')
            del feat
            print('gc: ', gc.collect())
            feat = label

        # 用户店铺其他
        feat = pd.merge(feat, feat_user_shop_action_ratio(start_date, end_date), on=['user_id', 'shop_id'], how='left')
        feat = pd.merge(feat, feat_user_shop_user_action_ratio(start_date, end_date), on=['user_id', 'shop_id'],
                        how='left')
        feat.fillna(0, inplace=True)
        feat = feat.astype(int)
        if if_plot:
            print('>> 开始绘制特征%s' % (str(feat.shape)))
            for col in feat.columns:
                counts = feat[col].value_counts()
                plot_path = './vc/%s_%s/%s %s-%s.png' % (end_date.strftime('%y%m%d'), str(gap), col.replace('/', '#'),
                                                         start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
                if col not in ['user_id', 'cate', 'shop_id', 'label'] and len(counts) > 2 \
                        and if_plot and not os.path.exists(plot_path):
                    print('ploting: ', col)
                    fig, [ax1, ax2] = plt.subplots(2, 1, figsize=(8, 8))
                    sns.boxplot(x=col, y="label", orient='h', data=feat, ax=ax1)
                    ax1.set_title('%s-%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
                    sns.violinplot(x=col, y="label", orient='h', data=feat, ax=ax2)
                    plt.subplots_adjust(hspace=0.2)
                    # 指定子图的标题
                    plt.savefig(plot_path, dpi=300, bbox_inches='tight')
            del feat
            print('gc: ', gc.collect())
            feat = label

        # 计算vc
        print(datetime.now())
        f = open(
            './vc/%s_%s/%s_%s.txt' % (end_date.strftime('%y%m%d'), str(gap), end_date.strftime('%y%m%d'), str(gap)),
            'w')
        for col in feat.columns:
            if col not in ['user_id', 'cate', 'shop_id', 'label']:
                counts = feat[col].value_counts()
                print('> %s: %s' % (col, str(len(counts))))
                f.write(col + ': ' + str(counts.to_json()))
                f.write('\n')
        f.close()

        # 最后调整
        feat = feat.drop(['user_id', 'cate', 'shop_id', 'label'], axis=1)
        feat = feat.add_prefix(str(gap) + '_')  # 列名加上gap标签前缀
        if if_save_gap and not if_plot: feat.to_csv(dump_path, index=False)
    return feat


def gen_feat_3(end_date, label):
    """生成某一结束时间对应的特征
    特征缓存：pd.merge(feat,...) 换成 pd.merge(pkey,...)
    """
    gap = 3
    print(datetime.now())
    print('> 遍历特征 gap=%s' % (str(gap)))
    start_date = end_date - timedelta(days=gap - 1)
    dump_path = '%s/feat/%s_%s.csv' % (cache_path, end_date.strftime('%y%m%d'), str(gap))
    if os.path.exists(dump_path) and not if_plot:
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        # 初始化feat
        feat = label
        # GR: 用户
        # 用户是否
        feat = pd.merge(feat, feat_user_if_view(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_if_buy(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_if_follow(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_if_remark(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_if_cart(start_date, end_date), on='user_id', how='left')
        feat.fillna(0, inplace=True)
        feat = feat.astype(int)
        if if_plot:
            print('>> 开始绘制特征%s' % (str(feat.shape)))
            for col in feat.columns:
                counts = feat[col].value_counts()
                plot_path = './vc/%s_%s/%s %s-%s.png' % (end_date.strftime('%y%m%d'), str(gap), col.replace('/', '#'),
                                                         start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
                if col not in ['user_id', 'cate', 'shop_id', 'label'] and len(counts) > 2 \
                        and if_plot and not os.path.exists(plot_path):
                    print('ploting: ', col)
                    fig, [ax1, ax2] = plt.subplots(2, 1, figsize=(8, 8))
                    sns.boxplot(x=col, y="label", orient='h', data=feat, ax=ax1)
                    ax1.set_title('%s-%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
                    sns.violinplot(x=col, y="label", orient='h', data=feat, ax=ax2)
                    plt.subplots_adjust(hspace=0.2)
                    # 指定子图的标题
                    plt.savefig(plot_path, dpi=300, bbox_inches='tight')
            del feat
            print('gc: ', gc.collect())
            feat = label

        # 用户数量
        feat = pd.merge(feat, feat_user_action_amt(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_view_amt(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_buy_amt(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_follow_amt(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_remark_amt(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_cart_amt(start_date, end_date), on='user_id', how='left')
        feat.fillna(0, inplace=True)
        feat = feat.astype(int)
        if if_plot:
            print('>> 开始绘制特征%s' % (str(feat.shape)))
            for col in feat.columns:
                counts = feat[col].value_counts()
                plot_path = './vc/%s_%s/%s %s-%s.png' % (end_date.strftime('%y%m%d'), str(gap), col.replace('/', '#'),
                                                         start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
                if col not in ['user_id', 'cate', 'shop_id', 'label'] and len(counts) > 2 \
                        and if_plot and not os.path.exists(plot_path):
                    print('ploting: ', col)
                    fig, [ax1, ax2] = plt.subplots(2, 1, figsize=(8, 8))
                    sns.boxplot(x=col, y="label", orient='h', data=feat, ax=ax1)
                    ax1.set_title('%s-%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
                    sns.violinplot(x=col, y="label", orient='h', data=feat, ax=ax2)
                    plt.subplots_adjust(hspace=0.2)
                    # 指定子图的标题
                    plt.savefig(plot_path, dpi=300, bbox_inches='tight')
            del feat
            print('gc: ', gc.collect())
            feat = label

        # 用户天数
        feat = pd.merge(feat, feat_user_action_day(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_view_day(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_buy_day(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_follow_day(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_remark_day(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_cart_day(start_date, end_date), on='user_id', how='left')
        feat.fillna(0, inplace=True)
        feat = feat.astype(int)
        if if_plot:
            print('>> 开始绘制特征%s' % (str(feat.shape)))
            for col in feat.columns:
                counts = feat[col].value_counts()
                plot_path = './vc/%s_%s/%s %s-%s.png' % (end_date.strftime('%y%m%d'), str(gap), col.replace('/', '#'),
                                                         start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
                if col not in ['user_id', 'cate', 'shop_id', 'label'] and len(counts) > 2 \
                        and if_plot and not os.path.exists(plot_path):
                    print('ploting: ', col)
                    fig, [ax1, ax2] = plt.subplots(2, 1, figsize=(8, 8))
                    sns.boxplot(x=col, y="label", orient='h', data=feat, ax=ax1)
                    ax1.set_title('%s-%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
                    sns.violinplot(x=col, y="label", orient='h', data=feat, ax=ax2)
                    plt.subplots_adjust(hspace=0.2)
                    # 指定子图的标题
                    plt.savefig(plot_path, dpi=300, bbox_inches='tight')
            del feat
            print('gc: ', gc.collect())
            feat = label

        # 用户其他
        feat = pd.merge(feat, feat_user_action_ratio(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_buy_rate(start_date, end_date), on='user_id', how='left')
        feat.fillna(0, inplace=True)
        feat = feat.astype(int)
        if if_plot:
            print('>> 开始绘制特征%s' % (str(feat.shape)))
            for col in feat.columns:
                counts = feat[col].value_counts()
                plot_path = './vc/%s_%s/%s %s-%s.png' % (end_date.strftime('%y%m%d'), str(gap), col.replace('/', '#'),
                                                         start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
                if col not in ['user_id', 'cate', 'shop_id', 'label'] and len(counts) > 2 \
                        and if_plot and not os.path.exists(plot_path):
                    print('ploting: ', col)
                    fig, [ax1, ax2] = plt.subplots(2, 1, figsize=(8, 8))
                    sns.boxplot(x=col, y="label", orient='h', data=feat, ax=ax1)
                    ax1.set_title('%s-%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
                    sns.violinplot(x=col, y="label", orient='h', data=feat, ax=ax2)
                    plt.subplots_adjust(hspace=0.2)
                    # 指定子图的标题
                    plt.savefig(plot_path, dpi=300, bbox_inches='tight')
            del feat
            print('gc: ', gc.collect())
            feat = label

        # GR: 用户品类
        # 用户品类数量
        feat = pd.merge(feat, feat_user_cate_view_amt(start_date, end_date), on=['user_id', 'cate'], how='left')
        feat = pd.merge(feat, feat_user_cate_buy_amt(start_date, end_date), on=['user_id', 'cate'], how='left')
        feat = pd.merge(feat, feat_user_cate_follow_amt(start_date, end_date), on=['user_id', 'cate'], how='left')
        feat = pd.merge(feat, feat_user_cate_remark_amt(start_date, end_date), on=['user_id', 'cate'], how='left')
        feat = pd.merge(feat, feat_user_cate_cart_amt(start_date, end_date), on=['user_id', 'cate'], how='left')
        feat.fillna(0, inplace=True)
        feat = feat.astype(int)
        if if_plot:
            print('>> 开始绘制特征%s' % (str(feat.shape)))
            for col in feat.columns:
                counts = feat[col].value_counts()
                plot_path = './vc/%s_%s/%s %s-%s.png' % (end_date.strftime('%y%m%d'), str(gap), col.replace('/', '#'),
                                                         start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
                if col not in ['user_id', 'cate', 'shop_id', 'label'] and len(counts) > 2 \
                        and if_plot and not os.path.exists(plot_path):
                    print('ploting: ', col)
                    fig, [ax1, ax2] = plt.subplots(2, 1, figsize=(8, 8))
                    sns.boxplot(x=col, y="label", orient='h', data=feat, ax=ax1)
                    ax1.set_title('%s-%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
                    sns.violinplot(x=col, y="label", orient='h', data=feat, ax=ax2)
                    plt.subplots_adjust(hspace=0.2)
                    # 指定子图的标题
                    plt.savefig(plot_path, dpi=300, bbox_inches='tight')
            del feat
            print('gc: ', gc.collect())
            feat = label

        # 用户品类其他

        feat = pd.merge(feat, feat_user_cate_action_ratio(start_date, end_date), on=['user_id', 'cate'], how='left')
        feat = pd.merge(feat, feat_user_cate_user_action_ratio(start_date, end_date), on=['user_id', 'cate'],
                        how='left')
        feat.fillna(0, inplace=True)
        feat = feat.astype(int)
        if if_plot:
            print('>> 开始绘制特征%s' % (str(feat.shape)))
            for col in feat.columns:
                counts = feat[col].value_counts()
                plot_path = './vc/%s_%s/%s %s-%s.png' % (end_date.strftime('%y%m%d'), str(gap), col.replace('/', '#'),
                                                         start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
                if col not in ['user_id', 'cate', 'shop_id', 'label'] and len(counts) > 2 \
                        and if_plot and not os.path.exists(plot_path):
                    print('ploting: ', col)
                    fig, [ax1, ax2] = plt.subplots(2, 1, figsize=(8, 8))
                    sns.boxplot(x=col, y="label", orient='h', data=feat, ax=ax1)
                    ax1.set_title('%s-%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
                    sns.violinplot(x=col, y="label", orient='h', data=feat, ax=ax2)
                    plt.subplots_adjust(hspace=0.2)
                    # 指定子图的标题
                    plt.savefig(plot_path, dpi=300, bbox_inches='tight')
            del feat
            print('gc: ', gc.collect())
            feat = label

        # GR: 用户店铺

        # 用户店铺数量
        feat = pd.merge(feat, feat_user_shop_view_amt(start_date, end_date), on=['user_id', 'shop_id'], how='left')
        feat = pd.merge(feat, feat_user_shop_buy_amt(start_date, end_date), on=['user_id', 'shop_id'], how='left')
        feat = pd.merge(feat, feat_user_shop_follow_amt(start_date, end_date), on=['user_id', 'shop_id'], how='left')
        feat = pd.merge(feat, feat_user_shop_remark_amt(start_date, end_date), on=['user_id', 'shop_id'], how='left')
        feat = pd.merge(feat, feat_user_shop_cart_amt(start_date, end_date), on=['user_id', 'shop_id'], how='left')
        feat.fillna(0, inplace=True)
        feat = feat.astype(int)
        if if_plot:
            print('>> 开始绘制特征%s' % (str(feat.shape)))
            for col in feat.columns:
                counts = feat[col].value_counts()
                plot_path = './vc/%s_%s/%s %s-%s.png' % (end_date.strftime('%y%m%d'), str(gap), col.replace('/', '#'),
                                                         start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
                if col not in ['user_id', 'cate', 'shop_id', 'label'] and len(counts) > 2 \
                        and if_plot and not os.path.exists(plot_path):
                    print('ploting: ', col)
                    fig, [ax1, ax2] = plt.subplots(2, 1, figsize=(8, 8))
                    sns.boxplot(x=col, y="label", orient='h', data=feat, ax=ax1)
                    ax1.set_title('%s-%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
                    sns.violinplot(x=col, y="label", orient='h', data=feat, ax=ax2)
                    plt.subplots_adjust(hspace=0.2)
                    # 指定子图的标题
                    plt.savefig(plot_path, dpi=300, bbox_inches='tight')
            del feat
            print('gc: ', gc.collect())
            feat = label

        # 用户店铺其他
        feat = pd.merge(feat, feat_user_shop_action_ratio(start_date, end_date), on=['user_id', 'shop_id'], how='left')
        feat = pd.merge(feat, feat_user_shop_user_action_ratio(start_date, end_date), on=['user_id', 'shop_id'],
                        how='left')
        feat.fillna(0, inplace=True)
        feat = feat.astype(int)
        if if_plot:
            print('>> 开始绘制特征%s' % (str(feat.shape)))
            for col in feat.columns:
                counts = feat[col].value_counts()
                plot_path = './vc/%s_%s/%s %s-%s.png' % (end_date.strftime('%y%m%d'), str(gap), col.replace('/', '#'),
                                                         start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
                if col not in ['user_id', 'cate', 'shop_id', 'label'] and len(counts) > 2 \
                        and if_plot and not os.path.exists(plot_path):
                    print('ploting: ', col)
                    fig, [ax1, ax2] = plt.subplots(2, 1, figsize=(8, 8))
                    sns.boxplot(x=col, y="label", orient='h', data=feat, ax=ax1)
                    ax1.set_title('%s-%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
                    sns.violinplot(x=col, y="label", orient='h', data=feat, ax=ax2)
                    plt.subplots_adjust(hspace=0.2)
                    # 指定子图的标题
                    plt.savefig(plot_path, dpi=300, bbox_inches='tight')
            del feat
            print('gc: ', gc.collect())
            feat = label

        # 计算vc
        print(datetime.now())
        f = open(
            './vc/%s_%s/%s_%s.txt' % (end_date.strftime('%y%m%d'), str(gap), end_date.strftime('%y%m%d'), str(gap)),
            'w')
        for col in feat.columns:
            if col not in ['user_id', 'cate', 'shop_id', 'label']:
                counts = feat[col].value_counts()
                print('> %s: %s' % (col, str(len(counts))))
                f.write(col + ': ' + str(counts.to_json()))
                f.write('\n')
        f.close()

        # 最后调整
        feat = feat.drop(['user_id', 'cate', 'shop_id', 'label'], axis=1)
        feat = feat.add_prefix(str(gap) + '_')  # 列名加上gap标签前缀
        if if_save_gap and not if_plot: feat.to_csv(dump_path, index=False)
    return feat


def gen_feat_7(end_date, label):
    """生成某一结束时间对应的特征
    特征缓存：pd.merge(feat,...) 换成 pd.merge(pkey,...)
    """
    gap = 7
    print(datetime.now())
    print('> 遍历特征 gap=%s' % (str(gap)))
    start_date = end_date - timedelta(days=gap - 1)
    dump_path = '%s/feat/%s_%s.csv' % (cache_path, end_date.strftime('%y%m%d'), str(gap))
    if os.path.exists(dump_path) and not if_plot:
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        # 初始化feat
        feat = label
        # GR: 用户
        # 用户是否
        feat = pd.merge(feat, feat_user_if_view(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_if_buy(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_if_follow(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_if_remark(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_if_cart(start_date, end_date), on='user_id', how='left')
        feat.fillna(0, inplace=True)
        feat = feat.astype(int)
        if if_plot:
            print('>> 开始绘制特征%s' % (str(feat.shape)))
            for col in feat.columns:
                counts = feat[col].value_counts()
                plot_path = './vc/%s_%s/%s %s-%s.png' % (end_date.strftime('%y%m%d'), str(gap), col.replace('/', '#'),
                                                         start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
                if col not in ['user_id', 'cate', 'shop_id', 'label'] and len(counts) > 2 \
                        and if_plot and not os.path.exists(plot_path):
                    print('ploting: ', col)
                    fig, [ax1, ax2] = plt.subplots(2, 1, figsize=(8, 8))
                    sns.boxplot(x=col, y="label", orient='h', data=feat, ax=ax1)
                    ax1.set_title('%s-%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
                    sns.violinplot(x=col, y="label", orient='h', data=feat, ax=ax2)
                    plt.subplots_adjust(hspace=0.2)
                    # 指定子图的标题
                    plt.savefig(plot_path, dpi=300, bbox_inches='tight')
            del feat
            print('gc: ', gc.collect())
            feat = label

        # 用户数量
        feat = pd.merge(feat, feat_user_action_amt(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_view_amt(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_buy_amt(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_follow_amt(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_remark_amt(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_cart_amt(start_date, end_date), on='user_id', how='left')
        feat.fillna(0, inplace=True)
        feat = feat.astype(int)
        if if_plot:
            print('>> 开始绘制特征%s' % (str(feat.shape)))
            for col in feat.columns:
                counts = feat[col].value_counts()
                plot_path = './vc/%s_%s/%s %s-%s.png' % (end_date.strftime('%y%m%d'), str(gap), col.replace('/', '#'),
                                                         start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
                if col not in ['user_id', 'cate', 'shop_id', 'label'] and len(counts) > 2 \
                        and if_plot and not os.path.exists(plot_path):
                    print('ploting: ', col)
                    fig, [ax1, ax2] = plt.subplots(2, 1, figsize=(8, 8))
                    sns.boxplot(x=col, y="label", orient='h', data=feat, ax=ax1)
                    ax1.set_title('%s-%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
                    sns.violinplot(x=col, y="label", orient='h', data=feat, ax=ax2)
                    plt.subplots_adjust(hspace=0.2)
                    # 指定子图的标题
                    plt.savefig(plot_path, dpi=300, bbox_inches='tight')
            del feat
            print('gc: ', gc.collect())
            feat = label

        # 用户天数
        feat = pd.merge(feat, feat_user_action_day(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_view_day(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_buy_day(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_follow_day(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_remark_day(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_cart_day(start_date, end_date), on='user_id', how='left')
        feat.fillna(0, inplace=True)
        feat = feat.astype(int)
        if if_plot:
            print('>> 开始绘制特征%s' % (str(feat.shape)))
            for col in feat.columns:
                counts = feat[col].value_counts()
                plot_path = './vc/%s_%s/%s %s-%s.png' % (end_date.strftime('%y%m%d'), str(gap), col.replace('/', '#'),
                                                         start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
                if col not in ['user_id', 'cate', 'shop_id', 'label'] and len(counts) > 2 \
                        and if_plot and not os.path.exists(plot_path):
                    print('ploting: ', col)
                    fig, [ax1, ax2] = plt.subplots(2, 1, figsize=(8, 8))
                    sns.boxplot(x=col, y="label", orient='h', data=feat, ax=ax1)
                    ax1.set_title('%s-%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
                    sns.violinplot(x=col, y="label", orient='h', data=feat, ax=ax2)
                    plt.subplots_adjust(hspace=0.2)
                    # 指定子图的标题
                    plt.savefig(plot_path, dpi=300, bbox_inches='tight')
            del feat
            print('gc: ', gc.collect())
            feat = label

        # 用户其他
        feat = pd.merge(feat, feat_user_action_ratio(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_buy_rate(start_date, end_date), on='user_id', how='left')
        feat.fillna(0, inplace=True)
        feat = feat.astype(int)
        if if_plot:
            print('>> 开始绘制特征%s' % (str(feat.shape)))
            for col in feat.columns:
                counts = feat[col].value_counts()
                plot_path = './vc/%s_%s/%s %s-%s.png' % (end_date.strftime('%y%m%d'), str(gap), col.replace('/', '#'),
                                                         start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
                if col not in ['user_id', 'cate', 'shop_id', 'label'] and len(counts) > 2 \
                        and if_plot and not os.path.exists(plot_path):
                    print('ploting: ', col)
                    fig, [ax1, ax2] = plt.subplots(2, 1, figsize=(8, 8))
                    sns.boxplot(x=col, y="label", orient='h', data=feat, ax=ax1)
                    ax1.set_title('%s-%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
                    sns.violinplot(x=col, y="label", orient='h', data=feat, ax=ax2)
                    plt.subplots_adjust(hspace=0.2)
                    # 指定子图的标题
                    plt.savefig(plot_path, dpi=300, bbox_inches='tight')
            del feat
            print('gc: ', gc.collect())
            feat = label

        # GR: 用户品类
        # 用户品类数量
        feat = pd.merge(feat, feat_user_cate_view_amt(start_date, end_date), on=['user_id', 'cate'], how='left')
        feat = pd.merge(feat, feat_user_cate_buy_amt(start_date, end_date), on=['user_id', 'cate'], how='left')
        feat = pd.merge(feat, feat_user_cate_follow_amt(start_date, end_date), on=['user_id', 'cate'], how='left')
        feat = pd.merge(feat, feat_user_cate_remark_amt(start_date, end_date), on=['user_id', 'cate'], how='left')
        feat = pd.merge(feat, feat_user_cate_cart_amt(start_date, end_date), on=['user_id', 'cate'], how='left')
        feat.fillna(0, inplace=True)
        feat = feat.astype(int)
        if if_plot:
            print('>> 开始绘制特征%s' % (str(feat.shape)))
            for col in feat.columns:
                counts = feat[col].value_counts()
                plot_path = './vc/%s_%s/%s %s-%s.png' % (end_date.strftime('%y%m%d'), str(gap), col.replace('/', '#'),
                                                         start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
                if col not in ['user_id', 'cate', 'shop_id', 'label'] and len(counts) > 2 \
                        and if_plot and not os.path.exists(plot_path):
                    print('ploting: ', col)
                    fig, [ax1, ax2] = plt.subplots(2, 1, figsize=(8, 8))
                    sns.boxplot(x=col, y="label", orient='h', data=feat, ax=ax1)
                    ax1.set_title('%s-%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
                    sns.violinplot(x=col, y="label", orient='h', data=feat, ax=ax2)
                    plt.subplots_adjust(hspace=0.2)
                    # 指定子图的标题
                    plt.savefig(plot_path, dpi=300, bbox_inches='tight')
            del feat
            print('gc: ', gc.collect())
            feat = label

        # 用户品类其他

        feat = pd.merge(feat, feat_user_cate_action_ratio(start_date, end_date), on=['user_id', 'cate'], how='left')
        feat = pd.merge(feat, feat_user_cate_user_action_ratio(start_date, end_date), on=['user_id', 'cate'],
                        how='left')
        feat.fillna(0, inplace=True)
        feat = feat.astype(int)
        if if_plot:
            print('>> 开始绘制特征%s' % (str(feat.shape)))
            for col in feat.columns:
                counts = feat[col].value_counts()
                plot_path = './vc/%s_%s/%s %s-%s.png' % (end_date.strftime('%y%m%d'), str(gap), col.replace('/', '#'),
                                                         start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
                if col not in ['user_id', 'cate', 'shop_id', 'label'] and len(counts) > 2 \
                        and if_plot and not os.path.exists(plot_path):
                    print('ploting: ', col)
                    fig, [ax1, ax2] = plt.subplots(2, 1, figsize=(8, 8))
                    sns.boxplot(x=col, y="label", orient='h', data=feat, ax=ax1)
                    ax1.set_title('%s-%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
                    sns.violinplot(x=col, y="label", orient='h', data=feat, ax=ax2)
                    plt.subplots_adjust(hspace=0.2)
                    # 指定子图的标题
                    plt.savefig(plot_path, dpi=300, bbox_inches='tight')
            del feat
            print('gc: ', gc.collect())
            feat = label

        # GR: 用户店铺

        # 用户店铺数量
        feat = pd.merge(feat, feat_user_shop_view_amt(start_date, end_date), on=['user_id', 'shop_id'], how='left')
        feat = pd.merge(feat, feat_user_shop_buy_amt(start_date, end_date), on=['user_id', 'shop_id'], how='left')
        feat = pd.merge(feat, feat_user_shop_follow_amt(start_date, end_date), on=['user_id', 'shop_id'], how='left')
        feat = pd.merge(feat, feat_user_shop_remark_amt(start_date, end_date), on=['user_id', 'shop_id'], how='left')
        feat = pd.merge(feat, feat_user_shop_cart_amt(start_date, end_date), on=['user_id', 'shop_id'], how='left')
        feat.fillna(0, inplace=True)
        feat = feat.astype(int)
        if if_plot:
            print('>> 开始绘制特征%s' % (str(feat.shape)))
            for col in feat.columns:
                counts = feat[col].value_counts()
                plot_path = './vc/%s_%s/%s %s-%s.png' % (end_date.strftime('%y%m%d'), str(gap), col.replace('/', '#'),
                                                         start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
                if col not in ['user_id', 'cate', 'shop_id', 'label'] and len(counts) > 2 \
                        and if_plot and not os.path.exists(plot_path):
                    print('ploting: ', col)
                    fig, [ax1, ax2] = plt.subplots(2, 1, figsize=(8, 8))
                    sns.boxplot(x=col, y="label", orient='h', data=feat, ax=ax1)
                    ax1.set_title('%s-%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
                    sns.violinplot(x=col, y="label", orient='h', data=feat, ax=ax2)
                    plt.subplots_adjust(hspace=0.2)
                    # 指定子图的标题
                    plt.savefig(plot_path, dpi=300, bbox_inches='tight')
            del feat
            print('gc: ', gc.collect())
            feat = label

        # 用户店铺其他
        feat = pd.merge(feat, feat_user_shop_action_ratio(start_date, end_date), on=['user_id', 'shop_id'], how='left')
        feat = pd.merge(feat, feat_user_shop_user_action_ratio(start_date, end_date), on=['user_id', 'shop_id'],
                        how='left')
        feat.fillna(0, inplace=True)
        feat = feat.astype(int)
        if if_plot:
            print('>> 开始绘制特征%s' % (str(feat.shape)))
            for col in feat.columns:
                counts = feat[col].value_counts()
                plot_path = './vc/%s_%s/%s %s-%s.png' % (end_date.strftime('%y%m%d'), str(gap), col.replace('/', '#'),
                                                         start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
                if col not in ['user_id', 'cate', 'shop_id', 'label'] and len(counts) > 2 \
                        and if_plot and not os.path.exists(plot_path):
                    print('ploting: ', col)
                    fig, [ax1, ax2] = plt.subplots(2, 1, figsize=(8, 8))
                    sns.boxplot(x=col, y="label", orient='h', data=feat, ax=ax1)
                    ax1.set_title('%s-%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
                    sns.violinplot(x=col, y="label", orient='h', data=feat, ax=ax2)
                    plt.subplots_adjust(hspace=0.2)
                    # 指定子图的标题
                    plt.savefig(plot_path, dpi=300, bbox_inches='tight')
            del feat
            print('gc: ', gc.collect())
            feat = label

        # 计算vc
        print(datetime.now())
        f = open(
            './vc/%s_%s/%s_%s.txt' % (end_date.strftime('%y%m%d'), str(gap), end_date.strftime('%y%m%d'), str(gap)),
            'w')
        for col in feat.columns:
            if col not in ['user_id', 'cate', 'shop_id', 'label']:
                counts = feat[col].value_counts()
                print('> %s: %s' % (col, str(len(counts))))
                f.write(col + ': ' + str(counts.to_json()))
                f.write('\n')
        f.close()

        # 最后调整
        feat = feat.drop(['user_id', 'cate', 'shop_id', 'label'], axis=1)
        feat = feat.add_prefix(str(gap) + '_')  # 列名加上gap标签前缀
        if if_save_gap and not if_plot: feat.to_csv(dump_path, index=False)
    return feat


def gen_feat_14(end_date, label):
    """生成某一结束时间对应的特征
    特征缓存：pd.merge(feat,...) 换成 pd.merge(pkey,...)
    """
    gap = 14
    print(datetime.now())
    print('> 遍历特征 gap=%s' % (str(gap)))
    start_date = end_date - timedelta(days=gap - 1)
    dump_path = '%s/feat/%s_%s.csv' % (cache_path, end_date.strftime('%y%m%d'), str(gap))
    if os.path.exists(dump_path) and not if_plot:
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        # 初始化feat
        feat = label
        # GR: 用户
        # 用户是否
        feat = pd.merge(feat, feat_user_if_view(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_if_buy(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_if_follow(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_if_remark(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_if_cart(start_date, end_date), on='user_id', how='left')
        feat.fillna(0, inplace=True)
        feat = feat.astype(int)
        if if_plot:
            print('>> 开始绘制特征%s' % (str(feat.shape)))
            for col in feat.columns:
                counts = feat[col].value_counts()
                plot_path = './vc/%s_%s/%s %s-%s.png' % (end_date.strftime('%y%m%d'), str(gap), col.replace('/', '#'),
                                                         start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
                if col not in ['user_id', 'cate', 'shop_id', 'label'] and len(counts) > 2 \
                        and if_plot and not os.path.exists(plot_path):
                    print('ploting: ', col)
                    fig, [ax1, ax2] = plt.subplots(2, 1, figsize=(8, 8))
                    sns.boxplot(x=col, y="label", orient='h', data=feat, ax=ax1)
                    ax1.set_title('%s-%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
                    sns.violinplot(x=col, y="label", orient='h', data=feat, ax=ax2)
                    plt.subplots_adjust(hspace=0.2)
                    # 指定子图的标题
                    plt.savefig(plot_path, dpi=300, bbox_inches='tight')
            del feat
            print('gc: ', gc.collect())
            feat = label

        # 用户数量
        feat = pd.merge(feat, feat_user_action_amt(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_view_amt(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_buy_amt(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_follow_amt(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_remark_amt(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_cart_amt(start_date, end_date), on='user_id', how='left')
        feat.fillna(0, inplace=True)
        feat = feat.astype(int)
        if if_plot:
            print('>> 开始绘制特征%s' % (str(feat.shape)))
            for col in feat.columns:
                counts = feat[col].value_counts()
                plot_path = './vc/%s_%s/%s %s-%s.png' % (end_date.strftime('%y%m%d'), str(gap), col.replace('/', '#'),
                                                         start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
                if col not in ['user_id', 'cate', 'shop_id', 'label'] and len(counts) > 2 \
                        and if_plot and not os.path.exists(plot_path):
                    print('ploting: ', col)
                    fig, [ax1, ax2] = plt.subplots(2, 1, figsize=(8, 8))
                    sns.boxplot(x=col, y="label", orient='h', data=feat, ax=ax1)
                    ax1.set_title('%s-%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
                    sns.violinplot(x=col, y="label", orient='h', data=feat, ax=ax2)
                    plt.subplots_adjust(hspace=0.2)
                    # 指定子图的标题
                    plt.savefig(plot_path, dpi=300, bbox_inches='tight')
            del feat
            print('gc: ', gc.collect())
            feat = label

        # 用户天数
        feat = pd.merge(feat, feat_user_action_day(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_view_day(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_buy_day(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_follow_day(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_remark_day(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_cart_day(start_date, end_date), on='user_id', how='left')
        feat.fillna(0, inplace=True)
        feat = feat.astype(int)
        if if_plot:
            print('>> 开始绘制特征%s' % (str(feat.shape)))
            for col in feat.columns:
                counts = feat[col].value_counts()
                plot_path = './vc/%s_%s/%s %s-%s.png' % (end_date.strftime('%y%m%d'), str(gap), col.replace('/', '#'),
                                                         start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
                if col not in ['user_id', 'cate', 'shop_id', 'label'] and len(counts) > 2 \
                        and if_plot and not os.path.exists(plot_path):
                    print('ploting: ', col)
                    fig, [ax1, ax2] = plt.subplots(2, 1, figsize=(8, 8))
                    sns.boxplot(x=col, y="label", orient='h', data=feat, ax=ax1)
                    ax1.set_title('%s-%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
                    sns.violinplot(x=col, y="label", orient='h', data=feat, ax=ax2)
                    plt.subplots_adjust(hspace=0.2)
                    # 指定子图的标题
                    plt.savefig(plot_path, dpi=300, bbox_inches='tight')
            del feat
            print('gc: ', gc.collect())
            feat = label

        # 用户其他
        feat = pd.merge(feat, feat_user_action_ratio(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_buy_rate(start_date, end_date), on='user_id', how='left')
        feat.fillna(0, inplace=True)
        feat = feat.astype(int)
        if if_plot:
            print('>> 开始绘制特征%s' % (str(feat.shape)))
            for col in feat.columns:
                counts = feat[col].value_counts()
                plot_path = './vc/%s_%s/%s %s-%s.png' % (end_date.strftime('%y%m%d'), str(gap), col.replace('/', '#'),
                                                         start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
                if col not in ['user_id', 'cate', 'shop_id', 'label'] and len(counts) > 2 \
                        and if_plot and not os.path.exists(plot_path):
                    print('ploting: ', col)
                    fig, [ax1, ax2] = plt.subplots(2, 1, figsize=(8, 8))
                    sns.boxplot(x=col, y="label", orient='h', data=feat, ax=ax1)
                    ax1.set_title('%s-%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
                    sns.violinplot(x=col, y="label", orient='h', data=feat, ax=ax2)
                    plt.subplots_adjust(hspace=0.2)
                    # 指定子图的标题
                    plt.savefig(plot_path, dpi=300, bbox_inches='tight')
            del feat
            print('gc: ', gc.collect())
            feat = label

        # GR: 用户品类
        # 用户品类数量
        feat = pd.merge(feat, feat_user_cate_view_amt(start_date, end_date), on=['user_id', 'cate'], how='left')
        feat = pd.merge(feat, feat_user_cate_buy_amt(start_date, end_date), on=['user_id', 'cate'], how='left')
        feat = pd.merge(feat, feat_user_cate_follow_amt(start_date, end_date), on=['user_id', 'cate'], how='left')
        feat = pd.merge(feat, feat_user_cate_remark_amt(start_date, end_date), on=['user_id', 'cate'], how='left')
        feat = pd.merge(feat, feat_user_cate_cart_amt(start_date, end_date), on=['user_id', 'cate'], how='left')
        feat.fillna(0, inplace=True)
        feat = feat.astype(int)
        if if_plot:
            print('>> 开始绘制特征%s' % (str(feat.shape)))
            for col in feat.columns:
                counts = feat[col].value_counts()
                plot_path = './vc/%s_%s/%s %s-%s.png' % (end_date.strftime('%y%m%d'), str(gap), col.replace('/', '#'),
                                                         start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
                if col not in ['user_id', 'cate', 'shop_id', 'label'] and len(counts) > 2 \
                        and if_plot and not os.path.exists(plot_path):
                    print('ploting: ', col)
                    fig, [ax1, ax2] = plt.subplots(2, 1, figsize=(8, 8))
                    sns.boxplot(x=col, y="label", orient='h', data=feat, ax=ax1)
                    ax1.set_title('%s-%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
                    sns.violinplot(x=col, y="label", orient='h', data=feat, ax=ax2)
                    plt.subplots_adjust(hspace=0.2)
                    # 指定子图的标题
                    plt.savefig(plot_path, dpi=300, bbox_inches='tight')
            del feat
            print('gc: ', gc.collect())
            feat = label

        # 用户品类其他

        feat = pd.merge(feat, feat_user_cate_action_ratio(start_date, end_date), on=['user_id', 'cate'], how='left')
        feat = pd.merge(feat, feat_user_cate_user_action_ratio(start_date, end_date), on=['user_id', 'cate'],
                        how='left')
        feat.fillna(0, inplace=True)
        feat = feat.astype(int)
        if if_plot:
            print('>> 开始绘制特征%s' % (str(feat.shape)))
            for col in feat.columns:
                counts = feat[col].value_counts()
                plot_path = './vc/%s_%s/%s %s-%s.png' % (end_date.strftime('%y%m%d'), str(gap), col.replace('/', '#'),
                                                         start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
                if col not in ['user_id', 'cate', 'shop_id', 'label'] and len(counts) > 2 \
                        and if_plot and not os.path.exists(plot_path):
                    print('ploting: ', col)
                    fig, [ax1, ax2] = plt.subplots(2, 1, figsize=(8, 8))
                    sns.boxplot(x=col, y="label", orient='h', data=feat, ax=ax1)
                    ax1.set_title('%s-%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
                    sns.violinplot(x=col, y="label", orient='h', data=feat, ax=ax2)
                    plt.subplots_adjust(hspace=0.2)
                    # 指定子图的标题
                    plt.savefig(plot_path, dpi=300, bbox_inches='tight')
            del feat
            print('gc: ', gc.collect())
            feat = label

        # GR: 用户店铺

        # 用户店铺数量
        feat = pd.merge(feat, feat_user_shop_view_amt(start_date, end_date), on=['user_id', 'shop_id'], how='left')
        feat = pd.merge(feat, feat_user_shop_buy_amt(start_date, end_date), on=['user_id', 'shop_id'], how='left')
        feat = pd.merge(feat, feat_user_shop_follow_amt(start_date, end_date), on=['user_id', 'shop_id'], how='left')
        feat = pd.merge(feat, feat_user_shop_remark_amt(start_date, end_date), on=['user_id', 'shop_id'], how='left')
        feat = pd.merge(feat, feat_user_shop_cart_amt(start_date, end_date), on=['user_id', 'shop_id'], how='left')
        feat.fillna(0, inplace=True)
        feat = feat.astype(int)
        if if_plot:
            print('>> 开始绘制特征%s' % (str(feat.shape)))
            for col in feat.columns:
                counts = feat[col].value_counts()
                plot_path = './vc/%s_%s/%s %s-%s.png' % (end_date.strftime('%y%m%d'), str(gap), col.replace('/', '#'),
                                                         start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
                if col not in ['user_id', 'cate', 'shop_id', 'label'] and len(counts) > 2 \
                        and if_plot and not os.path.exists(plot_path):
                    print('ploting: ', col)
                    fig, [ax1, ax2] = plt.subplots(2, 1, figsize=(8, 8))
                    sns.boxplot(x=col, y="label", orient='h', data=feat, ax=ax1)
                    ax1.set_title('%s-%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
                    sns.violinplot(x=col, y="label", orient='h', data=feat, ax=ax2)
                    plt.subplots_adjust(hspace=0.2)
                    # 指定子图的标题
                    plt.savefig(plot_path, dpi=300, bbox_inches='tight')
            del feat
            print('gc: ', gc.collect())
            feat = label

        # 用户店铺其他
        feat = pd.merge(feat, feat_user_shop_action_ratio(start_date, end_date), on=['user_id', 'shop_id'], how='left')
        feat = pd.merge(feat, feat_user_shop_user_action_ratio(start_date, end_date), on=['user_id', 'shop_id'],
                        how='left')
        feat.fillna(0, inplace=True)
        feat = feat.astype(int)
        if if_plot:
            print('>> 开始绘制特征%s' % (str(feat.shape)))
            for col in feat.columns:
                counts = feat[col].value_counts()
                plot_path = './vc/%s_%s/%s %s-%s.png' % (end_date.strftime('%y%m%d'), str(gap), col.replace('/', '#'),
                                                         start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
                if col not in ['user_id', 'cate', 'shop_id', 'label'] and len(counts) > 2 \
                        and if_plot and not os.path.exists(plot_path):
                    print('ploting: ', col)
                    fig, [ax1, ax2] = plt.subplots(2, 1, figsize=(8, 8))
                    sns.boxplot(x=col, y="label", orient='h', data=feat, ax=ax1)
                    ax1.set_title('%s-%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
                    sns.violinplot(x=col, y="label", orient='h', data=feat, ax=ax2)
                    plt.subplots_adjust(hspace=0.2)
                    # 指定子图的标题
                    plt.savefig(plot_path, dpi=300, bbox_inches='tight')
            del feat
            print('gc: ', gc.collect())
            feat = label

        # 计算vc
        print(datetime.now())
        f = open(
            './vc/%s_%s/%s_%s.txt' % (end_date.strftime('%y%m%d'), str(gap), end_date.strftime('%y%m%d'), str(gap)),
            'w')
        for col in feat.columns:
            if col not in ['user_id', 'cate', 'shop_id', 'label']:
                counts = feat[col].value_counts()
                print('> %s: %s' % (col, str(len(counts))))
                f.write(col + ': ' + str(counts.to_json()))
                f.write('\n')
        f.close()

        # 最后调整
        feat = feat.drop(['user_id', 'cate', 'shop_id', 'label'], axis=1)
        feat = feat.add_prefix(str(gap) + '_')  # 列名加上gap标签前缀
        if if_save_gap and not if_plot: feat.to_csv(dump_path, index=False)
    return feat


def gen_feat_30(end_date, label):
    """生成某一结束时间对应的特征
    特征缓存：pd.merge(feat,...) 换成 pd.merge(pkey,...)
    """
    gap = 30
    print(datetime.now())
    print('> 遍历特征 gap=%s' % (str(gap)))
    start_date = end_date - timedelta(days=gap - 1)
    dump_path = '%s/feat/%s_%s.csv' % (cache_path, end_date.strftime('%y%m%d'), str(gap))
    if os.path.exists(dump_path) and not if_plot:
        feat = pd.read_csv(dump_path, na_filter=False, skip_blank_lines=True)
    else:
        # 初始化feat
        feat = label
        # GR: 用户
        # 用户是否
        feat = pd.merge(feat, feat_user_if_view(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_if_buy(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_if_follow(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_if_remark(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_if_cart(start_date, end_date), on='user_id', how='left')
        feat.fillna(0, inplace=True)
        feat = feat.astype(int)
        if if_plot:
            print('>> 开始绘制特征%s' % (str(feat.shape)))
            for col in feat.columns:
                counts = feat[col].value_counts()
                plot_path = './vc/%s_%s/%s %s-%s.png' % (end_date.strftime('%y%m%d'), str(gap), col.replace('/', '#'),
                                                         start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
                if col not in ['user_id', 'cate', 'shop_id', 'label'] and len(counts) > 2 \
                        and if_plot and not os.path.exists(plot_path):
                    print('ploting: ', col)
                    fig, [ax1, ax2] = plt.subplots(2, 1, figsize=(8, 8))
                    sns.boxplot(x=col, y="label", orient='h', data=feat, ax=ax1)
                    ax1.set_title('%s-%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
                    sns.violinplot(x=col, y="label", orient='h', data=feat, ax=ax2)
                    plt.subplots_adjust(hspace=0.2)
                    # 指定子图的标题
                    plt.savefig(plot_path, dpi=300, bbox_inches='tight')
            del feat
            print('gc: ', gc.collect())
            feat = label

        # 用户数量
        feat = pd.merge(feat, feat_user_action_amt(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_view_amt(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_buy_amt(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_follow_amt(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_remark_amt(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_cart_amt(start_date, end_date), on='user_id', how='left')
        feat.fillna(0, inplace=True)
        feat = feat.astype(int)
        if if_plot:
            print('>> 开始绘制特征%s' % (str(feat.shape)))
            for col in feat.columns:
                counts = feat[col].value_counts()
                plot_path = './vc/%s_%s/%s %s-%s.png' % (end_date.strftime('%y%m%d'), str(gap), col.replace('/', '#'),
                                                         start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
                if col not in ['user_id', 'cate', 'shop_id', 'label'] and len(counts) > 2 \
                        and if_plot and not os.path.exists(plot_path):
                    print('ploting: ', col)
                    fig, [ax1, ax2] = plt.subplots(2, 1, figsize=(8, 8))
                    sns.boxplot(x=col, y="label", orient='h', data=feat, ax=ax1)
                    ax1.set_title('%s-%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
                    sns.violinplot(x=col, y="label", orient='h', data=feat, ax=ax2)
                    plt.subplots_adjust(hspace=0.2)
                    # 指定子图的标题
                    plt.savefig(plot_path, dpi=300, bbox_inches='tight')
            del feat
            print('gc: ', gc.collect())
            feat = label

        # 用户天数
        feat = pd.merge(feat, feat_user_action_day(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_view_day(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_buy_day(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_follow_day(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_remark_day(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_cart_day(start_date, end_date), on='user_id', how='left')
        feat.fillna(0, inplace=True)
        feat = feat.astype(int)
        if if_plot:
            print('>> 开始绘制特征%s' % (str(feat.shape)))
            for col in feat.columns:
                counts = feat[col].value_counts()
                plot_path = './vc/%s_%s/%s %s-%s.png' % (end_date.strftime('%y%m%d'), str(gap), col.replace('/', '#'),
                                                         start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
                if col not in ['user_id', 'cate', 'shop_id', 'label'] and len(counts) > 2 \
                        and if_plot and not os.path.exists(plot_path):
                    print('ploting: ', col)
                    fig, [ax1, ax2] = plt.subplots(2, 1, figsize=(8, 8))
                    sns.boxplot(x=col, y="label", orient='h', data=feat, ax=ax1)
                    ax1.set_title('%s-%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
                    sns.violinplot(x=col, y="label", orient='h', data=feat, ax=ax2)
                    plt.subplots_adjust(hspace=0.2)
                    # 指定子图的标题
                    plt.savefig(plot_path, dpi=300, bbox_inches='tight')
            del feat
            print('gc: ', gc.collect())
            feat = label

        # 用户其他
        feat = pd.merge(feat, feat_user_action_ratio(start_date, end_date), on='user_id', how='left')
        feat = pd.merge(feat, feat_user_buy_rate(start_date, end_date), on='user_id', how='left')
        feat.fillna(0, inplace=True)
        feat = feat.astype(int)
        if if_plot:
            print('>> 开始绘制特征%s' % (str(feat.shape)))
            for col in feat.columns:
                counts = feat[col].value_counts()
                plot_path = './vc/%s_%s/%s %s-%s.png' % (end_date.strftime('%y%m%d'), str(gap), col.replace('/', '#'),
                                                         start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
                if col not in ['user_id', 'cate', 'shop_id', 'label'] and len(counts) > 2 \
                        and if_plot and not os.path.exists(plot_path):
                    print('ploting: ', col)
                    fig, [ax1, ax2] = plt.subplots(2, 1, figsize=(8, 8))
                    sns.boxplot(x=col, y="label", orient='h', data=feat, ax=ax1)
                    ax1.set_title('%s-%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
                    sns.violinplot(x=col, y="label", orient='h', data=feat, ax=ax2)
                    plt.subplots_adjust(hspace=0.2)
                    # 指定子图的标题
                    plt.savefig(plot_path, dpi=300, bbox_inches='tight')
            del feat
            print('gc: ', gc.collect())
            feat = label

        # GR: 用户品类
        # 用户品类数量
        feat = pd.merge(feat, feat_user_cate_view_amt(start_date, end_date), on=['user_id', 'cate'], how='left')
        feat = pd.merge(feat, feat_user_cate_buy_amt(start_date, end_date), on=['user_id', 'cate'], how='left')
        feat = pd.merge(feat, feat_user_cate_follow_amt(start_date, end_date), on=['user_id', 'cate'], how='left')
        feat = pd.merge(feat, feat_user_cate_remark_amt(start_date, end_date), on=['user_id', 'cate'], how='left')
        feat = pd.merge(feat, feat_user_cate_cart_amt(start_date, end_date), on=['user_id', 'cate'], how='left')
        feat.fillna(0, inplace=True)
        feat = feat.astype(int)
        if if_plot:
            print('>> 开始绘制特征%s' % (str(feat.shape)))
            for col in feat.columns:
                counts = feat[col].value_counts()
                plot_path = './vc/%s_%s/%s %s-%s.png' % (end_date.strftime('%y%m%d'), str(gap), col.replace('/', '#'),
                                                         start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
                if col not in ['user_id', 'cate', 'shop_id', 'label'] and len(counts) > 2 \
                        and if_plot and not os.path.exists(plot_path):
                    print('ploting: ', col)
                    fig, [ax1, ax2] = plt.subplots(2, 1, figsize=(8, 8))
                    sns.boxplot(x=col, y="label", orient='h', data=feat, ax=ax1)
                    ax1.set_title('%s-%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
                    sns.violinplot(x=col, y="label", orient='h', data=feat, ax=ax2)
                    plt.subplots_adjust(hspace=0.2)
                    # 指定子图的标题
                    plt.savefig(plot_path, dpi=300, bbox_inches='tight')
            del feat
            print('gc: ', gc.collect())
            feat = label

        # 用户品类天数
        feat = pd.merge(feat, feat_user_cate_view_day(start_date, end_date), on=['user_id', 'cate'], how='left')
        feat = pd.merge(feat, feat_user_cate_buy_day(start_date, end_date), on=['user_id', 'cate'], how='left')
        feat = pd.merge(feat, feat_user_cate_follow_day(start_date, end_date), on=['user_id', 'cate'], how='left')
        feat = pd.merge(feat, feat_user_cate_remark_day(start_date, end_date), on=['user_id', 'cate'], how='left')
        feat = pd.merge(feat, feat_user_cate_cart_day(start_date, end_date), on=['user_id', 'cate'], how='left')
        feat.fillna(0, inplace=True)
        feat = feat.astype(int)
        if if_plot:
            print('>> 开始绘制特征%s' % (str(feat.shape)))
            for col in feat.columns:
                counts = feat[col].value_counts()
                plot_path = './vc/%s_%s/%s %s-%s.png' % (end_date.strftime('%y%m%d'), str(gap), col.replace('/', '#'),
                                                         start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
                if col not in ['user_id', 'cate', 'shop_id', 'label'] and len(counts) > 2 \
                        and if_plot and not os.path.exists(plot_path):
                    print('ploting: ', col)
                    fig, [ax1, ax2] = plt.subplots(2, 1, figsize=(8, 8))
                    sns.boxplot(x=col, y="label", orient='h', data=feat, ax=ax1)
                    ax1.set_title('%s-%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
                    sns.violinplot(x=col, y="label", orient='h', data=feat, ax=ax2)
                    plt.subplots_adjust(hspace=0.2)
                    # 指定子图的标题
                    plt.savefig(plot_path, dpi=300, bbox_inches='tight')
            del feat
            print('gc: ', gc.collect())
            feat = label

        # 用户品类其他
        feat = pd.merge(feat, feat_user_cate_action_ratio(start_date, end_date), on=['user_id', 'cate'], how='left')
        feat = pd.merge(feat, feat_user_cate_user_action_ratio(start_date, end_date), on=['user_id', 'cate'],
                        how='left')
        feat = pd.merge(feat, feat_user_cate_first_hour(start_date, end_date), on=['user_id', 'cate'], how='left')
        feat = pd.merge(feat, feat_user_cate_last_hour(start_date, end_date), on=['user_id', 'cate'], how='left')
        feat = pd.merge(feat, feat_user_cate_last_amt(start_date, end_date), on=['user_id', 'cate'], how='left')
        feat.fillna(0, inplace=True)
        feat = feat.astype(int)
        if if_plot:
            print('>> 开始绘制特征%s' % (str(feat.shape)))
            for col in feat.columns:
                counts = feat[col].value_counts()
                plot_path = './vc/%s_%s/%s %s-%s.png' % (end_date.strftime('%y%m%d'), str(gap), col.replace('/', '#'),
                                                         start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
                if col not in ['user_id', 'cate', 'shop_id', 'label'] and len(counts) > 2 \
                        and if_plot and not os.path.exists(plot_path):
                    print('ploting: ', col)
                    fig, [ax1, ax2] = plt.subplots(2, 1, figsize=(8, 8))
                    sns.boxplot(x=col, y="label", orient='h', data=feat, ax=ax1)
                    ax1.set_title('%s-%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
                    sns.violinplot(x=col, y="label", orient='h', data=feat, ax=ax2)
                    plt.subplots_adjust(hspace=0.2)
                    # 指定子图的标题
                    plt.savefig(plot_path, dpi=300, bbox_inches='tight')
            del feat
            print('gc: ', gc.collect())
            feat = label

        # 特殊
        feat = pd.merge(feat, feat_user_cate_wait(start_date, end_date), on=['user_id', 'cate'], how='left')
        feat.fillna(0, inplace=True)
        feat = feat.astype(int)
        if if_plot:
            print('>> 开始绘制特征%s' % (str(feat.shape)))
            for col in feat.columns:
                counts = feat[col].value_counts()
                plot_path = './vc/%s_%s/%s %s-%s.png' % (end_date.strftime('%y%m%d'), str(gap), col.replace('/', '#'),
                                                         start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
                if col not in ['user_id', 'cate', 'shop_id', 'label'] and len(counts) > 2 \
                        and if_plot and not os.path.exists(plot_path):
                    print('ploting: ', col)
                    fig, [ax1, ax2] = plt.subplots(2, 1, figsize=(8, 8))
                    sns.boxplot(x=col, y="label", orient='h', data=feat, ax=ax1)
                    ax1.set_title('%s-%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
                    sns.violinplot(x=col, y="label", orient='h', data=feat, ax=ax2)
                    plt.subplots_adjust(hspace=0.2)
                    # 指定子图的标题
                    plt.savefig(plot_path, dpi=300, bbox_inches='tight')
            del feat
            print('gc: ', gc.collect())
            feat = label

        # GR: 用户店铺
        # 用户店铺数量
        feat = pd.merge(feat, feat_user_shop_view_amt(start_date, end_date), on=['user_id', 'shop_id'], how='left')
        feat = pd.merge(feat, feat_user_shop_buy_amt(start_date, end_date), on=['user_id', 'shop_id'], how='left')
        feat = pd.merge(feat, feat_user_shop_follow_amt(start_date, end_date), on=['user_id', 'shop_id'], how='left')
        feat = pd.merge(feat, feat_user_shop_remark_amt(start_date, end_date), on=['user_id', 'shop_id'], how='left')
        feat = pd.merge(feat, feat_user_shop_cart_amt(start_date, end_date), on=['user_id', 'shop_id'], how='left')
        feat.fillna(0, inplace=True)
        feat = feat.astype(int)
        if if_plot:
            print('>> 开始绘制特征%s' % (str(feat.shape)))
            for col in feat.columns:
                counts = feat[col].value_counts()
                plot_path = './vc/%s_%s/%s %s-%s.png' % (end_date.strftime('%y%m%d'), str(gap), col.replace('/', '#'),
                                                         start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
                if col not in ['user_id', 'cate', 'shop_id', 'label'] and len(counts) > 2 \
                        and if_plot and not os.path.exists(plot_path):
                    print('ploting: ', col)
                    fig, [ax1, ax2] = plt.subplots(2, 1, figsize=(8, 8))
                    sns.boxplot(x=col, y="label", orient='h', data=feat, ax=ax1)
                    ax1.set_title('%s-%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
                    sns.violinplot(x=col, y="label", orient='h', data=feat, ax=ax2)
                    plt.subplots_adjust(hspace=0.2)
                    # 指定子图的标题
                    plt.savefig(plot_path, dpi=300, bbox_inches='tight')
            del feat
            print('gc: ', gc.collect())
            feat = label

        # 用户店铺其他
        feat = pd.merge(feat, feat_user_shop_action_ratio(start_date, end_date), on=['user_id', 'shop_id'], how='left')
        feat = pd.merge(feat, feat_user_shop_user_action_ratio(start_date, end_date), on=['user_id', 'shop_id'],
                        how='left')
        feat = pd.merge(feat, feat_user_shop_first_hour(start_date, end_date), on=['user_id', 'shop_id'], how='left')
        feat = pd.merge(feat, feat_user_shop_last_hour(start_date, end_date), on=['user_id', 'shop_id'], how='left')
        feat = pd.merge(feat, feat_user_shop_last_amt(start_date, end_date), on=['user_id', 'shop_id'], how='left')
        feat.fillna(0, inplace=True)
        feat = feat.astype(int)
        if if_plot:
            print('>> 开始绘制特征%s' % (str(feat.shape)))
            for col in feat.columns:
                counts = feat[col].value_counts()
                plot_path = './vc/%s_%s/%s %s-%s.png' % (end_date.strftime('%y%m%d'), str(gap), col.replace('/', '#'),
                                                         start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
                if col not in ['user_id', 'cate', 'shop_id', 'label'] and len(counts) > 2 \
                        and if_plot and not os.path.exists(plot_path):
                    print('ploting: ', col)
                    fig, [ax1, ax2] = plt.subplots(2, 1, figsize=(8, 8))
                    sns.boxplot(x=col, y="label", orient='h', data=feat, ax=ax1)
                    ax1.set_title('%s-%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
                    sns.violinplot(x=col, y="label", orient='h', data=feat, ax=ax2)
                    plt.subplots_adjust(hspace=0.2)
                    # 指定子图的标题
                    plt.savefig(plot_path, dpi=300, bbox_inches='tight')
            del feat
            print('gc: ', gc.collect())
            feat = label

        # 特殊
        feat = pd.merge(feat, feat_user_shop_wait(start_date, end_date), on=['user_id', 'shop_id'], how='left')
        feat.fillna(0, inplace=True)
        feat = feat.astype(int)
        if if_plot:
            print('>> 开始绘制特征%s' % (str(feat.shape)))
            for col in feat.columns:
                counts = feat[col].value_counts()
                plot_path = './vc/%s_%s/%s %s-%s.png' % (end_date.strftime('%y%m%d'), str(gap), col.replace('/', '#'),
                                                         start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d'))
                if col not in ['user_id', 'cate', 'shop_id', 'label'] and len(counts) > 2 \
                        and if_plot and not os.path.exists(plot_path):
                    print('ploting: ', col)
                    fig, [ax1, ax2] = plt.subplots(2, 1, figsize=(8, 8))
                    sns.boxplot(x=col, y="label", orient='h', data=feat, ax=ax1)
                    ax1.set_title('%s-%s' % (start_date.strftime('%y%m%d'), end_date.strftime('%y%m%d')))
                    sns.violinplot(x=col, y="label", orient='h', data=feat, ax=ax2)
                    plt.subplots_adjust(hspace=0.2)
                    # 指定子图的标题
                    plt.savefig(plot_path, dpi=300, bbox_inches='tight')
            del feat
            print('gc: ', gc.collect())
            feat = label

        # 计算vc
        print(datetime.now())
        f = open(
            './vc/%s_%s/%s_%s.txt' % (end_date.strftime('%y%m%d'), str(gap), end_date.strftime('%y%m%d'), str(gap)),
            'w')
        for col in feat.columns:
            if col not in ['user_id', 'cate', 'shop_id', 'label']:
                counts = feat[col].value_counts()
                print('> %s: %s' % (col, str(len(counts))))
                f.write(col + ': ' + str(counts.to_json()))
                f.write('\n')
        f.close()

        # 最后调整
        feat = feat.drop(['user_id', 'cate', 'shop_id', 'label'], axis=1)
        feat = feat.add_prefix(str(gap) + '_')  # 列名加上gap标签前缀
        if if_save_gap and not if_plot: feat.to_csv(dump_path, index=False)
    return feat


def gen_label(end_date, label_gap, mark):
    """生成某一结束时间对应的特征label
    label：预测label,提交集=-1
    """
    print(datetime.now())
    print('> 获取标签')
    if mark == 'submit':
        action = feat_action(end_date - timedelta(days=label_gap - 1), end_date)[['user_id', 'sku_id']]
        pkey = action.drop_duplicates(['user_id', 'sku_id'])
        label = pd.concat([pkey.reset_index(drop=True), pd.DataFrame({'label': [-1] * pkey.shape[0]})], axis=1)
    else:
        # 可能购买
        action = feat_action(end_date - timedelta(days=label_gap - 1), end_date)[['user_id', 'sku_id']]
        product = pd.read_csv(product_path, na_filter=False, usecols=['sku_id', 'cate', 'shop_id'])
        pkey = pd.merge(action, product, on='sku_id', how='left')
        pkey = pkey.drop(['sku_id'], axis=1)
        pkey = pkey.drop_duplicates(['user_id', 'cate', 'shop_id'])
        # 真实购买
        buy = feat_buy_plus(end_date + timedelta(days=1), end_date + timedelta(days=7))[['user_id', 'cate', 'shop_id']]
        buy = buy.drop_duplicates(['user_id', 'cate', 'shop_id'])
        label_1 = pd.concat([buy.reset_index(drop=True), pd.DataFrame({'label': [1] * buy.shape[0]})], axis=1)
        label = pd.merge(pkey, label_1, on=['user_id', 'cate', 'shop_id'], how='left')
        label.fillna(0, inplace=True)
        print('真实购买', buy.shape)
        print('可能购买', pkey.shape)
    # 最后调整
    label = label.astype('int')
    print("shape", label.shape)
    return label
