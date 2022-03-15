import time
import unittest
from business.Login_B import Login_B
from business.Dept_B import Dept_B
from element.Dept_E import Dept_E
class Dept_C(unittest.TestCase,Login_B,Dept_B,Dept_E):
	def test1Login1(self):
		self.login_businessl('admin','123456')
	def test2add_Dept(self):
		self.add_Dept('2','2','接触网检修车间','2','广州供电段','2','1111','接触网检修车间','王小海','2','2')
	def test3search_Dept(self):
		self.search_Dept('接触网检修车间','2','2','接触网检修车间')
	def test4alter_Dept(self):
		self.alter_Dept('接触网检修车间1','2','接触网检修车间1')
	def test5del_Dept(self):
		self.del_Dept('2','2')
		self.Close()
	