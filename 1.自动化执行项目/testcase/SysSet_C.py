import time
import unittest
from business.Login_B import Login_B
from business.SysSet_B import SysSet_B
from element.SysSet_E import SysSet_E
class SysSet_C(unittest.TestCase,Login_B,SysSet_B,SysSet_E):
	def test1Login1(self):
		self.login_businessl('admin','123456')
	def test2add_SysSet(self):
		self.add_SysSet('2','系统级别','2','SystemLevel','段','标识该系统是段级还是局级','2','2')
	def test3search_SysSet(self):
		self.search_SysSet('级别','2','2','系统级别')
	def test4alter_SysSet(self):
		self.alter_SysSet('SystemLevel1','SystemLevel1')
	def test5del_SysSet(self):
		self.del_SysSet('2','2','共 0 条')
		self.Close()
	