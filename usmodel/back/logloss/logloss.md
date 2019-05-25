C:\Users\lenovo\.conda\envs\env_jdata\python.exe C:/Users/lenovo/Documents/GitHub/JData-UCS/usmodel/us_xgb.py
2019-05-25 18:59:58.536036

>> 开始生成特征(X,y)
end_date 2018-4-8
2019-05-25 18:59:58.537039
> 获取标签
action_180406_180408
buy_180409_180415
真实购买 (185423, 2)
可能购买 (738726, 2)
shape (738726, 3)
cols Index(['user_id', 'sku_id', 'label'], dtype='object')
head
   user_id  sku_id  label
0        2  268259      0
1        2   57634      0
2        2   98543      0
3        2  341714      0
4        2  185628      0
tail
        user_id  sku_id  label
738721  1608705   10554      0
738722  1608705  238979      0
738723  1608705  101645      0
738724  1608705   50755      0
738725  1608707  100598      0
2019-05-25 19:00:00.016760
> 遍历特征 gap=1
user_if_view_180408_180408
user_if_buy_180408_180408
user_if_follow_180408_180408
user_if_remark_180408_180408
user_if_cart_180408_180408
user_action_amt_180408_180408
user_view_amt_180408_180408
user_buy_amt_180408_180408
user_follow_amt_180408_180408
user_remark_amt_180408_180408
user_cart_amt_180408_180408
user_action_day_180408_180408
user_view_day_180408_180408
user_buy_day_180408_180408
user_follow_day_180408_180408
user_remark_day_180408_180408
user_cart_day_180408_180408
sku_if_view_180408_180408
sku_if_buy_180408_180408
sku_if_follow_180408_180408
sku_if_remark_180408_180408
sku_if_cart_180408_180408
sku_action_amt_180408_180408
sku_view_amt_180408_180408
sku_buy_amt_180408_180408
sku_follow_amt_180408_180408
sku_remark_amt_180408_180408
sku_cart_amt_180408_180408
sku_action_day_180408_180408
sku_view_day_180408_180408
sku_buy_day_180408_180408
sku_follow_day_180408_180408
sku_remark_day_180408_180408
sku_cart_day_180408_180408
user_sku_if_view_180408_180408
user_sku_if_buy_180408_180408
user_sku_if_follow_180408_180408
user_sku_if_remark_180408_180408
user_sku_if_cart_180408_180408
user_sku_action_amt_180408_180408
user_sku_view_amt_180408_180408
user_sku_buy_amt_180408_180408
user_sku_follow_amt_180408_180408
user_sku_remark_amt_180408_180408
user_sku_cart_amt_180408_180408
user_sku_action_day_180408_180408
user_sku_view_day_180408_180408
user_sku_buy_day_180408_180408
user_sku_follow_day_180408_180408
user_sku_remark_day_180408_180408
user_sku_cart_day_180408_180408
user_sku_user_action_ratio_180408_180408
2019-05-25 19:00:32.926555
> 遍历特征 gap=2
user_if_view_180407_180408
user_if_buy_180407_180408
user_if_follow_180407_180408
user_if_remark_180407_180408
user_if_cart_180407_180408
user_action_amt_180407_180408
user_view_amt_180407_180408
user_buy_amt_180407_180408
user_follow_amt_180407_180408
user_remark_amt_180407_180408
user_cart_amt_180407_180408
user_action_day_180407_180408
user_view_day_180407_180408
user_buy_day_180407_180408
user_follow_day_180407_180408
user_remark_day_180407_180408
user_cart_day_180407_180408
sku_if_view_180407_180408
sku_if_buy_180407_180408
sku_if_follow_180407_180408
sku_if_remark_180407_180408
sku_if_cart_180407_180408
sku_action_amt_180407_180408
sku_view_amt_180407_180408
sku_buy_amt_180407_180408
sku_follow_amt_180407_180408
sku_remark_amt_180407_180408
sku_cart_amt_180407_180408
sku_action_day_180407_180408
sku_view_day_180407_180408
sku_buy_day_180407_180408
sku_follow_day_180407_180408
sku_remark_day_180407_180408
sku_cart_day_180407_180408
user_sku_if_view_180407_180408
user_sku_if_buy_180407_180408
user_sku_if_follow_180407_180408
user_sku_if_remark_180407_180408
user_sku_if_cart_180407_180408
user_sku_action_amt_180407_180408
user_sku_view_amt_180407_180408
user_sku_buy_amt_180407_180408
user_sku_follow_amt_180407_180408
user_sku_remark_amt_180407_180408
user_sku_cart_amt_180407_180408
user_sku_action_day_180407_180408
user_sku_view_day_180407_180408
user_sku_buy_day_180407_180408
user_sku_follow_day_180407_180408
user_sku_remark_day_180407_180408
user_sku_cart_day_180407_180408
user_sku_user_action_ratio_180407_180408
2019-05-25 19:00:51.722456
> 遍历特征 gap=3
user_if_view_180406_180408
user_if_buy_180406_180408
user_if_follow_180406_180408
user_if_remark_180406_180408
user_if_cart_180406_180408
user_action_amt_180406_180408
user_view_amt_180406_180408
user_buy_amt_180406_180408
user_follow_amt_180406_180408
user_remark_amt_180406_180408
user_cart_amt_180406_180408
user_action_day_180406_180408
user_view_day_180406_180408
user_buy_day_180406_180408
user_follow_day_180406_180408
user_remark_day_180406_180408
user_cart_day_180406_180408
sku_if_view_180406_180408
sku_if_buy_180406_180408
sku_if_follow_180406_180408
sku_if_remark_180406_180408
sku_if_cart_180406_180408
sku_action_amt_180406_180408
sku_view_amt_180406_180408
sku_buy_amt_180406_180408
sku_follow_amt_180406_180408
sku_remark_amt_180406_180408
sku_cart_amt_180406_180408
sku_action_day_180406_180408
sku_view_day_180406_180408
sku_buy_day_180406_180408
sku_follow_day_180406_180408
sku_remark_day_180406_180408
sku_cart_day_180406_180408
user_sku_if_view_180406_180408
user_sku_if_buy_180406_180408
user_sku_if_follow_180406_180408
user_sku_if_remark_180406_180408
user_sku_if_cart_180406_180408
user_sku_action_amt_180406_180408
user_sku_view_amt_180406_180408
user_sku_buy_amt_180406_180408
user_sku_follow_amt_180406_180408
user_sku_remark_amt_180406_180408
user_sku_cart_amt_180406_180408
user_sku_action_day_180406_180408
user_sku_view_day_180406_180408
user_sku_buy_day_180406_180408
user_sku_follow_day_180406_180408
user_sku_remark_day_180406_180408
user_sku_cart_day_180406_180408
user_sku_user_action_ratio_180406_180408
2019-05-25 19:01:11.208588
> 遍历特征 gap=7
user_if_view_180402_180408
user_if_buy_180402_180408
user_if_follow_180402_180408
user_if_remark_180402_180408
user_if_cart_180402_180408
user_action_amt_180402_180408
user_view_amt_180402_180408
user_buy_amt_180402_180408
user_follow_amt_180402_180408
user_remark_amt_180402_180408
user_cart_amt_180402_180408
user_action_day_180402_180408
user_view_day_180402_180408
user_buy_day_180402_180408
user_follow_day_180402_180408
user_remark_day_180402_180408
user_cart_day_180402_180408
sku_if_view_180402_180408
sku_if_buy_180402_180408
sku_if_follow_180402_180408
sku_if_remark_180402_180408
sku_if_cart_180402_180408
sku_action_amt_180402_180408
sku_view_amt_180402_180408
sku_buy_amt_180402_180408
sku_follow_amt_180402_180408
sku_remark_amt_180402_180408
sku_cart_amt_180402_180408
sku_action_day_180402_180408
sku_view_day_180402_180408
sku_buy_day_180402_180408
sku_follow_day_180402_180408
sku_remark_day_180402_180408
sku_cart_day_180402_180408
user_sku_if_view_180402_180408
user_sku_if_buy_180402_180408
user_sku_if_follow_180402_180408
user_sku_if_remark_180402_180408
user_sku_if_cart_180402_180408
user_sku_action_amt_180402_180408
user_sku_view_amt_180402_180408
user_sku_buy_amt_180402_180408
user_sku_follow_amt_180402_180408
user_sku_remark_amt_180402_180408
user_sku_cart_amt_180402_180408
user_sku_action_day_180402_180408
user_sku_view_day_180402_180408
user_sku_buy_day_180402_180408
user_sku_follow_day_180402_180408
user_sku_remark_day_180402_180408
user_sku_cart_day_180402_180408
user_sku_user_action_ratio_180402_180408
2019-05-25 19:01:34.178795
> 遍历特征 gap=14
user_if_view_180326_180408
user_if_buy_180326_180408
user_if_follow_180326_180408
user_if_remark_180326_180408
user_if_cart_180326_180408
user_action_amt_180326_180408
user_view_amt_180326_180408
user_buy_amt_180326_180408
user_follow_amt_180326_180408
user_remark_amt_180326_180408
user_cart_amt_180326_180408
user_action_day_180326_180408
user_view_day_180326_180408
user_buy_day_180326_180408
user_follow_day_180326_180408
user_remark_day_180326_180408
user_cart_day_180326_180408
sku_if_view_180326_180408
sku_if_buy_180326_180408
sku_if_follow_180326_180408
sku_if_remark_180326_180408
sku_if_cart_180326_180408
sku_action_amt_180326_180408
sku_view_amt_180326_180408
sku_buy_amt_180326_180408
sku_follow_amt_180326_180408
sku_remark_amt_180326_180408
sku_cart_amt_180326_180408
sku_action_day_180326_180408
sku_view_day_180326_180408
sku_buy_day_180326_180408
sku_follow_day_180326_180408
sku_remark_day_180326_180408
sku_cart_day_180326_180408
user_sku_if_view_180326_180408
user_sku_if_buy_180326_180408
user_sku_if_follow_180326_180408
user_sku_if_remark_180326_180408
user_sku_if_cart_180326_180408
user_sku_action_amt_180326_180408
user_sku_view_amt_180326_180408
user_sku_buy_amt_180326_180408
user_sku_follow_amt_180326_180408
user_sku_remark_amt_180326_180408
user_sku_cart_amt_180326_180408
user_sku_action_day_180326_180408
user_sku_view_day_180326_180408
user_sku_buy_day_180326_180408
user_sku_follow_day_180326_180408
user_sku_remark_day_180326_180408
user_sku_cart_day_180326_180408
user_sku_user_action_ratio_180326_180408
2019-05-25 19:02:01.772623
> 遍历全局特征
user.csv
user_action_amt_180310_180408
user_view_amt_180310_180408
user_buy_amt_180310_180408
user_follow_amt_180310_180408
user_remark_amt_180310_180408
user_cart_amt_180310_180408
user_action_day_180310_180408
user_view_day_180310_180408
user_buy_day_180310_180408
user_follow_day_180310_180408
user_remark_day_180310_180408
user_cart_day_180310_180408
user_action_ratio_180310_180408
user_buy_rate_180310_180408
user_first_hour_180310_180408
user_last_hour_180310_180408
user_last_amt_180310_180408
sku_plus
sku_action_amt_180310_180408
sku_view_amt_180310_180408
sku_buy_amt_180310_180408
sku_follow_amt_180310_180408
sku_remark_amt_180310_180408
sku_cart_amt_180310_180408
sku_action_day_180310_180408
sku_view_day_180310_180408
sku_buy_day_180310_180408
sku_follow_day_180310_180408
sku_remark_day_180310_180408
sku_cart_day_180310_180408
sku_action_ratio_180310_180408
sku_buy_rate_180310_180408
sku_rebuy_rate_180310_180408
sku_first_hour_180310_180408
sku_last_hour_180310_180408
sku_last_amt_180310_180408
user_sku_if_view_180310_180408
user_sku_if_buy_180310_180408
user_sku_if_follow_180310_180408
user_sku_if_remark_180310_180408
user_sku_if_cart_180310_180408
user_sku_action_amt_180310_180408
user_sku_view_amt_180310_180408
user_sku_buy_amt_180310_180408
user_sku_follow_amt_180310_180408
user_sku_remark_amt_180310_180408
user_sku_cart_amt_180310_180408
user_sku_action_day_180310_180408
user_sku_view_day_180310_180408
user_sku_buy_day_180310_180408
user_sku_follow_day_180310_180408
user_sku_remark_day_180310_180408
user_sku_cart_day_180310_180408
user_sku_action_ratio_180310_180408
user_sku_user_action_ratio_180310_180408
user_sku_first_hour_180310_180408
user_sku_last_hour_180310_180408
user_sku_last_amt_180310_180408
2019-05-25 19:03:44.578227
>>开始保存特征(738726, 391)
feat (738726, 391)
cols Index(['user_id', 'sku_id', 'label', '1_user_if_view', '1_user_if_buy',
       '1_user_if_follow', '1_user_if_remark', '1_user_if_cart',
       '1_user_action_amt', '1_user_view_amt',
       ...
       'user_sku_cart_ratio', 'user_sku_user_action_ratio',
       'user_sku_user_view_ratio', 'user_sku_user_buy_ratio',
       'user_sku_user_follow_ratio', 'user_sku_user_remark_ratio',
       'user_sku_user_cart_ratio', 'user_sku_first_hour', 'user_sku_last_hour',
       'user_sku_last_amt'],
      dtype='object', length=391)
head
   user_id  sku_id  label  1_user_if_view  1_user_if_buy  1_user_if_follow  1_user_if_remark  1_user_if_cart  1_user_action_amt  1_user_view_amt  1_user_buy_amt  1_user_follow_amt  1_user_remark_amt  1_user_cart_amt  1_user_active_day  1_user_view_day  1_user_buy_day  1_user_follow_day  1_user_remark_day  1_user_cart_day  1_sku_if_view  1_sku_if_buy  1_sku_if_follow  1_sku_if_remark  1_sku_if_cart  1_sku_action_amt  1_sku_view_amt  1_sku_buy_amt  1_sku_follow_amt  1_sku_remark_amt  1_sku_cart_amt  1_sku_active_day  1_sku_view_day  1_sku_buy_day  1_sku_follow_day  1_sku_remark_day  1_sku_cart_day  1_user_sku_if_view  1_user_sku_if_buy  1_user_sku_if_follow  1_user_sku_if_remark  1_user_sku_if_cart  1_user_sku_action_amt  1_user_sku_view_amt  1_user_sku_buy_amt  1_user_sku_follow_amt  1_user_sku_remark_amt  1_user_sku_cart_amt  1_user_sku_action_day  1_user_sku_view_day  1_user_sku_buy_day  1_user_sku_follow_day  1_user_sku_remark_day  1_user_sku_cart_day  1_user_sku_user_action_ratio  1_user_sku_user_view_ratio  1_user_sku_user_buy_ratio  1_user_sku_user_follow_ratio  1_user_sku_user_remark_ratio  1_user_sku_user_cart_ratio  2_user_if_view  2_user_if_buy  2_user_if_follow  2_user_if_remark  2_user_if_cart  2_user_action_amt  2_user_view_amt  2_user_buy_amt  2_user_follow_amt  2_user_remark_amt  2_user_cart_amt  2_user_active_day  2_user_view_day  2_user_buy_day  2_user_follow_day  2_user_remark_day  2_user_cart_day  2_sku_if_view  2_sku_if_buy  2_sku_if_follow  2_sku_if_remark  2_sku_if_cart  2_sku_action_amt  2_sku_view_amt  2_sku_buy_amt  2_sku_follow_amt  2_sku_remark_amt  2_sku_cart_amt  2_sku_active_day  2_sku_view_day  2_sku_buy_day  2_sku_follow_day  2_sku_remark_day  2_sku_cart_day  2_user_sku_if_view  2_user_sku_if_buy  2_user_sku_if_follow  2_user_sku_if_remark  2_user_sku_if_cart  2_user_sku_action_amt  2_user_sku_view_amt  2_user_sku_buy_amt  2_user_sku_follow_amt  2_user_sku_remark_amt  2_user_sku_cart_amt  2_user_sku_action_day  2_user_sku_view_day  2_user_sku_buy_day  2_user_sku_follow_day  2_user_sku_remark_day  2_user_sku_cart_day  2_user_sku_user_action_ratio  2_user_sku_user_view_ratio  2_user_sku_user_buy_ratio  2_user_sku_user_follow_ratio  2_user_sku_user_remark_ratio  2_user_sku_user_cart_ratio  3_user_if_view  3_user_if_buy  3_user_if_follow  3_user_if_remark  3_user_if_cart  3_user_action_amt  3_user_view_amt  3_user_buy_amt  3_user_follow_amt  3_user_remark_amt  3_user_cart_amt  3_user_action_day  3_user_view_day  3_user_buy_day  3_user_follow_day  3_user_remark_day  3_user_cart_day  3_sku_if_view  3_sku_if_buy  3_sku_if_follow  3_sku_if_remark  3_sku_if_cart  3_sku_action_amt  3_sku_view_amt  3_sku_buy_amt  3_sku_follow_amt  3_sku_remark_amt  3_sku_cart_amt  3_sku_active_day  3_sku_view_day  3_sku_buy_day  3_sku_follow_day  3_sku_remark_day  3_sku_cart_day  3_user_sku_if_view  3_user_sku_if_buy  3_user_sku_if_follow  3_user_sku_if_remark  3_user_sku_if_cart  3_user_sku_action_amt  3_user_sku_view_amt  3_user_sku_buy_amt  3_user_sku_follow_amt  3_user_sku_remark_amt  3_user_sku_cart_amt  3_user_sku_action_day  3_user_sku_view_day  3_user_sku_buy_day  3_user_sku_follow_day  3_user_sku_remark_day  3_user_sku_cart_day  3_user_sku_user_action_ratio  3_user_sku_user_view_ratio  3_user_sku_user_buy_ratio  3_user_sku_user_follow_ratio  3_user_sku_user_remark_ratio  3_user_sku_user_cart_ratio  7_user_if_view  7_user_if_buy  7_user_if_follow  7_user_if_remark  7_user_if_cart  7_user_action_amt  7_user_view_amt  7_user_buy_amt  7_user_follow_amt  7_user_remark_amt  7_user_cart_amt  7_user_active_day  7_user_view_day  7_user_buy_day  7_user_follow_day  7_user_remark_day  7_user_cart_day  7_sku_if_view  7_sku_if_buy  7_sku_if_follow  7_sku_if_remark  7_sku_if_cart  7_sku_action_amt  7_sku_view_amt  7_sku_buy_amt  7_sku_follow_amt  7_sku_remark_amt  7_sku_cart_amt  7_sku_active_day  7_sku_view_day  7_sku_buy_day  7_sku_follow_day  7_sku_remark_day  7_sku_cart_day  7_user_sku_if_view  7_user_sku_if_buy  7_user_sku_if_follow  7_user_sku_if_remark  7_user_sku_if_cart  7_user_sku_action_amt  7_user_sku_view_amt  7_user_sku_buy_amt  7_user_sku_follow_amt  7_user_sku_remark_amt  7_user_sku_cart_amt  7_user_sku_action_day  7_user_sku_view_day  7_user_sku_buy_day  7_user_sku_follow_day  7_user_sku_remark_day  7_user_sku_cart_day  7_user_sku_user_action_ratio  7_user_sku_user_view_ratio  7_user_sku_user_buy_ratio  7_user_sku_user_follow_ratio  7_user_sku_user_remark_ratio  7_user_sku_user_cart_ratio  14_user_if_view  14_user_if_buy  14_user_if_follow  14_user_if_remark  14_user_if_cart  14_user_action_amt  14_user_view_amt  14_user_buy_amt  14_user_follow_amt  14_user_remark_amt  14_user_cart_amt  14_user_active_day  14_user_view_day  14_user_buy_day  14_user_follow_day  14_user_remark_day  14_user_cart_day  14_sku_if_view  14_sku_if_buy  14_sku_if_follow  14_sku_if_remark  14_sku_if_cart  14_sku_action_amt  14_sku_view_amt  14_sku_buy_amt  14_sku_follow_amt  14_sku_remark_amt  14_sku_cart_amt  14_sku_active_day  14_sku_view_day  14_sku_buy_day  14_sku_follow_day  14_sku_remark_day  14_sku_cart_day  14_user_sku_if_view  14_user_sku_if_buy  14_user_sku_if_follow  14_user_sku_if_remark  14_user_sku_if_cart  14_user_sku_action_amt  14_user_sku_view_amt  14_user_sku_buy_amt  14_user_sku_follow_amt  14_user_sku_remark_amt  14_user_sku_cart_amt  14_user_sku_action_day  14_user_sku_view_day  14_user_sku_buy_day  14_user_sku_follow_day  14_user_sku_remark_day  14_user_sku_cart_day  14_user_sku_user_action_ratio  14_user_sku_user_view_ratio  14_user_sku_user_buy_ratio  14_user_sku_user_follow_ratio  14_user_sku_user_remark_ratio  14_user_sku_user_cart_ratio  age  sex  user_lv_cd  city_level  province  city  county  user_reg_day  user_reg_month  user_reg_cate  user_reg_year  user_action_amt  user_view_amt  user_buy_amt  user_follow_amt  user_remark_amt  user_cart_amt  user_active_day  user_view_day  user_buy_day  user_follow_day  user_remark_day  user_cart_day  user_view_ratio  user_buy_ratio  user_follow_ratio  user_remark_ratio  user_cart_ratio  user_buy/view  user_buy/follow  user_buy/remark  user_buy/cart  user_first_hour  user_last_hour  user_last_amt  brand  cate  product_reg_day  product_reg_month  product_reg_cate  product_reg_year  fans_num  vip_num  shop_cate  shop_score  shop_reg_month  shop_reg_cate  sku_action_amt  sku_view_amt  sku_buy_amt  sku_follow_amt  sku_remark_amt  sku_cart_amt  sku_active_day  sku_view_day  sku_buy_day  sku_follow_day  sku_remark_day  sku_cart_day  sku_view_ratio  sku_buy_ratio  sku_follow_ratio  sku_remark_ratio  sku_cart_ratio  sku_buy/view  sku_buy/follow  sku_buy/remark  sku_buy/cart  sku_rebuy_rate  sku_first_hour  sku_last_hour  sku_last_amt  user_sku_if_view  user_sku_if_buy  user_sku_if_follow  user_sku_if_remark  user_sku_if_cart  user_sku_action_amt  user_sku_view_amt  user_sku_buy_amt  user_sku_follow_amt  user_sku_remark_amt  user_sku_cart_amt  user_sku_action_day  user_sku_view_day  user_sku_buy_day  user_sku_follow_day  user_sku_remark_day  user_sku_cart_day  user_sku_view_ratio  user_sku_buy_ratio  user_sku_follow_ratio  user_sku_remark_ratio  user_sku_cart_ratio  user_sku_user_action_ratio  user_sku_user_view_ratio  user_sku_user_buy_ratio  user_sku_user_follow_ratio  user_sku_user_remark_ratio  user_sku_user_cart_ratio  user_sku_first_hour  user_sku_last_hour  user_sku_last_amt
0        2  268259      0               0              0                 0                 0               0                  0                0               0                  0                  0                0                  0                0               0                  0                  0                0              0             0                0                0              0                 0               0              0                 0                 0               0                 0               0              0                 0                 0               0                   0                  0                     0                     0                   0                      0                    0                   0                      0                      0                    0                      0                    0                   0                      0                      0                    0                             0                           0                          0                             0                             0                           0               1              0                 0                 0               0                  8                8               0                  0                  0                0                  1                1               0                  0                  0                0              1             0                0                0              0                 7               7              0                 0                 0               0                 1               1              0                 0                 0               0                   0                  0                     0                     0                   0                      0                    0                   0                      0                      0                    0                      0                    0                   0                      0                      0                    0                             0                           0                          0                             0                             0                           0               1              0                 0                 0               0                  9                9               0                  0                  0                0                  2                2               0                  0                  0                0              1             0                0                0              0                21              21              0                 0                 0               0                 2               2              0                 0                 0               0                   1                  0                     0                     0                   0                      1                    1                   0                      0                      0                    0                      1                    1                   0                      0                      0                    0                            11                          11                          0                             0                             0                           0               1              0                 0                 0               0                 23               23               0                  0                  0                0                  5                5               0                  0                  0                0              1             0                1                0              0                78              77              0                 1                 0               0                 6               6              0                 1                 0               0                   1                  0                     0                     0                   0                      1                    1                   0                      0                      0                    0                      1                    1                   0                      0                      0                    0                             4                           4                          0                             0                             0                           0                1               0                  0                  1                0                  30                27                0                   0                   3                 0                  10                 8                0                   0                   2                 0               1              0                 1                 1               0                126              124               0                  1                  1                0                 13               12               0                  1                  1                0                    1                   0                      0                      0                    0                       1                     1                    0                       0                       0                     0                       1                     1                    0                       0                       0                     0                              3                            3                           0                              0                              0                            0    4    1           1           3        20   119     187          1091              36              5              2               86            261             1                0                4              1               18             41             1                0                2              1              303               1                  0                  4                1              0             -100               25            100                3             694              1   8633    22             1475                 49                 6                 4         0        0         -1           0              -1             -1             345           857            0              16               2             7              29            73            0              15               2             4             248              0                 4                 0               2             0               0               0             0               0               1            695            17                 1                0                   0                   0                 0                    1                  1                 0                    0                    0                  0                    1                  1                 0                    0                    0                  0                  100                   0                      0                      0                    0                           1                         0                        0                           0                           0                         0                   31                  31                  1
1        2   57634      0               0              0                 0                 0               0                  0                0               0                  0                  0                0                  0                0               0                  0                  0                0              0             0                0                0              0                 0               0              0                 0                 0               0                 0               0              0                 0                 0               0                   0                  0                     0                     0                   0                      0                    0                   0                      0                      0                    0                      0                    0                   0                      0                      0                    0                             0                           0                          0                             0                             0                           0               1              0                 0                 0               0                  8                8               0                  0                  0                0                  1                1               0                  0                  0                0              1             0                0                0              0                 1               1              0                 0                 0               0                 1               1              0                 0                 0               0                   1                  0                     0                     0                   0                      1                    1                   0                      0                      0                    0                      1                    1                   0                      0                      0                    0                            12                          12                          0                             0                             0                           0               1              0                 0                 0               0                  9                9               0                  0                  0                0                  2                2               0                  0                  0                0              1             0                0                0              0                 1               1              0                 0                 0               0                 1               1              0                 0                 0               0                   1                  0                     0                     0                   0                      1                    1                   0                      0                      0                    0                      1                    1                   0                      0                      0                    0                            11                          11                          0                             0                             0                           0               1              0                 0                 0               0                 23               23               0                  0                  0                0                  5                5               0                  0                  0                0              1             0                0                0              0                 2               2              0                 0                 0               0                 2               2              0                 0                 0               0                   1                  0                     0                     0                   0                      1                    1                   0                      0                      0                    0                      1                    1                   0                      0                      0                    0                             4                           4                          0                             0                             0                           0                1               0                  0                  1                0                  30                27                0                   0                   3                 0                  10                 8                0                   0                   2                 0               1              0                 0                 1               0                  7                6               0                  0                  1                0                  5                4               0                  0                  1                0                    1                   0                      0                      1                    0                       3                     2                    0                       0                       1                     0                       3                     2                    0                       0                       1                     0                             10                            7                           0                              0                             33                            0    4    1           1           3        20   119     187          1091              36              5              2               86            261             1                0                4              1               18             41             1                0                2              1              303               1                  0                  4                1              0             -100               25            100                3             694              1   3889    22              112                  3                 1                 0         0        0         -1           0              -1             -1              16            41            0               1               1             2              13            30            0               1               1             1             256              0                 6                 6              12             0               0               0             0               0               7            655             1                 1                0                   0                   1                 0                    4                  6                 0                    0                    1                  0                    4                  6                 0                    0                    1                  0                  150                   0                      0                     25                    0                           4                         2                        0                           0                          25                         0                    7                 368                  1
2        2   98543      0               0              0                 0                 0               0                  0                0               0                  0                  0                0                  0                0               0                  0                  0                0              0             0                0                0              0                 0               0              0                 0                 0               0                 0               0              0                 0                 0               0                   0                  0                     0                     0                   0                      0                    0                   0                      0                      0                    0                      0                    0                   0                      0                      0                    0                             0                           0                          0                             0                             0                           0               1              0                 0                 0               0                  8                8               0                  0                  0                0                  1                1               0                  0                  0                0              1             0                0                1              0                67              66              0                 0                 1               0                 1               1              0                 0                 1               0                   1                  0                     0                     0                   0                      1                    1                   0                      0                      0                    0                      1                    1                   0                      0                      0                    0                            12                          12                          0                             0                             0                           0               1              0                 0                 0               0                  9                9               0                  0                  0                0                  2                2               0                  0                  0                0              1             0                0                1              0               147             146              0                 0                 1               0                 2               2              0                 0                 1               0                   1                  0                     0                     0                   0                      1                    1                   0                      0                      0                    0                      1                    1                   0                      0                      0                    0                            11                          11                          0                             0                             0                           0               1              0                 0                 0               0                 23               23               0                  0                  0                0                  5                5               0                  0                  0                0              1             0                1                1              0               331             328              0                 1                 2               0                 6               6              0                 1                 2               0                   1                  0                     0                     0                   0                      1                    1                   0                      0                      0                    0                      1                    1                   0                      0                      0                    0                             4                           4                          0                             0                             0                           0                1               0                  0                  1                0                  30                27                0                   0                   3                 0                  10                 8                0                   0                   2                 0               1              0                 1                 1               0                606              590               0                  4                 12                0                 13               11               0                  4                  8                0                    1                   0                      0                      0                    0                       1                     1                    0                       0                       0                     0                       1                     1                    0                       0                       0                     0                              3                            3                           0                              0                              0                            0    4    1           1           3        20   119     187          1091              36              5              2               86            261             1                0                4              1               18             41             1                0                2              1              303               1                  0                  4                1              0             -100               25            100                3             694              1   3889    22              535                 17                 4                 1         0        0         -1           0              -1             -1            1591          3781            0              56              86            84              29            72            0              44              21             8             237              0                 3                 5               5             0               0               0             0               0               0            694            56                 1                0                   0                   0                 0                    4                 11                 0                    0                    0                  0                    4                 11                 0                    0                    0                  0                  275                   0                      0                      0                    0                           4                         4                        0                           0                           0                         0                    7                 565                  1
3        2  341714      0               0              0                 0                 0               0                  0                0               0                  0                  0                0                  0                0               0                  0                  0                0              0             0                0                0              0                 0               0              0                 0                 0               0                 0               0              0                 0                 0               0                   0                  0                     0                     0                   0                      0                    0                   0                      0                      0                    0                      0                    0                   0                      0                      0                    0                             0                           0                          0                             0                             0                           0               1              0                 0                 0               0                  8                8               0                  0                  0                0                  1                1               0                  0                  0                0              1             0                0                0              0                 8               8              0                 0                 0               0                 1               1              0                 0                 0               0                   1                  0                     0                     0                   0                      1                    1                   0                      0                      0                    0                      1                    1                   0                      0                      0                    0                            12                          12                          0                             0                             0                           0               1              0                 0                 0               0                  9                9               0                  0                  0                0                  2                2               0                  0                  0                0              1             0                0                0              0                25              25              0                 0                 0               0                 2               2              0                 0                 0               0                   1                  0                     0                     0                   0                      1                    1                   0                      0                      0                    0                      1                    1                   0                      0                      0                    0                            11                          11                          0                             0                             0                           0               1              0                 0                 0               0                 23               23               0                  0                  0                0                  5                5               0                  0                  0                0              1             0                0                0              0                85              85              0                 0                 0               0                 6               6              0                 0                 0               0                   1                  0                     0                     0                   0                      1                    1                   0                      0                      0                    0                      1                    1                   0                      0                      0                    0                             4                           4                          0                             0                             0                           0                1               0                  0                  1                0                  30                27                0                   0                   3                 0                  10                 8                0                   0                   2                 0               1              0                 1                 0               0                137              135               0                  2                  0                0                 11               11               0                  2                  0                0                    1                   0                      0                      0                    0                       1                     1                    0                       0                       0                     0                       1                     1                    0                       0                       0                     0                              3                            3                           0                              0                              0                            0    4    1           1           3        20   119     187          1091              36              5              2               86            261             1                0                4              1               18             41             1                0                2              1              303               1                  0                  4                1              0             -100               25            100                3             694              1   3889    22              340                 11                 3                 0         0        0         -1           0              -1             -1             394           922            0              14              19            26              27            72            0              13               4             7             234              0                 3                 4               6             0               0               0             0               0               2            685            16                 1                0                   0                   0                 0                    4                 10                 0                    0                    0                  0                    4                  9                 0                    0                    0                  0                  250                   0                      0                      0                    0                           4                         3                        0                           0                           0                         0                    7                 565                  1
4        2  185628      0               0              0                 0                 0               0                  0                0               0                  0                  0                0                  0                0               0                  0                  0                0              0             0                0                0              0                 0               0              0                 0                 0               0                 0               0              0                 0                 0               0                   0                  0                     0                     0                   0                      0                    0                   0                      0                      0                    0                      0                    0                   0                      0                      0                    0                             0                           0                          0                             0                             0                           0               1              0                 0                 0               0                  8                8               0                  0                  0                0                  1                1               0                  0                  0                0              1             0                1                0              0                 6               5              0                 1                 0               0                 1               1              0                 1                 0               0                   1                  0                     0                     0                   0                      1                    1                   0                      0                      0                    0                      1                    1                   0                      0                      0                    0                            12                          12                          0                             0                             0                           0               1              0                 0                 0               0                  9                9               0                  0                  0                0                  2                2               0                  0                  0                0              1             0                1                0              0                18              17              0                 1                 0               0                 2               2              0                 1                 0               0                   1                  0                     0                     0                   0                      1                    1                   0                      0                      0                    0                      1                    1                   0                      0                      0                    0                            11                          11                          0                             0                             0                           0               1              0                 0                 0               0                 23               23               0                  0                  0                0                  5                5               0                  0                  0                0              1             0                1                1              0                39              37              0                 1                 1               0                 6               6              0                 1                 1               0                   1                  0                     0                     0                   0                      1                    1                   0                      0                      0                    0                      1                    1                   0                      0                      0                    0                             4                           4                          0                             0                             0                           0                1               0                  0                  1                0                  30                27                0                   0                   3                 0                  10                 8                0                   0                   2                 0               1              0                 1                 1               0                 80               77               0                  1                  2                0                 12               11               0                  1                  2                0                    1                   0                      0                      0                    0                       1                     1                    0                       0                       0                     0                       1                     1                    0                       0                       0                     0                              3                            3                           0                              0                              0                            0    4    1           1           3        20   119     187          1091              36              5              2               86            261             1                0                4              1               18             41             1                0                2              1              303               1                  0                  4                1              0             -100               25            100                3             694              1   3889    22              161                  5                 2                 0         0        0         -1           0              -1             -1             224           622            0              12              10             3              28            72            0              10               5             3             277              0                 5                 4               1             0               0               0             0               0               3            687            12                 1                0                   0                   0                 0                    4                  8                 0                    0                    0                  0                    4                  8                 0                    0                    0                  0                  200                   0                      0                      0                    0                           4                         3                        0                           0                           0                         0                    7                 565                  1
tail
        user_id  sku_id  label  1_user_if_view  1_user_if_buy  1_user_if_follow  1_user_if_remark  1_user_if_cart  1_user_action_amt  1_user_view_amt  1_user_buy_amt  1_user_follow_amt  1_user_remark_amt  1_user_cart_amt  1_user_active_day  1_user_view_day  1_user_buy_day  1_user_follow_day  1_user_remark_day  1_user_cart_day  1_sku_if_view  1_sku_if_buy  1_sku_if_follow  1_sku_if_remark  1_sku_if_cart  1_sku_action_amt  1_sku_view_amt  1_sku_buy_amt  1_sku_follow_amt  1_sku_remark_amt  1_sku_cart_amt  1_sku_active_day  1_sku_view_day  1_sku_buy_day  1_sku_follow_day  1_sku_remark_day  1_sku_cart_day  1_user_sku_if_view  1_user_sku_if_buy  1_user_sku_if_follow  1_user_sku_if_remark  1_user_sku_if_cart  1_user_sku_action_amt  1_user_sku_view_amt  1_user_sku_buy_amt  1_user_sku_follow_amt  1_user_sku_remark_amt  1_user_sku_cart_amt  1_user_sku_action_day  1_user_sku_view_day  1_user_sku_buy_day  1_user_sku_follow_day  1_user_sku_remark_day  1_user_sku_cart_day  1_user_sku_user_action_ratio  1_user_sku_user_view_ratio  1_user_sku_user_buy_ratio  1_user_sku_user_follow_ratio  1_user_sku_user_remark_ratio  1_user_sku_user_cart_ratio  2_user_if_view  2_user_if_buy  2_user_if_follow  2_user_if_remark  2_user_if_cart  2_user_action_amt  2_user_view_amt  2_user_buy_amt  2_user_follow_amt  2_user_remark_amt  2_user_cart_amt  2_user_active_day  2_user_view_day  2_user_buy_day  2_user_follow_day  2_user_remark_day  2_user_cart_day  2_sku_if_view  2_sku_if_buy  2_sku_if_follow  2_sku_if_remark  2_sku_if_cart  2_sku_action_amt  2_sku_view_amt  2_sku_buy_amt  2_sku_follow_amt  2_sku_remark_amt  2_sku_cart_amt  2_sku_active_day  2_sku_view_day  2_sku_buy_day  2_sku_follow_day  2_sku_remark_day  2_sku_cart_day  2_user_sku_if_view  2_user_sku_if_buy  2_user_sku_if_follow  2_user_sku_if_remark  2_user_sku_if_cart  2_user_sku_action_amt  2_user_sku_view_amt  2_user_sku_buy_amt  2_user_sku_follow_amt  2_user_sku_remark_amt  2_user_sku_cart_amt  2_user_sku_action_day  2_user_sku_view_day  2_user_sku_buy_day  2_user_sku_follow_day  2_user_sku_remark_day  2_user_sku_cart_day  2_user_sku_user_action_ratio  2_user_sku_user_view_ratio  2_user_sku_user_buy_ratio  2_user_sku_user_follow_ratio  2_user_sku_user_remark_ratio  2_user_sku_user_cart_ratio  3_user_if_view  3_user_if_buy  3_user_if_follow  3_user_if_remark  3_user_if_cart  3_user_action_amt  3_user_view_amt  3_user_buy_amt  3_user_follow_amt  3_user_remark_amt  3_user_cart_amt  3_user_action_day  3_user_view_day  3_user_buy_day  3_user_follow_day  3_user_remark_day  3_user_cart_day  3_sku_if_view  3_sku_if_buy  3_sku_if_follow  3_sku_if_remark  3_sku_if_cart  3_sku_action_amt  3_sku_view_amt  3_sku_buy_amt  3_sku_follow_amt  3_sku_remark_amt  3_sku_cart_amt  3_sku_active_day  3_sku_view_day  3_sku_buy_day  3_sku_follow_day  3_sku_remark_day  3_sku_cart_day  3_user_sku_if_view  3_user_sku_if_buy  3_user_sku_if_follow  3_user_sku_if_remark  3_user_sku_if_cart  3_user_sku_action_amt  3_user_sku_view_amt  3_user_sku_buy_amt  3_user_sku_follow_amt  3_user_sku_remark_amt  3_user_sku_cart_amt  3_user_sku_action_day  3_user_sku_view_day  3_user_sku_buy_day  3_user_sku_follow_day  3_user_sku_remark_day  3_user_sku_cart_day  3_user_sku_user_action_ratio  3_user_sku_user_view_ratio  3_user_sku_user_buy_ratio  3_user_sku_user_follow_ratio  3_user_sku_user_remark_ratio  3_user_sku_user_cart_ratio  7_user_if_view  7_user_if_buy  7_user_if_follow  7_user_if_remark  7_user_if_cart  7_user_action_amt  7_user_view_amt  7_user_buy_amt  7_user_follow_amt  7_user_remark_amt  7_user_cart_amt  7_user_active_day  7_user_view_day  7_user_buy_day  7_user_follow_day  7_user_remark_day  7_user_cart_day  7_sku_if_view  7_sku_if_buy  7_sku_if_follow  7_sku_if_remark  7_sku_if_cart  7_sku_action_amt  7_sku_view_amt  7_sku_buy_amt  7_sku_follow_amt  7_sku_remark_amt  7_sku_cart_amt  7_sku_active_day  7_sku_view_day  7_sku_buy_day  7_sku_follow_day  7_sku_remark_day  7_sku_cart_day  7_user_sku_if_view  7_user_sku_if_buy  7_user_sku_if_follow  7_user_sku_if_remark  7_user_sku_if_cart  7_user_sku_action_amt  7_user_sku_view_amt  7_user_sku_buy_amt  7_user_sku_follow_amt  7_user_sku_remark_amt  7_user_sku_cart_amt  7_user_sku_action_day  7_user_sku_view_day  7_user_sku_buy_day  7_user_sku_follow_day  7_user_sku_remark_day  7_user_sku_cart_day  7_user_sku_user_action_ratio  7_user_sku_user_view_ratio  7_user_sku_user_buy_ratio  7_user_sku_user_follow_ratio  7_user_sku_user_remark_ratio  7_user_sku_user_cart_ratio  14_user_if_view  14_user_if_buy  14_user_if_follow  14_user_if_remark  14_user_if_cart  14_user_action_amt  14_user_view_amt  14_user_buy_amt  14_user_follow_amt  14_user_remark_amt  14_user_cart_amt  14_user_active_day  14_user_view_day  14_user_buy_day  14_user_follow_day  14_user_remark_day  14_user_cart_day  14_sku_if_view  14_sku_if_buy  14_sku_if_follow  14_sku_if_remark  14_sku_if_cart  14_sku_action_amt  14_sku_view_amt  14_sku_buy_amt  14_sku_follow_amt  14_sku_remark_amt  14_sku_cart_amt  14_sku_active_day  14_sku_view_day  14_sku_buy_day  14_sku_follow_day  14_sku_remark_day  14_sku_cart_day  14_user_sku_if_view  14_user_sku_if_buy  14_user_sku_if_follow  14_user_sku_if_remark  14_user_sku_if_cart  14_user_sku_action_amt  14_user_sku_view_amt  14_user_sku_buy_amt  14_user_sku_follow_amt  14_user_sku_remark_amt  14_user_sku_cart_amt  14_user_sku_action_day  14_user_sku_view_day  14_user_sku_buy_day  14_user_sku_follow_day  14_user_sku_remark_day  14_user_sku_cart_day  14_user_sku_user_action_ratio  14_user_sku_user_view_ratio  14_user_sku_user_buy_ratio  14_user_sku_user_follow_ratio  14_user_sku_user_remark_ratio  14_user_sku_user_cart_ratio  age  sex  user_lv_cd  city_level  province  city  county  user_reg_day  user_reg_month  user_reg_cate  user_reg_year  user_action_amt  user_view_amt  user_buy_amt  user_follow_amt  user_remark_amt  user_cart_amt  user_active_day  user_view_day  user_buy_day  user_follow_day  user_remark_day  user_cart_day  user_view_ratio  user_buy_ratio  user_follow_ratio  user_remark_ratio  user_cart_ratio  user_buy/view  user_buy/follow  user_buy/remark  user_buy/cart  user_first_hour  user_last_hour  user_last_amt  brand  cate  product_reg_day  product_reg_month  product_reg_cate  product_reg_year  fans_num  vip_num  shop_cate  shop_score  shop_reg_month  shop_reg_cate  sku_action_amt  sku_view_amt  sku_buy_amt  sku_follow_amt  sku_remark_amt  sku_cart_amt  sku_active_day  sku_view_day  sku_buy_day  sku_follow_day  sku_remark_day  sku_cart_day  sku_view_ratio  sku_buy_ratio  sku_follow_ratio  sku_remark_ratio  sku_cart_ratio  sku_buy/view  sku_buy/follow  sku_buy/remark  sku_buy/cart  sku_rebuy_rate  sku_first_hour  sku_last_hour  sku_last_amt  user_sku_if_view  user_sku_if_buy  user_sku_if_follow  user_sku_if_remark  user_sku_if_cart  user_sku_action_amt  user_sku_view_amt  user_sku_buy_amt  user_sku_follow_amt  user_sku_remark_amt  user_sku_cart_amt  user_sku_action_day  user_sku_view_day  user_sku_buy_day  user_sku_follow_day  user_sku_remark_day  user_sku_cart_day  user_sku_view_ratio  user_sku_buy_ratio  user_sku_follow_ratio  user_sku_remark_ratio  user_sku_cart_ratio  user_sku_user_action_ratio  user_sku_user_view_ratio  user_sku_user_buy_ratio  user_sku_user_follow_ratio  user_sku_user_remark_ratio  user_sku_user_cart_ratio  user_sku_first_hour  user_sku_last_hour  user_sku_last_amt
738721  1608705   10554      0               0              0                 0                 0               0                  0                0               0                  0                  0                0                  0                0               0                  0                  0                0              0             0                0                0              0                 0               0              0                 0                 0               0                 0               0              0                 0                 0               0                   0                  0                     0                     0                   0                      0                    0                   0                      0                      0                    0                      0                    0                   0                      0                      0                    0                             0                           0                          0                             0                             0                           0               0              0                 0                 0               0                  0                0               0                  0                  0                0                  0                0               0                  0                  0                0              0             0                0                0              0                 0               0              0                 0                 0               0                 0               0              0                 0                 0               0                   0                  0                     0                     0                   0                      0                    0                   0                      0                      0                    0                      0                    0                   0                      0                      0                    0                             0                           0                          0                             0                             0                           0               1              1                 0                 0               0                 21               20               1                  0                  0                0                  1                1               1                  0                  0                0              1             1                0                0              0                 6               4              2                 0                 0               0                 1               1              1                 0                 0               0                   1                  0                     0                     0                   0                      1                    1                   0                      0                      0                    0                      1                    1                   0                      0                      0                    0                             4                           5                          0                             0                             0                           0               1              1                 0                 0               0                 30               29               1                  0                  0                0                  2                2               1                  0                  0                0              1             1                0                1              0                21              16              4                 0                 1               0                 5               5              3                 0                 1               0                   1                  0                     0                     0                   0                      1                    1                   0                      0                      0                    0                      1                    1                   0                      0                      0                    0                             3                           3                          0                             0                             0                           0                1               1                  0                  0                0                  30                29                1                   0                   0                 0                   2                 2                1                   0                   0                 0               1              1                 0                 1               0                 34               26               5                  0                  3                0                 11               10               4                  0                  3                0                    1                   0                      0                      0                    0                       1                     1                    0                       0                       0                     0                       1                     1                    0                       0                       0                     0                              3                            3                           0                              0                              0                            0    6    1           1           4        20   120     741           454              15              4              1               30             32             1                0                0              0                2              3             1                0                0              0              106               3                  0                  0                0              3             -100             -100           -100               28             123              9   2777    34              856                 28                 5                 2    205360   545675         47           9              29              5             146           273           37               5              12            15              24            63           24               5               5             7             186             25                 3                 8              10            13             740             308           246               0              27            680             5                 1                0                   0                   0                 0                    1                  1                 0                    0                    0                  0                    1                  1                 0                    0                    0                  0                  100                   0                      0                      0                    0                           3                         3                        0                           0                           0                         0                   31                  31                  1
738722  1608705  238979      0               0              0                 0                 0               0                  0                0               0                  0                  0                0                  0                0               0                  0                  0                0              0             0                0                0              0                 0               0              0                 0                 0               0                 0               0              0                 0                 0               0                   0                  0                     0                     0                   0                      0                    0                   0                      0                      0                    0                      0                    0                   0                      0                      0                    0                             0                           0                          0                             0                             0                           0               0              0                 0                 0               0                  0                0               0                  0                  0                0                  0                0               0                  0                  0                0              0             0                0                0              0                 0               0              0                 0                 0               0                 0               0              0                 0                 0               0                   0                  0                     0                     0                   0                      0                    0                   0                      0                      0                    0                      0                    0                   0                      0                      0                    0                             0                           0                          0                             0                             0                           0               1              1                 0                 0               0                 21               20               1                  0                  0                0                  1                1               1                  0                  0                0              1             0                0                0              0                 1               1              0                 0                 0               0                 1               1              0                 0                 0               0                   1                  0                     0                     0                   0                      1                    1                   0                      0                      0                    0                      1                    1                   0                      0                      0                    0                             4                           5                          0                             0                             0                           0               1              1                 0                 0               0                 30               29               1                  0                  0                0                  2                2               1                  0                  0                0              1             0                1                0              0                 5               4              0                 1                 0               0                 4               4              0                 1                 0               0                   1                  0                     0                     0                   0                      1                    1                   0                      0                      0                    0                      1                    1                   0                      0                      0                    0                             3                           3                          0                             0                             0                           0                1               1                  0                  0                0                  30                29                1                   0                   0                 0                   2                 2                1                   0                   0                 0               1              0                 1                 0               0                  9                8               0                  1                  0                0                  7                7               0                  1                  0                0                    1                   0                      0                      0                    0                       1                     1                    0                       0                       0                     0                       1                     1                    0                       0                       0                     0                              3                            3                           0                              0                              0                            0    6    1           1           4        20   120     741           454              15              4              1               30             32             1                0                0              0                2              3             1                0                0              0              106               3                  0                  0                0              3             -100             -100           -100               28             123              9   2777    34              173                  5                 2                 0     66810    93048         47           9               5              2              67           109           14               1               2             1              22            48           11               1               1             1             162             20                 1                 2               1            12            1400             700          1400               7              31            687             3                 1                0                   0                   0                 0                    1                  1                 0                    0                    0                  0                    1                  1                 0                    0                    0                  0                  100                   0                      0                      0                    0                           3                         3                        0                           0                           0                         0                   31                  31                  1
738723  1608705  101645      0               0              0                 0                 0               0                  0                0               0                  0                  0                0                  0                0               0                  0                  0                0              0             0                0                0              0                 0               0              0                 0                 0               0                 0               0              0                 0                 0               0                   0                  0                     0                     0                   0                      0                    0                   0                      0                      0                    0                      0                    0                   0                      0                      0                    0                             0                           0                          0                             0                             0                           0               0              0                 0                 0               0                  0                0               0                  0                  0                0                  0                0               0                  0                  0                0              1             0                1                1              0               373             360              0                 6                 7               0                 1               1              0                 1                 1               0                   0                  0                     0                     0                   0                      0                    0                   0                      0                      0                    0                      0                    0                   0                      0                      0                    0                             0                           0                          0                             0                             0                           0               1              1                 0                 0               0                 21               20               1                  0                  0                0                  1                1               1                  0                  0                0              1             0                1                1              0               806             773              0                14                19               0                 2               2              0                 2                 2               0                   1                  0                     0                     0                   0                      1                    1                   0                      0                      0                    0                      1                    1                   0                      0                      0                    0                             4                           5                          0                             0                             0                           0               1              1                 0                 0               0                 30               29               1                  0                  0                0                  2                2               1                  0                  0                0              1             0                1                1              0              2226            2144              0                28                54               0                 6               6              0                 6                 6               0                   1                  0                     0                     0                   0                      2                    2                   0                      0                      0                    0                      2                    2                   0                      0                      0                    0                             6                           6                          0                             0                             0                           0                1               1                  0                  0                0                  30                29                1                   0                   0                 0                   2                 2                1                   0                   0                 0               1              0                 1                 1               0               4150             3984               0                 52                114                0                 13               13               0                 12                 13                0                    1                   0                      0                      0                    0                       2                     2                    0                       0                       0                     0                       2                     2                    0                       0                       0                     0                              6                            6                           0                              0                              0                            0    6    1           1           4        20   120     741           454              15              4              1               30             32             1                0                0              0                2              3             1                0                0              0              106               3                  0                  0                0              3             -100             -100           -100               28             123              9   2484    34             1138                 37                 5                 3         0        0         -1           0              -1             -1           11647         28790            0             314             553           498              29            74            0              70              29             8             247              0                 2                 4               4             0               0               0             0               0               0            695           563                 1                0                   0                   0                 0                    2                  2                 0                    0                    0                  0                    2                  2                 0                    0                    0                  0                  100                   0                      0                      0                    0                           6                         6                        0                           0                           0                         0                   31                 123                  1
738724  1608705   50755      0               0              0                 0                 0               0                  0                0               0                  0                  0                0                  0                0               0                  0                  0                0              0             0                0                0              0                 0               0              0                 0                 0               0                 0               0              0                 0                 0               0                   0                  0                     0                     0                   0                      0                    0                   0                      0                      0                    0                      0                    0                   0                      0                      0                    0                             0                           0                          0                             0                             0                           0               0              0                 0                 0               0                  0                0               0                  0                  0                0                  0                0               0                  0                  0                0              1             0                1                1              0               104             102              0                 1                 1               0                 1               1              0                 1                 1               0                   0                  0                     0                     0                   0                      0                    0                   0                      0                      0                    0                      0                    0                   0                      0                      0                    0                             0                           0                          0                             0                             0                           0               1              1                 0                 0               0                 21               20               1                  0                  0                0                  1                1               1                  0                  0                0              1             0                1                1              0               206             203              0                 2                 1               0                 2               2              0                 2                 1               0                   1                  0                     0                     0                   0                      1                    1                   0                      0                      0                    0                      1                    1                   0                      0                      0                    0                             4                           5                          0                             0                             0                           0               1              1                 0                 0               0                 30               29               1                  0                  0                0                  2                2               1                  0                  0                0              1             0                1                1              0               623             614              0                 6                 3               0                 6               6              0                 5                 3               0                   1                  0                     0                     0                   0                      1                    1                   0                      0                      0                    0                      1                    1                   0                      0                      0                    0                             3                           3                          0                             0                             0                           0                1               1                  0                  0                0                  30                29                1                   0                   0                 0                   2                 2                1                   0                   0                 0               1              0                 1                 1               0               1189             1151               0                 19                 19                0                 13               12               0                 12                 10                0                    1                   0                      0                      0                    0                       1                     1                    0                       0                       0                     0                       1                     1                    0                       0                       0                     0                              3                            3                           0                              0                              0                            0    6    1           1           4        20   120     741           454              15              4              1               30             32             1                0                0              0                2              3             1                0                0              0              106               3                  0                  0                0              3             -100             -100           -100               28             123              9   2777    34              552                 18                 4                 1         0        0         -1           0              -1             -1            4075         14436            0             180             175           110              29            73            0              67              23             8             354              0                 4                 4               2             0               0               0             0               0               0            695           227                 1                0                   0                   0                 0                    1                  1                 0                    0                    0                  0                    1                  1                 0                    0                    0                  0                  100                   0                      0                      0                    0                           3                         3                        0                           0                           0                         0                   31                  31                  1
738725  1608707  100598      0               0              0                 0                 0               0                  0                0               0                  0                  0                0                  0                0               0                  0                  0                0              0             0                0                0              0                 0               0              0                 0                 0               0                 0               0              0                 0                 0               0                   0                  0                     0                     0                   0                      0                    0                   0                      0                      0                    0                      0                    0                   0                      0                      0                    0                             0                           0                          0                             0                             0                           0               1              1                 0                 0               0                  2                1               1                  0                  0                0                  1                1               1                  0                  0                0              1             1                1                1              0               248             125             80                38                 5               0                 1               1              1                 1                 1               0                   1                  1                     0                     0                   0                      2                    1                   1                      0                      0                    0                      1                    1                   1                      0                      0                    0                           100                         100                        100                             0                             0                           0               1              1                 0                 0               0                  2                1               1                  0                  0                0                  1                1               1                  0                  0                0              1             1                1                1              0               284             154             82                38                10               0                 2               2              2                 1                 2               0                   1                  1                     0                     0                   0                      2                    1                   1                      0                      0                    0                      1                    1                   1                      0                      0                    0                           100                         100                        100                             0                             0                           0               1              1                 0                 0               0                  2                1               1                  0                  0                0                  1                1               1                  0                  0                0              1             1                1                1              0               443             277            106                42                18               0                 6               6              6                 3                 6               0                   1                  1                     0                     0                   0                      2                    1                   1                      0                      0                    0                      1                    1                   1                      0                      0                    0                           100                         100                        100                             0                             0                           0                1               1                  0                  0                0                   2                 1                1                   0                   0                 0                   1                 1                1                   0                   0                 0               1              1                 1                 1               0                759              462             178                 64                 55                0                 13               11              13                  8                 12                0                    1                   1                      0                      0                    0                       2                     1                    1                       0                       0                     0                       1                     1                    1                       0                       0                     0                            100                          100                         100                              0                              0                            0    5    1           6           3        23   204    1991            41               1              1              0                2              1             1                0                1              0                1              1             1                0                0              0               50              50                  0                 50                0            100             -100              100           -100               13              13              2   2777    34              173                  5                 2                 0     66810    93048         47           9               5              2            1437          2915          606             160             246            72              29            72           74              39              27             8             202             42                11                17               5            20             378             246           841               3               0            695            40                 1                1                   0                   0                 0                    2                  1                 1                    0                    0                  0                    1                  1                 1                    0                    0                  0                   50                  50                      0                      0                    0                         100                       100                      100                           0                           0                         0                   13                  13                  2
2019-05-25 19:03:44.702595
>> 完成生成特征(738726, 391)
2019-05-25 19:03:44.703597

>> 开始生成特征(X,y)
end_date 2018-4-1
2019-05-25 19:03:44.704098
> 获取标签
action_180330_180401
buy_180402_180408
真实购买 (168034, 2)
可能购买 (732229, 2)
shape (732229, 3)
cols Index(['user_id', 'sku_id', 'label'], dtype='object')
head
   user_id  sku_id  label
0        2   45733      0
1        2  338588      0
2        4  262872      0
3        4  295865      0
4        4  337682      0
tail
        user_id  sku_id  label
732224  1608696  121463      0
732225  1608696   74146      0
732226  1608696  322243      0
732227  1608704  320471      0
732228  1608704   31993      0
2019-05-25 19:03:46.104281
> 遍历特征 gap=1
user_if_view_180401_180401
user_if_buy_180401_180401
user_if_follow_180401_180401
user_if_remark_180401_180401
user_if_cart_180401_180401
user_action_amt_180401_180401
user_view_amt_180401_180401
user_buy_amt_180401_180401
user_follow_amt_180401_180401
user_remark_amt_180401_180401
user_cart_amt_180401_180401
user_action_day_180401_180401
user_view_day_180401_180401
user_buy_day_180401_180401
user_follow_day_180401_180401
user_remark_day_180401_180401
user_cart_day_180401_180401
sku_if_view_180401_180401
sku_if_buy_180401_180401
sku_if_follow_180401_180401
sku_if_remark_180401_180401
sku_if_cart_180401_180401
sku_action_amt_180401_180401
sku_view_amt_180401_180401
sku_buy_amt_180401_180401
sku_follow_amt_180401_180401
sku_remark_amt_180401_180401
sku_cart_amt_180401_180401
sku_action_day_180401_180401
sku_view_day_180401_180401
sku_buy_day_180401_180401
sku_follow_day_180401_180401
sku_remark_day_180401_180401
sku_cart_day_180401_180401
user_sku_if_view_180401_180401
user_sku_if_buy_180401_180401
user_sku_if_follow_180401_180401
user_sku_if_remark_180401_180401
user_sku_if_cart_180401_180401
user_sku_action_amt_180401_180401
user_sku_view_amt_180401_180401
user_sku_buy_amt_180401_180401
user_sku_follow_amt_180401_180401
user_sku_remark_amt_180401_180401
user_sku_cart_amt_180401_180401
user_sku_action_day_180401_180401
user_sku_view_day_180401_180401
user_sku_buy_day_180401_180401
user_sku_follow_day_180401_180401
user_sku_remark_day_180401_180401
user_sku_cart_day_180401_180401
user_sku_user_action_ratio_180401_180401
2019-05-25 19:04:24.163427
> 遍历特征 gap=2
user_if_view_180331_180401
user_if_buy_180331_180401
user_if_follow_180331_180401
user_if_remark_180331_180401
user_if_cart_180331_180401
user_action_amt_180331_180401
user_view_amt_180331_180401
user_buy_amt_180331_180401
user_follow_amt_180331_180401
user_remark_amt_180331_180401
user_cart_amt_180331_180401
user_action_day_180331_180401
user_view_day_180331_180401
user_buy_day_180331_180401
user_follow_day_180331_180401
user_remark_day_180331_180401
user_cart_day_180331_180401
sku_if_view_180331_180401
sku_if_buy_180331_180401
sku_if_follow_180331_180401
sku_if_remark_180331_180401
sku_if_cart_180331_180401
sku_action_amt_180331_180401
sku_view_amt_180331_180401
sku_buy_amt_180331_180401
sku_follow_amt_180331_180401
sku_remark_amt_180331_180401
sku_cart_amt_180331_180401
sku_action_day_180331_180401
sku_view_day_180331_180401
sku_buy_day_180331_180401
sku_follow_day_180331_180401
sku_remark_day_180331_180401
sku_cart_day_180331_180401
user_sku_if_view_180331_180401
user_sku_if_buy_180331_180401
user_sku_if_follow_180331_180401
user_sku_if_remark_180331_180401
user_sku_if_cart_180331_180401
user_sku_action_amt_180331_180401
user_sku_view_amt_180331_180401
user_sku_buy_amt_180331_180401
user_sku_follow_amt_180331_180401
user_sku_remark_amt_180331_180401
user_sku_cart_amt_180331_180401
user_sku_action_day_180331_180401
user_sku_view_day_180331_180401
user_sku_buy_day_180331_180401
user_sku_follow_day_180331_180401
user_sku_remark_day_180331_180401
user_sku_cart_day_180331_180401
user_sku_user_action_ratio_180331_180401
2019-05-25 19:04:47.940151
> 遍历特征 gap=3
user_if_view_180330_180401
user_if_buy_180330_180401
user_if_follow_180330_180401
user_if_remark_180330_180401
user_if_cart_180330_180401
user_action_amt_180330_180401
user_view_amt_180330_180401
user_buy_amt_180330_180401
user_follow_amt_180330_180401
user_remark_amt_180330_180401
user_cart_amt_180330_180401
user_action_day_180330_180401
user_view_day_180330_180401
user_buy_day_180330_180401
user_follow_day_180330_180401
user_remark_day_180330_180401
user_cart_day_180330_180401
sku_if_view_180330_180401
sku_if_buy_180330_180401
sku_if_follow_180330_180401
sku_if_remark_180330_180401
sku_if_cart_180330_180401
sku_action_amt_180330_180401
sku_view_amt_180330_180401
sku_buy_amt_180330_180401
sku_follow_amt_180330_180401
sku_remark_amt_180330_180401
sku_cart_amt_180330_180401
sku_action_day_180330_180401
sku_view_day_180330_180401
sku_buy_day_180330_180401
sku_follow_day_180330_180401
sku_remark_day_180330_180401
sku_cart_day_180330_180401
user_sku_if_view_180330_180401
user_sku_if_buy_180330_180401
user_sku_if_follow_180330_180401
user_sku_if_remark_180330_180401
user_sku_if_cart_180330_180401
user_sku_action_amt_180330_180401
user_sku_view_amt_180330_180401
user_sku_buy_amt_180330_180401
user_sku_follow_amt_180330_180401
user_sku_remark_amt_180330_180401
user_sku_cart_amt_180330_180401
user_sku_action_day_180330_180401
user_sku_view_day_180330_180401
user_sku_buy_day_180330_180401
user_sku_follow_day_180330_180401
user_sku_remark_day_180330_180401
user_sku_cart_day_180330_180401
user_sku_user_action_ratio_180330_180401
2019-05-25 19:05:12.560586
> 遍历特征 gap=7
user_if_view_180326_180401
user_if_buy_180326_180401
user_if_follow_180326_180401
user_if_remark_180326_180401
user_if_cart_180326_180401
user_action_amt_180326_180401
user_view_amt_180326_180401
user_buy_amt_180326_180401
user_follow_amt_180326_180401
user_remark_amt_180326_180401
user_cart_amt_180326_180401
user_action_day_180326_180401
user_view_day_180326_180401
user_buy_day_180326_180401
user_follow_day_180326_180401
user_remark_day_180326_180401
user_cart_day_180326_180401
sku_if_view_180326_180401
sku_if_buy_180326_180401
sku_if_follow_180326_180401
sku_if_remark_180326_180401
sku_if_cart_180326_180401
sku_action_amt_180326_180401
sku_view_amt_180326_180401
sku_buy_amt_180326_180401
sku_follow_amt_180326_180401
sku_remark_amt_180326_180401
sku_cart_amt_180326_180401
sku_action_day_180326_180401
sku_view_day_180326_180401
sku_buy_day_180326_180401
sku_follow_day_180326_180401
sku_remark_day_180326_180401
sku_cart_day_180326_180401
user_sku_if_view_180326_180401
user_sku_if_buy_180326_180401
user_sku_if_follow_180326_180401
user_sku_if_remark_180326_180401
user_sku_if_cart_180326_180401
user_sku_action_amt_180326_180401
user_sku_view_amt_180326_180401
user_sku_buy_amt_180326_180401
user_sku_follow_amt_180326_180401
user_sku_remark_amt_180326_180401
user_sku_cart_amt_180326_180401
user_sku_action_day_180326_180401
user_sku_view_day_180326_180401
user_sku_buy_day_180326_180401
user_sku_follow_day_180326_180401
user_sku_remark_day_180326_180401
user_sku_cart_day_180326_180401
user_sku_user_action_ratio_180326_180401
2019-05-25 19:05:39.476912
> 遍历特征 gap=14
user_if_view_180319_180401
user_if_buy_180319_180401
user_if_follow_180319_180401
user_if_remark_180319_180401
user_if_cart_180319_180401
user_action_amt_180319_180401
user_view_amt_180319_180401
user_buy_amt_180319_180401
user_follow_amt_180319_180401
user_remark_amt_180319_180401
user_cart_amt_180319_180401
user_action_day_180319_180401
user_view_day_180319_180401
user_buy_day_180319_180401
user_follow_day_180319_180401
user_remark_day_180319_180401
user_cart_day_180319_180401
sku_if_view_180319_180401
sku_if_buy_180319_180401
sku_if_follow_180319_180401
sku_if_remark_180319_180401
sku_if_cart_180319_180401
sku_action_amt_180319_180401
sku_view_amt_180319_180401
sku_buy_amt_180319_180401
sku_follow_amt_180319_180401
sku_remark_amt_180319_180401
sku_cart_amt_180319_180401
sku_action_day_180319_180401
sku_view_day_180319_180401
sku_buy_day_180319_180401
sku_follow_day_180319_180401
sku_remark_day_180319_180401
sku_cart_day_180319_180401
user_sku_if_view_180319_180401
user_sku_if_buy_180319_180401
user_sku_if_follow_180319_180401
user_sku_if_remark_180319_180401
user_sku_if_cart_180319_180401
user_sku_action_amt_180319_180401
user_sku_view_amt_180319_180401
user_sku_buy_amt_180319_180401
user_sku_follow_amt_180319_180401
user_sku_remark_amt_180319_180401
user_sku_cart_amt_180319_180401
user_sku_action_day_180319_180401
user_sku_view_day_180319_180401
user_sku_buy_day_180319_180401
user_sku_follow_day_180319_180401
user_sku_remark_day_180319_180401
user_sku_cart_day_180319_180401
user_sku_user_action_ratio_180319_180401
2019-05-25 19:06:13.910021
> 遍历全局特征
user.csv
user_action_amt_180303_180401
user_view_amt_180303_180401
user_buy_amt_180303_180401
user_follow_amt_180303_180401
user_remark_amt_180303_180401
user_cart_amt_180303_180401
user_action_day_180303_180401
user_view_day_180303_180401
user_buy_day_180303_180401
user_follow_day_180303_180401
user_remark_day_180303_180401
user_cart_day_180303_180401
user_action_ratio_180303_180401
user_buy_rate_180303_180401
user_first_hour_180303_180401
user_last_hour_180303_180401
user_last_amt_180303_180401
sku_plus
sku_action_amt_180303_180401
sku_view_amt_180303_180401
sku_buy_amt_180303_180401
sku_follow_amt_180303_180401
sku_remark_amt_180303_180401
sku_cart_amt_180303_180401
sku_action_day_180303_180401
sku_view_day_180303_180401
sku_buy_day_180303_180401
sku_follow_day_180303_180401
sku_remark_day_180303_180401
sku_cart_day_180303_180401
sku_action_ratio_180303_180401
sku_buy_rate_180303_180401
sku_rebuy_rate_180303_180401
sku_first_hour_180303_180401
sku_last_hour_180303_180401
sku_last_amt_180303_180401
user_sku_if_view_180303_180401
user_sku_if_buy_180303_180401
user_sku_if_follow_180303_180401
user_sku_if_remark_180303_180401
user_sku_if_cart_180303_180401
user_sku_action_amt_180303_180401
user_sku_view_amt_180303_180401
user_sku_buy_amt_180303_180401
user_sku_follow_amt_180303_180401
user_sku_remark_amt_180303_180401
user_sku_cart_amt_180303_180401
user_sku_action_day_180303_180401
user_sku_view_day_180303_180401
user_sku_buy_day_180303_180401
user_sku_follow_day_180303_180401
user_sku_remark_day_180303_180401
user_sku_cart_day_180303_180401
user_sku_action_ratio_180303_180401
user_sku_user_action_ratio_180303_180401
user_sku_first_hour_180303_180401
user_sku_last_hour_180303_180401
user_sku_last_amt_180303_180401
2019-05-25 19:07:46.546065
>>开始保存特征(732229, 391)
feat (732229, 391)
cols Index(['user_id', 'sku_id', 'label', '1_user_if_view', '1_user_if_buy',
       '1_user_if_follow', '1_user_if_remark', '1_user_if_cart',
       '1_user_action_amt', '1_user_view_amt',
       ...
       'user_sku_cart_ratio', 'user_sku_user_action_ratio',
       'user_sku_user_view_ratio', 'user_sku_user_buy_ratio',
       'user_sku_user_follow_ratio', 'user_sku_user_remark_ratio',
       'user_sku_user_cart_ratio', 'user_sku_first_hour', 'user_sku_last_hour',
       'user_sku_last_amt'],
      dtype='object', length=391)
head
   user_id  sku_id  label  1_user_if_view  1_user_if_buy  1_user_if_follow  1_user_if_remark  1_user_if_cart  1_user_action_amt  1_user_view_amt  1_user_buy_amt  1_user_follow_amt  1_user_remark_amt  1_user_cart_amt  1_user_action_day  1_user_view_day  1_user_buy_day  1_user_follow_day  1_user_remark_day  1_user_cart_day  1_sku_if_view  1_sku_if_buy  1_sku_if_follow  1_sku_if_remark  1_sku_if_cart  1_sku_action_amt  1_sku_view_amt  1_sku_buy_amt  1_sku_follow_amt  1_sku_remark_amt  1_sku_cart_amt  1_sku_action_day  1_sku_view_day  1_sku_buy_day  1_sku_follow_day  1_sku_remark_day  1_sku_cart_day  1_user_sku_if_view  1_user_sku_if_buy  1_user_sku_if_follow  1_user_sku_if_remark  1_user_sku_if_cart  1_user_sku_action_amt  1_user_sku_view_amt  1_user_sku_buy_amt  1_user_sku_follow_amt  1_user_sku_remark_amt  1_user_sku_cart_amt  1_user_sku_action_day  1_user_sku_view_day  1_user_sku_buy_day  1_user_sku_follow_day  1_user_sku_remark_day  1_user_sku_cart_day  1_user_sku_user_action_ratio  1_user_sku_user_view_ratio  1_user_sku_user_buy_ratio  1_user_sku_user_follow_ratio  1_user_sku_user_remark_ratio  1_user_sku_user_cart_ratio  2_user_if_view  2_user_if_buy  2_user_if_follow  2_user_if_remark  2_user_if_cart  2_user_action_amt  2_user_view_amt  2_user_buy_amt  2_user_follow_amt  2_user_remark_amt  2_user_cart_amt  2_user_action_day  2_user_view_day  2_user_buy_day  2_user_follow_day  2_user_remark_day  2_user_cart_day  2_sku_if_view  2_sku_if_buy  2_sku_if_follow  2_sku_if_remark  2_sku_if_cart  2_sku_action_amt  2_sku_view_amt  2_sku_buy_amt  2_sku_follow_amt  2_sku_remark_amt  2_sku_cart_amt  2_sku_action_day  2_sku_view_day  2_sku_buy_day  2_sku_follow_day  2_sku_remark_day  2_sku_cart_day  2_user_sku_if_view  2_user_sku_if_buy  2_user_sku_if_follow  2_user_sku_if_remark  2_user_sku_if_cart  2_user_sku_action_amt  2_user_sku_view_amt  2_user_sku_buy_amt  2_user_sku_follow_amt  2_user_sku_remark_amt  2_user_sku_cart_amt  2_user_sku_action_day  2_user_sku_view_day  2_user_sku_buy_day  2_user_sku_follow_day  2_user_sku_remark_day  2_user_sku_cart_day  2_user_sku_user_action_ratio  2_user_sku_user_view_ratio  2_user_sku_user_buy_ratio  2_user_sku_user_follow_ratio  2_user_sku_user_remark_ratio  2_user_sku_user_cart_ratio  3_user_if_view  3_user_if_buy  3_user_if_follow  3_user_if_remark  3_user_if_cart  3_user_action_amt  3_user_view_amt  3_user_buy_amt  3_user_follow_amt  3_user_remark_amt  3_user_cart_amt  3_user_action_day  3_user_view_day  3_user_buy_day  3_user_follow_day  3_user_remark_day  3_user_cart_day  3_sku_if_view  3_sku_if_buy  3_sku_if_follow  3_sku_if_remark  3_sku_if_cart  3_sku_action_amt  3_sku_view_amt  3_sku_buy_amt  3_sku_follow_amt  3_sku_remark_amt  3_sku_cart_amt  3_sku_action_day  3_sku_view_day  3_sku_buy_day  3_sku_follow_day  3_sku_remark_day  3_sku_cart_day  3_user_sku_if_view  3_user_sku_if_buy  3_user_sku_if_follow  3_user_sku_if_remark  3_user_sku_if_cart  3_user_sku_action_amt  3_user_sku_view_amt  3_user_sku_buy_amt  3_user_sku_follow_amt  3_user_sku_remark_amt  3_user_sku_cart_amt  3_user_sku_action_day  3_user_sku_view_day  3_user_sku_buy_day  3_user_sku_follow_day  3_user_sku_remark_day  3_user_sku_cart_day  3_user_sku_user_action_ratio  3_user_sku_user_view_ratio  3_user_sku_user_buy_ratio  3_user_sku_user_follow_ratio  3_user_sku_user_remark_ratio  3_user_sku_user_cart_ratio  7_user_if_view  7_user_if_buy  7_user_if_follow  7_user_if_remark  7_user_if_cart  7_user_action_amt  7_user_view_amt  7_user_buy_amt  7_user_follow_amt  7_user_remark_amt  7_user_cart_amt  7_user_action_day  7_user_view_day  7_user_buy_day  7_user_follow_day  7_user_remark_day  7_user_cart_day  7_sku_if_view  7_sku_if_buy  7_sku_if_follow  7_sku_if_remark  7_sku_if_cart  7_sku_action_amt  7_sku_view_amt  7_sku_buy_amt  7_sku_follow_amt  7_sku_remark_amt  7_sku_cart_amt  7_sku_action_day  7_sku_view_day  7_sku_buy_day  7_sku_follow_day  7_sku_remark_day  7_sku_cart_day  7_user_sku_if_view  7_user_sku_if_buy  7_user_sku_if_follow  7_user_sku_if_remark  7_user_sku_if_cart  7_user_sku_action_amt  7_user_sku_view_amt  7_user_sku_buy_amt  7_user_sku_follow_amt  7_user_sku_remark_amt  7_user_sku_cart_amt  7_user_sku_action_day  7_user_sku_view_day  7_user_sku_buy_day  7_user_sku_follow_day  7_user_sku_remark_day  7_user_sku_cart_day  7_user_sku_user_action_ratio  7_user_sku_user_view_ratio  7_user_sku_user_buy_ratio  7_user_sku_user_follow_ratio  7_user_sku_user_remark_ratio  7_user_sku_user_cart_ratio  14_user_if_view  14_user_if_buy  14_user_if_follow  14_user_if_remark  14_user_if_cart  14_user_action_amt  14_user_view_amt  14_user_buy_amt  14_user_follow_amt  14_user_remark_amt  14_user_cart_amt  14_user_action_day  14_user_view_day  14_user_buy_day  14_user_follow_day  14_user_remark_day  14_user_cart_day  14_sku_if_view  14_sku_if_buy  14_sku_if_follow  14_sku_if_remark  14_sku_if_cart  14_sku_action_amt  14_sku_view_amt  14_sku_buy_amt  14_sku_follow_amt  14_sku_remark_amt  14_sku_cart_amt  14_sku_action_day  14_sku_view_day  14_sku_buy_day  14_sku_follow_day  14_sku_remark_day  14_sku_cart_day  14_user_sku_if_view  14_user_sku_if_buy  14_user_sku_if_follow  14_user_sku_if_remark  14_user_sku_if_cart  14_user_sku_action_amt  14_user_sku_view_amt  14_user_sku_buy_amt  14_user_sku_follow_amt  14_user_sku_remark_amt  14_user_sku_cart_amt  14_user_sku_action_day  14_user_sku_view_day  14_user_sku_buy_day  14_user_sku_follow_day  14_user_sku_remark_day  14_user_sku_cart_day  14_user_sku_user_action_ratio  14_user_sku_user_view_ratio  14_user_sku_user_buy_ratio  14_user_sku_user_follow_ratio  14_user_sku_user_remark_ratio  14_user_sku_user_cart_ratio  age  sex  user_lv_cd  city_level  province  city  county  user_reg_day  user_reg_month  user_reg_cate  user_reg_year  user_action_amt  user_view_amt  user_buy_amt  user_follow_amt  user_remark_amt  user_cart_amt  user_action_day  user_view_day  user_buy_day  user_follow_day  user_remark_day  user_cart_day  user_view_ratio  user_buy_ratio  user_follow_ratio  user_remark_ratio  user_cart_ratio  user_buy/view  user_buy/follow  user_buy/remark  user_buy/cart  user_first_hour  user_last_hour  user_last_amt  brand  cate  product_reg_day  product_reg_month  product_reg_cate  product_reg_year  fans_num  vip_num  shop_cate  shop_score  shop_reg_month  shop_reg_cate  sku_action_amt  sku_view_amt  sku_buy_amt  sku_follow_amt  sku_remark_amt  sku_cart_amt  sku_action_day  sku_view_day  sku_buy_day  sku_follow_day  sku_remark_day  sku_cart_day  sku_view_ratio  sku_buy_ratio  sku_follow_ratio  sku_remark_ratio  sku_cart_ratio  sku_buy/view  sku_buy/follow  sku_buy/remark  sku_buy/cart  sku_rebuy_rate  sku_first_hour  sku_last_hour  sku_last_amt  user_sku_if_view  user_sku_if_buy  user_sku_if_follow  user_sku_if_remark  user_sku_if_cart  user_sku_action_amt  user_sku_view_amt  user_sku_buy_amt  user_sku_follow_amt  user_sku_remark_amt  user_sku_cart_amt  user_sku_action_day  user_sku_view_day  user_sku_buy_day  user_sku_follow_day  user_sku_remark_day  user_sku_cart_day  user_sku_view_ratio  user_sku_buy_ratio  user_sku_follow_ratio  user_sku_remark_ratio  user_sku_cart_ratio  user_sku_user_action_ratio  user_sku_user_view_ratio  user_sku_user_buy_ratio  user_sku_user_follow_ratio  user_sku_user_remark_ratio  user_sku_user_cart_ratio  user_sku_first_hour  user_sku_last_hour  user_sku_last_amt
0        2   45733      0               0              0                 0                 0               0                  0                0               0                  0                  0                0                  0                0               0                  0                  0                0              0             0                0                0              0                 0               0              0                 0                 0               0                 0               0              0                 0                 0               0                   0                  0                     0                     0                   0                      0                    0                   0                      0                      0                    0                      0                    0                   0                      0                      0                    0                             0                           0                          0                             0                             0                           0               1              0                 0                 0               0                  1                1               0                  0                  0                0                  1                1               0                  0                  0                0              1             0                0                0              0                 8               8              0                 0                 0               0                 1               1              0                 0                 0               0                   0                  0                     0                     0                   0                      0                    0                   0                      0                      0                    0                      0                    0                   0                      0                      0                    0                             0                           0                          0                             0                             0                           0               1              0                 0                 1               0                  2                1               0                  0                  1                0                  2                1               0                  0                  1                0              1             0                0                1              0                18              17              0                 0                 1               0                 2               2              0                 0                 1               0                   0                  0                     0                     1                   0                      1                    0                   0                      0                      1                    0                      1                    0                   0                      0                      1                    0                            50                           0                          0                             0                           100                           0               1              0                 0                 1               0                  7                4               0                  0                  3                0                  5                3               0                  0                  2                0              1             0                0                1              0                47              45              0                 0                 2               0                 4               4              0                 0                 2               0                   0                  0                     0                     1                   0                      1                    0                   0                      0                      1                    0                      1                    0                   0                      0                      1                    0                            14                           0                          0                             0                            33                           0                1               0                  0                  1                0                  44                41                0                   0                   3                 0                   9                 7                0                   0                   2                 0               1              0                 1                 1               0                115              111               0                  1                  3                0                 11               11               0                  1                  3                0                    1                   0                      0                      1                    0                       3                     2                    0                       0                       1                     0                       3                     2                    0                       0                       1                     0                              6                            4                           0                              0                             33                            0    4    1           1           3        20   119     187          1091              36              5              2              110            107             0                0                3              0               20             18             0                0                2              0               97               0                  0                  2                0              0                0                0              0               14             683              2   3889    27               80                  2                 1                 0         0        0         -1           0              -1             -1             156           152            0               1               3             0              18            18            0               1               3             0              97              0                 0                 1               0             0               0               0             0               0               2            489             5                 1                0                   0                   1                 0                    4                  3                 0                    0                    1                  0                    4                  3                 0                    0                    1                  0                   75                   0                      0                     25                    0                           3                         2                        0                           0                          33                         0                   37                 397                  1
1        2  338588      0               0              0                 0                 0               0                  0                0               0                  0                  0                0                  0                0               0                  0                  0                0              0             0                0                0              0                 0               0              0                 0                 0               0                 0               0              0                 0                 0               0                   0                  0                     0                     0                   0                      0                    0                   0                      0                      0                    0                      0                    0                   0                      0                      0                    0                             0                           0                          0                             0                             0                           0               1              0                 0                 0               0                  1                1               0                  0                  0                0                  1                1               0                  0                  0                0              1             0                0                1              0                14              13              0                 0                 1               0                 1               1              0                 0                 1               0                   1                  0                     0                     0                   0                      1                    1                   0                      0                      0                    0                      1                    1                   0                      0                      0                    0                           100                         100                          0                             0                             0                           0               1              0                 0                 1               0                  2                1               0                  0                  1                0                  2                1               0                  0                  1                0              1             0                0                1              0                26              25              0                 0                 1               0                 2               2              0                 0                 1               0                   1                  0                     0                     0                   0                      1                    1                   0                      0                      0                    0                      1                    1                   0                      0                      0                    0                            50                         100                          0                             0                             0                           0               1              0                 0                 1               0                  7                4               0                  0                  3                0                  5                3               0                  0                  2                0              1             0                1                1              0                58              55              0                 1                 2               0                 4               4              0                 1                 2               0                   1                  0                     0                     0                   0                      1                    1                   0                      0                      0                    0                      1                    1                   0                      0                      0                    0                            14                          25                          0                             0                             0                           0                1               0                  0                  1                0                  44                41                0                   0                   3                 0                   9                 7                0                   0                   2                 0               1              0                 1                 1               0                140              135               0                  1                  4                0                 11               11               0                  1                  4                0                    1                   0                      0                      0                    0                       2                     2                    0                       0                       0                     0                       2                     2                    0                       0                       0                     0                              4                            4                           0                              0                              0                            0    4    1           1           3        20   119     187          1091              36              5              2              110            107             0                0                3              0               20             18             0                0                2              0               97               0                  0                  2                0              0                0                0              0               14             683              2   3889    55              347                 11                 3                 0         0        0         -1           0              -1             -1             351           341            0               6               4             0              26            26            0               6               4             0              97              0                 1                 1               0             0               0               0             0               0               0            687             3                 1                0                   0                   0                 0                    2                  2                 0                    0                    0                  0                    2                  2                 0                    0                    0                  0                  100                   0                      0                      0                    0                           1                         1                        0                           0                           0                         0                   14                 206                  1
2        4  262872      0               0              0                 0                 0               0                  0                0               0                  0                  0                0                  0                0               0                  0                  0                0              0             0                0                0              0                 0               0              0                 0                 0               0                 0               0              0                 0                 0               0                   0                  0                     0                     0                   0                      0                    0                   0                      0                      0                    0                      0                    0                   0                      0                      0                    0                             0                           0                          0                             0                             0                           0               1              0                 0                 0               0                  3                3               0                  0                  0                0                  1                1               0                  0                  0                0              1             0                1                1              0               367             355              0                 1                11               0                 1               1              0                 1                 1               0                   1                  0                     0                     0                   0                      1                    1                   0                      0                      0                    0                      1                    1                   0                      0                      0                    0                            33                          33                          0                             0                             0                           0               1              0                 0                 0               0                  3                3               0                  0                  0                0                  1                1               0                  0                  0                0              1             0                1                1              0               585             562              0                 4                19               0                 2               2              0                 2                 2               0                   1                  0                     0                     0                   0                      1                    1                   0                      0                      0                    0                      1                    1                   0                      0                      0                    0                            33                          33                          0                             0                             0                           0               1              0                 0                 0               0                  3                3               0                  0                  0                0                  1                1               0                  0                  0                0              1             0                1                1              0               905             849              0                 7                49               0                 6               4              0                 5                 6               0                   1                  0                     0                     0                   0                      1                    1                   0                      0                      0                    0                      1                    1                   0                      0                      0                    0                            33                          33                          0                             0                             0                           0                1               1                  1                  0                0                  16                14                1                   1                   0                 0                   5                 5                1                   1                   0                 0               1              0                 1                 1               0               2034             1920               0                 12                102                0                 13               11               0                  9                 13                0                    1                   0                      0                      0                    0                       1                     1                    0                       0                       0                     0                       1                     1                    0                       0                       0                     0                              6                            7                           0                              0                              0                            0    6    1           7           4        20   120     741          2207              73              6              6               66             61             1                1                3              0               15             15             1                1                1              0               92               1                  1                  4                0              1              100               33           -100                1             617             14   9985    73             1405                 46                 5                 3         0        0         -1           0              -1             -1            5457          5208            0              27             222             0              29            27            0              19              29             0              95              0                 0                 4               0             0               0               0             0               0               0            695           221                 1                0                   0                   0                 0                    2                  2                 0                    0                    0                  0                    2                  2                 0                    0                    0                  0                  100                   0                      0                      0                    0                           3                         3                        0                           0                           0                         0                   12                 315                  1
3        4  295865      0               0              0                 0                 0               0                  0                0               0                  0                  0                0                  0                0               0                  0                  0                0              0             0                0                0              0                 0               0              0                 0                 0               0                 0               0              0                 0                 0               0                   0                  0                     0                     0                   0                      0                    0                   0                      0                      0                    0                      0                    0                   0                      0                      0                    0                             0                           0                          0                             0                             0                           0               1              0                 0                 0               0                  3                3               0                  0                  0                0                  1                1               0                  0                  0                0              1             0                1                1              0               912             904              0                 7                 1               0                 1               1              0                 1                 1               0                   1                  0                     0                     0                   0                      1                    1                   0                      0                      0                    0                      1                    1                   0                      0                      0                    0                            33                          33                          0                             0                             0                           0               1              0                 0                 0               0                  3                3               0                  0                  0                0                  1                1               0                  0                  0                0              1             0                1                1              0               990             980              0                 9                 1               0                 2               2              0                 2                 1               0                   1                  0                     0                     0                   0                      1                    1                   0                      0                      0                    0                      1                    1                   0                      0                      0                    0                            33                          33                          0                             0                             0                           0               1              0                 0                 0               0                  3                3               0                  0                  0                0                  1                1               0                  0                  0                0              1             0                1                1              0              1094            1079              0                10                 5               0                 6               4              0                 3                 4               0                   1                  0                     0                     0                   0                      1                    1                   0                      0                      0                    0                      1                    1                   0                      0                      0                    0                            33                          33                          0                             0                             0                           0                1               1                  1                  0                0                  16                14                1                   1                   0                 0                   5                 5                1                   1                   0                 0               1              0                 1                 1               0               1749             1720               0                 18                 11                0                 13               11               0                  9                  7                0                    1                   0                      0                      0                    0                       1                     1                    0                       0                       0                     0                       1                     1                    0                       0                       0                     0                              6                            7                           0                              0                              0                            0    6    1           7           4        20   120     741          2207              73              6              6               66             61             1                1                3              0               15             15             1                1                1              0               92               1                  1                  4                0              1              100               33           -100                1             617             14  11114    27             1116                 37                 5                 3         0        0         -1           0              -1             -1            3302          3224            0              46              32             0              29            27            0              23              19             0              97              0                 1                 0               0             0               0               0             0               0               0            695           103                 1                0                   0                   0                 0                    1                  1                 0                    0                    0                  0                    1                  1                 0                    0                    0                  0                  100                   0                      0                      0                    0                           1                         1                        0                           0                           0                         0                   11                  11                  1
4        4  337682      0               0              0                 0                 0               0                  0                0               0                  0                  0                0                  0                0               0                  0                  0                0              0             0                0                0              0                 0               0              0                 0                 0               0                 0               0              0                 0                 0               0                   0                  0                     0                     0                   0                      0                    0                   0                      0                      0                    0                      0                    0                   0                      0                      0                    0                             0                           0                          0                             0                             0                           0               1              0                 0                 0               0                  3                3               0                  0                  0                0                  1                1               0                  0                  0                0              1             1                1                0              0              1577            1247            309                21                 0               0                 1               1              1                 1                 0               0                   1                  0                     0                     0                   0                      1                    1                   0                      0                      0                    0                      1                    1                   0                      0                      0                    0                            33                          33                          0                             0                             0                           0               1              0                 0                 0               0                  3                3               0                  0                  0                0                  1                1               0                  0                  0                0              1             1                1                1              0              1595            1262            310                21                 2               0                 2               2              2                 1                 1               0                   1                  0                     0                     0                   0                      1                    1                   0                      0                      0                    0                      1                    1                   0                      0                      0                    0                            33                          33                          0                             0                             0                           0               1              0                 0                 0               0                  3                3               0                  0                  0                0                  1                1               0                  0                  0                0              1             1                1                1              0              1618            1271            317                24                 6               0                 5               4              3                 2                 2               0                   1                  0                     0                     0                   0                      1                    1                   0                      0                      0                    0                      1                    1                   0                      0                      0                    0                            33                          33                          0                             0                             0                           0                1               1                  1                  0                0                  16                14                1                   1                   0                 0                   5                 5                1                   1                   0                 0               1              1                 1                 1               0               1638             1290             318                 24                  6                0                 10                8               4                  2                  2                0                    1                   0                      0                      0                    0                       1                     1                    0                       0                       0                     0                       1                     1                    0                       0                       0                     0                              6                            7                           0                              0                              0                            0    6    1           7           4        20   120     741          2207              73              6              6               66             61             1                1                3              0               15             15             1                1                1              0               92               1                  1                  4                0              1              100               33           -100                1             617             14   7985    48               96                  3                 1                 0      2578    40796         35           9               4              2            1638          1290          318              24               6             0              10             8            4               2               2             0              78             19                 1                 0               0            24            1325            5300        -31800               0               0            296             1                 1                0                   0                   0                 0                    1                  1                 0                    0                    0                  0                    1                  1                 0                    0                    0                  0                  100                   0                      0                      0                    0                           1                         1                        0                           0                           0                         0                    1                   1                  1
tail
        user_id  sku_id  label  1_user_if_view  1_user_if_buy  1_user_if_follow  1_user_if_remark  1_user_if_cart  1_user_action_amt  1_user_view_amt  1_user_buy_amt  1_user_follow_amt  1_user_remark_amt  1_user_cart_amt  1_user_action_day  1_user_view_day  1_user_buy_day  1_user_follow_day  1_user_remark_day  1_user_cart_day  1_sku_if_view  1_sku_if_buy  1_sku_if_follow  1_sku_if_remark  1_sku_if_cart  1_sku_action_amt  1_sku_view_amt  1_sku_buy_amt  1_sku_follow_amt  1_sku_remark_amt  1_sku_cart_amt  1_sku_action_day  1_sku_view_day  1_sku_buy_day  1_sku_follow_day  1_sku_remark_day  1_sku_cart_day  1_user_sku_if_view  1_user_sku_if_buy  1_user_sku_if_follow  1_user_sku_if_remark  1_user_sku_if_cart  1_user_sku_action_amt  1_user_sku_view_amt  1_user_sku_buy_amt  1_user_sku_follow_amt  1_user_sku_remark_amt  1_user_sku_cart_amt  1_user_sku_action_day  1_user_sku_view_day  1_user_sku_buy_day  1_user_sku_follow_day  1_user_sku_remark_day  1_user_sku_cart_day  1_user_sku_user_action_ratio  1_user_sku_user_view_ratio  1_user_sku_user_buy_ratio  1_user_sku_user_follow_ratio  1_user_sku_user_remark_ratio  1_user_sku_user_cart_ratio  2_user_if_view  2_user_if_buy  2_user_if_follow  2_user_if_remark  2_user_if_cart  2_user_action_amt  2_user_view_amt  2_user_buy_amt  2_user_follow_amt  2_user_remark_amt  2_user_cart_amt  2_user_action_day  2_user_view_day  2_user_buy_day  2_user_follow_day  2_user_remark_day  2_user_cart_day  2_sku_if_view  2_sku_if_buy  2_sku_if_follow  2_sku_if_remark  2_sku_if_cart  2_sku_action_amt  2_sku_view_amt  2_sku_buy_amt  2_sku_follow_amt  2_sku_remark_amt  2_sku_cart_amt  2_sku_action_day  2_sku_view_day  2_sku_buy_day  2_sku_follow_day  2_sku_remark_day  2_sku_cart_day  2_user_sku_if_view  2_user_sku_if_buy  2_user_sku_if_follow  2_user_sku_if_remark  2_user_sku_if_cart  2_user_sku_action_amt  2_user_sku_view_amt  2_user_sku_buy_amt  2_user_sku_follow_amt  2_user_sku_remark_amt  2_user_sku_cart_amt  2_user_sku_action_day  2_user_sku_view_day  2_user_sku_buy_day  2_user_sku_follow_day  2_user_sku_remark_day  2_user_sku_cart_day  2_user_sku_user_action_ratio  2_user_sku_user_view_ratio  2_user_sku_user_buy_ratio  2_user_sku_user_follow_ratio  2_user_sku_user_remark_ratio  2_user_sku_user_cart_ratio  3_user_if_view  3_user_if_buy  3_user_if_follow  3_user_if_remark  3_user_if_cart  3_user_action_amt  3_user_view_amt  3_user_buy_amt  3_user_follow_amt  3_user_remark_amt  3_user_cart_amt  3_user_action_day  3_user_view_day  3_user_buy_day  3_user_follow_day  3_user_remark_day  3_user_cart_day  3_sku_if_view  3_sku_if_buy  3_sku_if_follow  3_sku_if_remark  3_sku_if_cart  3_sku_action_amt  3_sku_view_amt  3_sku_buy_amt  3_sku_follow_amt  3_sku_remark_amt  3_sku_cart_amt  3_sku_action_day  3_sku_view_day  3_sku_buy_day  3_sku_follow_day  3_sku_remark_day  3_sku_cart_day  3_user_sku_if_view  3_user_sku_if_buy  3_user_sku_if_follow  3_user_sku_if_remark  3_user_sku_if_cart  3_user_sku_action_amt  3_user_sku_view_amt  3_user_sku_buy_amt  3_user_sku_follow_amt  3_user_sku_remark_amt  3_user_sku_cart_amt  3_user_sku_action_day  3_user_sku_view_day  3_user_sku_buy_day  3_user_sku_follow_day  3_user_sku_remark_day  3_user_sku_cart_day  3_user_sku_user_action_ratio  3_user_sku_user_view_ratio  3_user_sku_user_buy_ratio  3_user_sku_user_follow_ratio  3_user_sku_user_remark_ratio  3_user_sku_user_cart_ratio  7_user_if_view  7_user_if_buy  7_user_if_follow  7_user_if_remark  7_user_if_cart  7_user_action_amt  7_user_view_amt  7_user_buy_amt  7_user_follow_amt  7_user_remark_amt  7_user_cart_amt  7_user_action_day  7_user_view_day  7_user_buy_day  7_user_follow_day  7_user_remark_day  7_user_cart_day  7_sku_if_view  7_sku_if_buy  7_sku_if_follow  7_sku_if_remark  7_sku_if_cart  7_sku_action_amt  7_sku_view_amt  7_sku_buy_amt  7_sku_follow_amt  7_sku_remark_amt  7_sku_cart_amt  7_sku_action_day  7_sku_view_day  7_sku_buy_day  7_sku_follow_day  7_sku_remark_day  7_sku_cart_day  7_user_sku_if_view  7_user_sku_if_buy  7_user_sku_if_follow  7_user_sku_if_remark  7_user_sku_if_cart  7_user_sku_action_amt  7_user_sku_view_amt  7_user_sku_buy_amt  7_user_sku_follow_amt  7_user_sku_remark_amt  7_user_sku_cart_amt  7_user_sku_action_day  7_user_sku_view_day  7_user_sku_buy_day  7_user_sku_follow_day  7_user_sku_remark_day  7_user_sku_cart_day  7_user_sku_user_action_ratio  7_user_sku_user_view_ratio  7_user_sku_user_buy_ratio  7_user_sku_user_follow_ratio  7_user_sku_user_remark_ratio  7_user_sku_user_cart_ratio  14_user_if_view  14_user_if_buy  14_user_if_follow  14_user_if_remark  14_user_if_cart  14_user_action_amt  14_user_view_amt  14_user_buy_amt  14_user_follow_amt  14_user_remark_amt  14_user_cart_amt  14_user_action_day  14_user_view_day  14_user_buy_day  14_user_follow_day  14_user_remark_day  14_user_cart_day  14_sku_if_view  14_sku_if_buy  14_sku_if_follow  14_sku_if_remark  14_sku_if_cart  14_sku_action_amt  14_sku_view_amt  14_sku_buy_amt  14_sku_follow_amt  14_sku_remark_amt  14_sku_cart_amt  14_sku_action_day  14_sku_view_day  14_sku_buy_day  14_sku_follow_day  14_sku_remark_day  14_sku_cart_day  14_user_sku_if_view  14_user_sku_if_buy  14_user_sku_if_follow  14_user_sku_if_remark  14_user_sku_if_cart  14_user_sku_action_amt  14_user_sku_view_amt  14_user_sku_buy_amt  14_user_sku_follow_amt  14_user_sku_remark_amt  14_user_sku_cart_amt  14_user_sku_action_day  14_user_sku_view_day  14_user_sku_buy_day  14_user_sku_follow_day  14_user_sku_remark_day  14_user_sku_cart_day  14_user_sku_user_action_ratio  14_user_sku_user_view_ratio  14_user_sku_user_buy_ratio  14_user_sku_user_follow_ratio  14_user_sku_user_remark_ratio  14_user_sku_user_cart_ratio  age  sex  user_lv_cd  city_level  province  city  county  user_reg_day  user_reg_month  user_reg_cate  user_reg_year  user_action_amt  user_view_amt  user_buy_amt  user_follow_amt  user_remark_amt  user_cart_amt  user_action_day  user_view_day  user_buy_day  user_follow_day  user_remark_day  user_cart_day  user_view_ratio  user_buy_ratio  user_follow_ratio  user_remark_ratio  user_cart_ratio  user_buy/view  user_buy/follow  user_buy/remark  user_buy/cart  user_first_hour  user_last_hour  user_last_amt  brand  cate  product_reg_day  product_reg_month  product_reg_cate  product_reg_year  fans_num  vip_num  shop_cate  shop_score  shop_reg_month  shop_reg_cate  sku_action_amt  sku_view_amt  sku_buy_amt  sku_follow_amt  sku_remark_amt  sku_cart_amt  sku_action_day  sku_view_day  sku_buy_day  sku_follow_day  sku_remark_day  sku_cart_day  sku_view_ratio  sku_buy_ratio  sku_follow_ratio  sku_remark_ratio  sku_cart_ratio  sku_buy/view  sku_buy/follow  sku_buy/remark  sku_buy/cart  sku_rebuy_rate  sku_first_hour  sku_last_hour  sku_last_amt  user_sku_if_view  user_sku_if_buy  user_sku_if_follow  user_sku_if_remark  user_sku_if_cart  user_sku_action_amt  user_sku_view_amt  user_sku_buy_amt  user_sku_follow_amt  user_sku_remark_amt  user_sku_cart_amt  user_sku_action_day  user_sku_view_day  user_sku_buy_day  user_sku_follow_day  user_sku_remark_day  user_sku_cart_day  user_sku_view_ratio  user_sku_buy_ratio  user_sku_follow_ratio  user_sku_remark_ratio  user_sku_cart_ratio  user_sku_user_action_ratio  user_sku_user_view_ratio  user_sku_user_buy_ratio  user_sku_user_follow_ratio  user_sku_user_remark_ratio  user_sku_user_cart_ratio  user_sku_first_hour  user_sku_last_hour  user_sku_last_amt
732224  1608696  121463      0               0              0                 0                 0               0                  0                0               0                  0                  0                0                  0                0               0                  0                  0                0              0             0                0                0              0                 0               0              0                 0                 0               0                 0               0              0                 0                 0               0                   0                  0                     0                     0                   0                      0                    0                   0                      0                      0                    0                      0                    0                   0                      0                      0                    0                             0                           0                          0                             0                             0                           0               1              0                 0                 0               0                  5                5               0                  0                  0                0                  1                1               0                  0                  0                0              1             0                0                0              0                 4               4              0                 0                 0               0                 1               1              0                 0                 0               0                   1                  0                     0                     0                   0                      2                    2                   0                      0                      0                    0                      1                    1                   0                      0                      0                    0                            40                          40                          0                             0                             0                           0               1              0                 0                 0               0                  5                5               0                  0                  0                0                  1                1               0                  0                  0                0              1             0                0                0              0                 4               4              0                 0                 0               0                 1               1              0                 0                 0               0                   1                  0                     0                     0                   0                      2                    2                   0                      0                      0                    0                      1                    1                   0                      0                      0                    0                            40                          40                          0                             0                             0                           0               1              0                 0                 0               0                  6                6               0                  0                  0                0                  2                2               0                  0                  0                0              1             0                0                0              0                 7               7              0                 0                 0               0                 3               3              0                 0                 0               0                   1                  0                     0                     0                   0                      3                    3                   0                      0                      0                    0                      2                    2                   0                      0                      0                    0                            50                          50                          0                             0                             0                           0                1               0                  0                  0                0                   6                 6                0                   0                   0                 0                   2                 2                0                   0                   0                 0               1              1                 0                 0               0                 26               25               1                  0                  0                0                  9                9               1                  0                  0                0                    1                   0                      0                      0                    0                       3                     3                    0                       0                       0                     0                       2                     2                    0                       0                       0                     0                             50                           50                           0                              0                              0                            0    6    1           5           3        11   348    2316          2331              77              6              6               16             14             1                1                0              0                6              6             1                1                0              0               87               6                  6                  0                0              7              100             -100           -100               17             684              2   9692    19              487                 16                 4                 1    174285   264951         47           9              46              5              51            48            2               1               0             0              21            21            2               1               0             0              94              3                 1                 0               0             4             200            -200          -200               0               1            677             1                 1                1                   1                   0                 0                    7                  5                 1                    1                    0                  0                    4                  4                 1                    1                    0                  0                   71                  14                     14                      0                    0                          43                        35                      100                         100                           0                         0                   17                 388                  2
732225  1608696   74146      0               0              0                 0                 0               0                  0                0               0                  0                  0                0                  0                0               0                  0                  0                0              0             0                0                0              0                 0               0              0                 0                 0               0                 0               0              0                 0                 0               0                   0                  0                     0                     0                   0                      0                    0                   0                      0                      0                    0                      0                    0                   0                      0                      0                    0                             0                           0                          0                             0                             0                           0               1              0                 0                 0               0                  5                5               0                  0                  0                0                  1                1               0                  0                  0                0              1             1                1                1              0                22              19              1                 1                 1               0                 1               1              1                 1                 1               0                   1                  0                     0                     0                   0                      1                    1                   0                      0                      0                    0                      1                    1                   0                      0                      0                    0                            20                          20                          0                             0                             0                           0               1              0                 0                 0               0                  5                5               0                  0                  0                0                  1                1               0                  0                  0                0              1             1                1                1              0                43              37              2                 2                 2               0                 2               2              2                 2                 2               0                   1                  0                     0                     0                   0                      1                    1                   0                      0                      0                    0                      1                    1                   0                      0                      0                    0                            20                          20                          0                             0                             0                           0               1              0                 0                 0               0                  6                6               0                  0                  0                0                  2                2               0                  0                  0                0              1             1                1                1              0                97              79              6                 7                 5               0                 6               4              4                 5                 4               0                   1                  0                     0                     0                   0                      1                    1                   0                      0                      0                    0                      1                    1                   0                      0                      0                    0                            16                          16                          0                             0                             0                           0                1               0                  0                  0                0                   6                 6                0                   0                   0                 0                   2                 2                0                   0                   0                 0               1              1                 1                 1               0                303              267              14                  9                 13                0                 13               11               7                  7                  9                0                    1                   0                      0                      0                    0                       1                     1                    0                       0                       0                     0                       1                     1                    0                       0                       0                     0                             16                           16                           0                              0                              0                            0    6    1           5           3        11   348    2316          2331              77              6              6               16             14             1                1                0              0                6              6             1                1                0              0               87               6                  6                  0                0              7              100             -100           -100               17             684              2   9692    19              431                 14                 4                 1    113149    54075         47           9              18              4             802           720           38              20              24             0              29            27           19              16              18             0              89              4                 2                 2               0             5             190             158         -3800               0               0            695            23                 1                0                   0                   0                 0                    1                  1                 0                    0                    0                  0                    1                  1                 0                    0                    0                  0                  100                   0                      0                      0                    0                           6                         7                        0                           0                           0                         0                   17                  17                  1
732226  1608696  322243      0               0              0                 0                 0               0                  0                0               0                  0                  0                0                  0                0               0                  0                  0                0              0             0                0                0              0                 0               0              0                 0                 0               0                 0               0              0                 0                 0               0                   0                  0                     0                     0                   0                      0                    0                   0                      0                      0                    0                      0                    0                   0                      0                      0                    0                             0                           0                          0                             0                             0                           0               1              0                 0                 0               0                  5                5               0                  0                  0                0                  1                1               0                  0                  0                0              1             1                0                1              0                35              33              1                 0                 1               0                 1               1              1                 0                 1               0                   1                  0                     0                     0                   0                      1                    1                   0                      0                      0                    0                      1                    1                   0                      0                      0                    0                            20                          20                          0                             0                             0                           0               1              0                 0                 0               0                  5                5               0                  0                  0                0                  1                1               0                  0                  0                0              1             1                0                1              0                81              76              4                 0                 1               0                 2               2              2                 0                 1               0                   1                  0                     0                     0                   0                      1                    1                   0                      0                      0                    0                      1                    1                   0                      0                      0                    0                            20                          20                          0                             0                             0                           0               1              0                 0                 0               0                  6                6               0                  0                  0                0                  2                2               0                  0                  0                0              1             1                1                1              0               175             153             15                 2                 5               0                 6               5              4                 2                 4               0                   1                  0                     0                     0                   0                      1                    1                   0                      0                      0                    0                      1                    1                   0                      0                      0                    0                            16                          16                          0                             0                             0                           0                1               0                  0                  0                0                   6                 6                0                   0                   0                 0                   2                 2                0                   0                   0                 0               1              1                 1                 1               0                578              526              35                  7                 10                0                 13               12               7                  5                  7                0                    1                   0                      0                      0                    0                       1                     1                    0                       0                       0                     0                       1                     1                    0                       0                       0                     0                             16                           16                           0                              0                              0                            0    6    1           5           3        11   348    2316          2331              77              6              6               16             14             1                1                0              0                6              6             1                1                0              0               87               6                  6                  0                0              7              100             -100           -100               17             684              2   9692    19              334                 11                 3                 0    174285   264951         47           9              46              5            1272          1176           68              12              16             0              29            28           21              10              11             0              92              5                 0                 1               0             5             566             425         -6800               3               0            690            53                 1                0                   0                   0                 0                    2                  2                 0                    0                    0                  0                    2                  2                 0                    0                    0                  0                  100                   0                      0                      0                    0                          12                        14                        0                           0                           0                         0                   17                 388                  1
732227  1608704  320471      0               0              0                 0                 0               0                  0                0               0                  0                  0                0                  0                0               0                  0                  0                0              0             0                0                0              0                 0               0              0                 0                 0               0                 0               0              0                 0                 0               0                   0                  0                     0                     0                   0                      0                    0                   0                      0                      0                    0                      0                    0                   0                      0                      0                    0                             0                           0                          0                             0                             0                           0               1              1                 0                 0               0                  3                2               1                  0                  0                0                  1                1               1                  0                  0                0              1             1                0                1              0               128              87             34                 0                 7               0                 1               1              1                 0                 1               0                   1                  1                     0                     0                   0                      2                    1                   1                      0                      0                    0                      1                    1                   1                      0                      0                    0                            66                          50                        100                             0                             0                           0               1              1                 0                 0               0                  3                2               1                  0                  0                0                  1                1               1                  0                  0                0              1             1                1                1              0               228             153             60                 1                14               0                 2               2              2                 1                 2               0                   1                  1                     0                     0                   0                      2                    1                   1                      0                      0                    0                      1                    1                   1                      0                      0                    0                            66                          50                        100                             0                             0                           0               1              1                 0                 0               0                  5                4               1                  0                  0                0                  2                2               1                  0                  0                0              1             1                1                1              0               524             328            164                 2                30               0                 6               5              6                 2                 6               0                   1                  1                     0                     0                   0                      2                    1                   1                      0                      0                    0                      1                    1                   1                      0                      0                    0                            40                          25                        100                             0                             0                           0                1               1                  0                  0                0                   5                 4                1                   0                   0                 0                   2                 2                1                   0                   0                 0               1              1                 1                 1               0               1382              982             317                 10                 73                0                 13               12              13                  7                 13                0                    1                   1                      0                      0                    0                       2                     1                    1                       0                       0                     0                       1                     1                    1                       0                       0                     0                             40                           25                         100                              0                              0                            0    6    0           7           3        20   119     187          2557              85              6              7                8              7             1                0                0              0                4              4             1                0                0              0               87              12                  0                  0                0             14             -100             -100           -100                1             531              2   5849     7              735                 24                 4                 2     74826   163282         12           9              24              4            3235          2429          602              24             180             0              29            28           29              18              29             0              75             18                 0                 5               0            24            2508             334        -60200               1               0            695           102                 1                1                   0                   0                 0                    3                  2                 1                    0                    0                  0                    2                  2                 1                    0                    0                  0                   66                  33                      0                      0                    0                          37                        28                      100                           0                           0                         0                    1                 531                  1
732228  1608704   31993      0               0              0                 0                 0               0                  0                0               0                  0                  0                0                  0                0               0                  0                  0                0              0             0                0                0              0                 0               0              0                 0                 0               0                 0               0              0                 0                 0               0                   0                  0                     0                     0                   0                      0                    0                   0                      0                      0                    0                      0                    0                   0                      0                      0                    0                             0                           0                          0                             0                             0                           0               1              1                 0                 0               0                  3                2               1                  0                  0                0                  1                1               1                  0                  0                0              1             0                0                0              0                16              16              0                 0                 0               0                 1               1              0                 0                 0               0                   1                  0                     0                     0                   0                      1                    1                   0                      0                      0                    0                      1                    1                   0                      0                      0                    0                            33                          50                          0                             0                             0                           0               1              1                 0                 0               0                  3                2               1                  0                  0                0                  1                1               1                  0                  0                0              1             1                0                1              0                44              42              1                 0                 1               0                 2               2              1                 0                 1               0                   1                  0                     0                     0                   0                      1                    1                   0                      0                      0                    0                      1                    1                   0                      0                      0                    0                            33                          50                          0                             0                             0                           0               1              1                 0                 0               0                  5                4               1                  0                  0                0                  2                2               1                  0                  0                0              1             1                0                1              0               118              87             27                 0                 4               0                 6               4              4                 0                 3               0                   1                  0                     0                     0                   0                      1                    1                   0                      0                      0                    0                      1                    1                   0                      0                      0                    0                            20                          25                          0                             0                             0                           0                1               1                  0                  0                0                   5                 4                1                   0                   0                 0                   2                 2                1                   0                   0                 0               1              1                 0                 1               0                276              223              45                  0                  8                0                 13               11               9                  0                  7                0                    1                   0                      0                      0                    0                       1                     1                    0                       0                       0                     0                       1                     1                    0                       0                       0                     0                             20                           25                           0                              0                              0                            0    6    0           7           3        20   119     187          2557              85              6              7                8              7             1                0                0              0                4              4             1                0                0              0               87              12                  0                  0                0             14             -100             -100           -100                1             531              2   5849     7              173                  5                 2                 0    424303    19445         12           9               5              2             469           380           69               2              18             0              29            27           20               2              14             0              81             14                 0                 3               0            18            3450             383         -6900               2               0            695            14                 1                0                   0                   0                 0                    1                  1                 0                    0                    0                  0                    1                  1                 0                    0                    0                  0                  100                   0                      0                      0                    0                          12                        14                        0                           0                           0                         0                    1                   1                  1
2019-05-25 19:07:46.695057
>> 完成生成特征(732229, 391)
2019-05-25 19:07:46.696562
>> 开始划分X,y
<< 完成划分X,y
2019-05-25 19:07:56.057327
>> 开始设置参数
<< 完成设置参数
2019-05-25 19:07:56.057327
>> 开始训练模型
[0]	eval-logloss:0.599079	train-logloss:0.599268
Multiple eval metrics have been passed: 'train-logloss' will be used for early stopping.

Will train until train-logloss hasn't improved in 50 rounds.
[1]	eval-logloss:0.522805	train-logloss:0.52305
[2]	eval-logloss:0.459139	train-logloss:0.459403
[3]	eval-logloss:0.40518	train-logloss:0.405354
[4]	eval-logloss:0.359053	train-logloss:0.359102
[5]	eval-logloss:0.320001	train-logloss:0.319856
[6]	eval-logloss:0.28568	train-logloss:0.285364
[7]	eval-logloss:0.255768	train-logloss:0.255218
[8]	eval-logloss:0.229817	train-logloss:0.229003
[9]	eval-logloss:0.2071	train-logloss:0.205997
[10]	eval-logloss:0.186848	train-logloss:0.18544
[11]	eval-logloss:0.169371	train-logloss:0.167637
[12]	eval-logloss:0.153689	train-logloss:0.151631
[13]	eval-logloss:0.139787	train-logloss:0.137387
[14]	eval-logloss:0.127492	train-logloss:0.124734
[15]	eval-logloss:0.116644	train-logloss:0.113518
[16]	eval-logloss:0.106737	train-logloss:0.103229
[17]	eval-logloss:0.098144	train-logloss:0.094245
[18]	eval-logloss:0.090446	train-logloss:0.086152
[19]	eval-logloss:0.083604	train-logloss:0.078882
[20]	eval-logloss:0.077493	train-logloss:0.072356
[21]	eval-logloss:0.072076	train-logloss:0.066416
[22]	eval-logloss:0.067234	train-logloss:0.061063
[23]	eval-logloss:0.062894	train-logloss:0.056189
[24]	eval-logloss:0.059029	train-logloss:0.051793
[25]	eval-logloss:0.05563	train-logloss:0.047847
[26]	eval-logloss:0.052666	train-logloss:0.044337
[27]	eval-logloss:0.049987	train-logloss:0.041144
[28]	eval-logloss:0.047586	train-logloss:0.038228
[29]	eval-logloss:0.045496	train-logloss:0.035589
[30]	eval-logloss:0.043622	train-logloss:0.033234
[31]	eval-logloss:0.042071	train-logloss:0.031161
[32]	eval-logloss:0.040677	train-logloss:0.029281
[33]	eval-logloss:0.039456	train-logloss:0.027495
[34]	eval-logloss:0.038377	train-logloss:0.025968
[35]	eval-logloss:0.037549	train-logloss:0.024515
[36]	eval-logloss:0.036731	train-logloss:0.023265
[37]	eval-logloss:0.036134	train-logloss:0.022101
[38]	eval-logloss:0.035568	train-logloss:0.02109
[39]	eval-logloss:0.035135	train-logloss:0.020141
[40]	eval-logloss:0.034839	train-logloss:0.019291
[41]	eval-logloss:0.034612	train-logloss:0.018481
[42]	eval-logloss:0.034416	train-logloss:0.017779
[43]	eval-logloss:0.034286	train-logloss:0.01715
[44]	eval-logloss:0.034252	train-logloss:0.016515
[45]	eval-logloss:0.034278	train-logloss:0.015969
[46]	eval-logloss:0.034315	train-logloss:0.015479
[47]	eval-logloss:0.03441	train-logloss:0.015027
[48]	eval-logloss:0.034606	train-logloss:0.014612
[49]	eval-logloss:0.034735	train-logloss:0.01427
[50]	eval-logloss:0.03495	train-logloss:0.013925
[51]	eval-logloss:0.035212	train-logloss:0.013654
[52]	eval-logloss:0.035484	train-logloss:0.013365
[53]	eval-logloss:0.035765	train-logloss:0.013124
[54]	eval-logloss:0.036045	train-logloss:0.012868
[55]	eval-logloss:0.036361	train-logloss:0.012673
[56]	eval-logloss:0.036701	train-logloss:0.012496
[57]	eval-logloss:0.037012	train-logloss:0.012319
[58]	eval-logloss:0.037341	train-logloss:0.012186
[59]	eval-logloss:0.037733	train-logloss:0.012047
[60]	eval-logloss:0.038044	train-logloss:0.011927
[61]	eval-logloss:0.03846	train-logloss:0.011801
[62]	eval-logloss:0.038879	train-logloss:0.011705
[63]	eval-logloss:0.039214	train-logloss:0.011598
[64]	eval-logloss:0.039627	train-logloss:0.011517
[65]	eval-logloss:0.040038	train-logloss:0.011428
[66]	eval-logloss:0.040378	train-logloss:0.011354
[67]	eval-logloss:0.040787	train-logloss:0.01128
[68]	eval-logloss:0.041217	train-logloss:0.011214
[69]	eval-logloss:0.041708	train-logloss:0.011144
[70]	eval-logloss:0.042139	train-logloss:0.011101
[71]	eval-logloss:0.042477	train-logloss:0.01104
[72]	eval-logloss:0.042919	train-logloss:0.010985
[73]	eval-logloss:0.043393	train-logloss:0.010919
[74]	eval-logloss:0.043856	train-logloss:0.010864
[75]	eval-logloss:0.044307	train-logloss:0.010832
[76]	eval-logloss:0.044725	train-logloss:0.01079
[77]	eval-logloss:0.045174	train-logloss:0.010745
[78]	eval-logloss:0.045617	train-logloss:0.010717
[79]	eval-logloss:0.046071	train-logloss:0.010683
[80]	eval-logloss:0.046514	train-logloss:0.010644
[81]	eval-logloss:0.046947	train-logloss:0.010606
[82]	eval-logloss:0.047451	train-logloss:0.010558
[83]	eval-logloss:0.047796	train-logloss:0.010542
[84]	eval-logloss:0.048233	train-logloss:0.01052
[85]	eval-logloss:0.048674	train-logloss:0.010485
[86]	eval-logloss:0.049105	train-logloss:0.010465
[87]	eval-logloss:0.049558	train-logloss:0.010427
[88]	eval-logloss:0.050005	train-logloss:0.01041
[89]	eval-logloss:0.050505	train-logloss:0.010371
[90]	eval-logloss:0.050833	train-logloss:0.010351
[91]	eval-logloss:0.051268	train-logloss:0.010321
[92]	eval-logloss:0.051579	train-logloss:0.010299
[93]	eval-logloss:0.051591	train-logloss:0.010279
[94]	eval-logloss:0.051934	train-logloss:0.010249
[95]	eval-logloss:0.051883	train-logloss:0.010219
[96]	eval-logloss:0.051876	train-logloss:0.010197
[97]	eval-logloss:0.051883	train-logloss:0.010168
[98]	eval-logloss:0.052007	train-logloss:0.010124
[99]	eval-logloss:0.052052	train-logloss:0.0101
[100]	eval-logloss:0.051998	train-logloss:0.010072
[101]	eval-logloss:0.052012	train-logloss:0.010053
[102]	eval-logloss:0.052177	train-logloss:0.010037
[103]	eval-logloss:0.052374	train-logloss:0.009999
[104]	eval-logloss:0.052831	train-logloss:0.009977
[105]	eval-logloss:0.052937	train-logloss:0.009955
[106]	eval-logloss:0.052959	train-logloss:0.009934
[107]	eval-logloss:0.053382	train-logloss:0.009916
[108]	eval-logloss:0.05332	train-logloss:0.009898
[109]	eval-logloss:0.053288	train-logloss:0.009878
[110]	eval-logloss:0.053278	train-logloss:0.009846
[111]	eval-logloss:0.053324	train-logloss:0.009807
[112]	eval-logloss:0.053557	train-logloss:0.009787
[113]	eval-logloss:0.053505	train-logloss:0.009765
[114]	eval-logloss:0.053703	train-logloss:0.009748
[115]	eval-logloss:0.053686	train-logloss:0.009736
[116]	eval-logloss:0.053668	train-logloss:0.009726
[117]	eval-logloss:0.05409	train-logloss:0.009712
[118]	eval-logloss:0.054098	train-logloss:0.009691
[119]	eval-logloss:0.054057	train-logloss:0.009647
[120]	eval-logloss:0.054036	train-logloss:0.009633
[121]	eval-logloss:0.054059	train-logloss:0.009621
[122]	eval-logloss:0.054364	train-logloss:0.009612
[123]	eval-logloss:0.054374	train-logloss:0.009602
[124]	eval-logloss:0.05431	train-logloss:0.009579
[125]	eval-logloss:0.054346	train-logloss:0.00957
[126]	eval-logloss:0.054768	train-logloss:0.009555
[127]	eval-logloss:0.054731	train-logloss:0.009542
[128]	eval-logloss:0.054734	train-logloss:0.009527
[129]	eval-logloss:0.054725	train-logloss:0.009514
[130]	eval-logloss:0.054717	train-logloss:0.009505
[131]	eval-logloss:0.05471	train-logloss:0.009496
[132]	eval-logloss:0.05474	train-logloss:0.009486
[133]	eval-logloss:0.054666	train-logloss:0.009447
[134]	eval-logloss:0.054605	train-logloss:0.009426
[135]	eval-logloss:0.054617	train-logloss:0.009417
[136]	eval-logloss:0.054605	train-logloss:0.009409
[137]	eval-logloss:0.05504	train-logloss:0.009398
[138]	eval-logloss:0.055179	train-logloss:0.009373
[139]	eval-logloss:0.055009	train-logloss:0.009358
[140]	eval-logloss:0.055185	train-logloss:0.009344
[141]	eval-logloss:0.055188	train-logloss:0.009334
[142]	eval-logloss:0.055239	train-logloss:0.009304
[143]	eval-logloss:0.055576	train-logloss:0.009288
[144]	eval-logloss:0.055497	train-logloss:0.009275
[145]	eval-logloss:0.055494	train-logloss:0.009267
[146]	eval-logloss:0.055481	train-logloss:0.009259
[147]	eval-logloss:0.055535	train-logloss:0.009234
[148]	eval-logloss:0.055482	train-logloss:0.009205
[149]	eval-logloss:0.055901	train-logloss:0.009196
[150]	eval-logloss:0.05591	train-logloss:0.009181
[151]	eval-logloss:0.055973	train-logloss:0.00917
[152]	eval-logloss:0.056014	train-logloss:0.009165
[153]	eval-logloss:0.056101	train-logloss:0.009157
[154]	eval-logloss:0.05612	train-logloss:0.009149
[155]	eval-logloss:0.056125	train-logloss:0.009139
[156]	eval-logloss:0.056118	train-logloss:0.009132
[157]	eval-logloss:0.05604	train-logloss:0.009109
[158]	eval-logloss:0.056493	train-logloss:0.009098
[159]	eval-logloss:0.05685	train-logloss:0.00908
[160]	eval-logloss:0.056835	train-logloss:0.009071
[161]	eval-logloss:0.05696	train-logloss:0.009063
[162]	eval-logloss:0.05696	train-logloss:0.009055
[163]	eval-logloss:0.057266	train-logloss:0.009048
[164]	eval-logloss:0.057264	train-logloss:0.009038
[165]	eval-logloss:0.057282	train-logloss:0.009026
[166]	eval-logloss:0.057294	train-logloss:0.009019
[167]	eval-logloss:0.057446	train-logloss:0.009009
[168]	eval-logloss:0.057418	train-logloss:0.008993
[169]	eval-logloss:0.057403	train-logloss:0.008978
[170]	eval-logloss:0.0574	train-logloss:0.008968
[171]	eval-logloss:0.057369	train-logloss:0.008958
[172]	eval-logloss:0.057565	train-logloss:0.008949
[173]	eval-logloss:0.057634	train-logloss:0.008931
[174]	eval-logloss:0.057632	train-logloss:0.008926
[175]	eval-logloss:0.05759	train-logloss:0.008915
[176]	eval-logloss:0.057591	train-logloss:0.008907
[177]	eval-logloss:0.057664	train-logloss:0.008901
[178]	eval-logloss:0.057662	train-logloss:0.008897
[179]	eval-logloss:0.057692	train-logloss:0.008887
[180]	eval-logloss:0.057705	train-logloss:0.008878
[181]	eval-logloss:0.057645	train-logloss:0.008868
[182]	eval-logloss:0.05769	train-logloss:0.008862
[183]	eval-logloss:0.057677	train-logloss:0.008842
[184]	eval-logloss:0.057685	train-logloss:0.008837
[185]	eval-logloss:0.057645	train-logloss:0.008833
[186]	eval-logloss:0.057675	train-logloss:0.008823
[187]	eval-logloss:0.057665	train-logloss:0.008819
[188]	eval-logloss:0.05809	train-logloss:0.008816
[189]	eval-logloss:0.058212	train-logloss:0.008808
[190]	eval-logloss:0.058203	train-logloss:0.008797
[191]	eval-logloss:0.058216	train-logloss:0.008787
[192]	eval-logloss:0.058224	train-logloss:0.008781
[193]	eval-logloss:0.058247	train-logloss:0.008773
[194]	eval-logloss:0.058252	train-logloss:0.008767
[195]	eval-logloss:0.058272	train-logloss:0.008762
[196]	eval-logloss:0.05826	train-logloss:0.008756
[197]	eval-logloss:0.05863	train-logloss:0.008744
[198]	eval-logloss:0.058623	train-logloss:0.008739
[199]	eval-logloss:0.058614	train-logloss:0.008733
[200]	eval-logloss:0.058599	train-logloss:0.008725
[201]	eval-logloss:0.058607	train-logloss:0.008716
[202]	eval-logloss:0.05858	train-logloss:0.008709
[203]	eval-logloss:0.05856	train-logloss:0.008701
[204]	eval-logloss:0.058943	train-logloss:0.008691
[205]	eval-logloss:0.058949	train-logloss:0.008684
[206]	eval-logloss:0.058947	train-logloss:0.008673
[207]	eval-logloss:0.058988	train-logloss:0.008666
[208]	eval-logloss:0.058984	train-logloss:0.008662
[209]	eval-logloss:0.058969	train-logloss:0.008657
[210]	eval-logloss:0.059048	train-logloss:0.008654
[211]	eval-logloss:0.059028	train-logloss:0.008648
[212]	eval-logloss:0.059021	train-logloss:0.008642
[213]	eval-logloss:0.05906	train-logloss:0.008635
[214]	eval-logloss:0.059055	train-logloss:0.008628
[215]	eval-logloss:0.059065	train-logloss:0.008621
[216]	eval-logloss:0.059151	train-logloss:0.008615
[217]	eval-logloss:0.059276	train-logloss:0.008609
[218]	eval-logloss:0.059298	train-logloss:0.008603
[219]	eval-logloss:0.059346	train-logloss:0.008588
[220]	eval-logloss:0.059346	train-logloss:0.008582
[221]	eval-logloss:0.059327	train-logloss:0.008576
[222]	eval-logloss:0.059288	train-logloss:0.008556
[223]	eval-logloss:0.059497	train-logloss:0.008551
[224]	eval-logloss:0.059507	train-logloss:0.008543
[225]	eval-logloss:0.059603	train-logloss:0.008532
[226]	eval-logloss:0.059603	train-logloss:0.008529
[227]	eval-logloss:0.059544	train-logloss:0.00852
[228]	eval-logloss:0.059526	train-logloss:0.00851
[229]	eval-logloss:0.059495	train-logloss:0.008504
[230]	eval-logloss:0.059505	train-logloss:0.008502
[231]	eval-logloss:0.059486	train-logloss:0.008496
[232]	eval-logloss:0.059706	train-logloss:0.008492
[233]	eval-logloss:0.059673	train-logloss:0.008486
[234]	eval-logloss:0.059676	train-logloss:0.008481
[235]	eval-logloss:0.05976	train-logloss:0.008472
[236]	eval-logloss:0.059821	train-logloss:0.008459
[237]	eval-logloss:0.059845	train-logloss:0.008451
[238]	eval-logloss:0.059914	train-logloss:0.008444
[239]	eval-logloss:0.059947	train-logloss:0.008437
[240]	eval-logloss:0.059952	train-logloss:0.008434
[241]	eval-logloss:0.059937	train-logloss:0.008428
[242]	eval-logloss:0.059954	train-logloss:0.008417
[243]	eval-logloss:0.05996	train-logloss:0.00841
[244]	eval-logloss:0.05996	train-logloss:0.008402
[245]	eval-logloss:0.059973	train-logloss:0.008393
[246]	eval-logloss:0.05998	train-logloss:0.008389
[247]	eval-logloss:0.059996	train-logloss:0.008383
[248]	eval-logloss:0.060001	train-logloss:0.00838
[249]	eval-logloss:0.059992	train-logloss:0.008377
[250]	eval-logloss:0.059992	train-logloss:0.008371
[251]	eval-logloss:0.059985	train-logloss:0.008366
[252]	eval-logloss:0.060016	train-logloss:0.008353
[253]	eval-logloss:0.060016	train-logloss:0.008346
[254]	eval-logloss:0.060006	train-logloss:0.00834
[255]	eval-logloss:0.059947	train-logloss:0.008334
[256]	eval-logloss:0.059946	train-logloss:0.00833
[257]	eval-logloss:0.059972	train-logloss:0.008321
[258]	eval-logloss:0.060313	train-logloss:0.008312
[259]	eval-logloss:0.060313	train-logloss:0.00831
[260]	eval-logloss:0.060336	train-logloss:0.008302
[261]	eval-logloss:0.060273	train-logloss:0.0083
[262]	eval-logloss:0.060314	train-logloss:0.008294
[263]	eval-logloss:0.060323	train-logloss:0.008288
[264]	eval-logloss:0.060313	train-logloss:0.008279
[265]	eval-logloss:0.06069	train-logloss:0.008275
[266]	eval-logloss:0.060693	train-logloss:0.008271
[267]	eval-logloss:0.060698	train-logloss:0.008263
[268]	eval-logloss:0.060708	train-logloss:0.008261
[269]	eval-logloss:0.060759	train-logloss:0.008253
[270]	eval-logloss:0.060726	train-logloss:0.00824
[271]	eval-logloss:0.060725	train-logloss:0.008237
[272]	eval-logloss:0.060729	train-logloss:0.00823
[273]	eval-logloss:0.060735	train-logloss:0.008224
[274]	eval-logloss:0.060795	train-logloss:0.008217
[275]	eval-logloss:0.060795	train-logloss:0.008209
[276]	eval-logloss:0.060807	train-logloss:0.008204
[277]	eval-logloss:0.060813	train-logloss:0.008198
[278]	eval-logloss:0.060816	train-logloss:0.008194
[279]	eval-logloss:0.060798	train-logloss:0.008188
[280]	eval-logloss:0.060797	train-logloss:0.008181
[281]	eval-logloss:0.060769	train-logloss:0.008178
[282]	eval-logloss:0.060834	train-logloss:0.008167
[283]	eval-logloss:0.060805	train-logloss:0.00816
[284]	eval-logloss:0.06082	train-logloss:0.008154
[285]	eval-logloss:0.060819	train-logloss:0.008152
[286]	eval-logloss:0.060764	train-logloss:0.008146
[287]	eval-logloss:0.060768	train-logloss:0.008142
[288]	eval-logloss:0.06079	train-logloss:0.008136
[289]	eval-logloss:0.060818	train-logloss:0.008131
[290]	eval-logloss:0.060809	train-logloss:0.008125
[291]	eval-logloss:0.06102	train-logloss:0.008119
[292]	eval-logloss:0.06152	train-logloss:0.008115
[293]	eval-logloss:0.061578	train-logloss:0.00811
[294]	eval-logloss:0.061594	train-logloss:0.008104
[295]	eval-logloss:0.061631	train-logloss:0.008102
[296]	eval-logloss:0.061661	train-logloss:0.008087
[297]	eval-logloss:0.061679	train-logloss:0.008082
[298]	eval-logloss:0.061677	train-logloss:0.008077
[299]	eval-logloss:0.061584	train-logloss:0.008073
[300]	eval-logloss:0.061765	train-logloss:0.008063
[301]	eval-logloss:0.061786	train-logloss:0.008058
[302]	eval-logloss:0.061788	train-logloss:0.008054
[303]	eval-logloss:0.061786	train-logloss:0.00805
[304]	eval-logloss:0.061793	train-logloss:0.008045
[305]	eval-logloss:0.061764	train-logloss:0.008036
[306]	eval-logloss:0.061965	train-logloss:0.008029
[307]	eval-logloss:0.061965	train-logloss:0.008021
[308]	eval-logloss:0.061962	train-logloss:0.008017
[309]	eval-logloss:0.061971	train-logloss:0.008012
[310]	eval-logloss:0.061968	train-logloss:0.008007
[311]	eval-logloss:0.061961	train-logloss:0.008
[312]	eval-logloss:0.06201	train-logloss:0.007992
[313]	eval-logloss:0.062187	train-logloss:0.007987
[314]	eval-logloss:0.062183	train-logloss:0.007981
[315]	eval-logloss:0.062148	train-logloss:0.007973
[316]	eval-logloss:0.062148	train-logloss:0.007967
[317]	eval-logloss:0.062121	train-logloss:0.007964
[318]	eval-logloss:0.062243	train-logloss:0.007956
[319]	eval-logloss:0.062249	train-logloss:0.00795
[320]	eval-logloss:0.062258	train-logloss:0.007947
[321]	eval-logloss:0.062261	train-logloss:0.007939
[322]	eval-logloss:0.062318	train-logloss:0.007933
[323]	eval-logloss:0.062364	train-logloss:0.00793
[324]	eval-logloss:0.06243	train-logloss:0.007927
[325]	eval-logloss:0.062451	train-logloss:0.007921
[326]	eval-logloss:0.062757	train-logloss:0.007917
[327]	eval-logloss:0.062756	train-logloss:0.007914
[328]	eval-logloss:0.062772	train-logloss:0.007909
[329]	eval-logloss:0.062764	train-logloss:0.007903
[330]	eval-logloss:0.062775	train-logloss:0.007896
[331]	eval-logloss:0.062777	train-logloss:0.00789
[332]	eval-logloss:0.063103	train-logloss:0.007886
[333]	eval-logloss:0.063096	train-logloss:0.00788
[334]	eval-logloss:0.063527	train-logloss:0.007878
[335]	eval-logloss:0.063544	train-logloss:0.007873
[336]	eval-logloss:0.06353	train-logloss:0.007868
[337]	eval-logloss:0.063759	train-logloss:0.007861
[338]	eval-logloss:0.064072	train-logloss:0.007856
[339]	eval-logloss:0.064078	train-logloss:0.007849
[340]	eval-logloss:0.064094	train-logloss:0.007844
[341]	eval-logloss:0.064127	train-logloss:0.00784
[342]	eval-logloss:0.064124	train-logloss:0.007832
[343]	eval-logloss:0.064123	train-logloss:0.007828
[344]	eval-logloss:0.064096	train-logloss:0.007824
[345]	eval-logloss:0.064108	train-logloss:0.007821
[346]	eval-logloss:0.064107	train-logloss:0.007818
[347]	eval-logloss:0.064124	train-logloss:0.007811
[348]	eval-logloss:0.064111	train-logloss:0.007806
[349]	eval-logloss:0.0641	train-logloss:0.007801
[350]	eval-logloss:0.064089	train-logloss:0.007797
[351]	eval-logloss:0.064082	train-logloss:0.007795
[352]	eval-logloss:0.064084	train-logloss:0.00779
[353]	eval-logloss:0.064099	train-logloss:0.007788
[354]	eval-logloss:0.064099	train-logloss:0.007786
[355]	eval-logloss:0.064101	train-logloss:0.007781
[356]	eval-logloss:0.064103	train-logloss:0.007775
[357]	eval-logloss:0.064102	train-logloss:0.007771
[358]	eval-logloss:0.064119	train-logloss:0.007765
[359]	eval-logloss:0.064126	train-logloss:0.007763
[360]	eval-logloss:0.064123	train-logloss:0.007761
[361]	eval-logloss:0.064127	train-logloss:0.007755
[362]	eval-logloss:0.064131	train-logloss:0.007747
[363]	eval-logloss:0.064128	train-logloss:0.007742
[364]	eval-logloss:0.064221	train-logloss:0.007735
[365]	eval-logloss:0.064248	train-logloss:0.007729
[366]	eval-logloss:0.064296	train-logloss:0.007725
[367]	eval-logloss:0.064291	train-logloss:0.007723
[368]	eval-logloss:0.064296	train-logloss:0.007718
[369]	eval-logloss:0.064285	train-logloss:0.007715
[370]	eval-logloss:0.064324	train-logloss:0.007709
[371]	eval-logloss:0.064334	train-logloss:0.007703
[372]	eval-logloss:0.064331	train-logloss:0.007699
[373]	eval-logloss:0.064308	train-logloss:0.007694
[374]	eval-logloss:0.064309	train-logloss:0.007689
[375]	eval-logloss:0.064284	train-logloss:0.007681
[376]	eval-logloss:0.064298	train-logloss:0.007677
[377]	eval-logloss:0.064299	train-logloss:0.007673
[378]	eval-logloss:0.064293	train-logloss:0.007668
[379]	eval-logloss:0.064506	train-logloss:0.007663
[380]	eval-logloss:0.064502	train-logloss:0.007659
[381]	eval-logloss:0.064513	train-logloss:0.007655
[382]	eval-logloss:0.064515	train-logloss:0.007652
[383]	eval-logloss:0.064519	train-logloss:0.007647
[384]	eval-logloss:0.064504	train-logloss:0.007642
[385]	eval-logloss:0.064325	train-logloss:0.007636
[386]	eval-logloss:0.064264	train-logloss:0.00763
[387]	eval-logloss:0.064263	train-logloss:0.007628
[388]	eval-logloss:0.064259	train-logloss:0.007626
[389]	eval-logloss:0.064637	train-logloss:0.007621
[390]	eval-logloss:0.064643	train-logloss:0.007618
[391]	eval-logloss:0.064666	train-logloss:0.007612
[392]	eval-logloss:0.064689	train-logloss:0.007609
[393]	eval-logloss:0.064801	train-logloss:0.007602
[394]	eval-logloss:0.064798	train-logloss:0.007597
[395]	eval-logloss:0.064802	train-logloss:0.007592
[396]	eval-logloss:0.064846	train-logloss:0.007588
[397]	eval-logloss:0.064847	train-logloss:0.007583
[398]	eval-logloss:0.064909	train-logloss:0.007573
[399]	eval-logloss:0.064922	train-logloss:0.007567
[400]	eval-logloss:0.064946	train-logloss:0.00756
[401]	eval-logloss:0.064976	train-logloss:0.007557
[402]	eval-logloss:0.064975	train-logloss:0.007553
[403]	eval-logloss:0.065027	train-logloss:0.007551
[404]	eval-logloss:0.065013	train-logloss:0.007548
[405]	eval-logloss:0.065044	train-logloss:0.007541
[406]	eval-logloss:0.065056	train-logloss:0.007535
[407]	eval-logloss:0.065035	train-logloss:0.007528
[408]	eval-logloss:0.065038	train-logloss:0.007524
[409]	eval-logloss:0.065022	train-logloss:0.007517
[410]	eval-logloss:0.065021	train-logloss:0.007516
[411]	eval-logloss:0.065024	train-logloss:0.007514
[412]	eval-logloss:0.065008	train-logloss:0.007509
[413]	eval-logloss:0.065017	train-logloss:0.007503
[414]	eval-logloss:0.06501	train-logloss:0.0075
[415]	eval-logloss:0.065006	train-logloss:0.007495
[416]	eval-logloss:0.064962	train-logloss:0.007489
[417]	eval-logloss:0.064964	train-logloss:0.007486
[418]	eval-logloss:0.064969	train-logloss:0.007483
[419]	eval-logloss:0.06499	train-logloss:0.00748
[420]	eval-logloss:0.064988	train-logloss:0.007475
[421]	eval-logloss:0.06499	train-logloss:0.00747
[422]	eval-logloss:0.064827	train-logloss:0.007465
[423]	eval-logloss:0.064851	train-logloss:0.007461
[424]	eval-logloss:0.064841	train-logloss:0.007456
[425]	eval-logloss:0.064922	train-logloss:0.007451
[426]	eval-logloss:0.064912	train-logloss:0.007448
[427]	eval-logloss:0.064915	train-logloss:0.007443
[428]	eval-logloss:0.064893	train-logloss:0.007437
[429]	eval-logloss:0.064893	train-logloss:0.007433
[430]	eval-logloss:0.064882	train-logloss:0.00743
[431]	eval-logloss:0.064893	train-logloss:0.007426
[432]	eval-logloss:0.065093	train-logloss:0.007422
[433]	eval-logloss:0.06509	train-logloss:0.007419
[434]	eval-logloss:0.065077	train-logloss:0.007415
[435]	eval-logloss:0.064819	train-logloss:0.007411
[436]	eval-logloss:0.064843	train-logloss:0.007409
[437]	eval-logloss:0.064843	train-logloss:0.007406
[438]	eval-logloss:0.065069	train-logloss:0.0074
[439]	eval-logloss:0.065057	train-logloss:0.007394
[440]	eval-logloss:0.065044	train-logloss:0.00739
[441]	eval-logloss:0.065061	train-logloss:0.007385
[442]	eval-logloss:0.06508	train-logloss:0.007381
[443]	eval-logloss:0.06511	train-logloss:0.007377
[444]	eval-logloss:0.065108	train-logloss:0.007373
[445]	eval-logloss:0.065153	train-logloss:0.007368
[446]	eval-logloss:0.065154	train-logloss:0.007364
[447]	eval-logloss:0.065037	train-logloss:0.00736
[448]	eval-logloss:0.065046	train-logloss:0.007354
[449]	eval-logloss:0.065044	train-logloss:0.007347
[450]	eval-logloss:0.065063	train-logloss:0.007343
[451]	eval-logloss:0.065079	train-logloss:0.00734
[452]	eval-logloss:0.065074	train-logloss:0.007337
[453]	eval-logloss:0.065091	train-logloss:0.007331
[454]	eval-logloss:0.065089	train-logloss:0.007326
[455]	eval-logloss:0.065087	train-logloss:0.007322
[456]	eval-logloss:0.065068	train-logloss:0.007318
[457]	eval-logloss:0.065079	train-logloss:0.007316
[458]	eval-logloss:0.065129	train-logloss:0.007312
[459]	eval-logloss:0.065129	train-logloss:0.007309
[460]	eval-logloss:0.065127	train-logloss:0.007306
[461]	eval-logloss:0.065132	train-logloss:0.007303
[462]	eval-logloss:0.065144	train-logloss:0.007298
[463]	eval-logloss:0.065146	train-logloss:0.007297
[464]	eval-logloss:0.065164	train-logloss:0.007291
[465]	eval-logloss:0.065154	train-logloss:0.007287
[466]	eval-logloss:0.065146	train-logloss:0.007283
[467]	eval-logloss:0.065153	train-logloss:0.007277
[468]	eval-logloss:0.065136	train-logloss:0.007273
[469]	eval-logloss:0.065141	train-logloss:0.007271
[470]	eval-logloss:0.065122	train-logloss:0.007265
[471]	eval-logloss:0.065121	train-logloss:0.007261
[472]	eval-logloss:0.065114	train-logloss:0.007256
[473]	eval-logloss:0.065118	train-logloss:0.007253
[474]	eval-logloss:0.065095	train-logloss:0.00725
[475]	eval-logloss:0.065102	train-logloss:0.007248
[476]	eval-logloss:0.065163	train-logloss:0.00724
[477]	eval-logloss:0.065313	train-logloss:0.007234
[478]	eval-logloss:0.065307	train-logloss:0.007232
[479]	eval-logloss:0.06526	train-logloss:0.007225
[480]	eval-logloss:0.065294	train-logloss:0.007222
[481]	eval-logloss:0.065281	train-logloss:0.007217
[482]	eval-logloss:0.065281	train-logloss:0.007214
[483]	eval-logloss:0.065289	train-logloss:0.007212
[484]	eval-logloss:0.065291	train-logloss:0.007207
[485]	eval-logloss:0.065301	train-logloss:0.007204
[486]	eval-logloss:0.065604	train-logloss:0.007199
[487]	eval-logloss:0.065689	train-logloss:0.007194
[488]	eval-logloss:0.065744	train-logloss:0.007192
[489]	eval-logloss:0.06574	train-logloss:0.007187
[490]	eval-logloss:0.065716	train-logloss:0.007182
[491]	eval-logloss:0.065711	train-logloss:0.007179
[492]	eval-logloss:0.065717	train-logloss:0.007174
[493]	eval-logloss:0.065719	train-logloss:0.007172
[494]	eval-logloss:0.065999	train-logloss:0.007168
[495]	eval-logloss:0.066075	train-logloss:0.007163
[496]	eval-logloss:0.066062	train-logloss:0.007161
[497]	eval-logloss:0.066071	train-logloss:0.007158
[498]	eval-logloss:0.06646	train-logloss:0.007153
[499]	eval-logloss:0.066454	train-logloss:0.00715
<< 完成训练模型
2019-05-25 19:26:21.956188
>> 开始划分X,y
<< 完成划分X,y
>> 开始测试模型
> 概率转换0,1
buy_plus_180402_180408
buy_180402_180408
前154565行[test] label=1：
real
   user_id  cate  shop_id
0       11    69     3697
1       16    31     4303
2       29    75     5676
3       34    24     5545
4       37    77     4043
pred
   user_id  cate  shop_id  pred
0   768247     7     7114     0
1   421482     7      405     0
2   967737     7     7114     0
3   451713     7     7114     0
4  1303834     7     7114     0
所有用户品类中预测购买用户品类的准确率为 1.0
所有用户品类中预测购买用户品类的召回率1.2939539999353022e-05
F11=3.88176154338839e-05
所有用户品类中预测购买店铺的准确率为 1.0
所有用户品类中预测购买店铺的召回率1.9409309999029535e-05
F12=3.234843142456022e-05
score=3.4936105028289694e-05
前10000行 label=1：
real
   user_id  cate  shop_id
0       11    69     3697
1       16    31     4303
2       29    75     5676
3       34    24     5545
4       37    77     4043
pred
   user_id  cate  shop_id  pred
0   768247     7     7114     0
1   421482     7      405     0
2   967737     7     7114     0
3   451713     7     7114     0
4  1303834     7     7114     0
所有用户品类中预测购买用户品类的准确率为 1.0
所有用户品类中预测购买用户品类的召回率1.2939539999353022e-05
F11=3.88176154338839e-05
所有用户品类中预测购买店铺的准确率为 1.0
所有用户品类中预测购买店铺的召回率1.9409309999029535e-05
F12=3.234843142456022e-05
score=3.4936105028289694e-05
前20000行 label=1：
real
   user_id  cate  shop_id
0       11    69     3697
1       16    31     4303
2       29    75     5676
3       34    24     5545
4       37    77     4043
pred
   user_id  cate  shop_id  pred
0   768247     7     7114     0
1   421482     7      405     0
2   967737     7     7114     0
3   451713     7     7114     0
4  1303834     7     7114     0
所有用户品类中预测购买用户品类的准确率为 1.0
所有用户品类中预测购买用户品类的召回率1.2939539999353022e-05
F11=3.88176154338839e-05
所有用户品类中预测购买店铺的准确率为 1.0
所有用户品类中预测购买店铺的召回率1.9409309999029535e-05
F12=3.234843142456022e-05
score=3.4936105028289694e-05
前30000行 label=1：
real
   user_id  cate  shop_id
0       11    69     3697
1       16    31     4303
2       29    75     5676
3       34    24     5545
4       37    77     4043
pred
   user_id  cate  shop_id  pred
0   768247     7     7114     0
1   421482     7      405     0
2   967737     7     7114     0
3   451713     7     7114     0
4  1303834     7     7114     0
所有用户品类中预测购买用户品类的准确率为 1.0
所有用户品类中预测购买用户品类的召回率1.2939539999353022e-05
F11=3.88176154338839e-05
所有用户品类中预测购买店铺的准确率为 1.0
所有用户品类中预测购买店铺的召回率1.9409309999029535e-05
F12=3.234843142456022e-05
score=3.4936105028289694e-05
前40000行 label=1：
real
   user_id  cate  shop_id
0       11    69     3697
1       16    31     4303
2       29    75     5676
3       34    24     5545
4       37    77     4043
pred
   user_id  cate  shop_id  pred
0   768247     7     7114     0
1   421482     7      405     0
2   967737     7     7114     0
3   451713     7     7114     0
4  1303834     7     7114     0
所有用户品类中预测购买用户品类的准确率为 1.0
所有用户品类中预测购买用户品类的召回率1.2939539999353022e-05
F11=3.88176154338839e-05
所有用户品类中预测购买店铺的准确率为 1.0
所有用户品类中预测购买店铺的召回率1.9409309999029535e-05
F12=3.234843142456022e-05
score=3.4936105028289694e-05
前50000行 label=1：
real
   user_id  cate  shop_id
0       11    69     3697
1       16    31     4303
2       29    75     5676
3       34    24     5545
4       37    77     4043
pred
   user_id  cate  shop_id  pred
0   768247     7     7114     0
1   421482     7      405     0
2   967737     7     7114     0
3   451713     7     7114     0
4  1303834     7     7114     0
所有用户品类中预测购买用户品类的准确率为 1.0
所有用户品类中预测购买用户品类的召回率1.2939539999353022e-05
F11=3.88176154338839e-05
所有用户品类中预测购买店铺的准确率为 1.0
所有用户品类中预测购买店铺的召回率1.9409309999029535e-05
F12=3.234843142456022e-05
score=3.4936105028289694e-05
前60000行 label=1：
real
   user_id  cate  shop_id
0       11    69     3697
1       16    31     4303
2       29    75     5676
3       34    24     5545
4       37    77     4043
pred
   user_id  cate  shop_id  pred
0   768247     7     7114     0
1   421482     7      405     0
2   967737     7     7114     0
3   451713     7     7114     0
4  1303834     7     7114     0
所有用户品类中预测购买用户品类的准确率为 1.0
所有用户品类中预测购买用户品类的召回率1.2939539999353022e-05
F11=3.88176154338839e-05
所有用户品类中预测购买店铺的准确率为 1.0
所有用户品类中预测购买店铺的召回率1.9409309999029535e-05
F12=3.234843142456022e-05
score=3.4936105028289694e-05
前70000行 label=1：
real
   user_id  cate  shop_id
0       11    69     3697
1       16    31     4303
2       29    75     5676
3       34    24     5545
4       37    77     4043
pred
   user_id  cate  shop_id  pred
0   768247     7     7114     0
1   421482     7      405     0
2   967737     7     7114     0
3   451713     7     7114     0
4  1303834     7     7114     0
所有用户品类中预测购买用户品类的准确率为 1.0
所有用户品类中预测购买用户品类的召回率1.2939539999353022e-05
F11=3.88176154338839e-05
所有用户品类中预测购买店铺的准确率为 1.0
所有用户品类中预测购买店铺的召回率1.9409309999029535e-05
F12=3.234843142456022e-05
score=3.4936105028289694e-05
前80000行 label=1：
real
   user_id  cate  shop_id
0       11    69     3697
1       16    31     4303
2       29    75     5676
3       34    24     5545
4       37    77     4043
pred
   user_id  cate  shop_id  pred
0   768247     7     7114     0
1   421482     7      405     0
2   967737     7     7114     0
3   451713     7     7114     0
4  1303834     7     7114     0
所有用户品类中预测购买用户品类的准确率为 1.0
所有用户品类中预测购买用户品类的召回率1.2939539999353022e-05
F11=3.88176154338839e-05
所有用户品类中预测购买店铺的准确率为 1.0
所有用户品类中预测购买店铺的召回率1.9409309999029535e-05
F12=3.234843142456022e-05
score=3.4936105028289694e-05
前90000行 label=1：
real
   user_id  cate  shop_id
0       11    69     3697
1       16    31     4303
2       29    75     5676
3       34    24     5545
4       37    77     4043
pred
   user_id  cate  shop_id  pred
0   768247     7     7114     0
1   421482     7      405     0
2   967737     7     7114     0
3   451713     7     7114     0
4  1303834     7     7114     0
所有用户品类中预测购买用户品类的准确率为 1.0
所有用户品类中预测购买用户品类的召回率1.2939539999353022e-05
F11=3.88176154338839e-05
所有用户品类中预测购买店铺的准确率为 1.0
所有用户品类中预测购买店铺的召回率1.9409309999029535e-05
F12=3.234843142456022e-05
score=3.4936105028289694e-05
前100000行 label=1：
real
   user_id  cate  shop_id
0       11    69     3697
1       16    31     4303
2       29    75     5676
3       34    24     5545
4       37    77     4043
pred
   user_id  cate  shop_id  pred
0   768247     7     7114     0
1   421482     7      405     0
2   967737     7     7114     0
3   451713     7     7114     0
4  1303834     7     7114     0
所有用户品类中预测购买用户品类的准确率为 1.0
所有用户品类中预测购买用户品类的召回率1.2939539999353022e-05
F11=3.88176154338839e-05
所有用户品类中预测购买店铺的准确率为 1.0
所有用户品类中预测购买店铺的召回率1.9409309999029535e-05
F12=3.234843142456022e-05
score=3.4936105028289694e-05
前110000行 label=1：
real
   user_id  cate  shop_id
0       11    69     3697
1       16    31     4303
2       29    75     5676
3       34    24     5545
4       37    77     4043
pred
   user_id  cate  shop_id  pred
0   768247     7     7114     0
1   421482     7      405     0
2   967737     7     7114     0
3   451713     7     7114     0
4  1303834     7     7114     0
所有用户品类中预测购买用户品类的准确率为 1.0
所有用户品类中预测购买用户品类的召回率1.2939539999353022e-05
F11=3.88176154338839e-05
所有用户品类中预测购买店铺的准确率为 1.0
所有用户品类中预测购买店铺的召回率1.9409309999029535e-05
F12=3.234843142456022e-05
score=3.4936105028289694e-05
前120000行 label=1：
real
   user_id  cate  shop_id
0       11    69     3697
1       16    31     4303
2       29    75     5676
3       34    24     5545
4       37    77     4043
pred
   user_id  cate  shop_id  pred
0   768247     7     7114     0
1   421482     7      405     0
2   967737     7     7114     0
3   451713     7     7114     0
4  1303834     7     7114     0
所有用户品类中预测购买用户品类的准确率为 1.0
所有用户品类中预测购买用户品类的召回率1.2939539999353022e-05
F11=3.88176154338839e-05
所有用户品类中预测购买店铺的准确率为 1.0
所有用户品类中预测购买店铺的召回率1.9409309999029535e-05
F12=3.234843142456022e-05
score=3.4936105028289694e-05
前130000行 label=1：
real
   user_id  cate  shop_id
0       11    69     3697
1       16    31     4303
2       29    75     5676
3       34    24     5545
4       37    77     4043
pred
   user_id  cate  shop_id  pred
0   768247     7     7114     0
1   421482     7      405     0
2   967737     7     7114     0
3   451713     7     7114     0
4  1303834     7     7114     0
所有用户品类中预测购买用户品类的准确率为 1.0
所有用户品类中预测购买用户品类的召回率1.2939539999353022e-05
F11=3.88176154338839e-05
所有用户品类中预测购买店铺的准确率为 1.0
所有用户品类中预测购买店铺的召回率1.9409309999029535e-05
F12=3.234843142456022e-05
score=3.4936105028289694e-05
前140000行 label=1：
real
   user_id  cate  shop_id
0       11    69     3697
1       16    31     4303
2       29    75     5676
3       34    24     5545
4       37    77     4043
pred
   user_id  cate  shop_id  pred
0   768247     7     7114     0
1   421482     7      405     0
2   967737     7     7114     0
3   451713     7     7114     0
4  1303834     7     7114     0
所有用户品类中预测购买用户品类的准确率为 1.0
所有用户品类中预测购买用户品类的召回率1.2939539999353022e-05
F11=3.88176154338839e-05
所有用户品类中预测购买店铺的准确率为 1.0
所有用户品类中预测购买店铺的召回率1.9409309999029535e-05
F12=3.234843142456022e-05
score=3.4936105028289694e-05
前150000行 label=1：
real
   user_id  cate  shop_id
0       11    69     3697
1       16    31     4303
2       29    75     5676
3       34    24     5545
4       37    77     4043
pred
   user_id  cate  shop_id  pred
0   768247     7     7114     0
1   421482     7      405     0
2   967737     7     7114     0
3   451713     7     7114     0
4  1303834     7     7114     0
所有用户品类中预测购买用户品类的准确率为 1.0
所有用户品类中预测购买用户品类的召回率1.2939539999353022e-05
F11=3.88176154338839e-05
所有用户品类中预测购买店铺的准确率为 1.0
所有用户品类中预测购买店铺的召回率1.9409309999029535e-05
F12=3.234843142456022e-05
score=3.4936105028289694e-05
<< 完成测试模型
2019-05-25 19:27:51.598273
>> 开始获取特征
<< 完成获取特征
>> 开始加载模型
f384
f375
f370
f148
f281
f381
f358
f378
f364
f154
f166
f263
f269
f363
f262
f307
f268
f308
f374
f167
f149
f366
f383
f211
f377
f360
f177
f316
f193
f275
f373
f351
f312
f352
f224
f367
f239
f172
f253
f217
f194
f386
f313
f234
f218
f344
f274
f335
f311
f206
f315
f300
f309
f361
f273
f210
f184
f216
f348
f347
f223
f298
f229
f322
f333
f330
f359
f82
f345
f336
f138
f291
f321
f337
f292
f297
f241
f320
f301
f251
f304
f290
f195
f356
f385
f109
f182
f279
f289
f75
f139
f120
f369
f328
f318
f136
f326
f288
f362
f202
f355
f329
f81
f317
f235
f153
f282
f233
f341
f79
f350
f323
f267
f200
f340
f319
f349
f165
f346
f121
f115
f201
f280
f376
f63
f62
f260
f132
f338
f327
f368
f137
f83
f231
f380
f343
f293
f119
f353
f283
f258
f145
f286
f303
f176
f97
f354
f285
f196
f314
f183
f342
f264
f80
f379
f296
f140
f295
f331
f68
f339
f96
f310
f122
f159
f287
f252
f123
f250
f108
f174
f256
f382
f178
f254
f334
f332
f111
f240
f237
f222
f387
f226
f125
f302
f305
f365
f114
f180
f197
f299
f236
f306
f203
f110
f186
f259
f225
f169

Process finished with exit code 0
