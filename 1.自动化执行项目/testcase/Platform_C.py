import time
import unittest
from business.Login_B import Login_B
from business.Platform_B import Platform_B
from element.Platform_E import Platform_E
class Platform_C(unittest.TestCase,Login_B,Platform_B,Platform_E):
	def test1Login1(self):
		self.login_businessl('admin','123456')
	def test2add_Platform(self):
		self.add_Platform('2','2','新浪','A110','https://www.sina.com.cn/','新浪,新浪网,SINA,sina,sina.com.cn,新浪首页,门户,资讯','2','2')
	def test3search_Platform(self):
		self.search_Platform('新浪','2','2','新浪')
	def test4alter_Platform(self):
		self.alter_Platform('login','2','https://www.sina.com.cn/login')
	def test5del_Platform(self):
		self.del_Platform('2','2')
		self.Close()
	