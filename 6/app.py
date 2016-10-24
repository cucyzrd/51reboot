#coding:utf-8

from flask import Flask
import loganalysis
from flask import render_template
from flask import request
import user
from flask import redirect
app = Flask(__name__)

@app.route('/logs/')
def logs():
    logfile = 'www_access_20140823.log'

    topn = request.args.get('topn','10')
    topn = int(topn) if topn.isdigit() else 10

    rt_list = loganalysis.get_topn(logfile=logfile,topn=topn)
    return render_template('logs.html',rt_list=rt_list,title='top n log')

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login/',methods=['POST','GET'])
def login():
    params = request.args  if request.method == 'GET' else request.form
    username = params.get('username','')
    password = params.get('password','')

    if user.validate_login(username,password):
        return redirect('/users/')
    return render_template('login.html',username=username,error='username or password is error')
@app.route('/users/')
def users():
    return render_template('users.html',user_list=user.get_users())

# 跳转到新建用户信息输入的页面
@app.route('/user/crate/')
def create_user():
    render_template('user_create.html')

# 新建用户
@app.route('/user/add/',methods=['post'])
def add_user():
    username = request.form.get('username','')
    password = request.form.get('password','')
    age = request.form.get('age','')

    #     check user information
    _is_ok,_error = user.validate_add_user(username.password,age)
    if _is_ok:
        user.add_user(username,password,age)
        return render_template('users',action='create')
    else:
        #跳转到新用户创建页面，回显用户信息
        render_template('user_create.html', \
                        error=_error, \
                        username=username, \
                        password=password, age=age)
# 打开用户修改页面
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

# 保存用户信息
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

# 删除用户
@app.route('/user/delete/')
def delete_user():
    username = request.args.get('username')
    user.delete_user(username)
    return redirect('/users/')

if __name__ == '__main__':
    print app.url_map
    app.run(port=2000,debug=True)