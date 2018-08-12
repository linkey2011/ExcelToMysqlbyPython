import excel
import databseExecute
import pymysql.cursors

#打开excel
myExcel = excel.opneExcel()
print(myExcel.sheet_names()[0])   #打印打一个sheet的名字
count = len(myExcel.sheets())     #获取sheet数目
print(count)

#连数据库并获取游标
myConnect = databseExecute.connectMysql()
cursor = myConnect.cursor()
cursor.execute("use data")
#读取插入
for k in range(0,len(myExcel.sheets())):
    print("正在插入第",k+1,"个sheet的数据")
    sheet = myExcel.sheet_by_index(k)
    print(sheet.name)
    databseExecute.myindert(cursor,myConnect,sheet)


