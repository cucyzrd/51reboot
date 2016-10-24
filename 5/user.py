# -*- coding: utf-8 -*-
# __author__ = 'zhourudong'
import gconf
import json

# 读取文件获取用户
def get_users():
    try:
        with open(gconf.USER_FILE,'rb' ) as handler:
            cxt = handler.read()
            return json.loads(cxt)
    except:
        return []  # 文件为空的时候返回空的列表


def validate_login(username,password):
    users = get_users()
    for user in users:
        if user.get('username') == username and user.get('password') == password:
            return True
    return False

if __name__ == '__main__':
  print  validate_login('cucy','123456')
