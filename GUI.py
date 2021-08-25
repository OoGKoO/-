# -*- coding: UTF-8 -*-
import tkinter as tk
import time
import threading
import Garbage_classification as gc
import Text_To_Speech as tts
# from picamera import PiCamera


W = 800  # 窗口宽度
H = 600  # 窗口高度
result_H = 150  # 显示结果的标签高度
img_W = 200  # 图片宽度
img_H = 200  # 图片高度
btnBoderWidth = 0.5  # 边框宽度
btnHeight = 250  # 按钮高度
msFont = '微软雅黑'  # 字体
fontSize = 80  # 字体大小

mainWindows = tk.Tk()
mainWindows.title('凌云智能垃圾分类桶')
mainWindows.minsize(W, H)  # 设置窗口


def down(color):  # 结果输出
    global img_khsw
    global img_glj
    global img_slj
    global img_yhlj
    global khsw
    global glj
    global slj
    global yhlj
    global str_result
    global data_result
    global result

    result = tk.Label(mainWindows, font=(msFont, fontSize),
                      bg='white', fg=color, textvariable=str_result)
    result.place(width=W, height=result_H)  # 显示垃圾类别文本和文本颜色

    khsw = tk.Label(compound='center', image=img_khsw)
    khsw.place(x=0, y=result_H, width=img_W, height=img_H)
    glj = tk.Label(compound='center', image=img_glj)
    glj.place(x=img_W, y=result_H, width=img_W, height=img_H)
    slj = tk.Label(compound='center', image=img_slj)
    slj.place(x=img_W*2, y=result_H, width=img_W, height=img_H)
    yhlj = tk.Label(compound='center', image=img_yhlj)
    yhlj.place(x=img_W*3, y=result_H, width=img_W, height=img_H)  # 把垃圾的类别高亮显示

    data_label = tk.Label(mainWindows, font=(
        msFont, fontSize-50), bg='white', fg='black', textvariable=data_result)
    data_label.place(x=0, y=img_H+result_H, width=W, height=btnHeight)


def loading():  # 后台代码运行时提示等待
    global str_result
    global result
    str_result.set("运行中")
    result = tk.Label(mainWindows, font=(msFont, fontSize),
                      bg='white', fg='orange', textvariable=str_result)
    result.place(width=W, height=result_H)

    data_result.set("该图片显示的可能是\n\n......")
    data_label = tk.Label(mainWindows, font=(
        msFont, fontSize-50), bg='white', fg='black', textvariable=data_result)
    data_label.place(x=0, y=img_H+result_H, width=W, height=btnHeight)


def click():  # 点击按钮运行程序
    global img_khsw
    global img_glj
    global img_slj
    global img_yhlj
    global khsw
    global glj
    global slj
    global yhlj
    global str_result
    global data_result

    # camera = PiCamera()
    # camera.resolution=(480,320)
    # camera.start_preview(alpha=200)
    # camera.capture('temp.jpg',use_video_port = False)
    # camera.stop_preview()
    # camera.close()

    token = gc.token()
    data = gc.baiduace(token)  # 显示的数据仍然是5个
    select_data = dict(data)  # 复制字典
    for i in list(select_data.keys()):  # 筛选出三个字以内的垃圾名，提高检测效率
        if len(i) > 3:
            del select_data[i]
    type = gc.classify(select_data)  # 获取Garbage_classification.py文件运行的数据

    # type='可回收垃圾'
    # data={'鱼钩': '19.24%', '剪刀': '14.44%', '夹子': '9.87%', 'N': '5.16%', '眼镜': '0.45%'}#测试用
    garbage = []  # 垃圾列表
    percent = []  # 概率列表
    for i in data.keys():
        garbage.append(i)
    for i in data.values():
        percent.append(i)

    if type == '可回收垃圾':
        # 根据垃圾类别高亮不同照片，同时设置结果标签文本
        img_khsw = tk.PhotoImage(file="img/可回收物on.png")
        color = 'DeepSkyBlue'
        str_result.set(type)
    elif type == '干垃圾':
        img_glj = tk.PhotoImage(file="img/干垃圾on.png")
        color = 'black'
        str_result.set(type)
    elif type == '湿垃圾':
        img_slj = tk.PhotoImage(file="img/湿垃圾on.png")
        color = 'green'
        str_result.set(type)
    elif type == '有害垃圾':
        img_yhlj = tk.PhotoImage(file="img/有害垃圾on.png")
        color = 'red'
        str_result.set(type)
    else:
        color = 'gray'
        str_result.set('未识别出垃圾类型')

    data_result.set("\n"+garbage[0]+"，概率："+percent[0]+"\n" +
                    garbage[1]+"，概率："+percent[1]+"\n" +
                    garbage[2]+"，概率："+percent[2]+"\n" +
                    garbage[3]+"，概率："+percent[3]+"\n" +
                    garbage[4]+"，概率："+percent[4]+"\n")

    down(color)  # 结果输出
    tts.speak(type)  # 语音提示结果


def init():  # 按钮按下后7秒，系统初始化
    global W
    global H
    global result_H
    global img_W
    global img_H
    global btnBoderWidth
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

    time.sleep(7)

    str_result = tk.StringVar()
    str_result.set("闲置中")  # 结果标签初始化

    img_khsw = tk.PhotoImage(file="img/可回收物off.png")
    img_glj = tk.PhotoImage(file="img/干垃圾off.png")
    img_slj = tk.PhotoImage(file="img/湿垃圾off.png")
    img_yhlj = tk.PhotoImage(file="img/有害垃圾off.png")  # 垃圾类别图片初始化

    result = tk.Label(mainWindows, font=(msFont, fontSize),
                      bg='white', fg='gray', textvariable=str_result)
    result.place(width=W, height=result_H)  # 显示结果标签

    khsw = tk.Label(compound='center', image=img_khsw)
    khsw.place(x=0, y=result_H, width=img_W, height=img_H)
    glj = tk.Label(compound='center', image=img_glj)
    glj.place(x=img_W, y=result_H, width=img_W, height=img_H)
    slj = tk.Label(compound='center', image=img_slj)
    slj.place(x=img_W*2, y=result_H, width=img_W, height=img_H)
    yhlj = tk.Label(compound='center', image=img_yhlj)
    yhlj.place(x=img_W*3, y=result_H, width=img_W, height=img_H)  # 显示垃圾类别图片

    button_start2 = tk.Button(mainWindows, font=(
        msFont, fontSize), text='运行', bd=btnBoderWidth, command=thread)
    button_start2.place(x=0, y=img_H+result_H, width=W, height=btnHeight)


def thread():  # 多线程运行处理并发
    t1 = threading.Thread(target=loading)  # 等待
    t2 = threading.Thread(target=click)  # 执行
    t3 = threading.Thread(target=init)  # 初始化
    t1.start()
    t2.setDaemon(t1)
    t2.start()
    t3.setDaemon(t2)
    t3.start()


str_process = tk.StringVar()
str_process.set("")
str_result = tk.StringVar()
str_result.set("闲置中")  # 结果标签初始化
data_result = tk.StringVar()
data_result.set("闲置中")  # 结果标签初始化

img_khsw = tk.PhotoImage(file="img/可回收物off.png")
img_glj = tk.PhotoImage(file="img/干垃圾off.png")
img_slj = tk.PhotoImage(file="img/湿垃圾off.png")
img_yhlj = tk.PhotoImage(file="img/有害垃圾off.png")  # 垃圾类别图片初始化

result = tk.Label(mainWindows, font=(msFont, fontSize),
                  bg='white', fg='gray', textvariable=str_result)
result.place(width=W, height=result_H)  # 显示结果标签

khsw = tk.Label(compound='center', image=img_khsw)
khsw.place(x=0, y=result_H, width=img_W, height=img_H)
glj = tk.Label(compound='center', image=img_glj)
glj.place(x=img_W, y=result_H, width=img_W, height=img_H)
slj = tk.Label(compound='center', image=img_slj)
slj.place(x=img_W*2, y=result_H, width=img_W, height=img_H)
yhlj = tk.Label(compound='center', image=img_yhlj)
yhlj.place(x=img_W*3, y=result_H, width=img_W, height=img_H)  # 显示垃圾类别图片

button_start2 = tk.Button(mainWindows, font=(
    msFont, fontSize), text='运行', bd=btnBoderWidth, command=thread)
button_start2.place(x=0, y=img_H+result_H, width=W, height=btnHeight)
# 窗口初始化

mainWindows.mainloop()  # 显示窗口
