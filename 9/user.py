# -*- coding: utf-8 -*-
# __author__ = 'zhourudong'
import gconf
import json

# 读取文件获取用户列表
def get_users():
    try:
        with open(gconf.USER_FILE,'rb' ) as handler:
            cxt = handler.read()
            return json.loads(cxt)
    except BaseException as e:
        print e
        return []  # 文件为空的时候返回空的列表
"""
保存用户信息到文件
"""
def save_users(users):
    with open(gconf.USER_FILE,'wb') as f:
        f.write(json.dumps(users))
        f.close()
"""
验证用户名，密码是否正确
返回值: True/False
"""
def validate_login(username,password):
    _users = get_users()
    for _user in _users:
        # 比较用户名和密码信息
        if username == _user.get('username') and password == _user.get('password'):
            return True
    return False

"""
检查新建用户信息
返回值 True/False,错误信息
"""
# def validate_add_user(username,password,age):
#     if username.strip() == '':
#         return False,u'用户名不能为空'
#
#     # 检查用户名是否重复
#     _users = get_users()
#     for _user in _users:
#         if username == _user.get('username'):
#             return False,u'用户名已存在'
#
#     # 密码长度要求必须大于等于6
#     if len(password) < 6:
#         return False,u'密码长度要大于6'
#
#     if not str(age).isdigit() or int(age) <= 0 or int(age) >=120:
#         return False,u'年龄必须是0-120的数字'
#     return True,''
def validate_add_user(username, password, age):
    if username.strip() == '':
        return False, u'用户名不能为空'

    #检查用户名是否重复
    _users = get_users()
    for _user in _users:
        if username == _user.get('username'):
            return False, u'用户名已存在'

    #密码要求长度必须大于等于6
    if len(password) < 6:
        return False, u'密码必须大于等于6'

    if not str(age).isdigit() or int(age) <= 0 or int(age) > 100:
        return False, u'年龄必须是0到100的数字'

    return True, ''

"""
添加用户信息
"""
def add_user(username,password,age):
    _user = {'username':username, 'password':password, 'age':age}
    _users = get_users()
    _users.append(_user)
    save_users(_users)


"""
获取用户信息
"""
def get_user(username):
    _users = get_users()
    for _user in _users:
        if _user.get('username') == username:
            return _user
    return None

"""
检查更新用户信息
返回值 True/False ,错误信息
"""
def validate_update_user(username,password,age):
    if get_user(username) is None:
        return False,u'用户信息不存在'
    # 密码长度要大于6
    if len(password) <6:
        return False,u'密码必须大于6'

    if not str(age).isdigit() or int(age) <= 0 or int(age) > 120:
        return False,u'年龄必须是0-120的数字'
    return  True ,''



"""
更新用户信息
"""
def update_user(username,password,age):
    _users = get_users()
    for _user in _users:
        if _user.get('username') == username:
            _user['password'] = password
            _user['age'] = age
            save_users(_users)
            break

"""
删除用户信息
"""
def delete_user(username):
    _users = get_users()
    _idx = -1
    for _user in _users:
        _idx += 1
        if _user.get('username') == username:
            del _users[_idx]
            save_users(_users)
            break

"""
用户登入信息获取
"""
def validate_login(username,password):
    users = get_users()
    for user in users:
        if user.get('username') == username and user.get('password') == password:
            return True
    return False

if __name__ == '__main__':
  print  validate_login('cucy','123456')
