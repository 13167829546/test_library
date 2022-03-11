import unittest,time,ddt
class Test(unittest.TestCase):  # 定义一个测试的类，并继承unittest.TestCase这个类
    @classmethod  # 装饰器，所有用例执行前执行一次
    def setUpClass(cls):
        print("start!")

    @classmethod  # 装饰器，所有用例执行后执行一次
    def tearDownClass(cls):
        time.sleep(1)
        print("end!")

    def setUp(self):  # 每条用例执行前执行一次
        print("开始")

    def tearDown(self):  # 每条用例执行后执行一次
        print("结束")

    def test01(self):  # 测试用例的名称以test开头，每条函数相当于一条测试用例
        print("执行测试用例01")
        a = 1
        b = 1
        self.assertEqual(a, b) # 判断a和b是否相等

    def test03(self):
        print("执行测试用例03")
        a = "h"
        b = "hello world!"
        self.assertIn(a, b)  # 判断a是否在b中

    def test02(self):
        print("执行测试用例02")
        a = True
        self.assertTrue(a)  # 判断a是True
unittest.main(verbosity=2)