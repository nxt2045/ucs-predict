## Jshop的思路

### 数据筛选/特征选择
    商家数据：（shopid）
    1.粉丝数量
    2.会员数量
    3.店铺评分（shop_score)
    4.主营类目（cate）（比较cate与购买行为表中cate）

    用户行为数据：（user+shop+cate）
    1.用户前1/3/5天浏览店铺某品类的次数
    2.用户前5/7/14天购买该店铺某品类的次数
    3.用户前1/3/5天购物车店铺某品类的次数
    
用户行为数据中选取 type=2取出skuid与jdata_product表对比取出shopid，取得shop_id对应的主营项目