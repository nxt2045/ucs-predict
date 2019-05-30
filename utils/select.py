# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @DATE    : 4/17/2019
# @Author  : xiaotong
# @File    : anaylse
# @Project : PyCharm
# @Github  ：https://github.com/isNxt
# @Describ : ...
import seaborn as sns
import matplotlib.pyplot as plt
from feature.feat_user import *
from feature.feat_cate import *
import os, time
import numpy as np
import pandas as pd
import matplotlib.dates as mdates
from pandas.plotting import register_matplotlib_converters
from matplotlib.font_manager import FontProperties
import xgboost as xgb
from sklearn import metrics
from sklearn.model_selection import GridSearchCV
from xgboost import XGBClassifier

myfont = FontProperties(fname=r'C:\Windows\Fonts\msyh.ttc', size=14)
sns.set(font=myfont.get_name())

# 配置
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
cache_path = '../cache'


def report_u(real, pred):
    # print('real:', real.shape)
    # # print(real.head())
    # print('pred:', pred.shape)
    # # print(pred.head())

    # 所有购买用户
    all_1 = real[['user_id']]
    # print('all_1:', all_1.shape)
    # 所有预测购买用户
    all_pred_1 = pred[['user_id']]
    # print('all_pred_1:', all_pred_1.shape)
    # 计算所有用户购买评价指标
    intersect = pd.merge(all_1, all_pred_1, how='inner')
    pos = intersect.shape[0]
    neg = all_pred_1.shape[0] - pos
    # print('pos:', pos)
    # print('neg:', neg)
    all_1_acc = 1.0 * pos / (pos + neg)
    all_1_recall = 1.0 * pos / len(all_1)
    # print('所有用户中预测购买用户的准确率为 ' + str(all_1_acc))
    # print('所有用户中预测购买用户的召回率' + str(all_1_recall))
    F11 = 3.0 * all_1_recall * all_1_acc / (2.0 * all_1_recall + all_1_acc)
    print('F11=' + str(F11))

def report_uc(real, pred):
    # print('real:', real.shape)
    # # print(real.head())
    # print('pred:', pred.shape)
    # # print(pred.head())

    # 所有购买用户品类
    all_2 = real[['user_id', 'cate']]
    # print('all_2:', all_2.shape)
    # 所有预测购买用户品类
    all_pred_2 = pred[['user_id', 'cate']]
    # print('all_pred_2:', all_pred_2.shape)
    # 计算所有用户品类购买评价指标
    intersect = pd.merge(all_2, all_pred_2, how='inner')
    pos = intersect.shape[0]
    neg = all_pred_2.shape[0] - pos
    # print('pos:', pos)
    # print('neg:', neg)
    all_2_acc = 1.0 * pos / (pos + neg)
    all_2_recall = 1.0 * pos / len(all_2)
    # print('所有用户品类中预测购买用户品类的准确率为 ' + str(all_2_acc))
    # print('所有用户品类中预测购买用户品类的召回率' + str(all_2_recall))
    F11 = 3.0 * all_2_recall * all_2_acc / (2.0 * all_2_recall + all_2_acc)
    print('F11=' + str(F11))


def report_ucs(real, pred):
    # print('real:', real.shape)
    # # print(real.head())
    # print('pred:', pred.shape)
    # # print(pred.head())

    # 所有购买用户品类
    all_2 = real[['user_id', 'cate']]
    # print('all_2:', all_2.shape)
    # 所有预测购买用户品类
    all_pred_2 = pred[['user_id', 'cate']]
    # print('all_pred_2:', all_pred_2.shape)
    # 计算所有用户品类购买评价指标
    intersect = pd.merge(all_2, all_pred_2, how='inner')
    pos = intersect.shape[0]
    neg = all_pred_2.shape[0] - pos
    # print('pos:', pos)
    # print('neg:', neg)
    all_2_acc = 1.0 * pos / (pos + neg)
    all_2_recall = 1.0 * pos / len(all_2)
    # print('所有用户品类中预测购买用户品类的准确率为 ' + str(all_2_acc))
    # print('所有用户品类中预测购买用户品类的召回率' + str(all_2_recall))
    F11 = 3.0 * all_2_recall * all_2_acc / (2.0 * all_2_recall + all_2_acc)
    # print('F11=' + str(F11))

    # 所有用户品类店铺对
    all_3 = real[['user_id', 'cate', 'shop_id']]
    # print('all_3:', all_3.shape)
    # 所有预测用户品类店铺对
    all_pred_3 = pred[['user_id', 'cate', 'shop_id']]
    # print('all_pred_3:', all_pred_3.shape)
    intersect = pd.merge(all_3, all_pred_3, how='inner')
    pos = intersect.shape[0]
    neg = all_pred_2.shape[0] - pos
    # print('pos:', pos)
    # print('neg:', neg)
    all_3_acc = 1.0 * pos / (pos + neg)
    all_3_recall = 1.0 * pos / len(all_3)
    # print('所有用户品类中预测购买店铺的准确率为 ' + str(all_3_acc))
    # print('所有用户品类中预测购买店铺的召回率' + str(all_3_recall))
    F12 = 5.0 * all_3_acc * all_3_recall / (2.0 * all_3_recall + 3.0 * all_3_acc)
    # print('F12=' + str(F12))

    score = 0.4 * F11 + 0.6 * F12
    print('score=' + str(score))

def impt_feat(df_train, drop_column):
    """ back 重要性
    """
    dump_path = './out/bst.model'
    if os.path.exists(dump_path):
        # 获取特征
        print(datetime.now())
        print('>> 开始特征重要性')
        feat_cols = (df_train.drop(drop_column, axis=1)).columns
        print('<< 完成特征重要性')
        # 测试模型
        bst = xgb.Booster(model_file=dump_path)
        f_score = bst.get_fscore()
        f_name = []
        for id in list(f_score.keys()):
            f_name.append(feat_cols[int(id[1:])])
        f_id = pd.DataFrame({'f_id': list(f_score.keys())})
        f_pro = pd.DataFrame({'f_pro': list(f_score.values())})
        f_name = pd.DataFrame({'f_name': f_name})
        f_score = pd.concat([f_id, f_name, f_pro], axis=1)
        f_score.sort_values(by=['f_pro'], ascending=[0], inplace=True)
        f_score.to_csv('./out/impt_feat.csv', index=False)

def gridcv(df_train, drop_column):
    """ 参数
    xgboost参数优化
    """
    # TODO: Success but Warning
    # 划分(X,y)
    print(datetime.now())
    print('>> 开始划分X,y')
    X_train = df_train.drop(drop_column, axis=1).values
    y_train = df_train['label'].values
    print('<< 完成划分数据')

    # 优化参数
    print(datetime.now())
    print('>> 开始优化参数')
    # F11_score = metrics.make_scorer(f11_score, greater_is_better=True, needs_proba=True)
    # scoring = {'F11': F11_score}
    xgb_model = XGBClassifier(learning_rate=0.1, n_estimators=200, max_depth=5, min_child_weight=2, gamma=0,
                              subsample=0.8, colsample_bytree=0.8, objective='binary:logistic', nthread=4,
                              scale_pos_weight=1, seed=27)
    param_list = [
        {'max_depth': range(3, 10, 1)},
        {'min_child_weight': range(1, 6, 1)},
        {'gamma': [i / 10.0 for i in range(0, 5)]},
        {'subsample': [i / 10.0 for i in range(6, 10)]},
        {'colsample_bytree': [i / 10.0 for i in range(6, 10)]},
        {'n_estimators': [50, 100, 200, 500, 1000]},
        {'learning_rate': [0.001, 0.01, 0.05, 0.1, 0.2]}
    ]
    bst_param = {'silent': 0, 'nthread': 4}
    for param_dict in param_list:
        print(datetime.now())
        clf = GridSearchCV(estimator=xgb_model, param_grid=param_dict, cv=5, n_jobs=-1, verbose=10,
                           return_train_score=True)
        clf.fit(X_train, y_train)
        bst_param.update(clf.best_params_)
        print(datetime.now())
        print("最佳参数:", clf.best_params_)
        print("最佳得分:", clf.best_score_)
        print("搜索得分:")
        means = clf.cv_results_['mean_test_score']
        stds = clf.cv_results_['std_test_score']
        for mean, std, params in zip(means, stds, clf.cv_results_['params']):
            print("%0.3f (+/-%0.03f) for %r"
                  % (mean, std * 2, params))
    print("最佳参数组合:")
    print(bst_param)
    print('<< 完成优化参数')

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
