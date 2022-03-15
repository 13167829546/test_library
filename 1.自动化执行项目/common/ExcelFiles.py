import xlrd
from common.FilePath import FilePath

class File_Excel():
    def __init__(self):
        #获取文件路径
        self.datePath = FilePath().get_File_Path('fileDataPath')
        print("lll")
    #登录URL
    def get_OpenBrowser(self):
        # 打开excel
        print(self.datePath)
        items = xlrd.open_workbook(self.datePath)
        # 找到需要定位的sheet页
        sheetLogin = items.sheet_by_name('登录URL')
        # 在sheet页中定位到需要的元素
        coloms = sheetLogin.col_values(2, 1, 10)
        listcoloms = []
        for colom in coloms:
            listcoloms.append(colom)
            #print(listcoloms)
        return listcoloms

    #登录页信息获取
    def get_LoginFiles(self):
        #打开excel
        items = xlrd.open_workbook(self.datePath)
        #找到需要定位的sheet页
        sheetLogin = items.sheet_by_name('登录')
        #print(sheetLogin)
        #在sheet页中定位到需要的元素
        coloms = sheetLogin.col_values(2,1,30)
        listcoloms = []
        for colom in coloms:
            listcoloms.append(colom)
        #print(listcoloms)
        return listcoloms

    #首页面元素获取
    def get_HomePage(self):
        # 打开excel
        items = xlrd.open_workbook(self.datePath)
        # 找到需要定位的sheet页
        sheetCreatePlan = items.sheet_by_name('首页面')
        # 在sheet页中定位到需要的元素
        coloms = sheetCreatePlan.col_values(2, 1, 10)
        listcoloms = []
        for colom in coloms:
            listcoloms.append(colom)
        #print(listcoloms)
        return listcoloms

    # 高铁运维元素获取
    def get_HighSpeedTrainMaintenance(self):
        # 打开excel
        items = xlrd.open_workbook(self.datePath)
        # 找到需要定位的sheet页
        sheetCreatePlan = items.sheet_by_name('高铁运维')
        # 在sheet页中定位到需要的元素
        coloms = sheetCreatePlan.col_values(2, 1, 10)
        listcoloms = []
        for colom in coloms:
            listcoloms.append(colom)
        # print(listcoloms)
        return listcoloms

    #创建日计划
    def get_CreatePlanFile(self):
        # 打开excel
        items = xlrd.open_workbook(self.datePath)
        # 找到需要定位的sheet页
        sheetCreatePlan = items.sheet_by_name('周计划')
        # 在sheet页中定位到需要的元素
        coloms = sheetCreatePlan.col_values(2, 1, 50)
        listcoloms = []
        for colom in coloms:
            listcoloms.append(colom)
        #print(listcoloms)
        return listcoloms

    #存在的iframe
    def get_iframeFile(self):
        # 打开excel
        items = xlrd.open_workbook(self.datePath)
        # 找到需要定位的sheet页
        sheetiframe = items.sheet_by_name('iframe')
        coloms = sheetiframe.col_values(2, 1, 10)
        listcoloms = []
        for colom in coloms:
            listcoloms.append(colom)
        #print(listcoloms)
        return listcoloms

    #创建周计划中的值
    def get_CreatePlanValues(self):
        # 打开excel
        items = xlrd.open_workbook(self.datePath)
        # 找到需要定位的sheet页
        sheetCreatePlan = items.sheet_by_name('周计划')
        # 在sheet页中定位到需要的元素
        coloms = sheetCreatePlan.col_values(3, 1, 50)
        listcoloms = []
        for colom in coloms:
            listcoloms.append(colom)
        print(listcoloms[35])
        return listcoloms

    #检测实验室审核
    def get_jcsys_Audit_Plan(self):
        # 打开excel
        items = xlrd.open_workbook(self.datePath)
        # 找到需要定位的sheet页
        sheetiframe = items.sheet_by_name('检测实验室审核周计划')
        coloms = sheetiframe.col_values(2, 1, 10)
        listcoloms = []
        for colom in coloms:
            listcoloms.append(colom)
        # print(listcoloms)
        return listcoloms

    #工区安全风险分析与工作票
    def get_risk_workSheet(self):
        # 打开excel
        items = xlrd.open_workbook(self.datePath)
        # 找到需要定位的sheet页
        sheetiframe = items.sheet_by_name('工区安全风险分析与工作票')
        coloms = sheetiframe.col_values(2, 1, 30)
        listcoloms = []
        for colom in coloms:
            listcoloms.append(colom)
        # print(listcoloms)
        return listcoloms


    #工作领导人审核
    def get_leader_auditPlan(self):
        # 打开excel
        items = xlrd.open_workbook(self.datePath)
        # 找到需要定位的sheet页
        sheetiframe = items.sheet_by_name('领导人审核')
        coloms = sheetiframe.col_values(2, 1, 30)
        listcoloms = []
        for colom in coloms:
            listcoloms.append(colom)
        # print(listcoloms)
        return listcoloms

    #车间审核工作票
    def get_workshop_auditWorkSheet(self):
        # 打开excel
        items = xlrd.open_workbook(self.datePath)
        # 找到需要定位的sheet页
        sheetiframe = items.sheet_by_name('检测实验室审核工作票')
        coloms = sheetiframe.col_values(2, 1, 30)
        listcoloms = []
        for colom in coloms:
            listcoloms.append(colom)
        # print(listcoloms)
        return listcoloms


    #领导人方案编制
    def get_leader_schemeDraft(self):
        # 打开excel
        items = xlrd.open_workbook(self.datePath)
        # 找到需要定位的sheet页
        sheetiframe = items.sheet_by_name('领导人方案编制')
        coloms = sheetiframe.col_values(2, 1, 30)
        listcoloms = []
        for colom in coloms:
            listcoloms.append(colom)
        # print(listcoloms)
        return listcoloms



    #检测实验室审核方案编制
    def get_jcsys_audit_schemeDraft(self):
        # 打开excel
        items = xlrd.open_workbook(self.datePath)
        # 找到需要定位的sheet页
        sheetiframe = items.sheet_by_name('实验室审核方案编制')
        coloms = sheetiframe.col_values(2, 1, 30)
        listcoloms = []
        for colom in coloms:
            listcoloms.append(colom)
        # print(listcoloms)
        return listcoloms



    #工区领导结束方案编制
    def get_gqleader_end_schemeDraft(self):
        # 打开excel
        items = xlrd.open_workbook(self.datePath)
        # 找到需要定位的sheet页
        sheetiframe = items.sheet_by_name('工区领导结束方案编制')
        coloms = sheetiframe.col_values(2, 1, 30)
        listcoloms = []
        for colom in coloms:
            listcoloms.append(colom)
        # print(listcoloms)
        return listcoloms

    #工区领导结束方案编制
    def get_gqleader_division(self):
        # 打开excel
        items = xlrd.open_workbook(self.datePath)
        # 找到需要定位的sheet页
        sheetiframe = items.sheet_by_name('工区领导结束分工会')
        coloms = sheetiframe.col_values(2, 1, 30)
        listcoloms = []
        for colom in coloms:
            listcoloms.append(colom)
        # print(listcoloms)
        return listcoloms


    #工区领导收工会
    def get_gqleader_acceptdivision(self):
        # 打开excel
        items = xlrd.open_workbook(self.datePath)
        # 找到需要定位的sheet页
        sheetiframe = items.sheet_by_name('工区领导收工会')
        coloms = sheetiframe.col_values(2, 1, 30)
        listcoloms = []
        for colom in coloms:
            listcoloms.append(colom)
        # print(listcoloms)
        return listcoloms


    #工区领导台账记录
    def get_gqleader_accountrecord(self):
        # 打开excel
        items = xlrd.open_workbook(self.datePath)
        # 找到需要定位的sheet页
        sheetiframe = items.sheet_by_name('工区领导台账记录')
        coloms = sheetiframe.col_values(2, 1, 30)
        listcoloms = []
        for colom in coloms:
            listcoloms.append(colom)
        # print(listcoloms)
        return listcoloms

# file1 = File_Excel()
# file1.get_LoginFiles()
