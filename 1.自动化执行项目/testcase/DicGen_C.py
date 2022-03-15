import time
import unittest
from business.Login_B import Login_B
from business.DicGen_B import DicGen_B
from element.DicGen_E import DicGen_E
class DicGen_C(unittest.TestCase,Login_B,DicGen_B,DicGen_E):
	def test1Login1(self):
		self.login_businessl('admin','123456')
	def test2add_generalDic(self):
		self.add_generalDic('2','2','川藏线','999','川藏线测试','2','2','2')
	def test3search_generalDic(self):
		self.search_generalDic('川藏线','2','2','川藏线')
	def test4alter_generalDic(self):
		self.alter_generalDic('8.0','2','9998')
	def test5del_generalDic(self):
		self.del_generalDic('2','2','共 0 条')
		self.Close()
	