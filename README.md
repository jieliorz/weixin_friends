---
title: 2017-4-4未命名文件 
tags: 新建,模板,小书匠
grammar_cjkRuby: true
---
**关于我：**
Life is short,I use Python!  
Author：zhiyinyouzhao  
Email：5251870@qq.com  
Date：April 3,2017  
**项目说明：**
该项目主要分析了微信通讯录好友的数据情况。  
安装说明：  
cd /opt  
git clone git@github.com:zhiyinyouzhao/weixin_friends.git  
cd weixin_data  
python weixin_analysisData.py  
**结果样例：**  
我们把程序结果做成简单的图标，大致是这样的。  
好友头像：  
![头像](https://github.com/zhiyinyouzhao/weixin_friends/raw/master/result_images/friends_circle.jpg)
好友性别分析：  
![性别分析](https://github.com/zhiyinyouzhao/weixin_friends/raw/master/result_images/friends.jpg)
好友全国分布：  
![全国](https://github.com/zhiyinyouzhao/weixin_friends/raw/master/result_images/friends_ChinaMap.jpg)
好友省内分布：  
![省内](https://github.com/zhiyinyouzhao/weixin_friends/raw/master/result_images/friends_Shanxi.jpg)
**个人小结：**  
1.项目用到了微信的第三方库[Itchat](http://itchat.readthedocs.io/zh/latest/)。  
2.如果想自己造轮子，那么你可能会需要urllib，urilib2，request登录[Web微信](https://wx.qq.com/)。  
3.数据制图使用的第三方工具,其中好友分布使用[地图慧](http://c.dituhui.com/),好友性别统计使用百度[ECharts](http://echarts.baidu.com/)。当然你也可以使用python matplotlib。  
4.Pandas库的安装可能会遇到一些问题，Ipython是极好的，推荐使用。  
5.有一半的时间都在同Unicode的中文乱码作斗争，在不修改list数据类型的情况下，得到中文并不是一件容易的事。  
6.数据存入csv文件不是必要的，可以将清洗后的friendslist直接拿来用。  
