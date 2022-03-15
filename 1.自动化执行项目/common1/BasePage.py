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
    #�������������ϵͳ
    def OpenThebrowser(self,browserName,Url):
        try:
            # ��Chrome���������
            if browserName == 'ie':
                #self.log.info('�����ΪIE')
                self.driver = webdriver.Ie()
            elif browserName == 'firefox':
                self.driver = webdriver.Firefox()
                #self.log.info('�����ΪFirefox')
            elif browserName == 'chrome':
                self.driver = webdriver.Chrome()
                #self.log.info('�����ΪChrome')
            else:
                print('���������֧�֣��������������!')
                self.log.info('���������֧�֣��������������!')
            # ��������
            self.driver.maximize_window()
            # �ȴ��������������
            self.driver.implicitly_wait(2)
            # ����ҳ LoginXpath[0]
            self.driver.get(Url)
            time.sleep(1)
        except :
            print("������򿪴���")
            raise

    #�ر������
    def Closebrowser(self):
        self.driver.quit()

    #�ı�У�飺����1 Xpath,����2 pValue
    def TextCheck(self,pType,pXpath,pValue):
        str = self.driver.find_element(pType,pXpath).text
        if str == pValue:
            return True
        else:
            return False

    #��ͼ������ע���ν�ͼ���������ظ����Ḳ��֮ǰ�Ľ�ͼ
    def Screenshot(self):
        #self.driver.get_screenshot_as_file("E:\\Image\\"+pInformation+".png")
        nowtime = time.strftime('%Y%m%d.%H.%M.%S')
        self.driver.get_screenshot_as_file('%s.jpg' % nowtime)

    #ѡ���ϴ��ļ�����δ��д�������ٲ��䣩
    def SelectFile(self):
        pass

    #�л�iFrame
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
                print('iframe��css��Xpath����ȷ')
        except:
            # ���쳣��Ϣд�뱨��
            print("ѡ��Iframe������ʧ��")
            raise

    #�л�Ĭ��iframe
    def selectDefalutFrame(self):
        try:
            self.driver.switch_to.default_content()
        except:
            print('�л�Ĭ��frameʧ��')

    #��ȡ��ǰ����
    def Current_Time(self):
        now_time = datetime.datetime.now().strftime('%Y-%m-%d')
        return  now_time

    #ҳ������ж�
    def ShouldContain(self,pType,pXpath):
        try:
            Result = self.driver.find_element(pType,pXpath)
            return True
        except:
            #���쳣��Ϣд�뱨��
            print("�ж�Ԫ���Ƿ����������ʧ��")
            return  False
            raise

    #�ж�Ԫ���Ƿ��û�
    def ElemetIsDisable(self,pType,pXpath):
        try:
            Result = self.driver.find_element(pType, pXpath).is_enabled()
            if Result == True :
                print("Ԫ��δ������")
                return True
            else:
                print("Ԫ�ر�����")
                return False
        except:
            #���쳣��Ϣд�뱨��
            print("�ж�Ԫ���Ƿ���ã�����ʧ��")
            return False
            raise

    # һֱ�ȴ�ĳԪ�ؿɼ���Ĭ�ϳ�ʱ10��,by_element��ʾ����By.Xpath������By.Css,locator��ʾxpath����cssԪ��
    def is_visible(self,by_element, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((by_element, locator)))
            return True
        except TimeoutException:
            # ���쳣��Ϣд�뱨��
            print("Ԫ�صȴ���ʱ/δ�ҵ���Ԫ��")
            Log().error("Ԫ�صȴ���ʱ/δ�ҵ���Ԫ��")
            return False
            raise

    # һֱ�ȴ�ĳ��Ԫ����ʧ��Ĭ�ϳ�ʱ10�룬by_element��ʾ����By.Xpath������By.Css,locator��ʾxpath����cssԪ��
    def is_not_visible(self,by_element, locator, timeout=10):
        try:
            ui.WebDriverWait(self.driver, timeout).until_not(EC.visibility_of_element_located((by_element, locator)))
            return True
        except TimeoutException:
            # ���쳣��Ϣд�뱨��
            print("Ԫ�صȴ���ʱ")
            return False
            raise

    #��ĳ��Ԫ�ؽ��е������
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
                print('���Ԫ�ز�����Ԫ�ص�xpath����css·�����ԣ����飡'+xpath)
                Log().info("���Ԫ�ز�����Ԫ�ص�xpath����css·�����ԣ����飡"+xpath)
        except Exception as e:
            print('�Ҳ�����Ԫ��' +xpath)
            Log().error("���Ԫ�ز����쳣+"+xpath)
            raise

    # �����������
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
                print('Ԫ�ص�xpath����css·�����ԣ����飡'+xpath)
                Log().info("Ԫ�ص�xpath����css·�����ԣ����飡"+xpath)
        except Exception as e:
            print('�Ҳ�����Ԫ��'+ xpath )
            Log().error("Ԫ�ز����쳣+"+xpath)
            raise

    #��Ԫ���������
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
                print('�������Ԫ�ؽ��в�����Ԫ�ص�css��xpath·�����ԣ�')
                Log().info('�������Ԫ�ؽ��в�����Ԫ�ص�css��xpath·�����ԣ�')
        except:
            print('�������Ԫ�ؽ��в���,δ�ҵ���Ԫ��!')
            Log().error('�������Ԫ�ؽ��в���,δ�ҵ���Ԫ��!')
            raise

    #ѡ��Ԫ��
    def select_Element(self,by_element,xpath,words):
        try:
            if by_element == 'xpath':
                Select(self.driver.find_element_by_xpath(xpath)).select_by_visible_text(words)
                #Log().info("��¼�û�����"+words)
            elif by_element == 'id':
                Select(self.driver.find_element_by_id(xpath)).select_by_visible_text(words)
                #Log().info("��¼�û�����" + words)
            else:
                print('Ԫ�ص�css��xpath·������')
                Log.info("ѡ��Ԫ�ص�css��xpath·������")
        except:
            print('�Ҳ�����Ԫ��')
            Log.error("�Ҳ�����Ԫ�أ�")
            raise

    #���Ԫ��
    def click_Element(self,by_element,xpath):
        try:
            if by_element == 'css':
                self.driver.find_element_by_css_selector(xpath).click()
            elif by_element == 'xpath':
                self.driver.find_element_by_xpath(xpath).click()
            elif by_element == 'id':
                self.driver.find_element_by_id(xpath).click()
            else:
                print('Ԫ�ص�xpath����css·�����ԣ����飡')
                Log().info("���Ԫ�ز���ʱ��Ԫ�ص�xpath����css·�����ԣ����飡")
        except Exception as e:
            print('Ԫ�ص���������Ҳ�����Ԫ��')
            Log().error('Ԫ�ص���������Ҳ�����Ԫ��')
            raise

    #Ԫ�ض�λ
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
                print('Ԫ�ص�xpath����css·�����ԣ����飡'+xpath)
                Log().info("Ԫ�ص�xpath����css·�����ԣ����飡"+xpath)
        except Exception as e:
            print('�Ҳ�����Ԫ��'+xpath)
            Log().error('�Ҳ�����Ԫ��'+xpath)
            return False
            raise

    #�����ͣ��ѡ��
    def move_Element(self,by_element,element1,element2):
        try:
            if by_element == 'xpath':
                move_element = self.driver.find_element_by_xpath(element1)
                ActionChains(self.driver).move_to_element(move_element).perform()
                self.driver.find_element_by_xpath(element2).click()
            else:
                print('����Ԫ�ص�id/xpath/css�Ƿ���ȷ')
        except:
            print('�Ҳ�����Ԫ��')
            raise

    #�ϴ��ļ�,�õ�autoit�����ϴ�
    def load_File(self,location):
        try:
            os.system(location)
        except:
            print("�Ҳ������ļ�")
            raise

    #�鿴�ı��Ƿ�ƥ��
    def get_is_same_Text(self,by_element,element,prepareText):
        try:
            if by_element == 'xpath':
                text = self.driver.find_element_by_xpath(element).text
                if text == prepareText:
                    print('����ƥ��')
                else:
                    print('���ֲ�ƥ��')
            else:
                print('·������')
        except:
            print('�Ҳ�����Ԫ��')
            raise

    #��ȡԪ���ı�
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
                print('Ԫ�ص�·������')
                Log().info('δ�ҵ���Ԫ�ص��ı���Ϣ')
        except:
            print('�Ҳ�����Ԫ��')
            Log().error("�Ҳ�����Ԫ��")
            raise

    #ˢ��ҳ��
    def refresh_Page(self):
        self.driver.refresh()

    #���ߵȴ�
    def Sleep(self,Time):
        time.sleep(int(Time))

    #�ж�Text1�Ƿ����Text2
    def ShouldContainText(self,Text1,Text2):
        try:
            if Text1.find(Text2):
                return True
            else:
                return False
        except:
            print('#�ж�Text1�Ƿ����Text2ʧ��')
            Log().error("#�ж�Text1�Ƿ����Text2ʧ��")

    # ת����ҳ��
    def SwichToWindow(self):
        self.driver.close()
        n = self.driver.window_handles
        self.driver.switch_to_window(n[0])

    def quit_driver(self):
        self.driver.quit()

    def save_picture(self):
        #�����ͼ
        self.driver.get_screenshot_as_file('D:\\picture1.png')
