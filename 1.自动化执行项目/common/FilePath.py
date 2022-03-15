class FilePath():
    def get_File_Path(self,flag):
        filePath = {'fileDataPath':'C:\\Users\\huwo\\Desktop\\1.自动化执行项目\\document\\牵引作业系统自动化.xls',\
                    'logPath':'C:\\Users\\huwo\\Desktop\\1.自动化执行项目\\logs',\
                    'reportPath':'C:\\Users\\huwo\\Desktop\\1.自动化执行项目\\report\\result.html',\
                    'testfile':'C:\\Users\\huwo\\Desktop\\1.自动化执行项目\\document\\'}
        for pathkey in filePath.keys():
            if flag == pathkey:
                #print(filePath[pathkey])
                return filePath[pathkey]

#file = FilePath()
#file.get_File_Path('reportPath')