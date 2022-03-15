#!user/bin/env python3
# -*- coding: gbk -*-
import time
import datetime
import os
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
import selenium.webdriver.support.expected_conditions as EC
import selenium.webdriver.support.ui as ui
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from common1.Logs import Log
class BasePageItems():
    FunctionCode = {
        'B001': 'OpenThebrowser',
        'B002': 'Closebrowser',
        'B003': 'Screenshot',
        'B004': 'refresh_Page',
        'B005': 'Sleep',
        'B006': 'SwichToWindow',
        'S001': 'TextCheck',
        'S002': 'ShouldContain',
        'S003': 'ElemetIsDisable',
        'S004': 'is_visible',
        'S005': 'get_is_same_Text',
        'S006': 'ShouldContainText',
        'E001': 'SelectFile',
        'E002': 'selectFrame',
        'E003': 'selectDefalutFrame',
        'E004': 'Current_Time',
        'E005': 'click_Element',
        'E006': 'move_Element',
        'E007': 'load_File',
        'E008': 'get_Text',
        'E009': 'send_Element',
        'E010': 'clear_Element'
    }
    #打开浏览器，进入系统
    def OpenThebrowser(self,browserName,Url):
        try:
            # 打开Chrome浏览器驱动
            if browserName == 'ie':
                #self.log.info('浏览器为IE')
                self.driver = webdriver.Ie()
            elif browserName == 'firefox':
                self.driver = webdriver.Firefox()
                #self.log.info('浏览器为Firefox')
            elif browserName == 'chrome':
                self.driver = webdriver.Chrome()
                #self.log.info('浏览器为Chrome')
            else:
                print('该浏览器不支持，请检查浏览器驱动!')
                self.log.info('该浏览器不支持，请检查浏览器驱动!')
            # 浏览器最大化
            self.driver.maximize_window()
            # 等待浏览器驱动运行
            self.driver.implicitly_wait(2)
            # 打开网页 LoginXpath[0]
            self.driver.get(Url)
            time.sleep(1)
        except :
            print("浏览器打开错误")
            raise

    #关闭浏览器
    def Closebrowser(self):
        self.driver.quit()

    #文本校验：参数1 Xpath,参数2 pValue
    def TextCheck(self,pType,pXpath,pValue):
        str = self.driver.find_element(pType,pXpath).text
        if str == pValue:
            return True
        else:
            return False

    #截图函数，注意多次截图，如名称重复，会覆盖之前的截图
    def Screenshot(self):
        #self.driver.get_screenshot_as_file("E:\\Image\\"+pInformation+".png")
        nowtime = time.strftime('%Y%m%d.%H.%M.%S')
        self.driver.get_screenshot_as_file('%s.jpg' % nowtime)

    #选择上传文件（暂未编写，遇到再补充）
    def SelectFile(self):
        pass

    #切换iFrame
    def selectFrame(self,by_element,Xpath):
        try:
            if by_element == 'css':
                iframe = self.driver.find_element_by_css_selector(Xpath)
                self.driver.switch_to.frame(iframe)
            elif by_element == 'xpath':
                iframe = self.driver.find_element_by_xpath(Xpath)
                self.driver.switch_to.frame(iframe)
            elif by_element == 'id':
                self.driver.switch_to.frame(Xpath)
            else:
                print('iframe的css或Xpath不正确')
        except:
            # 将异常信息写入报告
            print("选择Iframe，调用失败")
            raise

    #切换默认iframe
    def selectDefalutFrame(self):
        try:
            self.driver.switch_to.default_content()
        except:
            print('切换默认frame失败')

    #获取当前日期
    def Current_Time(self):
        now_time = datetime.datetime.now().strftime('%Y-%m-%d')
        return  now_time

    #页面包含判断
    def ShouldContain(self,pType,pXpath):
        try:
            Result = self.driver.find_element(pType,pXpath)
            return True
        except:
            #将异常信息写入报告
            print("判断元素是否包含，调用失败")
            return  False
            raise

    #判断元素是否置灰
    def ElemetIsDisable(self,pType,pXpath):
        try:
            Result = self.driver.find_element(pType, pXpath).is_enabled()
            if Result == True :
                print("元素未被禁用")
                return True
            else:
                print("元素被禁用")
                return False
        except:
            #将异常信息写入报告
            print("判断元素是否禁用，调用失败")
            return False
            raise

    # 一直等待某元素可见，默认超时10秒,by_element表示：用By.Xpath还是用By.Css,locator表示xpath或者css元素
    def is_visible(self,by_element, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((by_element, locator)))
            return True
        except TimeoutException:
            # 将异常信息写入报告
            print("元素等待超时/未找到该元素")
            Log().error("元素等待超时/未找到该元素")
            return False
            raise

    # 一直等待某个元素消失，默认超时10秒，by_element表示：用By.Xpath还是用By.Css,locator表示xpath或者css元素
    def is_not_visible(self,by_element, locator, timeout=10):
        try:
            ui.WebDriverWait(self.driver, timeout).until_not(EC.visibility_of_element_located((by_element, locator)))
            return True
        except TimeoutException:
            # 将异常信息写入报告
            print("元素等待超时")
            return False
            raise

    #对某个元素进行点击操作
    def click_Element(self,by_element,xpath):
        try:
            if by_element == 'css':
                self.driver.find_element_by_css_selector(xpath).click()
            elif by_element == 'xpath':
                self.driver.find_element_by_xpath(xpath).click()
            elif by_element == 'name':
                self.driver.find_element_by_name(xpath).click()
            elif by_element == 'id':
                self.driver.find_element_by_id(xpath).click()
            else:
                print('点击元素操作，元素的xpath或者css路径不对，请检查！'+xpath)
                Log().info("点击元素操作，元素的xpath或者css路径不对，请检查！"+xpath)
        except Exception as e:
            print('找不到该元素' +xpath)
            Log().error("点击元素操作异常+"+xpath)
            raise

    # 清空输入框操作
    def clear_Element(self,by_element,xpath):
        try:
            if by_element == 'css':
                self.driver.find_element_by_css_selector(xpath).clear()
            elif by_element == 'xpath':
                self.driver.find_element_by_xpath(xpath).clear()
            elif by_element == 'name':
                self.driver.find_element_by_name(xpath).clear()
            elif by_element == 'id':
                self.driver.find_element_by_id(xpath).clear()
            else:
                print('元素的xpath或者css路径不对，请检查！'+xpath)
                Log().info("元素的xpath或者css路径不对，请检查！"+xpath)
        except Exception as e:
            print('找不到该元素'+ xpath )
            Log().error("元素操作异常+"+xpath)
            raise

    #对元素输入操作
    def send_Element(self,by_element,xpath,Value):
        try:
            if by_element == 'xpath':
                self.driver.find_element_by_xpath(xpath).send_keys(Value)
            elif by_element == 'css':
                self.driver.find_element_by_css_selector(xpath).send_keys(Value)
            elif by_element == 'id':
                self.driver.find_element_by_id(xpath).send_keys(Value)
            elif by_element == 'name':
                self.driver.find_element_by_name(xpath).send_keys(Value)
            else:
                print('对输入框元素进行操作，元素的css或xpath路径不对！')
                Log().info('对输入框元素进行操作，元素的css或xpath路径不对！')
        except:
            print('对输入框元素进行操作,未找到该元素!')
            Log().error('对输入框元素进行操作,未找到该元素!')
            raise

    #选择元素
    def select_Element(self,by_element,xpath,words):
        try:
            if by_element == 'xpath':
                Select(self.driver.find_element_by_xpath(xpath)).select_by_visible_text(words)
                #Log().info("登录用户名："+words)
            elif by_element == 'id':
                Select(self.driver.find_element_by_id(xpath)).select_by_visible_text(words)
                #Log().info("登录用户名：" + words)
            else:
                print('元素的css或xpath路径不对')
                Log.info("选择元素的css或xpath路径不对")
        except:
            print('找不到该元素')
            Log.error("找不到该元素！")
            raise

    #点击元素
    def click_Element(self,by_element,xpath):
        try:
            if by_element == 'css':
                self.driver.find_element_by_css_selector(xpath).click()
            elif by_element == 'xpath':
                self.driver.find_element_by_xpath(xpath).click()
            elif by_element == 'id':
                self.driver.find_element_by_id(xpath).click()
            else:
                print('元素的xpath或者css路径不对，请检查！')
                Log().info("点击元素操作时，元素的xpath或者css路径不对，请检查！")
        except Exception as e:
            print('元素点击操作，找不到该元素')
            Log().error('元素点击操作，找不到该元素')
            raise

    #元素定位
    def check_element(self,by_element,xpath):
        try:
            if by_element == 'css':
                self.driver.find_element_by_css_selector(xpath)
            elif by_element == 'xpath':
                self.driver.find_element_by_xpath(xpath)
                return True
            elif by_element == 'id':
                self.driver.find_element_by_id(xpath)
            else:
                print('元素的xpath或者css路径不对，请检查！'+xpath)
                Log().info("元素的xpath或者css路径不对，请检查！"+xpath)
        except Exception as e:
            print('找不到该元素'+xpath)
            Log().error('找不到该元素'+xpath)
            return False
            raise

    #鼠标悬停后选择
    def move_Element(self,by_element,element1,element2):
        try:
            if by_element == 'xpath':
                move_element = self.driver.find_element_by_xpath(element1)
                ActionChains(self.driver).move_to_element(move_element).perform()
                self.driver.find_element_by_xpath(element2).click()
            else:
                print('请检查元素的id/xpath/css是否正确')
        except:
            print('找不到该元素')
            raise

    #上传文件,用的autoit工具上传
    def load_File(self,location):
        try:
            os.system(location)
        except:
            print("找不到该文件")
            raise

    #查看文本是否匹配
    def get_is_same_Text(self,by_element,element,prepareText):
        try:
            if by_element == 'xpath':
                text = self.driver.find_element_by_xpath(element).text
                if text == prepareText:
                    print('文字匹配')
                else:
                    print('文字不匹配')
            else:
                print('路径不对')
        except:
            print('找不到该元素')
            raise

    #获取元素文本
    def get_Text(self,by_element,element):
        try:
            if by_element == 'xpath':
                text = self.driver.find_element_by_xpath(element).text
                #print(text)
                return text
            elif by_element == 'css':
                text = self.driver.find_element_by_css_selector(element).text
                return text
            else:
                print('元素的路径不对')
                Log().info('未找到该元素的文本信息')
        except:
            print('找不到该元素')
            Log().error("找不到该元素")
            raise

    #刷新页面
    def refresh_Page(self):
        self.driver.refresh()

    #休眠等待
    def Sleep(self,Time):
        time.sleep(int(Time))

    #判断Text1是否包含Text2
    def ShouldContainText(self,Text1,Text2):
        try:
            if Text1.find(Text2):
                return True
            else:
                return False
        except:
            print('#判断Text1是否包含Text2失败')
            Log().error("#判断Text1是否包含Text2失败")

    # 转换新页面
    def SwichToWindow(self):
        self.driver.close()
        n = self.driver.window_handles
        self.driver.switch_to_window(n[0])

    def quit_driver(self):
        self.driver.quit()

    def save_picture(self):
        #保存截图
        self.driver.get_screenshot_as_file('D:\\picture1.png')
