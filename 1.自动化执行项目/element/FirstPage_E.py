from common1.Logs import Log
from common1.BasePage import BasePageItems
from common1.File_Excel import File_Excel
from time import sleep
from PIL import Image
import pytesseract
import os

class FirstPage_E(BasePageItems):
	BasePageItems = BasePageItems()
	def clickBtu(self):
		try:
			self.XpathList,self.TypeList=File_Excel().get_FirstPage_E()
			self.BasePageItems.click_Element(self.TypeList[0],self.XpathList[0])
			Log().info("点击成功")
		except:
			Log().error("点击异常")
			raise

	def click(self,list,num):
		try:
			self.XpathList,self.TypeList=File_Excel().get_excel(list)
			self.BasePageItems.click_Element(self.TypeList[num],self.XpathList[num])
			Log().info("点击成功")
			sleep(1)
		except:
			Log().error("点击%s异常"%(self.XpathList[num]))
			raise

	def finish_driver(self):
		self.quit_driver()

	def send(self,list,num,keys):
		try:
			self.XpathList, self.TypeList = File_Excel().get_excel(list)
			self.BasePageItems.send_Element(self.TypeList[num], self.XpathList[num],keys)
		except:
			Log().error("点击%s异常"%(self.XpathList[num]))
			raise

	def switch_frame(self,list,num):
		try:
			self.XpathList, self.TypeList = File_Excel().get_excel(list)
			self.BasePageItems.selectFrame(self.TypeList[num], self.XpathList[num])
			sleep(1)
		except:
			Log().error("点击%s异常"%(self.XpathList[num]))
			raise

	def save_code_picture(self, list, num):
		#保存验证码图片
		try:
			self.BasePageItems.save_picture()
			Log().info("保存页面截图成功")
			self.XpathList,self.TypeList=File_Excel().get_excel(list)
			#   self.TypeList[num], self.XpathList[num]
			imgelement = self.BasePageItems.driver.find_element_by_xpath(self.XpathList[num])  # 定位验证码
			location = imgelement.location  # 获取验证码x,y轴坐标
			size = imgelement.size  # 获取验证码的长宽
			rangle = (int(location['x']), int(location['y']), int(location['x'] + size['width']),
					  int(location['y'] + size['height']))  # 写成我们需要截取的位置坐标
			i = Image.open("D:\\picture1.png")  # 打开截图
			frame4 = i.crop(rangle)  # 使用Image的crop函数，从截图中再次截取我们需要的区域
			frame4.save('D:\\picture1.png')  # 保存我们接下来的验证码图片 进行打码
		except:
			Log().error("保存验证码截图失败")
			raise

	def check_code(self):
		#从图片中识别验证码（不是很准确）
		pytesseract.pytesseract.tesseract_cmd = r'D:\\work\\tesseract_ocr\\tesseract.exe'
		image = Image.open('D:\\picture1.png')
		code = pytesseract.image_to_string(image)
		os.system("del D:\picture1.png")
		return code

	def position(self,list,num):
		try:
			self.XpathList, self.TypeList = File_Excel().get_excel(list)
			result = self.BasePageItems.check_element(self.TypeList[num], self.XpathList[num])
			Log().info("点击登陆成功")
			return result
		except:
			Log().error("点击登陆异常")
			return result
			raise

	def clear(self,list,num):
		try:
			self.XpathList, self.TypeList = File_Excel().get_excel(list)
			self.BasePageItems.clear_Element(self.TypeList[num], self.XpathList[num])
			Log().info("清理成功")
			sleep(1)
		except:
			Log().error("清理异常")
			raise