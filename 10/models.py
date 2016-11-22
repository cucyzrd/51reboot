#encoding: utf-8

import MySQLdb
import datetime
import gconf

SQL_VALIDATE_LOGIN_COLUMNS = ('id', 'name')

SQL_VALIDATE_LOGIN = 'select id, name from user where name = %s and password = md5(%s)'
SQL_USER_SAVE = 'insert into user(name, age, password) values(%s, %s, md5(%s))'

SQL_USER_LIST_COLUMNS = ('id', 'name', 'age')
SQL_USER_LIST = 'select id, name, age from user'

SQL_USER_BY_ID_COLUMNS = ('id', 'name', 'age')
SQL_USER_BY_ID = 'select id, name, age from user where id=%s'

SQL_USER_MODIFY = 'update user set name=%s, age=%s where id=%s'

SQL_VALIDATE_USER_MODIFY = 'select id from user where id != %s and name = %s'

SQL_USER_DELETE = 'DELETE FROM `zrd`.`user` WHERE  `id`=%s'

# 数据库连接

def execu_sql(sql, args, is_fetch):
    rt_cnt = 0
    rt_list = []
    conn = MySQLdb.connect(host=gconf.MYSQL_HOST, \
                        port=gconf.MYSQL_PORT, \
                        user=gconf.MYSQL_USER, \
                        passwd=gconf.MYSQL_PASSWD, \
                        db=gconf.MYSQL_DB, \
                        charset=gconf.MYSQL_CHARSET)
    cursor = conn.cursor()
    rt_cnt = cursor.execute(sql, args)
    if is_fetch:
        rt_list = cursor.fetchall()
    else:
        conn.commit()
    cursor.close()
    conn.close()
    return rt_cnt, rt_list

'''
获取用户信息列表
'''
def get_users():
    sql = SQL_USER_LIST
    args = ()

    rt_cnt, rt_list = execu_sql(sql,args,True)

    return [dict(zip(SQL_USER_LIST_COLUMNS, line)) for line in rt_list]

'''
用户登录检查
'''
def validate_login(username, password):
    sql = SQL_VALIDATE_LOGIN
    args = (username, password)
    rt_cnt,rt_list = execu_sql(sql,args,True)

    return None if rt_list is None else dict(zip(SQL_VALIDATE_LOGIN_COLUMNS, rt_list))

'''
新增用户前 检查
'''
def validate_user_save(username, password, age):
    if username.strip() == '':
        return False, 'username is empty'
    if len(username.strip()) > 25:
        return False, 'username len is not gt 25'
    if password.strip() == '':
        return False, 'password is empty'
    if len(password.strip()) < 6 or len(password.strip()) > 25:
        return False, 'password len is between 6 and 25'

    if not str(age).isdigit() or int(age) < 1 or int(age) > 100:
        return False, 'age is not a between 1 and 100 integer'

    return True, ''

'''
保存新增用户信息
返回 True/False
'''
def user_save(username, password, age):
    sql = SQL_USER_SAVE
    args = (username, age, password)
    rt_cnt ,rt_list = execu_sql(sql,args,False)

    return rt_cnt != 0

'''
以ID获取用户信息
返回 : {'age': xx, 'id': xx, 'name': xx}
'''
def get_user_by_id(uid):
    sql = SQL_USER_BY_ID
    args = (uid,)
    rt_cnt, rt_list = execu_sql(sql,args,True)
    return {} if rt_list is None else dict(zip(SQL_USER_BY_ID_COLUMNS, (rt_list[0][0],rt_list[0][1],rt_list[0][2])))

'''
用户修改信息，合法性检查
返回值 True/False
'''
def validate_user_modify(uid, username, age):
    if not get_user_by_id(uid):
        return False, 'user is not found'
    if username.strip() == '':
        return False, 'username is empty'
    if len(username.strip()) > 25:
        return False, 'username len is not gt 25'
    if not str(age).isdigit() or int(age) < 1 or int(age) > 100:
        return False, 'age is not a between 1 and 100 integer'

    sql = SQL_VALIDATE_USER_MODIFY
    args = (uid, username.strip())
    rt_cnt , rt_list = execu_sql(sql,args,False)
    # 已用用户存在返回的值 必然不是0
    if rt_cnt != 0:
        return False, 'username is same to other'
    return True, ''

'''
保存用户修改信息
'''
def user_modify(uid, username, age):
    sql = SQL_USER_MODIFY
    args = (username, age, uid)
    rt_cnt , rt_list = execu_sql(sql,args,False)
    return True

"""
删除用户信息
"""
def delete_user(uid):
    sql = SQL_USER_DELETE
    args = (uid,)
    rt_cnt , rt_list = execu_sql(sql,args,False)
    return True


# -----------------------------------------------------------------------
'''
获取机房列表
'''
def get_machines():
    SQL_MACHINES_LIST = 'SELECT  `id`,  `room_name`,  `addr`,  LEFT(`ip_ranges`, 256) FROM `zrd`.`machine_room` LIMIT 1000'
    SQL_MACHINES_LIST_COLUMS = ('id', 'room_name', 'addr','ip_ranges')
    sql = SQL_MACHINES_LIST
    args = ()

    rt_cnt, rt_list=execu_sql(sql,args,True)
    a = [dict(zip(SQL_MACHINES_LIST_COLUMS,line)) for line in rt_list]
    # print a
    return a

'''
机房保存前检查
'''
def validate_machine_save(room_name,addr,ip_ranges):
    if room_name.strip() == '':
        return False, 'room_name is empty'
    if len(room_name.strip()) > 64:
        return False, 'room_name len is not gt 64'

    if addr.strip() == '':
        return False, 'addr is empty'
    if len(addr.strip()) > 128:
        return False, 'addr len is not gt 128'

    if ip_ranges.strip() == '':
        return False, 'ip_ranges is empty'

    SQL_VALIDATE_MACHINE_SAVE = 'SELECT  `room_name` FROM `zrd`.`machine_room` WHERE room_name=%s'
    sql = SQL_VALIDATE_MACHINE_SAVE
    args = (room_name,)
    rt_cnt,rt_list = execu_sql(sql,args,True)
    if rt_cnt:
        return False,'room_name is same'

    return True, ''

'''
保存机房信息
'''
def machine_save(room_name,addr,ip_ranges):
    SQL_USER_SAVE = 'INSERT INTO `zrd`.`machine_room` (`room_name`, `addr`, `ip_ranges`) VALUES (%s, %s, %s)'
    sql = SQL_USER_SAVE
    args = (room_name,addr,ip_ranges)
    rt_cnt,rt_list = execu_sql(sql,args,False)

    # 保存信息影响一行，否则都是不通过
    if rt_cnt == 1:
        return True,''
    return False,'保存信息失败'

'''
以ID获取机房信息
返回 : {'age': xx, 'id': xx, 'name': xx}
'''
def get_machine_by_id(id):
    SQL_MACHINE_BY_ID = 'SELECT `id`, `room_name`, `addr`, `ip_ranges` FROM `zrd`.`machine_room` WHERE  `id`=%s'
    SQL_MACHINE_BY_ID_COLUMS = ('id','room_name','addr','ip_ranges')
    sql = SQL_MACHINE_BY_ID
    args = (id,)
    rt_cnt, rt_list = execu_sql(sql,args,True)
    return {} if rt_list is None else dict(zip(SQL_MACHINE_BY_ID_COLUMS, (rt_list[0][0],rt_list[0][1],rt_list[0][2],rt_list[0][3])))



'''
机房修改信息，合法性检查
返回值 True/False
'''
def validate_machine_modify(id,room_name,addr,ip_ranges):
    if not get_machine_by_id(id):
        return False, 'machine is not found'
    if room_name.strip() == '':
        return False, 'username is empty'
    if addr.strip() == '':
        return False, 'addr  is empty'
    if ip_ranges.strip() == '':
        return False, 'ip_ranges is empty'
    print id
    SQL_VALIDATE_MACHINE_MODIFY ='SELECT  `room_name` FROM `zrd`.`machine_room` WHERE  `id`!=%s AND room_name=%s'
    sql = SQL_VALIDATE_MACHINE_MODIFY
    args = (id,room_name)
    rt_cnt , rt_list = execu_sql(sql,args,False)
    print rt_cnt
    # 已用机房存在返回的值 必然不是0
    if rt_cnt != 0:
        return False, 'room_name is same to other'
    return True, ''



'''
保存机房修改信息
'''
def machine_modify(id,room_name,addr,ip_ranges):
    SQL_MACHINE_MODIFY = 'UPDATE `zrd`.`machine_room` SET `room_name`=%s, `addr`=%s, `ip_ranges`=%s WHERE  `id`=%s'
    sql = SQL_MACHINE_MODIFY
    args = (room_name,addr,ip_ranges,id)
    rt_cnt , rt_list = execu_sql(sql,args,False)
    return True


"""
删除机房信息
"""
def delete_machine(id):
    SQL_MACHINE_DELETE = 'DELETE FROM `zrd`.`machine_room` WHERE  `id`=%s'
    sql = SQL_MACHINE_DELETE
    args = (id,)
    rt_cnt , rt_list = execu_sql(sql,args,False)
    return True



# ----------------------------------------------
'''
获取资产列表
'''
def get_assets():
    SQL_ASSET_LIST_SQL_COLUMNS = 'id,sn,hostname,os,ip,machine_room_id,vendor,model,ram,cpu,disk,time_on_shelves,over_guaranteed_date,buiness,admin,status'.split(',')
    SQL_ASSET_LIST_SQL = 'SELECT id,sn,hostname,os,ip, machine_room_id, vendor, model, ram, cpu, disk, time_on_shelves, over_guaranteed_date, buiness, admin, status FROM asset WHERE status != 2'
    rt_cnt,rt_list = execu_sql(SQL_ASSET_LIST_SQL,(),True)
    assets = []
    for rt in rt_list:
        # 取出数据转换成字典格式
        asset = dict(zip(SQL_ASSET_LIST_SQL_COLUMNS,rt))
        # 使用datetime将时间转换为字符串, json无法解析非str类型
        for key in 'time_on_shelves,over_guaranteed_date'.split(','):
            if asset[key]:
                asset[key] = asset[key].strftime('%Y-%m-%d')
        assets.append(asset)
    return assets
'''
获取资产ID
'''
def get_asset_by_id(aid):
    GET_ASSET_BY_ID_COLUMNS = 'id,sn,hostname,os,ip,machine_room_id,vendor,model,ram,cpu,disk,time_on_shelves,over_guaranteed_date,buiness,admin,status'.split(',')
    GET_ASSET_BY_ID = 'SELECT id,sn,hostname,os,ip, machine_room_id, vendor, model, ram, cpu, disk, time_on_shelves, over_guaranteed_date, buiness, admin, status FROM asset WHERE status != 2 AND id=%s'

    rt_cnt,rt_list = execu_sql(GET_ASSET_BY_ID,(aid,),True)
    assets = []
    for rt in rt_list:
        # 取出数据转换成字典格式
        asset = dict(zip(GET_ASSET_BY_ID_COLUMNS,rt))
        # 使用datetime将时间转换为字符串, json无法解析非str类型
        for key in 'time_on_shelves,over_guaranteed_date'.split(','):
            if asset[key]:
                asset[key] = asset[key].strftime('%Y-%m-%d')
        assets.append(asset)
    # 防止数据为空,使用三元操作符
    return assets[0] if assets else {}

'''
新增资产前 检查合法性
'''
def validate_asset_save(sn):
    if sn.strip() == '':
        return False, 'sn is empty'

    #  只检查SN号是否有重复 其他不做检查
    SQL_VALIDATE_ASSET_SAVE = 'SELECT  `sn` FROM asset WHERE sn=%s'
    sql = SQL_VALIDATE_ASSET_SAVE
    args = (sn,)
    rt_cnt,rt_list = execu_sql(sql,args,True)
    if rt_cnt:
        return False,'sn is same'
    return True, ''
'''
新增资产
'''
def asset_save(sn, hostname, os, ip, machine_room_id, vendor, model, ram, cpu, disk, time_on_shelves, over_guaranteed_date, buiness,  status):
    SQL_ASSET_SAVE = 'INSERT INTO asset (sn, hostname, os, ip, machine_room_id, vendor, model, ram, cpu, disk, time_on_shelves, over_guaranteed_date, buiness,  status) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    sql = SQL_ASSET_SAVE
    args = (sn, hostname, os, ip, machine_room_id, vendor, model, ram, cpu, disk, time_on_shelves, over_guaranteed_date, buiness, status)
    rt_cnt,rt_list = execu_sql(sql,args,False)

    # 保存信息影响一行，否则都是不通过
    if rt_cnt == 1:
        return True,''
    return False,'保存信息失败'


'''
更新资产前，检查合法性
'''
def validate_asset_update(aid,sn,hostname):
    if hostname.strip('') =='':
        return False,u'主机名不能为空'
    SQL_VALIDATE_ASSET_UPDATE='SELECT * FROM asset WHERE id=%s AND sn=%s'
    # 防止id 和 sn 被修改
    sql = SQL_VALIDATE_ASSET_UPDATE
    args = (aid,sn)
    rt_cnt,rt_list = execu_sql(sql,args,True)
    if rt_cnt != 1:
        return False,u'sn或者id不能修改'
    return True,''
'''
更新 资产
'''
def assets_update(sn, hostname, os, ip, machine_room_id,vendor, model, ram, cpu, disk, time_on_shelves,over_guaranteed_date, buiness,status,aid):
    SQL_ASSET_UPDATE='UPDATE asset SET sn=%s,hostname=%s,os=%s,ip=%s,machine_room_id=%s,vendor=%s,model=%s,ram=%s,cpu=%s,disk=%s,time_on_shelves=%s,over_guaranteed_date=%s, buiness=%s, status=%s WHERE  `id`=%s'
    sql = SQL_ASSET_UPDATE
    args = (sn, hostname, os, ip, machine_room_id,vendor, model, ram, cpu, disk, time_on_shelves,over_guaranteed_date, buiness,status,aid)
    rt_cnt,rt_list = execu_sql(sql,args,False)
    return True if rt_cnt else False


"""
删除资产信息
"""
def delete_asset(aid):
    SQL_ASSET_DELETE = 'DELETE FROM asset WHERE  `id`=%s'
    sql = SQL_ASSET_DELETE
    args = (aid,)
    rt_cnt , rt_list = execu_sql(sql,args,False)
    return True



# ---------------------------------------------
'''
日志信息
'''
def get_topn(src, topn=10):
    stat_dict = {}
    fhandler = open(src, "rb")

    for line in fhandler:
        line_list = line.split()
        key = (line_list[0], line_list[6], line_list[8])
        stat_dict[key] = stat_dict.setdefault(key, 0) + 1

    fhandler.close()

    result = sorted(stat_dict.items(), key=lambda x:x[1])
    return result[:-topn - 1:-1]

if __name__ == "__main__":
    print assets_update('sn2','host2','bsd1','192.168.1.21',2,'hp','380',2048,4,500,'2016-11-02','2016-11-23','dev',0,2)
