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
if __name__ == '__main__':
    print app.url_map
    app.run(port=2000,debug=True)