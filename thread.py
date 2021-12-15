import threading
import gui
from config import *
from getDatabase import *


#主页面点击运行按钮时调用Thread函数,多线程运行程序

def Thread():#多线程运行处理并发
    t1 = threading.Thread(target=gui.loading)#等待
    t2 = threading.Thread(target=gui.click)#执行
    # t3 = threading.Thread(target=init)#初始化
    t1.start()
    t2.setDaemon(t1)
    t2.start()
    # t3.setDaemon(t2)
    # t3.start()