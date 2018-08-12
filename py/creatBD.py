import excel
import databseExecute
import pymysql.cursors

#连数据库并获取游标
myConnect = databseExecute.connectMysql()
cursor = myConnect.cursor()
#创建库和表
databseExecute.CreatDbAndTable(cursor,myConnect)
print("建表成功")
