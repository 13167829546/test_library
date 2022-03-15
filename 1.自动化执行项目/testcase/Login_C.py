import time
import unittest
from business.Login_B import Login_B
from element.Login_E import Login_E
class Login_C(unittest.TestCase,Login_B,Login_E):
	def testLogin1(self):
		self.login_businessl('admin','Cdtye_2019@')
		self.Close()
	