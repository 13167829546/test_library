import time
import unittest
from business.Login_B import Login_B
from business.Dic_B import Dic_B
from element.Dic_E import Dic_E
class Dic_C(unittest.TestCase,Login_B,Dic_B,Dic_E):
	def testLogin1(self):
		self.login_businessl('admin','123456')
	def testadd_generalDic(self):
		self.add_generalDic('导出','export','testdec')
	def testsearch_generalDic(self):
		self.search_generalDic('导出','导出')
	def testalter_generalDic(self):
		self.alter_generalDic('export-test','export-test')
	def testdel_generalDic(self):
		self.del_generalDic('共 0 条')
	