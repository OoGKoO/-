# -*- coding: UTF-8 -*-
import requests
import base64

def token():
    AK='Runpjy2QX7h5XKi3mz8nGKVm'
    SK='cG4HKfw5H6BqSRTOpGFXG5CPMKdGsKQP'
    request_url = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id='+AK+'&client_secret='+SK
    response = requests.get(request_url)
    try:
        access_token = response.json()['access_token']
        echo="成功获取access_token\n"
    except:
        echo="access_token获取失败\n"
    finally:
        print(echo)
        return access_token



def baiduace(access_token):
    #识别图片，图片为py文件根目录的temp.jpg
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v2/advanced_general"
    # 二进制方式打开图片文件
    f = open('temp.jpg', 'rb')
    img = base64.b64encode(f.read())
    f.close()
    params = {"image":img}
    request_url = request_url + "?access_token=" + str(access_token)
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    try:
        garbage1=response.json()['result'][0]['keyword']
        percent1=str(round(response.json()['result'][0]['score']*100,2))+'%'
        garbage2=response.json()['result'][1]['keyword']
        percent2=str(round(response.json()['result'][1]['score']*100,2))+'%'
        garbage3=response.json()['result'][2]['keyword']
        percent3=str(round(response.json()['result'][2]['score']*100,2))+'%'
        garbage4=response.json()['result'][3]['keyword']
        percent4=str(round(response.json()['result'][3]['score']*100,2))+'%'
        garbage5=response.json()['result'][4]['keyword']
        percent5=str(round(response.json()['result'][4]['score']*100,2))+'%'
        data={garbage1:percent1,garbage2:percent2,garbage3:percent3,garbage4:percent4,garbage5:percent5}
        echo='该图片显示的可能是：\n'+garbage1+'，概率：'+percent1+'\n'+garbage2+'，概率：'+percent2+'\n'+garbage3+'，概率：'+percent3+'\n'+garbage4+'，概率：'+percent4+'\n'+garbage5+'，概率：'+percent5+'\n'
              

    except:
        echo="图像识别失败"

    finally:
        print(echo)
        return data
    


def classify(select_data):
    for i in select_data:
        try:
            request_url = 'https://api.muxiaoguo.cn/api/lajifl?api_key=9319f855d710556c&m='+i
            response = requests.get(request_url)
            type=response.json()['data']['type']#垃圾类别
            concept=response.json()['data']['description']['Concept']#垃圾基本概念
            including=response.json()['data']['description']['Including']#垃圾主要包括
            release_requirement=response.json()['data']['description']['Release_requirement']#投放要求
            echo='垃圾类别：'+type+'\n垃圾基本概念：'+concept+'\n垃圾主要包括：'+including+'\n投放要求：'+release_requirement

            if concept is not None:
                print("识别了"+i)
                break
        except:
            echo='垃圾分类失败，可能是图片过于离谱，或者服务器故障'

    print(echo)
    return type

# token=token()
# data=baiduace(token)#显示的数据仍然是5个
# select_data=dict(data)#复制字典
# for i in list(select_data.keys()):#筛选出三个字以内的垃圾名，提高检测效率
#     if len(i)>3:
#         del select_data[i]
# type=classify(select_data)

