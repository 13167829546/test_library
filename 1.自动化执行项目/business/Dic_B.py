from element.Dic_E import Dic_E
class Dic_B(Dic_E):
	def add_generalDic(self,DicName,DicValue,SysDec):
		self.clickDataCenter()
		self.clickSys()
		self.clickDic()
		self.clickGeneralDic()
		self.clickAddButton()
		self.sendDicName(DicName)
		self.sendDicValue(DicValue)
		self.sendSysDec(SysDec)
		self.clickDicType()
		self.selectDicType()
		self.clickSaveButton()
	def search_generalDic(self,DicName,assertDicName):
		self.sendSearchKey(DicName)
		self.clickSearchButton()
		self.shouldContainKey(assertDicName)
	def alter_generalDic(self,alterDicValue,assertAlterDicValue):
		self.clickAlterButton()
		self.alterDicValue(alterDicValue)
		self.clickSaveButton()
		self.shouldContainValue(assertAlterDicValue)
	def del_generalDic(self,sumDicTypeNumber):
		self.clickDelButton()
		self.clickConfirmButton()
		self.getIsSameText(sumDicTypeNumber)
	