# -*- coding: UTF-8 -*-
import tkinter as tk
import time
import threading
import Garbage_classification as gc



W = 480 #窗口宽度
H = 320 #窗口高度
result_H = 70   #显示结果的标签高度
img_W=120 #图片宽度
img_H=120 #图片高度
btnBoderWidth = 0.5 #边框宽度
btnWidth = 480 #按钮宽度
btnHeight = 130 #按钮高度
msFont = '微软雅黑' #字体
fontSize = 40 #字体大小

mainWindows = tk.Tk()
mainWindows.title('凌云智能垃圾分类桶')
mainWindows.minsize(W,H)



def down(color):
    global img_khsw
    global img_glj
    global img_slj
    global img_yhlj
    global khsw
    global glj
    global slj
    global yhlj
    global str_result
    global result

    # img_khsw = tk.PhotoImage(file="img/可回收物off.png")
    # img_glj = tk.PhotoImage(file="img/干垃圾off.png")
    # img_slj = tk.PhotoImage(file="img/湿垃圾off.png")
    # img_yhlj = tk.PhotoImage(file="img/有害垃圾off.png")

    result = tk.Label(mainWindows,font=(msFont,fontSize),bg='white',fg=color,textvariable=str_result)
    result.place(width=W,height=result_H) #显示结果标签

    khsw=tk.Label(compound='center',image= img_khsw)
    khsw.place(x=0,y=result_H,width=img_W,height=img_H)
    glj=tk.Label(compound='center',image= img_glj)
    glj.place(x=img_W,y=result_H,width=img_W,height=img_H)
    slj=tk.Label(compound='center',image= img_slj)
    slj.place(x=img_W*2,y=result_H,width=img_W,height=img_H)
    yhlj=tk.Label(compound='center',image= img_yhlj)
    yhlj.place(x=img_W*3,y=result_H,width=img_W,height=img_H)



def loading():
    global str_result
    global result
    str_result.set("运行中")
    result = tk.Label(mainWindows,font=(msFont,fontSize),bg='white',fg='orange',textvariable=str_result)
    result.place(width=W,height=result_H)



def init():
    global W
    global H
    global result_H
    global img_W
    global img_H
    global btnBoderWidth
    global btnWidth
    global btnHeight
    global msFont
    global fontSize 
    global img_khsw
    global img_glj
    global img_slj
    global img_yhlj
    global khsw
    global glj
    global slj
    global yhlj
    global str_result
    global result

    time.sleep(3)
    
    str_result = tk.StringVar()
    str_result.set("闲置中")#结果标签初始化

    img_khsw = tk.PhotoImage(file="img/可回收物off.png")
    img_glj = tk.PhotoImage(file="img/干垃圾off.png")
    img_slj = tk.PhotoImage(file="img/湿垃圾off.png")
    img_yhlj = tk.PhotoImage(file="img/有害垃圾off.png")#垃圾类别图片初始化

    result = tk.Label(mainWindows,font=(msFont,fontSize),bg='white',fg='gray',textvariable=str_result)
    result.place(width=W,height=result_H) #显示结果标签

    khsw=tk.Label(compound='center',image= img_khsw)
    khsw.place(x=0,y=result_H,width=img_W,height=img_H)
    glj=tk.Label(compound='center',image= img_glj)
    glj.place(x=img_W,y=result_H,width=img_W,height=img_H)
    slj=tk.Label(compound='center',image= img_slj)
    slj.place(x=img_W*2,y=result_H,width=img_W,height=img_H)
    yhlj=tk.Label(compound='center',image= img_yhlj)
    yhlj.place(x=img_W*3,y=result_H,width=img_W,height=img_H)#显示垃圾类别图片

    button_start2 = tk.Button(mainWindows,font=(msFont,fontSize),text='运行',bd=btnBoderWidth,command=thread)
    button_start2.place(x=0,y=img_H+result_H,width=btnWidth,height=btnHeight)



def click():#运行程序
    global img_khsw
    global img_glj
    global img_slj
    global img_yhlj
    global khsw
    global glj
    global slj
    global yhlj
    global str_result
    global result

    token=gc.token()
    data=gc.baiduace(token)
    type=gc.classify(data)#获取Garbage_classification.py文件运行的数据

    if type=='可回收垃圾':
        img_khsw = tk.PhotoImage(file="img/可回收物on.png")
        img_glj = tk.PhotoImage(file="img/干垃圾off.png")
        img_slj = tk.PhotoImage(file="img/湿垃圾off.png")
        img_yhlj = tk.PhotoImage(file="img/有害垃圾off.png")
        color='DeepSkyBlue'
    elif type=='干垃圾':
        img_khsw = tk.PhotoImage(file="img/可回收物off.png")
        img_glj = tk.PhotoImage(file="img/干垃圾on.png")
        img_slj = tk.PhotoImage(file="img/湿垃圾off.png")
        img_yhlj = tk.PhotoImage(file="img/有害垃圾off.png")
        color='black'
    elif type=='湿垃圾':
        img_khsw = tk.PhotoImage(file="img/可回收物off.png")
        img_glj = tk.PhotoImage(file="img/干垃圾off.png")
        img_slj = tk.PhotoImage(file="img/湿垃圾on.png")
        img_yhlj = tk.PhotoImage(file="img/有害垃圾off.png")
        color='green'
    elif type=='有害垃圾':
        img_khsw = tk.PhotoImage(file="img/可回收物off.png")
        img_glj = tk.PhotoImage(file="img/干垃圾off.png")
        img_slj = tk.PhotoImage(file="img/湿垃圾off.png")
        img_yhlj = tk.PhotoImage(file="img/有害垃圾on.png")
        color='red'

    str_result.set(type)
    result = tk.Label(mainWindows,font=(msFont,fontSize),bg='white',fg=color,textvariable=str_result)
    result.place(width=W,height=result_H) 

    down(color)



def thread():
    t1 = threading.Thread(target=loading)
    t2 = threading.Thread(target=click)
    t3 = threading.Thread(target=init)
    t1.start()
    t2.setDaemon(t1)
    t2.start()
    t3.setDaemon(t2)
    t3.start()



str_process = tk.StringVar()
str_process.set("")
str_result = tk.StringVar()
str_result.set("闲置中")#结果标签初始化

img_khsw = tk.PhotoImage(file="img/可回收物off.png")
img_glj = tk.PhotoImage(file="img/干垃圾off.png")
img_slj = tk.PhotoImage(file="img/湿垃圾off.png")
img_yhlj = tk.PhotoImage(file="img/有害垃圾off.png")#垃圾类别图片初始化

result = tk.Label(mainWindows,font=(msFont,fontSize),bg='white',fg='gray',textvariable=str_result)
result.place(width=W,height=result_H) #显示结果标签

khsw=tk.Label(compound='center',image= img_khsw)
khsw.place(x=0,y=result_H,width=img_W,height=img_H)
glj=tk.Label(compound='center',image= img_glj)
glj.place(x=img_W,y=result_H,width=img_W,height=img_H)
slj=tk.Label(compound='center',image= img_slj)
slj.place(x=img_W*2,y=result_H,width=img_W,height=img_H)
yhlj=tk.Label(compound='center',image= img_yhlj)
yhlj.place(x=img_W*3,y=result_H,width=img_W,height=img_H)#显示垃圾类别图片

button_start2 = tk.Button(mainWindows,font=(msFont,fontSize),text='运行',bd=btnBoderWidth,command=thread)
button_start2.place(x=0,y=img_H+result_H,width=btnWidth,height=btnHeight)


mainWindows.mainloop()