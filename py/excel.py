#excel头文件
import  xlrd


#打开Excel
def opneExcel():

    try:
        #FilePath = r"C:\Users\i\Desktop\1612CET成绩单发放名单.xls"    【\】为转义符，r前缀使之无效
        FilePath = "C:/Users/i/Desktop/1612CET成绩单发放名单.xls"       #此法为windows和linux通用路径格式
        ExcelFile = xlrd.open_workbook(FilePath)
        #print("excel中sheet包含",ExcelFile.sheet_names())
        return  ExcelFile
    except:
      print("读取exce文件失败")

