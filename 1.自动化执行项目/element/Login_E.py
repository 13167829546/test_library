from common.Logs import Log
from common.BasePage import BasePageItems
from common.File_Excel import File_Excel
from time import sleep
class Login_E(BasePageItems):
	BasePageItems = BasePageItems()
	def OpenThebrowser(self,list):
		try:
			self.XpathList,self.TypeList=File_Excel().get_excel(list)
			self.BasePageItems.OpenThebrowser(self.TypeList[0],self.XpathList[0])
			Log().info("打开浏览器成功")
		except:
			Log().error("打开浏览器异常")
			raise

	def InputUser(self,list,User):
		try:
			self.XpathList,self.TypeList=File_Excel().get_excel(list)
			self.BasePageItems.send_Element(self.TypeList[1],self.XpathList[1],User)
			Log().info("输入账号成功")
		except:
			Log().error("输入账号异常")
			raise

	def InputPassword(self,list,password):
		try:
			self.XpathList,self.TypeList=File_Excel().get_excel(list)
			self.BasePageItems.send_Element(self.TypeList[2],self.XpathList[2],password)
			Log().info("输入密码成功")
		except:
			Log().error("输入密码异常")
			raise

	def clickLog(self,list,num):
		sleep(1)
		try:
			self.XpathList,self.TypeList=File_Excel().get_excel(list)
			self.BasePageItems.click_Element(self.TypeList[num],self.XpathList[num])
			Log().info("点击登陆成功")
		except:
			Log().error("点击登陆异常")
			raise

	def waitSysNavVisible(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_Login_E()
			self.BasePageItems.is_visible(self.TypeList[4],self.XpathList[4])
			Log().info("等待系统导航出现成功")
		except:
			Log().error("等待系统导航出现异常")
			raise
	def Close(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_Login_E()
			self.BasePageItems.Closebrowser()
			Log().info("关闭浏览器成功")
		except:
			Log().error("关闭浏览器异常")
			raise

	def SHouldText(self,TextOne):
		try:
			self.XpathList,self.TypeList=File_Excel().get_Login_E()
			self.BasePageItems.TextCheck(self.TypeList[4],self.XpathList[4],TextOne)
			Log().info("文本是否一样成功")
		except:
			Log().error("文本是否一样异常")
			raise

	def WaitTime(self,Time):
		try:
			self.XpathList,self.TypeList=File_Excel().get_Login_E()
			self.BasePageItems.Sleep(Time)
			Log().info("Sleep一下成功")
		except:
			Log().error("Sleep一下异常")
			raise
