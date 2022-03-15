from common.Logs import Log
from common.BasePage import BasePageItems
from common.File_Excel import File_Excel
class Platform_E(BasePageItems):
	BasePageItems = BasePageItems()
	def clickSysNav(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_Platform_E()
			self.BasePageItems.click_Element(self.TypeList[0],self.XpathList[0])
			Log().info("鼠标点击系统导航成功")
		except:
			Log().error("鼠标点击系统导航异常")
			raise
	def clickDataCenter(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_Platform_E()
			self.BasePageItems.click_Element(self.TypeList[1],self.XpathList[1])
			Log().info("点击供电数据共享中心成功")
		except:
			Log().error("点击供电数据共享中心异常")
			raise
	def waitSysManVisible(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_Platform_E()
			self.BasePageItems.is_visible(self.TypeList[2],self.XpathList[2])
			Log().info("等待系统管理出现成功")
		except:
			Log().error("等待系统管理出现异常")
			raise
	def clickSys(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_Platform_E()
			self.BasePageItems.click_Element(self.TypeList[2],self.XpathList[2])
			Log().info("点击系统管理成功")
		except:
			Log().error("点击系统管理异常")
			raise
	def clickPlatform(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_Platform_E()
			self.BasePageItems.click_Element(self.TypeList[3],self.XpathList[3])
			Log().info("点击平台管理成功")
		except:
			Log().error("点击平台管理异常")
			raise
	def clickAddButton(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_Platform_E()
			self.BasePageItems.click_Element(self.TypeList[4],self.XpathList[4])
			Log().info("点击添加按钮成功")
		except:
			Log().error("点击添加按钮异常")
			raise
	def sendPlatformName(self,PlatformName):
		try:
			self.XpathList,self.TypeList=File_Excel().get_Platform_E()
			self.BasePageItems.send_Element(self.TypeList[5],self.XpathList[5],PlatformName)
			Log().info("输入平台名称成功")
		except:
			Log().error("输入平台名称异常")
			raise
	def sendPlatformNo(self,PlatformNo):
		try:
			self.XpathList,self.TypeList=File_Excel().get_Platform_E()
			self.BasePageItems.send_Element(self.TypeList[6],self.XpathList[6],PlatformNo)
			Log().info("输入平台编号成功")
		except:
			Log().error("输入平台编号异常")
			raise
	def sendPlatformUrl(self,PlatformUrl):
		try:
			self.XpathList,self.TypeList=File_Excel().get_Platform_E()
			self.BasePageItems.send_Element(self.TypeList[7],self.XpathList[7],PlatformUrl)
			Log().info("输入发布地址成功")
		except:
			Log().error("输入发布地址异常")
			raise
	def sendPlatformDec(self,PlatformDec):
		try:
			self.XpathList,self.TypeList=File_Excel().get_Platform_E()
			self.BasePageItems.send_Element(self.TypeList[8],self.XpathList[8],PlatformDec)
			Log().info("输入系统描述成功")
		except:
			Log().error("输入系统描述异常")
			raise
	def clickIsStart(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_Platform_E()
			self.BasePageItems.click_Element(self.TypeList[9],self.XpathList[9])
			Log().info("点击是否启用按钮成功")
		except:
			Log().error("点击是否启用按钮异常")
			raise
	def clickSaveButton(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_Platform_E()
			self.BasePageItems.click_Element(self.TypeList[10],self.XpathList[10])
			Log().info("点击保存按钮成功")
		except:
			Log().error("点击保存按钮异常")
			raise
	def sendSearchKey(self,PlatformName):
		try:
			self.XpathList,self.TypeList=File_Excel().get_Platform_E()
			self.BasePageItems.send_Element(self.TypeList[11],self.XpathList[11],PlatformName)
			Log().info("输入查询条件成功")
		except:
			Log().error("输入查询条件异常")
			raise
	def searchButtonVisible(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_Platform_E()
			self.BasePageItems.is_visible(self.TypeList[12],self.XpathList[12])
			Log().info("等待查询按钮出现成功")
		except:
			Log().error("等待查询按钮出现异常")
			raise
	def clickSearchButton(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_Platform_E()
			self.BasePageItems.click_Element(self.TypeList[12],self.XpathList[12])
			Log().info("点击查询按钮成功")
		except:
			Log().error("点击查询按钮异常")
			raise
	def assertPlatformName(self,IsPlatformName):
		try:
			self.XpathList,self.TypeList=File_Excel().get_Platform_E()
			self.BasePageItems.TextCheck(self.TypeList[13],self.XpathList[13],IsPlatformName)
			Log().info("验证平台名称成功")
		except:
			Log().error("验证平台名称异常")
			raise
	def clickAlterButton(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_Platform_E()
			self.BasePageItems.click_Element(self.TypeList[15],self.XpathList[15])
			Log().info("点击修改按钮成功")
		except:
			Log().error("点击修改按钮异常")
			raise
	def alterPlatformName(self,PlatformName):
		try:
			self.XpathList,self.TypeList=File_Excel().get_Platform_E()
			self.BasePageItems.send_Element(self.TypeList[7],self.XpathList[7],PlatformName)
			Log().info("修改平台发布地址成功")
		except:
			Log().error("修改平台发布地址异常")
			raise
	def clickSaveButton(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_Platform_E()
			self.BasePageItems.click_Element(self.TypeList[10],self.XpathList[10])
			Log().info("点击保存按钮成功")
		except:
			Log().error("点击保存按钮异常")
			raise
	def assertPlatformUrl(self,IsPlatformUrl):
		try:
			self.XpathList,self.TypeList=File_Excel().get_Platform_E()
			self.BasePageItems.TextCheck(self.TypeList[14],self.XpathList[14],IsPlatformUrl)
			Log().info("验证平台发布地址成功")
		except:
			Log().error("验证平台发布地址异常")
			raise
	def clickDelButton(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_Platform_E()
			self.BasePageItems.click_Element(self.TypeList[16],self.XpathList[16])
			Log().info("点击删除按钮成功")
		except:
			Log().error("点击删除按钮异常")
			raise
	def clickConfirmButton(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_Platform_E()
			self.BasePageItems.click_Element(self.TypeList[17],self.XpathList[17])
			Log().info("点击删除确认按钮成功")
		except:
			Log().error("点击删除确认按钮异常")
			raise
	def WaitTime(self,sleepTime):
		try:
			self.XpathList,self.TypeList=File_Excel().get_Platform_E()
			self.BasePageItems.Sleep(sleepTime)
			Log().info("等待时间成功")
		except:
			Log().error("等待时间异常")
			raise
	def Close(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_Platform_E()
			self.BasePageItems.Closebrowser()
			Log().info("关闭浏览器成功")
		except:
			Log().error("关闭浏览器异常")
			raise
	