import time
import unittest
from business.Login_B import Login_B
from business.Menu_B import Menu_B
from element.Menu_E import Menu_E
class Menu_C(unittest.TestCase,Login_B,Menu_B,Menu_E):
	def test1Login1(self):
		self.login_businessl('admin','123456')
	def test2add_Menu(self):
		self.add_Menu('2','系统级别','2','SystemLevel','段','标识该系统是段级还是局级','2','2')
	def test3search_Menu(self):
		self.search_Menu('级别','2','2','系统级别')
	def test4alter_Menu(self):
		self.alter_Menu('SystemLevel1','SystemLevel1')
	def test5del_Menu(self):
		self.del_Menu('2','2','共 0 条')
		self.Close()
	