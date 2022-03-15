import time
import unittest
import HTMLTestRunner_cn
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
#jenkins自动化构建用一下
curPath = 'C:\\Users\\huwo\\.jenkins\\workspace\\测试\\1.自动化执行项目\\testcase'
rootPath = 'C:\\Users\\huwo\\.jenkins\\workspace\\测试\\1.自动化执行项目'
sys.path.append(rootPath)
from common.FilePath import FilePath
from testcase.Login_C import Login_C
from testcase.FirstPage_C import FirstPage_C
def run():
	datePath = FilePath().get_File_Path('reportPath')
	suite0 = unittest.TestLoader().loadTestsFromTestCase(Login_C)
	suite1 = unittest.TestLoader().loadTestsFromTestCase(FirstPage_C)
	suite = unittest.TestSuite([suite1])
	fp = open(datePath, 'wb')
	runner = HTMLTestRunner_cn.HTMLTestRunner(stream=fp, title='自动化测试报告', description='测试')
	runner.run(suite)
	time.sleep(3)
	fp.close()  # 关闭报告文件
if __name__ == '__main__':
	run()
