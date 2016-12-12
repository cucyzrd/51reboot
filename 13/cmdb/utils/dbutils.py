#encoding: utf-8

import MySQLdb

import gconf

def execute_sql(sql, args, is_fetch):
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

if __name__ == '__main__':
    pass
