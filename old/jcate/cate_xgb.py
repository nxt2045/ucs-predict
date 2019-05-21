# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @DATE    : 5/14/2019
# @Author  : xiaotong niu
# @File    : uc_xgb.py
# @Project : JData-Predict
# @Github  ：https://github.com/isNxt
# @Describ : ...

import matplotlib.pyplot as plt
import xgboost as xgb
from merg_uc import *
from sklearn import metrics
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import ShuffleSplit
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier

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


# %% xgboost模型


def gen_dataset(time_gap, date_set, drop_column, mark):
    """ 生成(X,y)
    1. 获取特征
    2. 划分(X,y)
    """
    # 提取特征
    time_0 = time.clock()
    print('\n>> 开始提取%s特征' % mark)
    feat = gen_feat(date_set, time_gap, mark)  # 调用 merge_feat.py
    print('<< 完成提取%s特征, 用时%ss' % (mark, str(time.clock() - time_0)))
    # 划分(X,y)
    time_0 = time.clock()
    print('\n>> 开始划分%s特征' % mark)
    X = pd.DataFrame(feat.drop(drop_column, axis=1))
    y = pd.DataFrame(feat[drop_column])
    print('> X', X.shape)
    print('> y', y.shape)
    if mark != 'submit':
        y_pos = int(np.sum(y['label'].values))
        y_neg = y.shape[0] - y_pos
        print('> pos', y_pos)
        print('> neg', y_neg)
    print('<< 完成划分%s特征, 用时%ss' % (mark, str(time.clock() - time_0)))
    return X, y


def probab2label(y, pred):
    """ 概率转换0,1
    """
    y_pred = pd.DataFrame({'user_id': y['user_id'].values, 'cate': y['cate'].values, 'probab': pred, 'label': [0] * len(pred)})
    y_pred = y_pred.sort_values(['user_id', 'probab'])
    grouped = y_pred.groupby(['user_id']).size().reset_index(name='cate_size')
    sizes = grouped['cate_size'].values
    rows = np.cumsum(sizes) - 1
    y_pred.ix[rows, 'label'] = 1
    return y_pred


def train(time_gap, train_date_set, test_date_set, drop_column):
    """ 训练
    xgboost模型训练
    """
    time_0 = time.clock()
    # 生成(X,y)
    X_train, y_train = gen_dataset(time_gap, train_date_set, drop_column, 'train')
    train_pos = int(np.sum(y_train['label'].values))
    train_neg = y_train.shape[0] - train_pos
    X_test, y_test = gen_dataset(time_gap, test_date_set, drop_column, 'test')
    test_pos = int(np.sum(y_test['label'].values))
    test_neg = y_test.shape[0] - test_pos
    # 优化参数
    """
    sklearn.model_selection库中有GridSearchCV方法，作用是搜索模型的最优参数。
    """
    time_0 = time.clock()
    print('\n>> 开始优化参数')
    xgb_model = XGBClassifier(
        learning_rate=0.1,
        n_estimators=1000,
        max_depth=5,
        min_child_weight=1,
        gamma=0,
        subsample=0.8,
        colsample_bytree=0.8,
        objective='binary:logistic',
        nthread=4,
        scale_pos_weight=1,
        seed=27)

    cv_split = ShuffleSplit(n_splits=6, train_size=0.7, test_size=0.2)
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
        start = time.time()
        clf = GridSearchCV(estimator=xgb_model, param_grid=param_dict, scoring='roc_auc', n_jobs=4, iid=False, cv=5)
        clf.fit(X_train.values, y_train.values)
        print('\nGridSearchCV process use %.2f seconds' % (time.time() - start))
        print("Best parameters set:", clf.best_params_)
        bst_param.update(clf.best_params_)
        print("Grid scores:")
        means = clf.cv_results_['mean_test_score']
        stds = clf.cv_results_['std_test_score']
        for mean, std, params in zip(means, stds, clf.cv_results_['params']):
            print("%0.3f (+/-%0.03f) for %r"
                  % (mean, std * 2, params))
    print('<< 完成参数调优, 用时', time.clock() - time_0, 's')

    # 利用得到的参数，训练模型并测试
    time_0 = time.clock()
    # 生成(X,y)
    print('\n>> 开始训练模型')
    print('> train 负正:', int(train_neg), int(train_pos), round(1.0 * train_neg / train_pos, 4))
    print('> test 负正:', int(test_neg), int(test_pos), round(1.0 * test_neg / test_pos, 4))
    # 转换数据
    dtrain = xgb.DMatrix(X_train, label=y_train['label'].values)
    dtrain.save_binary(out_path + '/dtrain.buffer')
    dtest = xgb.DMatrix(X_test, label=y_test['label'].values)
    dtest.save_binary(out_path + '/dtest.buffer')
    y_real = y_test
    print("Best parameters set:")
    print(bst_param)
    num_rounds = 1000  # 迭代次数
    evallist = [(dtest, 'eval'), (dtrain, 'train')]
    bst = xgb.train(bst_param, dtrain, num_rounds, evallist)
    bst.save_model(out_path + "/bst.model")
    print('<< 完成训练模型, 用时', time.clock() - time_0, 's')
    # 测试模型
    print('\n>> 开始测试模型')
    pred = bst.predict(dtest)
    # 概率转换0,1
    print('> 概率转换0,1')
    y_pred = pd.DataFrame({'user_id': y_test['user_id'].values,'real':y_test['label'], 'cate': y_test['cate'].values, 'probab': pred, 'label': [0] * len(pred)})
    y_pred.to_csv(out_path + '/test_probab.csv', index=False)
    '''
    y_pred = probab2label(y_real, pred)
    y_pred.to_csv(out_path + '/test.csv', index=False)
    # 得分
    print('> test 负正:', int(test_neg), int(test_pos), round(1.0 * test_neg / test_pos, 4))
    pred_pos = int(np.sum(y_pred['label'].values))
    pred_neg = y_pred.shape[0] - pred_pos
    print('> pred 负正:', int(pred_neg), int(pred_pos), round(1.0 * pred_neg / pred_pos, 4))
    print('> classification_report:')
    print(metrics.classification_report(y_true=y_real['label'], y_pred=y_pred['label']))
    print('> confusion_matrix:')
    y_real = pd.Series(y_real['label'].values, name='Real')
    y_pred = pd.Series(y_pred['label'].values, name='Pred')
    print(pd.crosstab(y_real, y_pred, rownames=['Real'], colnames=['Pred'], margins=True))
    '''
    # feat 重要性
    plt.rcParams['figure.figsize'] = (20, 10)
    xgb.plot_importance(bst)
    plt.savefig(out_path + '/feat_import.png', dpi=300)
    f_score = bst.get_fscore()
    f_id = pd.DataFrame(list(f_score.keys()))
    f_pro = pd.DataFrame(list(f_score.values()))
    f_score = pd.concat([f_id, f_pro], axis=1)
    f_score.columns = ['f_id', 'f_pro']
    f_score.sort_values(by=['f_pro'], ascending=[0], inplace=True)
    f_score.to_csv(out_path + '/feat_import.csv', index=False)
    print('> 测试结果', y_pred.shape)
    print('<< 完成测试模型, 用时', time.clock() - time_0, 's')


def submit(time_gap, sub_date_set, drop_column, sub_name):
    """
    xgboost模型提交
    """
    # 加载模型
    dump_path = out_path + '/bst.model'
    if os.path.exists(dump_path):
        time_0 = time.clock()
        # 生成(X,y)
        X_sub, y_sub = gen_dataset(time_gap, sub_date_set, drop_column, 'submit')
        # 转换数据
        dsub = xgb.DMatrix(X_sub)
        dsub.save_binary(out_path + '/dsub.buffer')
        y_real = y_sub
        # 加载模型
        bst = xgb.Booster(model_file=dump_path)
        # 预测结果
        print('\n>> 开始预测提交结果')
        pred = bst.predict(dsub)
        # 概率转换0,1
        print('> 概率转换0,1')
        y_pred = pd.DataFrame({'user_id': y_sub['user_id'].values, 'cate': y_sub['cate'].values, 'probab': pred, 'label': [0] * len(pred)})
        y_pred.to_csv(out_path + '/sub_probab.csv', index=False)
        y_pred = probab2label(y_real, pred)
        y_pred.to_csv(out_path + '/submit.csv', index=False)
        # 格式化提交
        y_pred = y_pred[y_pred['label'] == 1]
        drop_column.remove('label')
        y_pred = y_pred[drop_column]
        y_pred.to_csv(sub_path + '/' + sub_name + '.csv', index=False)
        print('> 预测结果', y_pred.shape)
        print('<< 完成预测提交结果！用时', time.clock() - time_0, 's')
    else:
        print('\n<< 没有训练模型')


def main():
    """
    主流程
    """
    # 定义滑动窗口
    time_gap = [1, 2, 3, 7, 14]
    # 定义结束时间集
    train_date_set = ['2018-4-1', '2018-3-25', '2018-3-18', '2018-3-11']
    test_date_set = ['2018-4-8']
    sub_date_set = ['2018-4-15']
    # 定义非特征列
    drop_column = ['user_id', 'cate', 'label']
    # 训练模型
    train(time_gap, train_date_set, test_date_set, drop_column)
    # 生成提交结果
    submit(time_gap, sub_date_set, drop_column, 'cate')


if __name__ == "__main__":
    main()
