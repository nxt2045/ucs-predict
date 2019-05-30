# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @DATE    : 4/20/2019
# @Author  : xiaotong niu
# @File    : xgb_uc.py
# @Project : JData-UCS
# @Github  ：https://github.com/isNxt
# @Describ : ...

from feature.feat_shop import *
from model_1.merg_ucs import gen_feat
from utils.select import *

# %% 配置
# 输出设置

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)
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


def model(df_train, df_test, drop_column):
    """ 构造
    xgboost模型训练测试
    """

    dump_path = './out/bst.model'
    if os.path.exists(dump_path):
        # 划分(X,y)
        print(datetime.now())
        print('\n>> 开始加载已有模型')
        bst = xgb.Booster(model_file=dump_path)
    else:
        # 划分(X,y)
        print(datetime.now())
        print('\n>> 开始划分X,y')
        X_train = df_train.drop(drop_column, axis=1).values
        y_train = df_train['label'].values
        X_test = df_test.drop(drop_column, axis=1).values
        y_test = df_test['label'].values
        dtrain = xgb.DMatrix(X_train, label=y_train)
        dtest = xgb.DMatrix(X_test, label=y_test)
        print('<< 完成划分X,y')
        # 设置参数(gridcv最佳)
        print(datetime.now())
        print('\n>> 开始设置参数')
        weight = (len(y_train) - np.sum(y_train)) \
                 / (np.sum(y_train))
        param = {
            # 默认
            'silent': 0,
            'objective': 'binary:logistic',
            # 调整
            'scale_pos_weight': weight,
            'learning_rate': 0.01,
            'n_estimators': 1000,
            'max_depth': 4,
            'min_child_weight': 3,
            'gamma': 0,
            'subsample': 0.8,
            'colsample_bytree': 0.8,
            'eta': 0.05,
        }
        num_round = 1000

        plst = list(param.items())
        plst += [('eval_metric', ['accuracy','auc'])]  # auc logloss
        evallist = [(dtest, 'eval'), (dtrain, 'train')]
        print('<< 完成设置参数')

        # 训练模型(watchlist)
        print(datetime.now())
        print('\n>> 开始训练模型')
        bst = xgb.train(plst, dtrain, num_round, evallist, early_stopping_rounds=50)
        bst.save_model(dump_path)
        del dtest, dtrain
        print('<< 完成训练模型')

    # 划分(X,y)
    print(datetime.now())
    print('\n>> 开始划分X,y')
    X_test = df_test.drop(drop_column, axis=1).values
    y_test = df_test['label'].values
    dtest = xgb.DMatrix(X_test)
    print('<< 完成划分X,y')

    # 测试模型
    print('\n>> 开始测试模型')
    y_probab = bst.predict(dtest)
    del dtest
    print('> 概率转换0,1')
    df_pred = pd.concat([df_test, pd.DataFrame({'probab': y_probab, 'pred': [0] * len(y_probab)})], axis=1)
    del df_train, df_test
    df_pred.sort_values(by='probab', ascending=False, inplace=True)
    df_pred.drop_duplicates(['user_id', 'cate'], keep='first', inplace=True)
    df_pred.reset_index(drop=True, inplace=True)
    # df_pred.to_csv('./out/test_pred.csv', index=False)

    # 计算得分
    print('\n>> 开始计算得分')
    dump_path = cache_path + '/test_real.csv'
    if os.path.exists(dump_path):
        # 划分(X,y)
        print(datetime.now())
        df_real = pd.read_csv(dump_path)
    else:
        end_date = datetime.strptime('2018-4-1', '%Y-%m-%d')
        df_real = feat_buy_plus(end_date + timedelta(days=1), end_date + timedelta(days=7))[
            ['user_id', 'cate']]
        df_real.to_csv(dump_path, index=False)

    df_pred = df_pred[['user_id', 'cate', 'pred']]
    print('前%s行[test] label=1：' % (str(df_real.shape[0])))
    report_uc(df_real, df_pred.iloc[:df_real.shape[0]])

    for amt in range(80000, 280000, 10000):
        print('前%s行 label=1：' % (str(amt)))
        report_uc(df_real, df_pred.iloc[:amt])
    print('<< 完成测试模型')


def submit(df_sub, drop_column):
    """
    xgboost模型提交
    """
    dump_path = './output/bst.jcate'
    if os.path.exists(dump_path):
        # 划分(X,y)
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
        df_pred = pd.concat([df_sub, pd.DataFrame({'probab': y_probab, 'pred': [0] * len(y_probab)})], axis=1)
        del df_sub
        df_pred.sort_values(by='probab', ascending=False, inplace=True)
        df_pred.drop_duplicates(['user_id', 'cate'], keep='first', inplace=True)
        df_pred.reset_index(drop=True, inplace=True)
        # df_pred.to_csv('./out/test_pred.csv', index=False)

        df_pred = df_pred[['user_id', 'cate']]
        df_pred=df_pred.iloc[:180000]
        df_pred.to_csv(submit_path + '/uc.csv', index=False)
        print('<< 完成提交模型')
    else:
        print('<< 没有训练模型')


def main():
    """
    主流程
    """
    # 定义参数
    train_end_date = '2018-4-1'
    test_end_date = '2018-4-8'
    submit_end_date = '2018-4-15'
    drop_column = ['user_id', 'cate', 'label']
    label_gap = 30

    # 生成特征
    df_train = gen_feat(train_end_date, label_gap, 'train')
    df_test = gen_feat(test_end_date, label_gap, 'test')
    df_submit = gen_feat(submit_end_date, label_gap, 'submit')

    # 构造模型
    gridcv(df_train, drop_column)
    model(df_train, df_test, drop_column)
    impt_feat(df_train, drop_column)

    # 提交模型[阶段1]
    submit(df_submit,drop_column)


if __name__ == "__main__":
    main()
