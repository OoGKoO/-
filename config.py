import tkinter as tk
from getDatabase import *


#页面模块参数，单独写在config.py文件，方便其他模块修改

#--------------------------------------页面数据参数--------------------------------------
W = 800#窗口宽度
H = 600#窗口高度
result_H = 150#显示结果的标签高度
img_W = 200#图片宽度
img_H = 200#图片高度
btnBoderWidth = 0.5#边框宽度
btnHeight = 250#按钮高度
msFont = '微软雅黑'#字体
fontSize = 80#字体大小

mainWindows = tk.Tk()
mainWindows.title('凌云智能垃圾分类桶')
mainWindows.minsize(W, H)#设置窗口

str_process = tk.StringVar()
str_process.set("")
str_result = tk.StringVar()
str_result.set("闲置中")#结果标签初始化
data_result = tk.StringVar()
data_result.set("闲置中")#结果标签初始化

img_khsw = tk.PhotoImage(file="img/可回收物off.png")
img_glj = tk.PhotoImage(file="img/干垃圾off.png")
img_slj = tk.PhotoImage(file="img/湿垃圾off.png")
img_yhlj = tk.PhotoImage(file="img/有害垃圾off.png")#垃圾类别图片初始化
#--------------------------------------页面数据参数--------------------------------------

database=GetDatabase()



