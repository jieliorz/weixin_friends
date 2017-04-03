#!/usr/bin/env python
#coding: utf-8

import pandas as pd
import re
import codecs
import itchat
import csv
import os
from weixin_getData import login_weixin
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class friends_analysis(object):
	def friends_information(self):
		l = login_weixin()
		l.login()
		friends =  l.get_friends()
		friendsCount = len(friends)
		print (u'通讯录共%s位好友' % friendsCount)
		num = 1
		friend_info = []
		index = 1
		
		for friend in friends[0:]:
			#下载头像
			print (u"正在下载第:%d位好友头像" % num)
			img = itchat.get_head_img(userName=friend["UserName"])
			filepath = os.path.dirname(os.path.abspath(__file__))
			filename = filepath+'/friends_head_img/'
			imgName = filename+str(num)+'.jpg'
			fileImage = open(imgName,'wb')
			fileImage.write(img)
			fileImage.close()
			num += 1
			
			# 读取昵称，微信号，城市，性别，星标好友，个性签名，备注等信息
			
			nickname = friend['NickName']
			if nickname == '':
				nickname = 'nonick'
			else :
				nickname
			account = friend['Alias']
			if account == '':
				account = 'noalias'
			else:
				account
			city = friend['City']
			if city == '':
				city = 'nocity'
			else:
				city
			signature = friend['Signature']
			if signature == '':
				signature = 'nosign'
			else:
				signature
			remark = friend['RemarkName']
			if remark == '':
				remark = 'noremark'
			else:
				remark
			
			a = (index,nickname,account,city,friend['Sex'],friend['StarFriend'],signature,remark)
			index += 1
			friend_info.append(a)
		#b = str(friend_info).replace('u\'','\'')
		#info =  b.decode("unicode-escape")
		#将每个好友的信息写入csv文件
		return friend_info
		#c = friends_analysis()
		#c.friends_toCsv(friend_info)
	
	def friends_toCsv(self,info):
		filepath = os.path.dirname(os.path.abspath(__file__))
		filename = filepath+'/friends.csv'
		csvfile = file(filename, 'wb')
		csvfile.write(codecs.BOM_UTF8)
		writer = csv.writer(csvfile)
		writer.writerow([u'编号', u'昵称', u'微信号',u'城市',u'性别',u'星标好友',u'签名',u'备注'])
		data = info
		writer.writerows(data)
		csvfile.close()

class friends_census(object):
	#朋友城市
	def city(self):
		city = df['城市'].value_counts()
		print city
	#朋友性别，1:男，2:女，3:未知
	def gender(self):
		gender = df['性别'].value_counts()
		print gender
	#星标好友，1:星标，2：非星标
	def star(self):
		star = df['星标好友'].value_counts()
		print star
	#备注名
	def remark(self):
		remark = df['备注'].value_counts()
		print remark
	#昵称分析,count:中文昵称数目
	def nickname(self):
		nickname = df['昵称']
		string = u"^[\u4e00-\u9fa5]+(·[\u4e00-\u9fa5]+)*$"
		pattern = re.compile(string)
		count = 0
		malecount = 0
		femalecount = 0
		count1 = 0
		malecount1 = 0
		femalecount1 = 0
		for i in range(0,len(nickname)):
			match = pattern.match(str(nickname[i].strip()).decode('utf-8')) 
			if match:
				count += 1
				f = friends_census()
				if f.judgeGender(i) == 'male':
					malecount += 1
				if f.judgeGender(i) == 'female':
					femalecount += 1
			else:
				count1 += 1
				c = friends_census()
				if c.judgeGender(i) == 'male':
					malecount1 += 1
				if c.judgeGender(i) == 'female':
					femalecount1 += 1
		print '中文昵称好友:%d' % count
		print '中文昵称男好友:%d' % malecount
		print '中文昵称女好友:%d' % femalecount
		print '非中文昵称男好友:%d' % malecount1
		print '非中文昵称女好友:%d' % femalecount1
	def judgeGender(self,index):
		gender = df['性别']
		if gender[index] == 1:
			return 'male'
		elif gender[index] == 2:
			return 'female'
		else:
			return 'unknown' 
		

if __name__ == '__main__':
	fr = friends_analysis()
	result = fr.friends_information()
	fr.friends_toCsv(result)
	filepath = os.path.dirname(os.path.abspath(__file__))
	filename = filepath+'/friends.csv'
	df = pd.read_csv(filename)
	f = friends_census()
	f.city()
	f.gender()
	f.star()
	f.remark()
	f.nickname()

