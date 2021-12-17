import ai
import time
import thread
from config import *
from speak import *
from database import *


#GUI各种触发事件

def Loading():#点击运行按钮，后台正在运行时显示“运行中”
    str_result.set("运行中")
    result = tk.Label(mainWindows, font=(msFont, fontSize),bg='white', fg='orange', textvariable=str_result)
    result.place(width=W, height=result_H)

    data_result.set("该图片显示的可能是\n\n......")
    data_label = tk.Label(mainWindows, font=(msFont, fontSize-50), bg='white', fg='black', textvariable=data_result)
    data_label.place(x=0, y=img_H+result_H, width=W, height=btnHeight)



def Click():#后台运行
    global img_slj#垃圾类型图片全局变量
    global img_glj
    global img_khsw
    global img_yhlj

    # camera = PiCamera()#相机拍照
    # camera.resolution=(480,320)
    # camera.start_preview(alpha=200)
    # camera.capture('temp.jpg',use_video_port = False)
    # camera.stop_preview()
    # camera.close()

    token = ai.GetBaiduToken()
    data = ai.BaiduAce(token)#显示的数据仍然是5个

    # select_data = dict(data)#复制字典
    # for i in list(select_data.keys()):#筛选出三个字以内的垃圾名，提高检测效率
    #     if len(i) > 3:
    #         del select_data[i]

    type = ai.Classify(data)#获取ai.py文件运行的数据

    garbage = []#垃圾列表
    percent = []#概率列表
    for i in data:
        garbage.append(i['name'])
        percent.append(i['percent'])

    #根据垃圾类别高亮不同照片，同时设置结果标签文本
    if type['category'] == 1:#根据返回值判断类型
        img_slj = tk.PhotoImage(file="img/湿垃圾on.png")#更改显示的图片，使结果类型图片高亮
        color = 'green'#结果类型文本颜色
        str_result.set('湿垃圾')#结果文本
        angle=0#舵机转动角度
    
    elif type['category'] == 2:
        img_glj = tk.PhotoImage(file="img/干垃圾on.png")
        color = 'black'
        str_result.set('干垃圾')
        angle=45
    elif type['category'] == 3:
        img_khsw = tk.PhotoImage(file="img/可回收物on.png")
        color = 'DeepSkyBlue'
        str_result.set('可回收物')
        angle=90
    elif type['category'] == 4:
        img_yhlj = tk.PhotoImage(file="img/有害垃圾on.png")
        color = 'red'
        str_result.set('有害垃圾')
        angle=135
    else:
        color = 'gray'
        str_result.set('未识别出垃圾类型')

    data_result.set("\n"+garbage[0]+"，概率："+percent[0]+"\n" +
                         garbage[1]+"，概率："+percent[1]+"\n" +
                         garbage[2]+"，概率："+percent[2]+"\n" +
                         garbage[3]+"，概率："+percent[3]+"\n" +
                         garbage[4]+"，概率："+percent[4]+"\n")

    Done(color)#后台运行完成后改变GUI显示
    # SpeakType(type['name'],type['category'])#语音提示结果-------------------------------------------------------------------未来与舵机同步运行
    # # gpio.servo(angle)#转动舵机
    # PostLog(type['name'],type['category'])#运行记录上传至日志
    # time.sleep(1)
    thread.Running(type['name'],type['category'])#同时运行语音播报、舵机操作、写入日志
    Init()#全部运行结束后将GUI页面初始化



def Done(color):#后台运行完成后改变GUI显示
    result = tk.Label(mainWindows,font=(msFont, fontSize),bg='white',fg=color,textvariable=str_result)
    result.place(width=W, height=result_H)#显示垃圾类别文本和文本颜色

    khsw = tk.Label(compound='center', image=img_khsw)
    khsw.place(x=0, y=result_H, width=img_W, height=img_H)
    glj = tk.Label(compound='center', image=img_glj)
    glj.place(x=img_W, y=result_H, width=img_W, height=img_H)
    slj = tk.Label(compound='center', image=img_slj)
    slj.place(x=img_W*2, y=result_H, width=img_W, height=img_H)
    yhlj = tk.Label(compound='center', image=img_yhlj)
    yhlj.place(x=img_W*3, y=result_H, width=img_W, height=img_H)#把垃圾的类别高亮显示

    data_label = tk.Label(mainWindows,font=(msFont, fontSize-50),bg='white',fg='black',textvariable=data_result)
    data_label.place(x=0, y=img_H+result_H, width=W, height=btnHeight)



def Init():#GUI页面初始化
    global img_slj#垃圾类型图片全局变量
    global img_glj
    global img_khsw
    global img_yhlj
    
    str_result = tk.StringVar()
    str_result.set("闲置中")#结果标签初始化

    img_khsw = tk.PhotoImage(file="img/可回收物off.png")
    img_glj = tk.PhotoImage(file="img/干垃圾off.png")
    img_slj = tk.PhotoImage(file="img/湿垃圾off.png")
    img_yhlj = tk.PhotoImage(file="img/有害垃圾off.png")#垃圾类别图片初始化

    result = tk.Label(mainWindows,font=(msFont, fontSize),bg='white',fg='gray',textvariable=str_result)
    result.place(width=W, height=result_H)#显示结果标签

    khsw = tk.Label(compound='center', image=img_khsw)
    khsw.place(x=0, y=result_H, width=img_W, height=img_H)
    glj = tk.Label(compound='center', image=img_glj)
    glj.place(x=img_W, y=result_H, width=img_W, height=img_H)
    slj = tk.Label(compound='center', image=img_slj)
    slj.place(x=img_W*2, y=result_H, width=img_W, height=img_H)
    yhlj = tk.Label(compound='center', image=img_yhlj)
    yhlj.place(x=img_W*3, y=result_H, width=img_W, height=img_H)#显示垃圾类别图片

    button_start2 = tk.Button(mainWindows, font=(msFont, fontSize), text='运行', bd=btnBoderWidth, command=thread.Thread)
    button_start2.place(x=0, y=img_H+result_H, width=W, height=btnHeight)
