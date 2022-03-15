import time
import unittest
from business.Login_B import Login_B
from business.DicType_B import DicType_B
from element.DicType_E import DicType_E
class DicType_C(unittest.TestCase,Login_B,DicType_B,DicType_E):
	def test1Login1(self):
		self.login_businessl('admin','123456')
	def test2add_DicType(self):
		self.add_DicType('2','2','test','export','testdec','2')
	def test3search_DicType(self):
		self.search_DicType('test','2','2','test','export','testdec')
	def test4alter_DicType(self):
		self.alter_DicType('export-test','2','testexport-test')
	def test5del_DicType(self):
		self.del_DicType('2','2','共 0 条')
		self.Close()
	