#coding:utf-8

from flask import Flask
import loganalysis
from flask import render_template
from flask import request
import user
from flask import redirect, url_for
app = Flask(__name__)

"""
打开用户登录界面
"""
@app.route('/')
def index():
    return render_template('login.html')

"""
用户登录信息检查
"""
@app.route('/login/',methods=['POST','GET'])
def login():
    params = request.args  if request.method == 'GET' else request.form
    username = params.get('username','')
    password = params.get('password','')
    # 验证用户密码是否正确
    if user.validate_login(username,password):
        return redirect('/users/')
    # 登入失败
    return render_template('login.html',username=username,error='用户名或者密码错误')

"""
用户列表显示
"""
@app.route('/users/')
def users():
    # 获取所有用户信息
    _users = user.get_users()
    return render_template('users.html',users=_users)

"""
跳转到新建用户信息输入页面
"""
@app.route('/user/crate/')
def create_user():
    render_template('user_create.html')

"""
存储新建用户的信息
"""
@app.route('/user/add/',methods=['post'])
def add_user():
    username = request.form.get('username','')
    password = request.form.get('password','')
    age = request.form.get('age','')

    #     check user information
    _is_ok,_error = user.validate_add_user(username.password,age)
    if _is_ok:
        user.add_user(username,password,age)
        return redirect(url_for('users',action='create'))  # 跳转到用户列表页
    else:
        #跳转到新用户创建页面，回显错误户信息& 用户信息
        return render_template('user_create.html', \
                        error=_error, \
                        username=username, \
                        password=password, age=age)

"""
打开用户信息修改页面
"""
@app.route('/user/modify/')
def modify_user():
    username = request.args.get('username','')
    _user = user.get_users(username)
    _error = ''
    _username = ''
    _password = ''
    _age = ''
    if _user is None:
        _error = '用户下信息不存在'
    else:
        _username = _user.get('username')
        _password = _password.get('password')
        _age = _user.get('age')
    return render_template('user_modify.html',error=_error,password=_password,age=_age,username=_username)

"""
保存修改用户数据
"""
@app.route('/user/update',methods=['POST'])
def update_user():
    username = request.form.get('username','')
    password = request.form.get('password','')
    age = request.form.get('age','')

    # 检查用户信息
    _is_ok,_error = user.validate_update_user(username,password,age)
    if _is_ok:
        user.update_user(username,password,age)
        return redirect('/users/')
    else:
        return render_template('user_modify.html',error=_error,username=username,password=password,age=age)

"""
删除用户
"""
@app.route('/user/delete/')
def delete_user():
    username = request.args.get('username')
    user.delete_user(username)
    return redirect('/users/')

"""
日志界面
"""
@app.route('/logs/')
def logs():
    logfile = 'www_access_20140823.log'

    topn = request.args.get('topn','10')
    topn = int(topn) if topn.isdigit() else 10

    rt_list = loganalysis.get_topn(logfile=logfile,topn=topn)
    return render_template('logs.html',rt_list=rt_list,title='top n log')

"""
main
"""
if __name__ == '__main__':
    print app.url_map
    app.run(port=2000,debug=True)