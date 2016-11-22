#encoding: utf-8

# 从flask包导入Flask对象
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
import json
import models
from flask import  session
import os

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#创建Flask对象
app = Flask(__name__)
app.secret_key= 'ddddddddddddddddddddfgddddddddddddddddddddddddddddddddd'

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
    if session.get('user') is None: return redirect('/')   # 如果用户session为空直接跳转到首页
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

@app.route('/user/save/json/', methods=['POST'])
def user_save_json():
    username = request.form.get('username', '')
    password = request.form.get('password', '')
    # print request.form
    age = request.form.get('age', 0)
    ok, error = models.validate_user_save(username, password, age)
    if ok:
        models.user_save(username, password, age)
        return json.dumps({'code': 200})

    else:
        return json.dumps({'code': 400, 'error': error})


@app.route('/user/view/')
def user_view():
    user = models.get_user_by_id(request.args.get('id', 0))
    # print user
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

# ---------------------------------------------------------------------------
# 机房管理
# ---------------------------------------------------------------------------


# 机房列表
@app.route('/machines/')
def get_machines():
    machines = models.get_machines()

    return render_template('machine.html',machines=machines)

'''
机房添加
'''
@app.route('/machine/create/')
def machine_create():
    return render_template('machine_create.html')

'''
机房保存
'''
@app.route('/machine/save/',methods=['POST'])
def machine_save():
    room_name = request.form.get('room_name','')
    addr = request.form.get('addr','')
    ip_ranges = request.form.get('ip_ranges','')

    ok, error = models.validate_machine_save(room_name,addr,ip_ranges)
    if ok:
        ok, error = models.machine_save(room_name,addr,ip_ranges)
        if ok:
            return redirect('/machines/')
        return render_template('machine_create.html', room_name=room_name, addr=addr, ip_ranges=ip_ranges, error=error)
    return render_template('machine_create.html', room_name=room_name, addr=addr, ip_ranges=ip_ranges, error=error)

'''
json格式修改
'''
@app.route('/machine/save/json/', methods=['POST'])
def machine_save_json():
    room_name = request.form.get('room_name','')
    addr = request.form.get('addr','')
    ip_ranges = request.form.get('ip_ranges','')

    ok, error = models.validate_machine_save(room_name,addr,ip_ranges)
    if ok:
        models.machine_save(room_name,addr,ip_ranges)
        return json.dumps({'code': 200})

    else:
        return json.dumps({'code': 400, 'error': error})

'''
'''
@app.route('/machine/view/')
def machine_view():
    machine = models.get_machine_by_id(request.args.get('id', 0))
    # print machine
    return render_template('machine_view.html', id=machine.get('id', ''), room_name=machine.get('room_name', ''), addr=machine.get('addr', ''),ip_ranges=machine.get('ip_ranges', ''))

'''
机房修改
'''
@app.route('/machine/modify/', methods=['POST'])
def machine_modify():
    id = request.form.get('id', '')
    room_name = request.form.get('room_name', '')
    addr = request.form.get('addr', '')
    ip_ranges = request.form.get('ip_ranges', '')
    ok, error = models.validate_machine_modify(id,room_name,addr,ip_ranges)
    if ok:
        models.machine_modify(id,room_name,addr,ip_ranges)
        return redirect('/machines/')
    else:
        return render_template('machine_view.html', id=id, room_name=room_name, addr=addr,ip_ranges=ip_ranges, error=error)

"""
删除机房信息
"""
@app.route('/machine/delete/')
def delete_machine():
    id = request.args.get('id')
    models.delete_machine(id)
    return redirect('/machines/')

# ------------------------
#  资产管理
# ------------------------
@app.route('/assets/')
def assets_index():
    if session.get('user') is None: return redirect('/')   # 如果用户session为空直接跳转到首页
    return render_template('assets.html')

'''
获取资产列表
以ajax方式获取
'''
@app.route('/assets/list/')
def assets_list():
    assets= models.get_assets()
    return json.dumps( {'data': assets } )




'''
获取资产ID
'''
@app.route('/asset/view/')
def asset_view():
    aid = request.args.get('id',0)
    # print aid
    asset = models.get_asset_by_id(aid)
    return json.dumps(asset)
'''
新增资产 json格式上传
'''
@app.route('/asset/save/json/', methods=['POST'])
def asset_save_json():
    a = request.form
    sn =  a.get('sn',0)
    hostname =  a.get('hostname',0)
    ip =  a.get('ip',0)
    os =  a.get('os',0)
    ram =  a.get('ram',0)
    cpu =  a.get('cpu',0)
    disk = a.get('disk',0)
    buiness =  a.get('buiness',0)
    machine_room_id =  a.get('machine_room_id',0)
    time_on_shelves =  a.get('time_on_shelves',0)
    over_guaranteed_date =  a.get('over_guaranteed_date',0)
    vendor =  a.get('vendor',0)
    model =  a.get('model',0)
    status =  a.get('status',0)
    # print sn, hostname, os, ip, machine_room_id, vendor, model, ram, cpu, disk, time_on_shelves, over_guaranteed_date, buiness, status,'\n'
    #  只检查SN号是否有重复 其他不做检查
    ok, error = models.validate_asset_save(sn)
    if ok:
        models.asset_save(sn, hostname, os, ip, machine_room_id, vendor, model, ram, cpu, disk, time_on_shelves, over_guaranteed_date, buiness, status)
        return json.dumps({'code': 200})
    return json.dumps({'code': 400, 'error': error})


'''
保存编辑 接收ajax发过来的信息
'''
@app.route('/asset/update/',methods=['POST'])
def asset_update():
    a = request.form
    aid =  a.get('id',0)
    sn =  a.get('sn',0)
    hostname =  a.get('hostname',0)
    ip =  a.get('ip',0)
    os =  a.get('os',0)
    ram =  a.get('ram',0)
    cpu =  a.get('cpu',0)
    disk = a.get('disk',0)
    buiness =  a.get('buiness',0)
    machine_room_id =  a.get('machine_room_id',0)
    time_on_shelves =  a.get('time_on_shelves',0)
    over_guaranteed_date =  a.get('over_guaranteed_date',0)
    vendor =  a.get('vendor',0)
    model =  a.get('model',0)
    status =  a.get('status',0)
    # print 'over_guaranteed_date:',over_guaranteed_date
    _ok,_error = models.validate_asset_update(aid,sn,hostname)
    if _ok:
        models.assets_update(sn, hostname, os, ip, machine_room_id,vendor, model, ram, cpu, disk, time_on_shelves,over_guaranteed_date, buiness,status,aid)
        return json.dumps({'error': ''})
    return json.dumps({'code':400,'error' :_error})
'''
删除资产信息
'''
@app.route('/asset/delete/')
def delete_asset():
    aid = request.args.get('id')
    models.delete_asset(aid)
    return redirect('/assets/')
# ----------------------------
#  日志
# ----------------------------
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
