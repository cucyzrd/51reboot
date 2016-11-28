#encoding: utf-8
import json
import time
# 从flask包导入Flask对象
from flask import render_template
from flask import request
from flask import redirect
from flask import session

from cmdb import app
import models

@app.route('/')
def index():
    if session.get('user'): return redirect('/users/')
    return render_template('index.html')

@app.route('/login/', methods=['post', 'get'])
def login():
    if session.get('user'): return redirect('/users/')

    params = request.form if 'POST' == request.method else request.args
    username = params.get('username', '')
    password = params.get('password', '')

    user = models.validate_login(username, password)
    if user:
        session['user'] = user
        return redirect('/users/')
    else:
        return render_template('index.html', username=username, password=password, error='username or password is error')

@app.route('/users/')
def user_list():
    if session.get('user') is None: return redirect('/')

    users = models.get_users()
    return render_template('user.html', users=users)


@app.route('/user/save/', methods=['POST'])
def user_save():
    if session.get('user') is None: return json.dumps({'code' : 403, 'error' : ''})

    username = request.form.get('name', '')
    password = request.form.get('password', '')
    age = request.form.get('age', 0)
    ok, error = models.validate_user_save(username, password, age)
    if ok:
        models.user_save(username, password, age)
        return json.dumps({'code' : 200})
    else:
        return json.dumps({'code' : 400, 'error' : error})


@app.route('/user/view/')
def user_view():
    if session.get('user') is None: return json.dumps({'code' : 403, 'error' : ''})

    user = models.get_user_by_id(request.args.get('id', 0))
    return json.dumps(user) if user else json.dumps({})

@app.route('/user/modify/', methods=['POST'])
def user_modify():
    if session.get('user') is None: return json.dumps({'code' : 403, 'error' : ''})

    uid = request.form.get('id', '')
    username = request.form.get('name', '')
    age = request.form.get('age', '')
    ok, error = models.validate_user_modify(uid, username, age)
    if ok:
        models.user_modify(uid, username, age)
        return json.dumps({'code' : 200})
    else:
        return json.dumps({'code' : 400, 'error' : error})

@app.route('/user/password/modify/', methods=['POST'])
def user_password_modify():
    if session.get('user') is None: return json.dumps({'code' : 403, 'error' : ''})

    uid = request.form.get('id', '')
    passwrd = request.form.get('password', '')
    manager_password = request.form.get('manager-password', '')
    ok, error = models.validate_user_password_modify(uid, passwrd, session['user']['id'], manager_password)
    if ok:
        models.user_password_modify(uid, passwrd)
        return json.dumps({'code' : 200})
    else:
        return json.dumps({'code' : 400, 'error' : error})


@app.route('/user/delete/')
def user_delete():
    if session.get('user') is None: return json.dumps({'code' : 403, 'error' : ''})

    models.user_delete(request.args.get('id', 0))
    return json.dumps({'code' : 200})


@app.route('/machine_rooms/')
def machine_room_list():
    machine_rooms = models.get_machine_rooms()
    return render_template('machine_room.html', machine_rooms=machine_rooms);


@app.route('/machine_room/save/', methods=['POST'])
def machine_room_save():
    if session.get('user') is None: return json.dumps({'code' : 403, 'error' : ''})

    name = request.form.get('name', '')
    addr = request.form.get('addr', '')
    ip_ranges = request.form.get('ip_ranges', '')
    ok, error = models.validate_machine_room_save(name, addr, ip_ranges)
    if ok:
        models.machine_room_save(name, addr, ip_ranges)
        return json.dumps({'code' : 200})
    else:
        return json.dumps({'code' : 400, 'error' : error})


@app.route('/machine_room/delete/')
def machine_room_delete():
    if session.get('user') is None: return redirect('/')

    models.machine_room_delete(request.args.get('id', 0))
    return redirect('/machine_rooms/')


@app.route('/log/')
def log():
    if session.get('user') is None: return redirect('/')
    topn = request.args.get('topn', 10)
    topn = int(topn) if str(topn).isdigit() else 10
    access_file_path = "/home/kk/www_access_20140823.log"
    result = models.get_topn(access_file_path, topn)
    return render_template('log.html', logs=result)

@app.route('/log/upload/', methods=['POST'])
def log_upload():
    if session.get('user') is None: return redirect('/')
    file = request.files.get('log')
    if file:
        print file.filename
        filename = int(1000 * time.time())
        file.save('/tmp/kk/%s' % filename)
    return redirect('/log/')


@app.route('/assets/')
def asset_index():
    if session.get('user') is None: return redirect('/')
    machine_rooms = models.get_machine_rooms()
    return render_template('asset.html', machine_rooms=machine_rooms)


@app.route('/asset/list/')
def asset_list():
    if session.get('user') is None: json.dumps({'data' : []})

    assets = models.get_assets()
    return json.dumps({'data' : assets})


@app.route('/asset/save/', methods=['POST'])
def asset_save():
    if session.get('user') is None: return json.dumps({'code' : 403, 'error' : ''})

    params = request.form
    ok, error = models.validate_asset_save(params)
    if ok:
        models.asset_save(params)
        return json.dumps({'code' : 200})
    else:
        return json.dumps({'code' : 400, 'error' : error})


@app.route('/asset/view/')
def asset_view():
    if session.get('user') is None: return json.dumps({'code' : 403, 'error' : ''})

    aid = request.args.get('id', 0)
    asset = models.get_asset_by_id(aid)
    return json.dumps(asset)


@app.route('/asset/modify/', methods=['POST'])
def asset_modify():
    if session.get('user') is None: return json.dumps({'code' : 403, 'error' : ''})

    params = request.form
    ok, error = models.validate_asset_modify(params)
    if ok:
        models.asset_modify(params)
        return json.dumps({'code' : 200})
    else:
        return json.dumps({'code' : 400, 'error' : error})


@app.route('/asset/delete/')
def asset_delete():
    if session.get('user') is None: return json.dumps({'code' : 403, 'error' : ''})

    models.asset_delete(request.args.get('id', 0))
    return json.dumps({'code' : 200})


@app.route('/logout/')
def logout():
    session.clear()
    return redirect('/')


@app.route('/monitor/host/create/', methods=['POST'])
def monitor_host_create():
    models.monitor_host_create(request.form)
    return json.dumps({'code' : 200, 'result' : ''})

@app.route('/monitor/host/list/')
def monitor_host_list():
    asset = models.get_asset_by_id(request.args.get('id', 0))
    ip = asset.get('ip', '')
    result = models.monitor_host_list(ip)
    return json.dumps({'code' : 200, 'result' : result})

@app.route('/alert/')
def alert_index():
    if session.get('user') is None: return redirect('/')
    return render_template('alert.html')


@app.route('/alert/list/')
def alert_list():
    if session.get('user') is None: json.dumps({'data' : []})

    alerts = models.get_alerts()
    return json.dumps({'data' : alerts})
