from flask import request,render_template
import pymysql
from app import regist_blue

@regist_blue.route('/')
def regist(): 
    return render_template('regist.html')

@regist_blue.route('/post_regist',methods=['post'])
def post_regist():
    if request.method=="POST":
        username=request.form['username']
        password=request.form['password']
        password2=request.form['password2']
        user_class=request.form['class']
        if username=='':
            report_text="用户名不能为空"
            print(report_text)
            return render_template('return.html',  title='失败!',report=report_text,url="/regist",url_name="注册页面")
        elif password=='':
            report_text="密码不能为空"
            print(report_text)
            return render_template('return.html',  title='失败!',report=report_text,url="/regist",url_name="注册页面")
        elif username=='':
            report_text="请填写 确认密码"
            print(report_text)
            return render_template('return.html',  title='失败!',report=report_text,url="/regist",url_name="注册页面")    
        elif password != password2:
            report_text="密码不一致"
            print(report_text)
            return render_template('return.html',  title='失败!',report=report_text,url="/regist",url_name="注册页面")
        elif user_class == "--用户身份--":
            report_text="请选择用户身份"
            print(report_text)
            return render_template('return.html',  title='失败!',report=report_text,url="/regist",url_name="注册页面")

        conn=pymysql.connect(host="",
                           user="root",
                           password="123456",
                           port=3306,
                           database="Garbage_Classification")         
        cursor=conn.cursor()
        sql="insert into admin(username,password,user_class) values (%s,%s,%s)"
        data=(username,password,user_class)

        try:
            cursor.execute(sql,data)
        except:
            report_text="该用户名已注册"
            print(report_text)
            return render_template('return.html',  title='失败!',report=report_text,url="/regist",url_name="注册页面")
        else:
            conn.commit()    # 数据表内容有更新，必须使用到该语句
            print(cursor.rowcount, "注册成功。")
            report_text=str(username)+"用户注册成功"
            print(report_text)
            return render_template('return.html',  title='成功!',report=report_text,url="/",url_name="登录页面")
        finally:
            cursor.close()
            conn.close()
