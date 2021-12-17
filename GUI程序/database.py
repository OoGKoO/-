import pymysql,json
import time


def PostDatabase():#导入到数据库
    list=[]
    with open("./category.json",encoding='utf-8') as data:#获取category.json数据集的垃圾类别数据
        data = json.load(data)['data']
        slj=data['1']#湿垃圾
        glj=data['2']#干垃圾
        khsw=data['3']#可回收物
        yhlj=data['4']#有害垃圾
        list=slj+glj+khsw+yhlj#格式为列表嵌套字典

    conn = pymysql.connect(host='',
                            db='Garbage_Classification',
                            user='root',
                            passwd='123456',
                            port=3306,
                            charset='utf8')#连接数据库
    cursor = conn.cursor()#创建游标
    cursor.execute('truncate category')#先清空表

    sql='insert into category(name,category) values '
    vals=''
    num=0

    for i in list:
        num+=1
        val=(i['n'],i['c'])
        vals+=str(val)
        if num<len(list):
            vals+=','
    sql+=vals
    cursor.execute(sql)
    conn.commit()# 数据表内容有更新，必须使用到该语句
    print(sql)

    cursor.close()#清除游标
    conn.close()#断开数据库



def GetDatabase():#获取垃圾类型数据,用于程序运行时预先获取数据库垃圾类型，提高运行速度
    conn = pymysql.connect(host='',
                            db='Garbage_Classification',
                            user='root',
                            passwd='123456',
                            port=3306,
                            charset='utf8')#连接数据库
    cursor = conn.cursor()#创建游标

    cursor.execute("select * from category")
    results = cursor.fetchall()#输出字典
    cursor.close()#清除游标
    conn.close()#断开数据库

    return results



def PostLog(name,category):#运行数据上传到数据库running_log表
    conn = pymysql.connect(host='',
                            db='Garbage_Classification',
                            user='root',
                            passwd='123456',
                            port=3306,
                            charset='utf8')#连接数据库
    cursor = conn.cursor()#创建游标

    if category==1:
        category='湿垃圾'
    elif category==2:
        category='干垃圾'
    elif category==3:
        category='可回收物'
    elif category==4:
        category='有害垃圾'
    
    times=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    sql='insert into running_log values (%s,%s,%s)'
    val=(name,category,times)

    cursor.execute(sql,val)
    conn.commit()# 数据表内容有更新，必须使用到该语句

    cursor.close()#清除游标
    conn.close()#断开数据库



# PostLog('苹果',1)


