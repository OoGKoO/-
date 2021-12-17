from flask import Flask,request,render_template,make_response
import pymysql

app=Flask(__name__)

from app import regist_blue,admin_blue
app.register_blueprint(regist_blue)
app.register_blueprint(admin_blue)



@app.route('/')
def index():
    return render_template('index.html')



@app.route('/post_login',methods=['post'])
def post_login():
    if request.method=="POST":
        username=request.form['username']
        password=request.form['password']
        # print(username,password)
        if username=='':
            report_text="用户名不能为空"
            print(report_text)
            return render_template('return.html',title='登录失败',report=report_text,url="/login",url_name="登录页面")
        elif password=='':
            report_text="密码不能为空"
            print(report_text)
            return render_template('return.html',title='登录失败',report=report_text,url="/login",url_name="登录页面")

        conn=pymysql.connect(host="121.5.156.175",
                           user="root",
                           password="123456",
                           port=3306,
                           database="Garbage_Classification")
        cursor=conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("select * from admin")
        results = cursor.fetchall()#输出元组
        conn.close()
        
        for i in results:
            if username==i["username"] and password==i["password"]:
                
                report_text=i["user_class"]+i["username"]+"登录成功"
                cookie = make_response(render_template('return.html',title='登录成功',report=report_text,url="/admin/"+i["username"],url_name="后台管理页面"))
                cookie.set_cookie('username', username,max_age=600)#十分钟后失效
                cookie.set_cookie('password', password,max_age=600)
                cookie.set_cookie('class', i["user_class"],max_age=600)

                return cookie
        
        report_text="账号或密码错误"
        print(report_text)
        
        return render_template('return.html',title='失败!',report=report_text,url="/login",url_name="登录页面")



if __name__ == '__main__':
    app.run(port=5000,debug=True)