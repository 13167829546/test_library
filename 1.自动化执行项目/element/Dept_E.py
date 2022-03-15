from common.Logs import Log
from common.BasePage import BasePageItems
from common.File_Excel import File_Excel
class Dept_E(BasePageItems):
	BasePageItems = BasePageItems()
	def clickSysNav(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_Dept_E()
			self.BasePageItems.click_Element(self.TypeList[0],self.XpathList[0])
			Log().info("鼠标点击系统导航成功")
		except:
			Log().error("鼠标点击系统导航异常")
			raise
	def clickDataCenter(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_Dept_E()
			self.BasePageItems.click_Element(self.TypeList[1],self.XpathList[1])
			Log().info("点击供电数据共享中心成功")
		except:
			Log().error("点击供电数据共享中心异常")
			raise
	def waitSysManVisible(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_Dept_E()
			self.BasePageItems.is_visible(self.TypeList[2],self.XpathList[2])
			Log().info("等待系统管理出现成功")
		except:
			Log().error("等待系统管理出现异常")
			raise
	def clickSys(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_Dept_E()
			self.BasePageItems.click_Element(self.TypeList[2],self.XpathList[2])
			Log().info("点击系统管理成功")
		except:
			Log().error("点击系统管理异常")
			raise
	def clickDept(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_Dept_E()
			self.BasePageItems.click_Element(self.TypeList[3],self.XpathList[3])
			Log().info("点击部门管理成功")
		except:
			Log().error("点击部门管理异常")
			raise
	def clickAddButton(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_Dept_E()
			self.BasePageItems.click_Element(self.TypeList[4],self.XpathList[4])
			Log().info("点击添加按钮成功")
		except:
			Log().error("点击添加按钮异常")
			raise
	def sendDeptName(self,DeptName):
		try:
			self.XpathList,self.TypeList=File_Excel().get_Dept_E()
			self.BasePageItems.send_Element(self.TypeList[5],self.XpathList[5],DeptName)
			Log().info("输入部门名称成功")
		except:
			Log().error("输入部门名称异常")
			raise
	def sendDeptType(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_Dept_E()
			self.BasePageItems.click_Element(self.TypeList[10],self.XpathList[10])
			Log().info("点击部门类型成功")
		except:
			Log().error("点击部门类型异常")
			raise
	def sendDeptTypeValue(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_Dept_E()
			self.BasePageItems.click_Element(self.TypeList[11],self.XpathList[11])
			Log().info("选择部门类型选项成功")
		except:
			Log().error("选择部门类型选项异常")
			raise
	def clickSupperDept(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_Dept_E()
			self.BasePageItems.click_Element(self.TypeList[7],self.XpathList[7])
			Log().info("点击上级部门成功")
		except:
			Log().error("点击上级部门异常")
			raise
	def sendSupperDeptName(self,SupperDeptName):
		try:
			self.XpathList,self.TypeList=File_Excel().get_Dept_E()
			self.BasePageItems.send_Element(self.TypeList[8],self.XpathList[8],SupperDeptName)
			Log().info("输入上级部门名称查询成功")
		except:
			Log().error("输入上级部门名称查询异常")
			raise
	def clickSupperDeptValue(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_Dept_E()
			self.BasePageItems.click_Element(self.TypeList[9],self.XpathList[9])
			Log().info("选择上级部门选项成功")
		except:
			Log().error("选择上级部门选项异常")
			raise
	def sendDeptNo(self,DeptNo):
		try:
			self.XpathList,self.TypeList=File_Excel().get_Dept_E()
			self.BasePageItems.send_Element(self.TypeList[6],self.XpathList[6],DeptNo)
			Log().info("输入部门编号成功")
		except:
			Log().error("输入部门编号异常")
			raise
	def sendDeptShotName(self,DeptShotName):
		try:
			self.XpathList,self.TypeList=File_Excel().get_Dept_E()
			self.BasePageItems.send_Element(self.TypeList[15],self.XpathList[15],DeptShotName)
			Log().info("输入部门简称成功")
		except:
			Log().error("输入部门简称异常")
			raise
	def sendDeptLeader(self,DeptLeader):
		try:
			self.XpathList,self.TypeList=File_Excel().get_Dept_E()
			self.BasePageItems.send_Element(self.TypeList[16],self.XpathList[16],DeptLeader)
			Log().info("输入部门负责人成功")
		except:
			Log().error("输入部门负责人异常")
			raise
	def clickSaveButton(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_Dept_E()
			self.BasePageItems.click_Element(self.TypeList[17],self.XpathList[17])
			Log().info("点击保存按钮成功")
		except:
			Log().error("点击保存按钮异常")
			raise
	def sendSearchKey(self,DeptName):
		try:
			self.XpathList,self.TypeList=File_Excel().get_Dept_E()
			self.BasePageItems.send_Element(self.TypeList[18],self.XpathList[18],DeptName)
			Log().info("输入查询条件成功")
		except:
			Log().error("输入查询条件异常")
			raise
	def searchButtonVisible(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_Dept_E()
			self.BasePageItems.is_visible(self.TypeList[19],self.XpathList[19])
			Log().info("等待查询按钮出现成功")
		except:
			Log().error("等待查询按钮出现异常")
			raise
	def clickSearchButton(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_Dept_E()
			self.BasePageItems.click_Element(self.TypeList[19],self.XpathList[19])
			Log().info("点击查询按钮成功")
		except:
			Log().error("点击查询按钮异常")
			raise
	def assertDeptName(self,IsDeptName):
		try:
			self.XpathList,self.TypeList=File_Excel().get_Dept_E()
			self.BasePageItems.TextCheck(self.TypeList[20],self.XpathList[20],IsDeptName)
			Log().info("验证部门名称成功")
		except:
			Log().error("验证部门名称异常")
			raise
	def clickAlterButton(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_Dept_E()
			self.BasePageItems.click_Element(self.TypeList[22],self.XpathList[22])
			Log().info("点击修改按钮成功")
		except:
			Log().error("点击修改按钮异常")
			raise
	def clearDeptName(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_Dept_E()
			self.BasePageItems.clear_Element(self.TypeList[5],self.XpathList[5])
			Log().info("清空部门名称成功")
		except:
			Log().error("清空部门名称异常")
			raise
	def alterDeptName(self,DeptName):
		try:
			self.XpathList,self.TypeList=File_Excel().get_Dept_E()
			self.BasePageItems.send_Element(self.TypeList[5],self.XpathList[5],DeptName)
			Log().info("修改部门名称成功")
		except:
			Log().error("修改部门名称异常")
			raise
	def clickSaveButton(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_Dept_E()
			self.BasePageItems.click_Element(self.TypeList[17],self.XpathList[17])
			Log().info("点击保存按钮成功")
		except:
			Log().error("点击保存按钮异常")
			raise
	def assertDeptName(self,IsDeptName):
		try:
			self.XpathList,self.TypeList=File_Excel().get_Dept_E()
			self.BasePageItems.TextCheck(self.TypeList[5],self.XpathList[5],IsDeptName)
			Log().info("验证部门名称成功")
		except:
			Log().error("验证部门名称异常")
			raise
	def clickDelButton(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_Dept_E()
			self.BasePageItems.click_Element(self.TypeList[23],self.XpathList[23])
			Log().info("点击删除按钮成功")
		except:
			Log().error("点击删除按钮异常")
			raise
	def clickConfirmButton(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_Dept_E()
			self.BasePageItems.click_Element(self.TypeList[24],self.XpathList[24])
			Log().info("点击删除确认按钮成功")
		except:
			Log().error("点击删除确认按钮异常")
			raise
	def WaitTime(self,sleepTime):
		try:
			self.XpathList,self.TypeList=File_Excel().get_Dept_E()
			self.BasePageItems.Sleep(sleepTime)
			Log().info("等待时间成功")
		except:
			Log().error("等待时间异常")
			raise
	def Close(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_Dept_E()
			self.BasePageItems.Closebrowser()
			Log().info("关闭浏览器成功")
		except:
			Log().error("关闭浏览器异常")
			raise
	