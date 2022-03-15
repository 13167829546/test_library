from common.Logs import Log
from common.BasePage import BasePageItems
from common.File_Excel import File_Excel
class Dic_E(BasePageItems):
	BasePageItems = BasePageItems()
	def clickDataCenter(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_Dic_E()
			self.BasePageItems.click_Element(self.TypeList[0],self.XpathList[0])
			Log().info("点击供电数据共享中心成功")
		except:
			Log().error("点击供电数据共享中心异常")
			raise
	def clickSys(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_Dic_E()
			self.BasePageItems.click_Element(self.TypeList[1],self.XpathList[1])
			Log().info("点击系统管理成功")
		except:
			Log().error("点击系统管理异常")
			raise
	def clickDic(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_Dic_E()
			self.BasePageItems.click_Element(self.TypeList[2],self.XpathList[2])
			Log().info("点击字典管理成功")
		except:
			Log().error("点击字典管理异常")
			raise
	def clickGeneralDic(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_Dic_E()
			self.BasePageItems.click_Element(self.TypeList[3],self.XpathList[3])
			Log().info("点击通用字典成功")
		except:
			Log().error("点击通用字典异常")
			raise
	def clickAddButton(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_Dic_E()
			self.BasePageItems.click_Element(self.TypeList[4],self.XpathList[4])
			Log().info("点击添加按钮成功")
		except:
			Log().error("点击添加按钮异常")
			raise
	def sendDicName(self,DicName):
		try:
			self.XpathList,self.TypeList=File_Excel().get_Dic_E()
			self.BasePageItems.send_Element(self.TypeList[5],self.XpathList[5],DicName)
			Log().info("输入字典名称成功")
		except:
			Log().error("输入字典名称异常")
			raise
	def sendDicValue(self,DicValue):
		try:
			self.XpathList,self.TypeList=File_Excel().get_Dic_E()
			self.BasePageItems.send_Element(self.TypeList[6],self.XpathList[6],DicValue)
			Log().info("输入字典值成功")
		except:
			Log().error("输入字典值异常")
			raise
	def sendSysDec(self,SysDec):
		try:
			self.XpathList,self.TypeList=File_Excel().get_Dic_E()
			self.BasePageItems.send_Element(self.TypeList[7],self.XpathList[7],SysDec)
			Log().info("输入系统描述成功")
		except:
			Log().error("输入系统描述异常")
			raise
	def clickDicType(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_Dic_E()
			self.BasePageItems.click_Element(self.TypeList[8],self.XpathList[8])
			Log().info("点击字典类型成功")
		except:
			Log().error("点击字典类型异常")
			raise
	def selectDicType(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_Dic_E()
			self.BasePageItems.click_Element(self.TypeList[9],self.XpathList[9])
			Log().info("选择字典类型选项成功")
		except:
			Log().error("选择字典类型选项异常")
			raise
	def clickSaveButton(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_Dic_E()
			self.BasePageItems.click_Element(self.TypeList[10],self.XpathList[10])
			Log().info("点击保存按钮成功")
		except:
			Log().error("点击保存按钮异常")
			raise
	def sendSearchKey(self,DicName):
		try:
			self.XpathList,self.TypeList=File_Excel().get_Dic_E()
			self.BasePageItems.send_Element(self.TypeList[11],self.XpathList[11],DicName)
			Log().info("输入查询条件成功")
		except:
			Log().error("输入查询条件异常")
			raise
	def clickSearchButton(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_Dic_E()
			self.BasePageItems.click_Element(self.TypeList[12],self.XpathList[12])
			Log().info("点击查询按钮成功")
		except:
			Log().error("点击查询按钮异常")
			raise
	def shouldContainKey(self,assertDicName):
		try:
			self.XpathList,self.TypeList=File_Excel().get_Dic_E()
			self.BasePageItems.ShouldContain(self.TypeList[13],self.XpathList[13],assertDicName)
			Log().info("验证关键字名称成功")
		except:
			Log().error("验证关键字名称异常")
			raise
	def clickAlterButton(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_Dic_E()
			self.BasePageItems.click_Element(self.TypeList[14],self.XpathList[14])
			Log().info("点击修改按钮成功")
		except:
			Log().error("点击修改按钮异常")
			raise
	def alterDicValue(self,alterDicValue):
		try:
			self.XpathList,self.TypeList=File_Excel().get_Dic_E()
			self.BasePageItems.send_Element(self.TypeList[6],self.XpathList[6],alterDicValue)
			Log().info("修改字典值成功")
		except:
			Log().error("修改字典值异常")
			raise
	def clickSaveButton(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_Dic_E()
			self.BasePageItems.click_Element(self.TypeList[10],self.XpathList[10])
			Log().info("点击保存按钮成功")
		except:
			Log().error("点击保存按钮异常")
			raise
	def shouldContainValue(self,assertAlterDicValue):
		try:
			self.XpathList,self.TypeList=File_Excel().get_Dic_E()
			self.BasePageItems.ShouldContain(self.TypeList[15],self.XpathList[15],assertAlterDicValue)
			Log().info("验证字典值成功")
		except:
			Log().error("验证字典值异常")
			raise
	def clickDelButton(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_Dic_E()
			self.BasePageItems.click_Element(self.TypeList[16],self.XpathList[16])
			Log().info("点击删除按钮成功")
		except:
			Log().error("点击删除按钮异常")
			raise
	def clickConfirmButton(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_Dic_E()
			self.BasePageItems.click_Element(self.TypeList[17],self.XpathList[17])
			Log().info("点击删除弹窗确认按钮成功")
		except:
			Log().error("点击删除弹窗确认按钮异常")
			raise
	def getIsSameText(self,sumDicTypeNumber):
		try:
			self.XpathList,self.TypeList=File_Excel().get_Dic_E()
			self.BasePageItems.TextCheck(self.TypeList[18],self.XpathList[18],sumDicTypeNumber)
			Log().info("验证数量成功")
		except:
			Log().error("验证数量异常")
			raise
	