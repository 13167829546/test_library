from common.Logs import Log
from common.BasePage import BasePageItems
from common.File_Excel import File_Excel
class App_E(BasePageItems):
	BasePageItems = BasePageItems()
	def clickSysNav(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_App_E()
			self.BasePageItems.click_Element(self.TypeList[0],self.XpathList[0])
			Log().info("鼠标点击系统导航成功")
		except:
			Log().error("鼠标点击系统导航异常")
			raise
	def clickDataCenter(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_App_E()
			self.BasePageItems.click_Element(self.TypeList[1],self.XpathList[1])
			Log().info("点击供电数据共享中心成功")
		except:
			Log().error("点击供电数据共享中心异常")
			raise
	def waitSysManVisible(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_App_E()
			self.BasePageItems.is_visible(self.TypeList[2],self.XpathList[2])
			Log().info("等待系统管理出现成功")
		except:
			Log().error("等待系统管理出现异常")
			raise
	def clickSys(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_App_E()
			self.BasePageItems.click_Element(self.TypeList[2],self.XpathList[2])
			Log().info("点击系统管理成功")
		except:
			Log().error("点击系统管理异常")
			raise
	def clickApp(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_App_E()
			self.BasePageItems.click_Element(self.TypeList[3],self.XpathList[3])
			Log().info("点击应用管理成功")
		except:
			Log().error("点击应用管理异常")
			raise
	def clickAddButton(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_App_E()
			self.BasePageItems.click_Element(self.TypeList[4],self.XpathList[4])
			Log().info("点击添加按钮成功")
		except:
			Log().error("点击添加按钮异常")
			raise
	def sendAppName(self,AppName):
		try:
			self.XpathList,self.TypeList=File_Excel().get_App_E()
			self.BasePageItems.send_Element(self.TypeList[5],self.XpathList[5],AppName)
			Log().info("输入应用名称成功")
		except:
			Log().error("输入应用名称异常")
			raise
	def sendAppNo(self,AppNo):
		try:
			self.XpathList,self.TypeList=File_Excel().get_App_E()
			self.BasePageItems.send_Element(self.TypeList[6],self.XpathList[6],AppNo)
			Log().info("输入应用编号成功")
		except:
			Log().error("输入应用编号异常")
			raise
	def clickAppType(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_App_E()
			self.BasePageItems.click_Element(self.TypeList[7],self.XpathList[7])
			Log().info("点击所属平台成功")
		except:
			Log().error("点击所属平台异常")
			raise
	def clickAppTypeValue(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_App_E()
			self.BasePageItems.click_Element(self.TypeList[8],self.XpathList[8])
			Log().info("选择所属平台选项成功")
		except:
			Log().error("选择所属平台选项异常")
			raise
	def sendAppVersion(self,AppVersion):
		try:
			self.XpathList,self.TypeList=File_Excel().get_App_E()
			self.BasePageItems.send_Element(self.TypeList[9],self.XpathList[9],AppVersion)
			Log().info("输入版本号成功")
		except:
			Log().error("输入版本号异常")
			raise
	def sendClientID(self,ClientID):
		try:
			self.XpathList,self.TypeList=File_Excel().get_App_E()
			self.BasePageItems.send_Element(self.TypeList[10],self.XpathList[10],ClientID)
			Log().info("输入客户端ID成功")
		except:
			Log().error("输入客户端ID异常")
			raise
	def sendClientURL(self,ClientURL):
		try:
			self.XpathList,self.TypeList=File_Excel().get_App_E()
			self.BasePageItems.send_Element(self.TypeList[11],self.XpathList[11],ClientURL)
			Log().info("输入客户端跳转地址成功")
		except:
			Log().error("输入客户端跳转地址异常")
			raise
	def clickSaveButton(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_App_E()
			self.BasePageItems.click_Element(self.TypeList[13],self.XpathList[13])
			Log().info("点击保存按钮成功")
		except:
			Log().error("点击保存按钮异常")
			raise
	def sendSearchKey(self,AppName):
		try:
			self.XpathList,self.TypeList=File_Excel().get_App_E()
			self.BasePageItems.send_Element(self.TypeList[14],self.XpathList[14],AppName)
			Log().info("输入查询条件成功")
		except:
			Log().error("输入查询条件异常")
			raise
	def searchButtonVisible(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_App_E()
			self.BasePageItems.is_visible(self.TypeList[15],self.XpathList[15])
			Log().info("等待查询按钮出现成功")
		except:
			Log().error("等待查询按钮出现异常")
			raise
	def clickSearchButton(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_App_E()
			self.BasePageItems.click_Element(self.TypeList[15],self.XpathList[15])
			Log().info("点击查询按钮成功")
		except:
			Log().error("点击查询按钮异常")
			raise
	def assertAppName(self,IsAppName):
		try:
			self.XpathList,self.TypeList=File_Excel().get_App_E()
			self.BasePageItems.TextCheck(self.TypeList[16],self.XpathList[16],IsAppName)
			Log().info("验证应用名称成功")
		except:
			Log().error("验证应用名称异常")
			raise
	def clickAlterButton(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_App_E()
			self.BasePageItems.click_Element(self.TypeList[18],self.XpathList[18])
			Log().info("点击修改按钮成功")
		except:
			Log().error("点击修改按钮异常")
			raise
	def clearClientURL(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_App_E()
			self.BasePageItems.clear_Element(self.TypeList[11],self.XpathList[11])
			Log().info("清空应用跳转地址成功")
		except:
			Log().error("清空应用跳转地址异常")
			raise
	def alterClientURL(self,AppClientURL):
		try:
			self.XpathList,self.TypeList=File_Excel().get_App_E()
			self.BasePageItems.send_Element(self.TypeList[11],self.XpathList[11],AppClientURL)
			Log().info("修改应用跳转地址成功")
		except:
			Log().error("修改应用跳转地址异常")
			raise
	def clickSaveButton(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_App_E()
			self.BasePageItems.click_Element(self.TypeList[13],self.XpathList[13])
			Log().info("点击保存按钮成功")
		except:
			Log().error("点击保存按钮异常")
			raise
	def assertAppClientURL(self,IsAppClientURL):
		try:
			self.XpathList,self.TypeList=File_Excel().get_App_E()
			self.BasePageItems.TextCheck(self.TypeList[11],self.XpathList[11],IsAppClientURL)
			Log().info("验证应用跳转地址成功")
		except:
			Log().error("验证应用跳转地址异常")
			raise
	def clickDelButton(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_App_E()
			self.BasePageItems.click_Element(self.TypeList[19],self.XpathList[19])
			Log().info("点击删除按钮成功")
		except:
			Log().error("点击删除按钮异常")
			raise
	def clickConfirmButton(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_App_E()
			self.BasePageItems.click_Element(self.TypeList[20],self.XpathList[20])
			Log().info("点击删除确认按钮成功")
		except:
			Log().error("点击删除确认按钮异常")
			raise
	def WaitTime(self,sleepTime):
		try:
			self.XpathList,self.TypeList=File_Excel().get_App_E()
			self.BasePageItems.Sleep(sleepTime)
			Log().info("等待时间成功")
		except:
			Log().error("等待时间异常")
			raise
	def Close(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_App_E()
			self.BasePageItems.Closebrowser()
			Log().info("关闭浏览器成功")
		except:
			Log().error("关闭浏览器异常")
			raise
	