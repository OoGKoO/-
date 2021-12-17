# -*- coding: UTF-8 -*-
import requests,base64,pymysql
from config import *


#该模块用于识别temp.jpg图片

def GetBaiduToken():#获取百度开放接口Token
    AK = 'Runpjy2QX7h5XKi3mz8nGKVm'
    SK = 'cG4HKfw5H6BqSRTOpGFXG5CPMKdGsKQP'
    url = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id='+AK+'&client_secret='+SK
    response = requests.get(url)
    try:
        access_token = response.json()['access_token']
        echo = "成功获取access_token\n"
    except:
        echo = "access_token获取失败\n"
    finally:
        print(echo)
        return access_token



def BaiduAce(token):
    #识别图片，图片为py文件根目录的temp.jpg
    file = open('temp.jpg', 'rb')
    img = base64.b64encode(file.read())
    file.close()
    params = {"image": img}
    url="https://aip.baidubce.com/rest/2.0/image-classify/v2/advanced_general?access_token=" + str(token)
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(url, data=params, headers=headers)

    datalist=[]
    echo='该图片显示的可能是：\n'

    try:
        for i in response.json()['result']:
            dict={}
            dict['name']=i['keyword']
            dict['percent']=str(round(i['score']*100, 2))+'%'
            datalist.append(dict)
            echo+=dict['name'] + '，概率：' + dict['percent'] + '\n'

    except:
        echo = "图像识别失败"
    
    finally:
        print(echo)
        return datalist



def Classify(datalist):#与数据库的数据比对，返回类型：1为湿垃圾，2为干垃圾，3为可回收物，4为有害垃圾
    types={}
    for data in datalist:
        for i in database:
            if data['name']==i[1]:
                types['name']=i[1]
                types['category']=i[2]
                print('识别了'+types['name'])
                return types

    print('垃圾分类失败，无法识别垃圾类型，可能是数据库未收录')
    return types



# def run():
#     token=GetBaiduToken()
#     datalist=BaiduAce(token)
#     print(datalist)
#     types=Classify(datalist)



# if __name__=='__main__':
#     run()