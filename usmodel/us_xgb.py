# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @DATE    : 5/14/2019
# @Author  : xiaotong niu
# @File    : us_xgb.py
# @Project : JData-Predict
# @Github  ：https://github.com/isNxt
# @Describ : ...

import os
import time
from datetime import datetime
import numpy as np
import pandas as pd
import xgboost as xgb
from merg_us import gen_feat
from sklearn import metrics
from sklearn.model_selection import GridSearchCV
from xgboost import XGBClassifier
import matplotlib.pyplot as plt

# %% 配置
# 输出设置
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)
plt.rcParams['figure.figsize'] = (12, 8)

# 时间划分
data_start_date = "2018-02-01"
data_end_date = "2018-04-15"

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


# %% xgboost模型
def impt_feat(df_train, drop_column):
    """ back 重要性
    """
    dump_path = './out/bst.model'
    if os.path.exists(dump_path):
        # 获取特征
        print(datetime.now())
        print('>> 开始获取特征')
        feat_cols = (df_train.drop(drop_column, axis=1)).columns
        print('<< 完成获取特征')
        # 测试模型
        print('>> 开始加载模型')
        bst = xgb.Booster(model_file=dump_path)
        f_score = bst.get_fscore()
        f_name = []
        for id in list(f_score.keys()):
            print(id)
            f_name.append(feat_cols[int(id[1:])])
        f_id = pd.DataFrame({'f_id': list(f_score.keys())})
        f_pro = pd.DataFrame({'f_pro': list(f_score.values())})
        f_name = pd.DataFrame({'f_name': f_name})
        f_score = pd.concat([f_id, f_name, f_pro], axis=1)
        f_score.sort_values(by=['f_pro'], ascending=[0], inplace=True)
        f_score.to_csv('./out/impt_feat.csv', index=False)


def report(df):
    product = pd.read_csv(product_path, na_filter=False)
    df = pd.merge(df, product, on='sku_id', how='left')

    real = df[df['label'] == 1]
    pred = df[df['pred'] == 1]

    # 所有购买用户品类
    all_set = real[['user_id', 'cate']]
    # 所有用户品类店铺对
    all_item_pair = real['user_id'].map(str) + '-' + real['cate'].map(str) + '-' + real['sku_id'].map(str)
    all_item_pair = np.array(all_item_pair)

    # 所有预测购买用户品类
    all_pred_set = pred[['user_id', 'cate']]
    # 所有预测用户品类店铺对
    all_pred_item_pair = pred['user_id'].map(str) + '-' + pred['cate'].map(str) + '-' + pred['sku_id'].map(str)
    all_pred_item_pair = np.array(all_pred_item_pair)

    # 计算所有用户品类购买评价指标
    pos, neg = 0, 0
    for pkey in all_pred_set:
        if pkey in all_set:
            pos += 1
        else:
            neg += 1
    all_set_acc = 1.0 * pos / (pos + neg)
    all_set_recall = 1.0 * pos / len(all_set)
    print('所有用户品类中预测购买用户品类的准确率为 ' + str(all_set_acc))
    print('所有用户品类中预测购买用户品类的召回率' + str(all_set_recall))

    pos, neg = 0, 0
    for item_pair in all_pred_item_pair:
        if item_pair in all_item_pair:
            pos += 1
        else:
            neg += 1
    all_pair_acc = 1.0 * pos / (pos + neg)
    all_pair_recall = 1.0 * pos / len(all_item_pair)
    print('所有用户品类中预测购买店铺的准确率为 ' + str(all_pair_acc))
    print('所有用户品类中预测购买店铺的召回率' + str(all_pair_recall))
    F11 = 6.0 * all_set_recall * all_set_acc / (5.0 * all_set_recall + all_set_acc)
    F12 = 5.0 * all_pair_acc * all_pair_recall / (2.0 * all_pair_recall + 3 * all_pair_acc)
    score = 0.4 * F11 + 0.6 * F12
    print('F11=' + str(F11))
    print('F12=' + str(F12))
    print('score=' + str(score))


def f11_score(real, pred):
    # 计算所有用户购买评价指标
    precision = metrics.precision_score(real, pred)
    recall = metrics.recall_score(real, pred)
    print('准确率: ' + str(precision))
    print('召回率: ' + str(recall))
    F11 = 3.0 * precision * recall / (2.0 * precision + recall)
    print('F11=' + str(F11))
    return F11


def f12_score(real, pred):
    # 计算所有用户购买评价指标
    precision = metrics.precision_score(real, pred)
    recall = metrics.recall_score(real, pred)
    print('准确率: ' + str(precision))
    print('召回率: ' + str(recall))
    F11 = 3.0 * precision * recall / (2.0 * precision + recall)
    print('F11=' + str(F11))
    return F11


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
    xgb_model = XGBClassifier(objective='binary:logistic', seed=27)
    param_list = [
        {'max_depth': range(3, 10, 1)},
        {'min_child_weight': range(1, 6, 1)},
        {'gamma': [i / 10.0 for i in range(0, 5)]},
        {'subsample': [i / 10.0 for i in range(6, 10)]},
        {'colsample_bytree': [i / 10.0 for i in range(6, 10)]},
        {'n_estimators': [50, 100, 200, 500, 1000]},
        {'learning_rate': [0.001, 0.01, 0.05, 0.1, 0.2]},
        {'scale_pos_weight': [1, 2, 3, 4, 5]},
        {'reg_alpha': [1e-5, 1e-2, 0.1, 1, 100]}
    ]
    bst_param = {'silent': 0, 'nthread': 4}
    for param_dict in param_list:
        print(datetime.now())
        clf = GridSearchCV(estimator=xgb_model, param_grid=param_dict, scoring='roc_auc', cv=5, verbose=1)
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
    df = pd.DataFrame(bst_param)
    df.to_csv('./out/bst_param.csv')
    print('<< 完成优化参数')


def model(df_train, df_test, drop_column):
    """ 构造
    xgboost模型训练测试
    """
    # 划分(X,y)
    print(datetime.now())
    print('>> 开始划分X,y')
    X_train = df_train.drop(drop_column, axis=1).values
    y_train = df_train['label'].values
    X_test = df_test.drop(drop_column, axis=1).values
    y_test = df_test['label'].values
    print('>> 开始获取特征')
    print('<< 完成划分数据')

    # 设置参数(gridcv最佳)
    print(datetime.now())
    print('>> 开始设置参数')
    dtrain = xgb.DMatrix(X_train, label=y_train)
    dtest = xgb.DMatrix(X_test, label=y_test)
    param = {
        # 默认
        'silent': 1,
        'objective': 'binary:logistic',
        'scale_pos_weight': 1,
        'eval_metric': 'logloss',
        # 调整
        'learning_rate': 0.1,
        'n_estimators': 1000,
        'max_depth': 3,
        'min_child_weight': 5,
        'gamma': 0,
        'subsample': 1.0,
        'colsample_bytree': 0.8,
        'eta': 0.05,
    }
    num_round = 500
    evallist = [(dtest, 'eval'), (dtrain, 'train')]
    print('<< 完成设置参数')

    # 训练模型(watchlist)
    print(datetime.now())
    print('>> 开始训练模型')
    bst = xgb.train(param, dtrain, num_round, evallist, early_stopping_rounds=20)
    bst.save_model("./out/bst.model")
    print('<< 完成训练模型')

    # 测试模型
    print(datetime.now())
    print('>> 开始测试模型')
    y_probab = bst.predict(dtest)
    print('> 概率转换0,1')
    df_pred = pd.concat([df_test, pd.DataFrame({'probab': y_probab, 'pred': [0] * len(y_probab)})], axis=1)
    df_pred = df_pred.sort_values(by='probab', ascending=False)
    df_pred = df_pred.drop_duplicates(['user_id', 'cate'], keep='first')
    df_pred = df_pred.reset_index(drop=True)

    df_same = df_pred
    df_same.ix[:int(np.sum(df_test['label'].values)), 'pred'] = 1
    df_same.to_csv('./out/test_pred_same.csv', index=False)
    print('前%s行[same] label=1：' % (str(int(np.sum(df_same['label'].values)))))
    report(df_same)

    for i in range(10000, 160000, 10000):
        df = df_pred
        print('前%s行 label=1：' % (str(i)))
        df.ix[:i, 'pred'] = 1
        df.to_csv('./out/test_pred_%s.csv' % (str(i)), index=False)
        report(df)

    print('<< 完成测试模型')


def submit(df_sub, drop_column):
    """
    xgboost模型提交
    """
    dump_path = './out/bst.jcate'
    if os.path.exists(dump_path):
        # 划分(X,y)
        print(datetime.now())
        print('>> 开始划分X,y')
        X_sub = df_sub.drop(drop_column, axis=1).values
        print('<< 完成划分数据')

        # 预测提交
        print('>> 开始预测提交')
        dsub = xgb.DMatrix(X_sub)
        # dsub.save_binary('./out/dsub.buffer')
        bst = xgb.Booster(model_file=dump_path)
        y_probab = bst.predict(dsub)
        print('> 概率转换0,1')
        df_pred = pd.concat([df_sub, pd.DataFrame({'probab': y_probab, 'pred': [0] * len(y_probab)})])
        df_pred = df_pred.sort_values(by='probab', ascending=False)
        df_pred.ix[:160000, 'label'] = 1
        df_pred.to_csv('./out/sub_pred.csv', index=False)
        # 格式化提交
        df_pred = df_pred[df_pred['label'] == 1]
        df_pred = df_pred[drop_column]
        df_pred = df_pred.drop(['label'], axis=1)
        df_pred.to_csv(submit_path + '/user.csv', index=False)
        print('> 提交结果', df_pred.shape)
        print('<< 完成预测提交!')
    else:
        print('<< 没有训练模型')


def main():
    """
    主流程
    """
    # 定义参数
    time_gap = [1, 2, 3, 7, 14]
    train_end_date = '2018-4-8'
    test_end_date = '2018-4-1'
    sub_end_date = '2018-4-15'
    drop_column = ['user_id', 'sku_id', 'label']
    label_gap = 3  # [2,3,7]

    # 生成特征
    df_train = gen_feat(train_end_date, time_gap, label_gap, 'train')
    df_test = gen_feat(test_end_date, time_gap, label_gap, 'test')

    # 优化参数
    # gridcv(df_train, drop_column)

    # 构造模型
    # model(df_train, df_test, drop_column)
    # impt_feat(df_train, drop_column)

    # 生成提交结果
    df_sub = gen_feat(sub_end_date, time_gap, label_gap, 'submit')
    # submit(df_sub, drop_column)


if __name__ == "__main__":
    main()
