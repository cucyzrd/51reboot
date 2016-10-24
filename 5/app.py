#coding:utf-8

from flask import Flask
import loganalysis
from flask import render_template
app = Flask(__name__)

@app.route('/logs/')
def logs():
    logfile = 'www_access_20140823.log'
    rt_list = loganalysis.get_topn(logfile=logfile)
    return render_template('logs.html')

@app.route('/')
def index():
    return '<h1>hello world</h1>'

if __name__ == '__main__':
    print app.url_map
    app.run(port=2000,debug=True)