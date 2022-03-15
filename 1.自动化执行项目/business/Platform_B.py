from element.Platform_E import Platform_E
class Platform_B(Platform_E):
	def add_Platform(self,sleepTime10,sleepTime1,PlatformName,PlatformNo,PlatformUrl,PlatformDec,sleepTime2,sleepTime3):
		self.clickSysNav()
		self.WaitTime(sleepTime10)
		self.clickDataCenter()
		self.waitSysManVisible()
		self.clickSys()
		self.clickPlatform()
		self.WaitTime(sleepTime1)
		self.clickAddButton()
		self.sendPlatformName(PlatformName)
		self.sendPlatformNo(PlatformNo)
		self.sendPlatformUrl(PlatformUrl)
		self.sendPlatformDec(PlatformDec)
		self.WaitTime(sleepTime2)
		self.clickIsStart()
		self.clickSaveButton()
		self.WaitTime(sleepTime3)
	def search_Platform(self,PlatformName,sleepTime4,sleepTime5,IsPlatformName):
		self.sendSearchKey(PlatformName)
		self.WaitTime(sleepTime4)
		self.clickSearchButton()
		self.WaitTime(sleepTime5)
		self.assertPlatformName(IsPlatformName)
	def alter_Platform(self,PlatformName,sleepTime6,IsPlatformUrl):
		self.clickAlterButton()
		self.alterPlatformName(PlatformName)
		self.clickSaveButton()
		self.WaitTime(sleepTime6)
		self.assertPlatformUrl(IsPlatformUrl)
	def del_Platform(self,sleepTime7,sleepTime8):
		self.clickDelButton()
		self.WaitTime(sleepTime7)
		self.clickConfirmButton()
		self.WaitTime(sleepTime8)
	