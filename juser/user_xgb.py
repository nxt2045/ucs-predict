# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @DATE    : 5/14/2019
# @Author  : xiaotong niu
# @File    : user_xgb.py
# @Project : JData-Predict
# @Github  ：https://github.com/isNxt
# @Describ : ...

import os
import time
from datetime import datetime
import numpy as np
import pandas as pd
import xgboost as xgb
from merg_user import gen_feat
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
def impt_feat(feat_cols, bst):
    """ feat 重要性
    """
    f_score = bst.get_fscore()
    f_name = []
    for id in list(f_score.keys()):
        f_name.append(feat_cols[int(id)])
    f_id = pd.DataFrame({'f_id': list(f_score.keys())})
    f_pro = pd.DataFrame({'f_pro': list(f_score.values())})
    f_name = pd.DataFrame({'f_name': f_name})
    f_score = pd.concat([f_id, f_name, f_pro], axis=1)
    f_score.sort_values(by=['f_pro'], ascending=[0], inplace=True)
    f_score.to_csv('./output/impt_feat.csv', index=False)


def f11_score(real, pred):
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
    # F11_score = metrics.make_scorer(f11_score, greater_is_better=True, needs_proba=True)
    # scoring = {'F11': F11_score}
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
        clf = GridSearchCV(estimator=xgb_model, param_grid=param_dict, scoring='roc_auc', cv=5,verbose=1)
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
    df.to_csv('./output/gridcv/bst_param.csv')
    print('<< 完成优化参数')


def train(df_train, drop_column):
    """ 训练
    xgboost模型训练
    """
    # 划分(X,y)
    print(datetime.now())
    print('>> 开始划分X,y')
    X_train = df_train.drop(drop_column, axis=1).values
    y_train = df_train['label'].values
    feat_cols = df_train.drop(drop_column, axis=1).columns
    print('<< 完成划分数据')

    # 训练模型
    print(datetime.now())
    print('>> 开始训练模型')
    bst_param = {'silent': 0, 'nthread': -1, 'learning_rate': 0.1, 'n_estimators': 200,
                 'max_depth': 5, 'min_child_weight': 2, 'gamma': 0, 'subsample': 0.8, 'colsample_bytree': 0.8,
                 'objective': 'binary:logistic', 'scale_pos_weight': 1, 'seed': 27, 'tree_method': 'exact'}
    dtrain = xgb.DMatrix(X_train, label=y_train)
    # dtrain.save_binary('./output/dtrain.buffer')
    num_rounds = 1000  # 迭代次数
    bst = xgb.train(bst_param, dtrain, num_rounds)
    bst.save_model("./output/bst.model")
    impt_feat(feat_cols, bst)
    print(datetime.now())
    print('<< 完成训练模型')


def test(df_test, drop_column):
    """ 训练
    xgboost模型训练
    """
    dump_path = './output/bst.model'
    if os.path.exists(dump_path):

        # 划分(X,y)
        print(datetime.now())
        print('>> 开始划分X,y')
        X_test = df_test.drop(drop_column, axis=1).values
        print('<< 完成划分数据')
        # 测试模型
        print('>> 开始加载模型')
        dtest = xgb.DMatrix(X_test)
        bst = xgb.Booster(model_file=dump_path)
        # dtest.save_binary('./output/dtest.buffer')
        y_probab = bst.predict(dtest)
        print('> 概率转换0,1')
        df_pred = pd.concat([df_test, pd.DataFrame({'probab': y_probab, 'pred': [0] * len(y_probab)})], axis=1)
        df_pred = df_pred.sort_values(by='probab', ascending=False)
        df_pred.ix[:int(np.sum(df_test['label'].values)), 'pred'] = 1
        print('> 保存结果')
        df_pred.to_csv('./output/test_pred.csv', index=False)
        f11_score(df_pred['label'], df_pred['pred'])
        print('<< 完成测试模型')
    else:
        print('<< 没有训练模型')


def submit(df_sub, drop_column):
    """
    xgboost模型提交
    """
    dump_path = './output/bst.jcate'
    if os.path.exists(dump_path):
        # 划分(X,y)
        print(datetime.now())
        print('>> 开始划分X,y')
        X_sub = df_sub.drop(drop_column, axis=1).values
        print('<< 完成划分数据')

        # 预测提交
        print('>> 开始预测提交')
        dsub = xgb.DMatrix(X_sub)
        # dsub.save_binary('./output/dsub.buffer')
        bst = xgb.Booster(model_file=dump_path)
        y_probab = bst.predict(dsub)
        print('> 概率转换0,1')
        df_pred = pd.concat([df_sub, pd.DataFrame({'probab': y_probab, 'pred': [0] * len(y_probab)})])
        df_pred = df_pred.sort_values(by='probab', ascending=False)
        df_pred.ix[:160000, 'label'] = 1
        df_pred.to_csv('./output/sub_pred.csv', index=False)
        # 格式化提交
        df_pred = df_pred[df_pred['label'] == 1]
        df_pred = df_pred[drop_column]
        df_pred = df_pred.drop(['label'], axis=1)
        df_pred.to_csv(submit_path + '/uc.csv', index=False)
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
    drop_column = ['user_id', 'label']

    # 训练模型
    df_train = gen_feat(train_end_date, time_gap, 'train')
    gridcv(df_train, drop_column)
    # train(df_train, drop_column)

    # # 测试模型
    # df_test = gen_feat(test_end_date, time_gap, 'test')
    # test(df_test, drop_column)

    # # 生成提交结果
    # df_sub = gen_feat(sub_end_date, time_gap, 'submit')
    # submit(df_sub, drop_column)


if __name__ == "__main__":
    main()
