import databseExecute


#连数据库并获取游标
myConnect = databseExecute.connectMysql()
cursor = myConnect.cursor()
cursor.execute("use data")


whatDoYouWant = input()

databseExecute.myselect(cursor,cursor,whatDoYouWant)