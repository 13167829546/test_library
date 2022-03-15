from common.Logs import Log
from common.BasePage import BasePageItems
from common.File_Excel import File_Excel
class SysSet_E(BasePageItems):
	BasePageItems = BasePageItems()
	def clickSysNav(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_SysSet_E()
			self.BasePageItems.click_Element(self.TypeList[0],self.XpathList[0])
			Log().info("鼠标点击系统导航成功")
		except:
			Log().error("鼠标点击系统导航异常")
			raise
	def clickDataCenter(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_SysSet_E()
			self.BasePageItems.click_Element(self.TypeList[1],self.XpathList[1])
			Log().info("点击供电数据共享中心成功")
		except:
			Log().error("点击供电数据共享中心异常")
			raise
	def waitSysManVisible(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_SysSet_E()
			self.BasePageItems.is_visible(self.TypeList[2],self.XpathList[2])
			Log().info("等待系统管理出现成功")
		except:
			Log().error("等待系统管理出现异常")
			raise
	def clickSys(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_SysSet_E()
			self.BasePageItems.click_Element(self.TypeList[2],self.XpathList[2])
			Log().info("点击系统管理成功")
		except:
			Log().error("点击系统管理异常")
			raise
	def clickSysSet(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_SysSet_E()
			self.BasePageItems.click_Element(self.TypeList[3],self.XpathList[3])
			Log().info("点击系统参数成功")
		except:
			Log().error("点击系统参数异常")
			raise
	def clickAddButton(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_SysSet_E()
			self.BasePageItems.click_Element(self.TypeList[4],self.XpathList[4])
			Log().info("点击添加按钮成功")
		except:
			Log().error("点击添加按钮异常")
			raise
	def sendSysSetName(self,SysSetName):
		try:
			self.XpathList,self.TypeList=File_Excel().get_SysSet_E()
			self.BasePageItems.send_Element(self.TypeList[5],self.XpathList[5],SysSetName)
			Log().info("输入配置名称成功")
		except:
			Log().error("输入配置名称异常")
			raise
	def sendSysSetType(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_SysSet_E()
			self.BasePageItems.click_Element(self.TypeList[6],self.XpathList[6])
			Log().info("点击配置类型成功")
		except:
			Log().error("点击配置类型异常")
			raise
	def sendSysSetTypeValue(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_SysSet_E()
			self.BasePageItems.click_Element(self.TypeList[7],self.XpathList[7])
			Log().info("选择配置类型选项成功")
		except:
			Log().error("选择配置类型选项异常")
			raise
	def sendSysSetNo(self,SysSetNo):
		try:
			self.XpathList,self.TypeList=File_Excel().get_SysSet_E()
			self.BasePageItems.send_Element(self.TypeList[8],self.XpathList[8],SysSetNo)
			Log().info("输入配置编号成功")
		except:
			Log().error("输入配置编号异常")
			raise
	def sendSysSetValue(self,SysSetValue):
		try:
			self.XpathList,self.TypeList=File_Excel().get_SysSet_E()
			self.BasePageItems.send_Element(self.TypeList[9],self.XpathList[9],SysSetValue)
			Log().info("输入配置值成功")
		except:
			Log().error("输入配置值异常")
			raise
	def sendSysSetDec(self,SysSetDec):
		try:
			self.XpathList,self.TypeList=File_Excel().get_SysSet_E()
			self.BasePageItems.send_Element(self.TypeList[10],self.XpathList[10],SysSetDec)
			Log().info("输入描述成功")
		except:
			Log().error("输入描述异常")
			raise
	def clickSaveButton(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_SysSet_E()
			self.BasePageItems.click_Element(self.TypeList[12],self.XpathList[12])
			Log().info("点击保存按钮成功")
		except:
			Log().error("点击保存按钮异常")
			raise
	def sendSearchKey(self,SysSetName):
		try:
			self.XpathList,self.TypeList=File_Excel().get_SysSet_E()
			self.BasePageItems.send_Element(self.TypeList[15],self.XpathList[15],SysSetName)
			Log().info("输入查询条件成功")
		except:
			Log().error("输入查询条件异常")
			raise
	def searchButtonVisible(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_SysSet_E()
			self.BasePageItems.is_visible(self.TypeList[16],self.XpathList[16])
			Log().info("等待查询按钮出现成功")
		except:
			Log().error("等待查询按钮出现异常")
			raise
	def clickSearchButton(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_SysSet_E()
			self.BasePageItems.click_Element(self.TypeList[16],self.XpathList[16])
			Log().info("点击查询按钮成功")
		except:
			Log().error("点击查询按钮异常")
			raise
	def assertSysSetName(self,IsSysSetName):
		try:
			self.XpathList,self.TypeList=File_Excel().get_SysSet_E()
			self.BasePageItems.TextCheck(self.TypeList[17],self.XpathList[17],IsSysSetName)
			Log().info("验证配置名称成功")
		except:
			Log().error("验证配置名称异常")
			raise
	def clickAlterButton(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_SysSet_E()
			self.BasePageItems.click_Element(self.TypeList[18],self.XpathList[18])
			Log().info("点击修改按钮成功")
		except:
			Log().error("点击修改按钮异常")
			raise
	def clearSysSetValue(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_SysSet_E()
			self.BasePageItems.clear_Element(self.TypeList[9],self.XpathList[9])
			Log().info("清空配置值输入框成功")
		except:
			Log().error("清空配置值输入框异常")
			raise
	def alterSysSetValue(self,SysSetValue):
		try:
			self.XpathList,self.TypeList=File_Excel().get_SysSet_E()
			self.BasePageItems.send_Element(self.TypeList[9],self.XpathList[9],SysSetValue)
			Log().info("修改配置值成功")
		except:
			Log().error("修改配置值异常")
			raise
	def clickSaveButton(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_SysSet_E()
			self.BasePageItems.click_Element(self.TypeList[12],self.XpathList[12])
			Log().info("点击保存按钮成功")
		except:
			Log().error("点击保存按钮异常")
			raise
	def assertSysSetValue(self,IsSysSetValue):
		try:
			self.XpathList,self.TypeList=File_Excel().get_SysSet_E()
			self.BasePageItems.TextCheck(self.TypeList[19],self.XpathList[19],IsSysSetValue)
			Log().info("验证配置值成功")
		except:
			Log().error("验证配置值异常")
			raise
	def clickDelButton(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_SysSet_E()
			self.BasePageItems.click_Element(self.TypeList[20],self.XpathList[20])
			Log().info("点击删除按钮成功")
		except:
			Log().error("点击删除按钮异常")
			raise
	def clickConfirmButton(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_SysSet_E()
			self.BasePageItems.click_Element(self.TypeList[21],self.XpathList[21])
			Log().info("点击删除确认按钮成功")
		except:
			Log().error("点击删除确认按钮异常")
			raise
	def WaitTime(self,sleepTime):
		try:
			self.XpathList,self.TypeList=File_Excel().get_SysSet_E()
			self.BasePageItems.Sleep(sleepTime)
			Log().info("等待时间成功")
		except:
			Log().error("等待时间异常")
			raise
	def getIsSameSysSetText(self,sumSysSetNumber):
		try:
			self.XpathList,self.TypeList=File_Excel().get_SysSet_E()
			self.BasePageItems.TextCheck(self.TypeList[22],self.XpathList[22],sumSysSetNumber)
			Log().info("验证数量成功")
		except:
			Log().error("验证数量异常")
			raise
	def Close(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_SysSet_E()
			self.BasePageItems.Closebrowser()
			Log().info("关闭浏览器成功")
		except:
			Log().error("关闭浏览器异常")
			raise
	