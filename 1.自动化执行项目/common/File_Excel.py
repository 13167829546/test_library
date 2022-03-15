import xlrd
from common.FilePath import FilePath
class File_Excel():
	datePath = FilePath().get_File_Path('fileDataPath')
	testPath = FilePath().get_File_Path('testfile')
	def get_Login_E(self):
		items = xlrd.open_workbook(self.datePath)
		sheetLogin = items.sheet_by_name('登录（Login_E）')
		LocationValueList = sheetLogin.col_values(2, 1, 6)
		LocationTypeList = sheetLogin.col_values(3, 1, 6)
		return LocationValueList,LocationTypeList

	def get_FirstPage_E(self):
		items = xlrd.open_workbook(self.datePath)
		sheetLogin = items.sheet_by_name('首页（FirstPage_E）')
		LocationValueList = sheetLogin.col_values(2, 1, 2)
		LocationTypeList = sheetLogin.col_values(3, 1, 2)
		return LocationValueList,LocationTypeList

	def get_excel(self,list):
		filepath = self.testPath+list[0]
		sheetname = list[1]
		items = xlrd.open_workbook(filepath)
		sheetLogin = items.sheet_by_name(sheetname)
		LocationValueList = sheetLogin.col_values(2, 1, 100)
		LocationTypeList = sheetLogin.col_values(3, 1, 100)
		return LocationValueList,LocationTypeList
	