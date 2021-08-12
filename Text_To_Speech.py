import pyttsx3


def speak(word):
    if word == '干垃圾':  # 声调纠正
        word = '肝垃圾'
    # 说什么
    pt.say(word)
    # 开始说
    pt.runAndWait()


pt = pyttsx3.init()  # 初始化
