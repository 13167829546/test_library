from element.Login_E import Login_E
from time import sleep
from element.FirstPage_E import FirstPage_E
from common.Logs import Log
from common.File_Excel import File_Excel
class Login_B(Login_E, FirstPage_E):
	def 	login_businessl(self,username,password,check_code=0):
		list = ["牵引作业系统自动化.xls", "登录"]
		self.OpenThebrowser(list)
		self.InputUser(list,username)
		self.InputPassword(list,password)
		#输入验证码

		for i in range(50):
			if check_code == 0:
				self.clickLog(list,3)
				break
			try:
				# 获得验证码
				self.save_code_picture(list,4)
				code = self.check_code()
				if code =="":
					code="null"
				#输入验证码并登录
				self.clear(list, 5)
				self.send(list,5,code)
				#sleep(1)
				self.clickLog(list,3)
				result = self.position(list,6)
				if  result == True:
					break
			except:
				self.clickLog(list,4)
				if i == 49:
					Log().error("验证码识别%s次，未识别成功"%(i+1))
				continue

	