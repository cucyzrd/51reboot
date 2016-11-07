#encoding: utf-8

# 从flask包导入Flask对象
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

import models
from flask import  session
import os
#创建Flask对象
app = Flask(__name__)
app.secret_key= os.urandom(32)

#/ ==> index........
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login/', methods=['post', 'get'])
def login():
    params = request.form if 'POST' == request.method else request.args
    username = params.get('username', '')
    password = params.get('password', '')

    user = models.validate_login(username, password)
    if user:
        session['user'] = {'username' : username}
        return redirect('/users/')
    else:
        return render_template('index.html', username=username, password=password, error='username or password is error')

@app.route('/users/')
def user_list():
    if session.get('user') is None:
        return redirect('/')   # 如果用户session为空直接跳转到首页
    users = models.get_users()
    return render_template('user.html', users=users)


@app.route('/user/create/')
def user_create():
    return render_template('user_create.html')

@app.route('/user/save/', methods=['POST'])
def user_save():
    username = request.form.get('username', '')
    password = request.form.get('password', '')
    age = request.form.get('age', 0)
    ok, error = models.validate_user_save(username, password, age)
    if ok:
        models.user_save(username, password, age)
        return redirect('/users/')
    else:
        return render_template('user_create.html', username=username, age=age, error=error)

@app.route('/user/view/')
def user_view():
    user = models.get_user_by_id(request.args.get('id', 0))
    print user
    return render_template('user_view.html', id=user.get('id', ''), username=user.get('name', ''), age=user.get('age', ''))
'''
用户修改
'''
@app.route('/user/modify/', methods=['POST'])
def user_modify():
    uid = request.form.get('id', '')
    username = request.form.get('username', '')
    age = request.form.get('age', '')
    ok, error = models.validate_user_modify(uid, username, age)
    if ok:
        models.user_modify(uid, username, age)
        return redirect('/users/')
    else:
        return render_template('user_view.html', id=uid, username=username, age=age, error=error)
"""
删除用户
"""
@app.route('/user/delete/')
def delete_user():
    uid = request.args.get('id')
    models.delete_user(uid)
    return redirect('/users/')

'''
登出
'''

@app.route('/logout/')
def logout():
    return redirect('/')


@app.route('/log/')
def log():
    topn = request.args.get('topn', 10)
    topn = int(topn) if str(topn).isdigit() else 10
    access_file_path = "www_access_20140823.log"
    result = models.get_topn(access_file_path, topn)
    return render_template('log.html', logs=result)

if __name__ == '__main__':
    # 启动app
    # print app.url_map
    app.run(host='127.0.0.1', port=5000, debug=True)
