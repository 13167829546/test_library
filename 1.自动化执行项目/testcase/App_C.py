import time
import unittest
from business.Login_B import Login_B
from business.App_B import App_B
from element.App_E import App_E
class App_C(unittest.TestCase,Login_B,App_B,App_E):
	def test1Login1(self):
		self.login_businessl('admin','123456')
	def test2add_App(self):
		self.add_App('2','系统级别','2','SystemLevel','段','标识该系统是段级还是局级','2','2')
	def test3search_App(self):
		self.search_App('级别','2','2','系统级别')
	def test4alter_App(self):
		self.alter_App('SystemLevel1','SystemLevel1')
	def test5del_App(self):
		self.del_App('2','2','共 0 条')
		self.Close()