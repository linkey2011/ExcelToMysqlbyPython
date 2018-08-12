#mysql头文件
import pymysql
import pymysql.cursors

#创建数据库连接
def connectMysql():
    try:
        connect = pymysql.Connect(
            host    = '127.0.0.1',
            port    = 3306,
            user    = 'root',
            passwd  = 'root',
            charset = 'utf8'
        )
        return connect
    except:
        print("连接数据库失败")
#建库和表
def CreatDbAndTable(cursor,connect):

    sql_creatTable="""create table data
    (
     id         bigint not null auto_increment,
     department varchar(64), 
     profession varchar(64), 
     grade      varchar(64), 
     studentId  varchar(64), 
     name       varchar(64), 
     sex        varchar(64), 
     cardId     varchar(64), 
     primary    key (id)
    )"""

    try:
        ## 使用 cursor() 方法创建一个游标对象，cursor
        cursor=connect.cursor()
        cursor.execute("drop database if exists data")
        cursor.execute("create database data")  #数据名 data
        #选择 students 这个数据库
        cursor.execute("use data")
        #表名 data
        cursor.execute("drop table if exists data")
        cursor.execute(sql_creatTable)
        connect.commit()
    except:
        print('建表失败')
#读取并插入
def myindert(cursor,connect,sheet):
    try:
        #逐行插入数据
        for k in range(1,sheet.nrows):   #
            department = sheet.cell(k, 2).value
            profession = sheet.cell(k, 3).value
            grade      = sheet.cell(k, 4).value
            studentId  = sheet.cell(k, 6).value
            name       = sheet.cell(k, 7).value
            sex        = sheet.cell(k, 8).value
            cardId     = sheet.cell(k, 9).value

            # sql = "INSERT INTO data (department,profession,grade,studentId,name,sex,cardId) " \
            #       "VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s');"
            # data = (department,profession,grade,studentId,name,sex,cardId)
            # cursor.execute(sql % data)
            sql = "INSERT INTO ctgudata (department,profession,grade,studentId,name,sex,cardId)" \
                  "VALUES ( '%s', '%s', '%s', '%s', '%s', '%s', '%s' );"
            data = (department,profession,grade,studentId,name,sex,cardId)
            cursor.execute(sql % data)
            connect.commit()
            print('已插入第',k,'条')
    except:
        print('插入数据出错')
#数据库查询
def myselect(cursor,connect,whatDoYouWant):


    sql = "select * from data where concat(department,profession,grade,studentId,name,sex,cardId) like  '%%%%%s%%%%'"
    data = whatDoYouWant
    cursor.execute(sql % data)
    for row in cursor.fetchall():
        id         = row[0]
        department = row[1]
        profession = row[2]
        grade      = row[3]
        studentId  = row[4]
        name       = row[5]
        sex        = row[6]
        cardId     = row[7]
        print(id,department,profession,grade,studentId,name,sex,cardId)




