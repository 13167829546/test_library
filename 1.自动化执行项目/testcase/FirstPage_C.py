import time
import unittest
from business.Login_B import Login_B
from element.FirstPage_E import FirstPage_E
class FirstPage_C(unittest.TestCase,Login_B,FirstPage_E):
	def testFirstPage1(self):
		list = ["牵引作业系统自动化.xls", "test"]
		self.login_businessl('测试1','##￥124567aaa',1)
		self.click(list,0)
		#点击区间车订单
		self.click(list,1)
		#输入订单号
		self.switch_frame(list,2)
		self.send(list,3,"PC1468789474970144768")
		#点击查询
		self.click(list, 4)

	# def test_finish(self):
	# 	self.finish_driver()