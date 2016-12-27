1. 复习
2. 作业
3. 课程
    a. 装饰器使用
    b. threading
    c. csv是什么，如何操作（读，写）   
    d. 蓝图
    e. restapi
    f. flask文档
    g. boostrapvalidate


a. 装饰器

参数func 是一个函数

def test_wrapper(func):
    def wrapper(*args, **kwargs):
        print 'before function'
        rt = func(*args, **kwargs)
        print 'after function'
        return rt
    return wrapper

@test_wrapper
def test():
    print 'test'
    return '11111'

b. 线程
c. csv
    csv文本，可以包含多行（每一行为excel打开的行），每行可以由多列，每列使用逗号分割

d.e:
    蓝图: 一个完整app的功能放在单独的文件夹中管理 => Blueprint
    Flask app<=> Blueprint 一样的
    1. Flask  <=> Blueprint
    2. view app.route <=> bp.route
    3. Blueprint static/templates => 加载blueprint template， 引用blueprint static

    restapi
        定义一切皆资源 url

        GET获取资源
        PUT创建资源
        POST修改资源
        DELETE删除资源

        一个资源(GET, PUT, POST, DELETE)只有一个操作URL
        request.method GET获取资源  获取某一个<pkey>/获取所有
                       PUT创建资源  创建资源的信息{"name" : "", 'password' : ""}
                       POST修改资源 修改某一个，修改的资源信息 <pkey> {"name" : "", 'password' : ""}
                       DELETE删除资源   删除某一个<pkey>

        url, pkey(get), params(request post/put)
        用户
            GET /users/12/
                /users/
            PUT /users/  {"name" : "", "password" : ""}
            POST /users/12/ {"name" : "", "password" : ""}
            DLETE /users/12/

            return json
 

 sn
 hostname
 ip
 os
 cpu
 ram
 disk
 admin
 buiness
 machine_room_id
 time_on_shelves
 over_guaranteed_date
 vendor
 model
 status