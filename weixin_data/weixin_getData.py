#!/usr/bin/env pythoon
#coding: utf-8


import itchat
class login_weixin(object):
	def login(self):
		itchat.auto_login()
		#登录成功，手机上的微信文件助手，会收到这条信息，用于验证是否成功
		itchat.send('Hello, filehelper', toUserName='filehelper')
	def get_friends(self):
		friendslist = itchat.get_friends(update=True)[0:]
		return friendslist
