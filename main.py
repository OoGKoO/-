# -*- coding: UTF-8 -*-
import tkinter as tk
from thread import *
from config import *


#--------------------------------------页面模块--------------------------------------
result = tk.Label(mainWindows, font=(msFont, fontSize),bg='white', fg='gray', textvariable=str_result)
result.place(width=W, height=result_H)#显示结果标签

khsw = tk.Label(compound='center', image=img_khsw)
khsw.place(x=0, y=result_H, width=img_W, height=img_H)
glj = tk.Label(compound='center', image=img_glj)
glj.place(x=img_W, y=result_H, width=img_W, height=img_H)
slj = tk.Label(compound='center', image=img_slj)
slj.place(x=img_W*2, y=result_H, width=img_W, height=img_H)
yhlj = tk.Label(compound='center', image=img_yhlj)
yhlj.place(x=img_W*3, y=result_H, width=img_W, height=img_H)#显示垃圾类别图片

button_start2 = tk.Button(mainWindows, font=(msFont, fontSize), text='运行', bd=btnBoderWidth, command=Thread)#按下按钮运行多线程
button_start2.place(x=0, y=img_H+result_H, width=W, height=btnHeight)
#--------------------------------------页面模块--------------------------------------



def Run():
    
    mainWindows.mainloop()#显示窗口



if __name__=='__main__':
    Run()

