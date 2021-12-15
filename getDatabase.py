import pymysql


#该模块用于程序运行时预先获取数据库垃圾类型
#方便识别时不用调用数据库，提高运行速度

def GetDatabase():#获取垃圾类型数据
    conn = pymysql.connect(host='',
                            db='Garbage_Classification',
                            user='root',
                            passwd='123456',
                            port=3306,
                            charset='utf8')#连接数据库
    cursor = conn.cursor()#创建游标

    cursor.execute("select * from category")
    results = cursor.fetchall()#输出字典
    conn.close()

    return results



# data=GetDatabase()
# for i in data:
#     if i[1]=='苹果':
#         print(i)
