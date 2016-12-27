# 复习
var th = null;
var cnt = 0;
var th_i = null;
if(th_i){th_i = setInterval(test, 5 * 1000);}

var th_i = setInterval(test, 5 * 1000)
clearInterval(th_i);
th_i = null;
function test() {
var xxx = 'a';
    cnt += 1;
    console.log(new Date());
    if(cnt <= 10) {
        th = setTimeout(test, 5 * 1000);
    }
}
test()

# 作业
@app.route("/tests/<name1>/<name2>/")
def tests(name1, name2):
    print name1
    print name2

    配置 gconf.py
            
    业务功能      blueprint
        user
        asset
        log
        monitor

    工具脚本
        dbutils
        encrypt
        mailutils
        ssh
    
    命令持久的命令/定时周期的命令
        monitor.py

    cmdb/
        configs/
            __init__.py
            gconf.py
        user/
            __init__.py
            templates
            views.py
            models.py
            *.py
            import gconf => from configs improt gconf
                            from utils improt ssh
            commands/
                __init__.py
                python xxx.py
        asset/
            __init__.py
            templates
            views.py
            models.py
        log/
            __init__.py
            templates
            views.py
            models.py

        utils/
            __init__.py
            mail
            db
            encrypt
            ssh

        manage.py


# 课程
1. echarts
    0. ip, url, code, cnt(X)
        time
        ip=>lat, lng

        表time, ip, url, code, lat, lng
            ip=>lat, lng

        create table accesslog2 (
            id bigint primary key auto_increment,
            logtime datetime,
            ip varchar(128),
            url text,
            status int,
            lat float,
            lng float
        ) engine=innodb default charset=utf8;

    a. 饼状图
        状态码分布图
    b. 层叠柱状图
        最近12小时，每分钟/每小时，每个状态码出现次数的层叠柱状图
        12:15:00 200 5, 404 3
    c. 地图
        ip => 坐标
        i. legend 删广州，上海
        ii. 删serial 广州，上海
        iii.删全国，发现有问题，恢复，删除全国中markline
        iiii. 删除serial 北京 markLine, markpoint中数据，只留3-4条
        iiiii. 修改北京markline中，数据顺序
        iiiiii. 删除全国中geocoord，只留serial中使用的城市坐标

url:/charts/ => charts.html extends layout.html
layout.html => 菜单
charts.html => block
js => echarts-2.2.7\build\dist\echarts-all.js


2. python manage.py
    web服务器 nginx + uwsgi + flask
    wsgi => web server 网关接口 => 规范
    uwsgi => 实现，工具, gunicorn
    pip install uwsgi
    pip install gunicorn

    uwsgi -s 127.0.0.1:9010 -w moduel:Flask

    user/__init__.py
    uwsgi -s 127.0.0.1:9010 -w user:app
    #uwsgi --http :9010 -w user:app
    ngix => 9010



3. 蓝图


作业
1. 地图数据拼写，显示
select city, lat, lng, count(*) from accesslog2 group by city, lat, lng;



3. 蓝图

csv
导入 上传文件+csv读取+数据insert
导出 下载文件+csv写+数据select