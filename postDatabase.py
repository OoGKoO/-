import pymysql,json


def PostDatabase(list):#导入到数据库
    conn = pymysql.connect(host='',
                            db='Garbage_Classification',
                            user='root',
                            passwd='123456',
                            port=3306,
                            charset='utf8')#连接数据库
    cursor = conn.cursor()#创建游标

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



def GetTypes():#获取数据集的类别数据
    with open("./category.json",encoding='utf-8') as data:#获取category.json数据集的垃圾类别数据
        data = json.load(data)['data']
        slj=data['1']#湿垃圾
        glj=data['2']#干垃圾
        khsw=data['3']#可回收物
        yhlj=data['4']#有害垃圾
        return slj+glj+khsw+yhlj#返回列表嵌套字典


data=GetTypes()
PostDatabase(data)