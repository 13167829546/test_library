import logging
import time
import os
from common1.FilePath import FilePath

#保存日志本地路径
#获取文件路径
log_path = FilePath().get_File_Path('logPath')
#log_path = "D:\\python\\automatic\\Po_Model_Test\\logs"
class Log:
    def __init__(self):
        #文件的命名
        self.logname = os.path.join(log_path,'%s.log'%time.strftime('%Y_%m_%d'))
        #创建logger
        self.logger = logging.getLogger()
        #设置日志等级
        self.logger.setLevel(logging.DEBUG)
        #日志输入格式
        self.formatter = logging.Formatter('[%(asctime)s] - %(filename)s] - %(levelname)s: %(message)s')
    def __console(self,level,message):
        #创建一个fileHandler,用于写日志到本地(fh = logging.FileHandler(self.logname,'W'))
        fh = logging.FileHandler(self.logname,'a',encoding='utf-8') #追加模式
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        #给logger添加handler
        self.logger.addHandler(fh)
        #创建一个streamhandler,用于输入到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)
        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
        #这2行是为了避免日志输入重复问题
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)
        #关闭文件
        fh.close()
    def debug(self,message):
        self.__console('debug',message)
    def info(self,message):
        self.__console('info',message)
    def warning(self,message):
        self.__console('warning',message)
    def error(self,message):
        self.__console('error',message)


if __name__ == '__main__':
    log = Log()
    log.info("--开始测试--")
    log.info("输入密码")
    log.warning("--测试结束--")



'''
#coding=utf-8
import logging
import time
import os
log_path = "D:\\python\\automatic\\Po_Model_Test\\logs"
class Log:
    def __init__(self):
        #self.logname = os.path.join(log_path, '{0}.log'.format(time.strftime('%Y-%m-%d')))
        #self.logname = os.path.join(log_path, '%s.log' % time.strftime('%Y_%m_%d_%H_%M_%S'))
        self.logname = os.path.join(log_path, '%s.log' % time.strftime('%Y_%m_%d'))

    def __printconsole(self, level, message):
        # 创建一个logger
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        # 创建一个handler，用于写入日志文件
        fh = logging.FileHandler(self.logname,'a',encoding='utf-8')
        fh.setLevel(logging.DEBUG)
        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        # 给logger添加handler
        logger.addHandler(fh)
        logger.addHandler(ch)
        # 记录一条日志
        if level == 'info':
            logger.info(message)
        elif level == 'debug':
            logger.debug(message)
        elif level == 'warning':
            logger.warning(message)
        elif level == 'error':
            logger.error(message)
        logger.removeHandler(ch)
        logger.removeHandler(fh)
        # 关闭打开的文件
        fh.close()

    def debug(self,message):
        self.__printconsole('debug', message)

    def info(self,message):
        self.__printconsole('info', message)

    def warning(self,message):
        self.__printconsole('warning', message)

    def error(self,message):
        self.__printconsole('error', message)

'''
