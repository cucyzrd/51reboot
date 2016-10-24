#coding:utf-8

from flask import Flask
import loganalysis
app = Flask(__name__)

@app.route('/logs/')
def logs():
    logfile = 'www_access_20140823.log'
    return loganalysis.loganalysis(logfile=logfile)



@app.route('/')
def index():
    return '<h1>hello world</h1>'

if __name__ == '__main__':
    app.run(port=2000,debug=True)