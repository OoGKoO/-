import ai
from config import *

token = ai.GetBaiduToken()
data = ai.BaiduAce(token)#显示的数据仍然是5个
selectData=[]
for i in data:#筛选出三个字以内的垃圾名，提高检测效率
    if len(i['name']) <= 3:
        selectData.append(i)
type = ai.Classify(selectData)
print(type)