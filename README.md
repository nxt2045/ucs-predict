
### 统计规律
- 每个用户都至少购买过一次
- 2月23日前7天购买用户人数异常
- user 数据分箱结果变差

### TODO
- 每日(0,1) 特征堆积图
- 日期转梯度


### 特征
用户特征：    
- [x] 用户年龄特征
- [x] 用户性别
- [x] 用户等级特征（等级 2）
- [x] 注册时间与截止日期的时间间隔（天）
- [x] 用户前 1/2/3/7/14/28 天各行为次数
- [x] 用户的行为转化率（行为 4/行为 1 、行为 4/行为 2 、行为 4/行为 5、行为 4/行为 6、行为 3/行为 2）
- [ ] 用户购买 /加购/关注前浏览天数
- [ ] 用户购买 /加购/关注前浏览次数
- [ ] 用户平均访问时间间隔
- [ ] 用户六种行为的平均访问时间
- [ ] 用户前 1/2/3/7/14/28 天 6 种行为 0/1 提取
- [ ] 用户最早/最近一次行为时间距离最后日期的时间（精确到小时）
- [ ] 用户最后一次行为的次数
- [ ] 用户层级 2/3/7/14/28 各行为天数
- [ ] 用户各行为/总行为的比值
- [ ] 用户前 1/2/3/7 天访问 P 集合的商品数
- [ ] 用户前 14/28 天访问 P 集合的商品数/用户访问总体的商品数
- [ ] 用户购买每种 cate 的数量
- [ ] 用户子集全集的活跃天数
- [ ] 用户前 1/2/3/7/14/28 天购买/加购/关注/点击/浏览品牌数
- [ ] 用户点击各模块的数量（模块 14、21、28、110、210）/点击所有模块的数量
- [ ] 用户购买 cate8 的数量占购买数量的比率
- [ ] 用户子集行为与全集行为比值




### 参考
- jdata 思路
```txt
https://blog.csdn.net/weixin_42182923/article/details/82432717
```
- jdata 代码
```txt    
https://github.com/hecongqing/2017-jdata-competition
https://github.com/foursking1/jd
https://zhuanlan.zhihu.com/p/26177617
```
- xgboost 调参    
```txt   
https://xgboost.readthedocs.io/en/latest/parameter.html#general-parameters 
https://wuhuhu800.github.io/2018/02/28/xgboost_parameters/
https://blog.csdn.net/han_xiaoyang/article/details/52665396
https://blog.csdn.net/SzM21C11U68n04vdcLmJ/article/details/78516866
```

- xgboost 官方文档
```txt    
https://xgboost.readthedocs.io/en/latest/python/python_intro.html
```

- xgboost 代码
```txt    
https://github.com/dmlc/xgboost/tree/master/demo/guide-python
https://github.com/dmlc/xgboost/tree/master/tests/python
https://zhuanlan.zhihu.com/p/31182879
```

- python画图
```txt    
https://matplotlib.org/gallery/index.html
https://seaborn.pydata.org/tutorial.html
http://liyangbit.com/pythonvisualization/matplotlib-top-50-visualizations/#20-%E8%BF%9E%E7%BB%AD%E5%8F%98%E9%87%8F%E7%9A%84%E7%9B%B4%E6%96%B9%E5%9B%BE-histogram-for-continuous-variable
```

- pandas大数据
```txt    
https://blog.csdn.net/weiyongle1996/article/details/78498603
```

- pandas参数
```txt    
https://blog.csdn.net/u010801439/article/details/80033341
```

- pandas报错
```txt    
https://zhuanlan.zhihu.com/p/41202576
```

- 样本不平衡
```txt    
https://blog.csdn.net/pearl8899/article/details/80820067
https://blog.csdn.net/u012735708/article/details/82877501
```


### 步骤
1. 将原数据放至data/ori 

### 环境
```txt
certifi==2019.3.9
chardet==3.0.4
cycler==0.10.0
docopt==0.6.2
idna==2.8
kiwisolver==1.1.0
matplotlib==3.0.3
numpy==1.16.3
pandas==0.24.2
pyparsing==2.4.0
python-dateutil==2.8.0
pytz==2019.1
requests==2.21.0
scikit-learn==0.20.3
scipy==1.2.1
six==1.12.0
urllib3==1.24.3
wincertstore==0.2
xgboost==0.82
yarg==0.1.9
```
