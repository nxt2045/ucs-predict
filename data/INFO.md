## 0 文件
分隔符：逗号，字符编码：utf-8
行为表:jdata_action
用户表:jdata_user
店铺表:jdata_shop
商品表::jdata_product
评论表:jdata_comment

## 1 评分

参赛者提交的结果文件中包含对所有用户购买意向的预测结果。对每一个用户的预测结果包括两方面：    

1. 该用户2018-04-16到2018-04-22是否对品类有购买，提交的结果文件中仅包含预测为下单的用户和品类（预测为未下单的用户和品类无须在结果中出现）。评测时将对提交结果中重复的“用户-品类”做排重处理，若预测正确，则评测算法中置label=1，不正确label=0。

2. 如果用户对品类有购买，还需要预测对该品类下哪个店铺有购买，若店铺预测正确，则评测算法中置pred=1，不正确pred=0。
对于参赛者提交的结果文件，按如下公式计算得分：score=0.4 F11 +0.6 F12    
此处的F1值定义为：      
![upfile](https://img30.360buyimg.com/img/jfs/t1/31376/19/11155/9346/5cb3f143E00446b31/4c9c697ff32863ba.png)    
其中：Precise为准确率，Recall为召回率；F11 是label=1或0的F1值，F12 是pred=1或0的F1值。

## 2 赛题数据

### 2.1 训练数据    
提供2018-02-01到2018-04-15用户集合U中的用户，对商品集合S中部分商品的行为、评价、用户数据。

### 2.2 预测数据    
提供2018-04-16到2018-04-22预测用户U对哪些品类和店铺有购买，用户对品类下的店铺只会购买一次。

### 2.3 数据表说明    
![upfile](https://img30.360buyimg.com/img/jfs/t1/40477/10/154/22847/5cc0f9d5Ea5384d90/47fa7d3c9e716bdc.png)    
温馨提示：如需下载赛题数据，请先登录并完成报名参赛。

1. 用户数据（jdata_user）     
![upfile](https://img30.360buyimg.com/img/jfs/t1/39786/9/3409/20079/5cc5127bE6a7b600f/455d400b45340acb.png)    

2. 商品数据（jdata_product）    
![upfile](https://img30.360buyimg.com/img/jfs/t1/35486/39/1595/13140/5cb3f32fE031c1097/5f755655f8f04b9d.png)    

3. 评论数据（jdata_comment）   
![upfile](https://img30.360buyimg.com/img/jfs/t1/29102/7/11323/13160/5c8f67ccE19fae655/f9c20e5e7a081bb7.png)    

4. 行为数据（jdata_action）   
![upfile](https://img30.360buyimg.com/img/jfs/t1/29115/12/11325/20616/5c8f67f7E8a50fa4d/86d3150ed8531ba6.png)    

5. 商家店铺数据（jdata_shop）    
![upfile](https://img30.360buyimg.com/img/jfs/t1/25892/4/11318/17058/5c8f6770E1935911b/f42b9c036885a4c9.png)    


## 3 任务描述及作品要求

### 3.1 任务描述
对于训练集中出现的每一个用户，参赛者的模型需要预测该用户在未来7天内对某个目标品类下某个店铺的购买意向。

### 3.2 作品要求
提交的CSV文件要求如下：
1. UTF-8无BOM格式编码；
2. 第一行为字段名，即：user_id,cate,shop_id（数据使用英文逗号分隔）
其中：user_id：用户表（jdata_user ）中用户ID；cate：商品表（jdata_product）中商品sku_id对应的品类cate ；shop_id：商家表（jdata_shop）中店铺ID；
3. 结果不存在重复的记录行数，否则无效；
对于预测出没有购买意向的用户，在提交的CSV文件中不要包含该用户的信息。
提交结果示例如下图：      
![upfile](https://img30.360buyimg.com/img/jfs/t1/36264/7/1799/2752/5cb43b54E3ba0ba72/7c87da10ffb98407.png)