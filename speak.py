import pyttsx3


def SpeakType(name,category):
    str=name+','

    if category==1:
        str+='湿垃圾'
    elif category==2:
        str+='肝垃圾'
    elif category==3:
        str+='可回收物'
    elif category==4:
        str+='有害垃圾'

    engine = pyttsx3.init()#初始化
    engine.say(str)#说什么
    engine.runAndWait()# #开始说

# speak('苹果',1)
    
    


