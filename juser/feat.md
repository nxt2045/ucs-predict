```txt
2019-05-23 22:40:19.277495
>> 开始生成特征(X,y)
end_date 2018-4-8
2019-05-23 22:40:19.279488
> 开始生成标签
user_buy_amt_180409_180415.csv
真实购买 (160044, 2)
shape (1602150, 2)
cols Index(['user_id', 'label'], dtype='object')
head
   user_id  label
0        1      0
1        2      1
2        3      0
3        4      0
4        5      0
tail
         user_id  label
1602145  1608703      0
1602146  1608704      0
1602147  1608705      0
1602148  1608706      0
1602149  1608707      0
2019-05-23 22:40:20.165119
> 开始生成特征 gap=1
user_view_amt_180408_180408.csv
user_buy_amt_180408_180408.csv
user_follow_amt_180408_180408.csv
user_remark_amt_180408_180408.csv
user_cart_amt_180408_180408.csv
   1_user_view_amt  1_user_buy_amt  1_user_follow_amt  1_user_remark_amt  1_user_cart_amt
0                0               0                  0                  0                0
1                0               0                  0                  0                0
2                0               0                  0                  0                0
3                0               0                  0                  0                0
4                0               0                  0                  0                0
2019-05-23 22:40:23.961926
> 开始生成特征 gap=2
user_view_amt_180407_180408.csv
user_buy_amt_180407_180408.csv
user_follow_amt_180407_180408.csv
user_remark_amt_180407_180408.csv
user_cart_amt_180407_180408.csv
   2_user_view_amt  2_user_buy_amt  2_user_follow_amt  2_user_remark_amt  2_user_cart_amt
0                0               0                  0                  0                0
1                8               0                  0                  0                0
2                0               0                  0                  0                0
3                0               0                  0                  0                0
4                0               0                  0                  0                0
2019-05-23 22:40:26.333579
> 开始生成特征 gap=3
user_view_amt_180406_180408.csv
user_buy_amt_180406_180408.csv
user_follow_amt_180406_180408.csv
user_remark_amt_180406_180408.csv
user_cart_amt_180406_180408.csv
   3_user_view_amt  3_user_buy_amt  3_user_follow_amt  3_user_remark_amt  3_user_cart_amt
0                0               0                  0                  0                0
1                9               0                  0                  0                0
2                0               0                  0                  0                0
3                1               0                  0                  1                0
4                0               0                  0                  0                0
2019-05-23 22:40:28.766072
> 开始生成特征 gap=7
user_view_amt_180402_180408.csv
user_buy_amt_180402_180408.csv
user_follow_amt_180402_180408.csv
user_remark_amt_180402_180408.csv
user_cart_amt_180402_180408.csv
   7_user_view_amt  7_user_buy_amt  7_user_follow_amt  7_user_remark_amt  7_user_cart_amt
0                0               0                  0                  0                0
1               23               0                  0                  0                0
2                0               0                  0                  0                0
3                5               0                  0                  1                0
4                0               0                  0                  0                0
2019-05-23 22:40:31.172670
> 开始生成特征 gap=14
user_view_amt_180326_180408.csv
user_buy_amt_180326_180408.csv
user_follow_amt_180326_180408.csv
user_remark_amt_180326_180408.csv
user_cart_amt_180326_180408.csv
   14_user_view_amt  14_user_buy_amt  14_user_follow_amt  14_user_remark_amt  14_user_cart_amt
0                29                0                   0                   0                 0
1                27                0                   0                   3                 0
2                 0                0                   0                   0                 0
3                10                0                   0                   1                 0
4                 0                0                   0                   0                 0
2019-05-23 22:40:33.900397
> 生成全局特征
user.csv
user_view_amt_180310_180408.csv
user_buy_amt_180310_180408.csv
user_follow_amt_180310_180408.csv
user_remark_amt_180310_180408.csv
user_cart_amt_180310_180408.csv
user_action_ratio_180310_180408.csv
   user_id  label  1_user_view_amt  1_user_buy_amt  1_user_follow_amt  1_user_remark_amt  1_user_cart_amt  2_user_view_amt  2_user_buy_amt  2_user_follow_amt  2_user_remark_amt  2_user_cart_amt  3_user_view_amt  3_user_buy_amt  3_user_follow_amt  3_user_remark_amt  3_user_cart_amt  7_user_view_amt  7_user_buy_amt  7_user_follow_amt  7_user_remark_amt  7_user_cart_amt  14_user_view_amt  14_user_buy_amt  14_user_follow_amt  14_user_remark_amt  14_user_cart_amt  age  sex  user_lv_cd  city_level  province  city  county  user_reg_month  user_reg_cate  user_view_amt  user_buy_amt  user_follow_amt  user_remark_amt  user_cart_amt  user_buy/view  user_buy/follow  user_buy/remark  user_buy/cart
0        1      0                0               0                  0                  0                0                0               0                  0                  0                0                0               0                  0                  0                0                0               0                  0                  0                0                29                0                   0                   0                 0    5    1           7           5        20   176    1933              37              5             30             1                0                0              0              3             -100             -100           -100
1        2      1                0               0                  0                  0                0                8               0                  0                  0                0                9               0                  0                  0                0               23               0                  0                  0                0                27                0                   0                   3                 0    4    1           1           3        20   119     187              36              5            261             1                0                4              1              0             -100               25            100
2        3      0                0               0                  0                  0                0                0               0                  0                  0                0                0               0                  0                  0                0                0               0                  0                  0                0                 0                0                   0                   0                 0    6    0           1           1        26     4    2723              39              5              0             1                0                0              0           -100             -100             -100           -100
3        4      0                0               0                  0                  0                0                0               0                  0                  0                0                1               0                  0                  1                0                5               0                  0                  1                0                10                0                   0                   1                 0    6    1           7           4        20   120     741              73              6             79             1                1                4              4              1              100               25             25
4        5      0                0               0                  0                  0                0                0               0                  0                  0                0                0               0                  0                  0                0                0               0                  0                  0                0                 0                0                   0                   0                 0    4    0           6           4        20   120     741               2              1              0             1                0                0              0           -100             -100             -100           -100
2019-05-23 22:41:36.542762

```