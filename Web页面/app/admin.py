from flask import request,render_template,make_response
import pymysql
from app import admin_blue

@admin_blue.route('/<username>',methods=['GET'])
def user_index(username): 
    ck_username=request.cookies.get("username")
    ck_class=request.cookies.get("class")

    if ck_username != username:
        report_text="登录超时"
        return render_template('return.html',report_title='失败!',report=report_text,url="/",url_name="登录页面")#判断cookie是否生效，如果无效则跳转到主页面

    else:
        conn=pymysql.connect(host="",
                           user="root",
                           password="123456",
                           port=3306,
                           database="Garbage_Classification")
        cursor=conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("select * from running_log")
        results = cursor.fetchall()#输出元组
        conn.close()

        garbage_table=""
        for i in results:
            garbage_table+="<tr>"+\
                           "<th>"+str(i["name"])+"</th>"+\
                           "<th>"+str(i["category"])+"</th>"+\
                           "<th>"+str(i["time"])+"</th>"+\
                           "</tr>"

        return render_template('admin.html',username=username,garbage_table=garbage_table)



@admin_blue.route('/<username>/logout',methods=['POST'])
def logout(username):
    if username==request.cookies.get("username"):
        report_text="已退出登录"
        cookie_off = make_response(render_template('return.html',report_title='失败!',report=report_text,url="/",url_name="登录页面"))  # 设置响应体,使cookie失效
        cookie_off.delete_cookie("username")
        cookie_off.delete_cookie("password")
        cookie_off.delete_cookie("class")
        return cookie_off
