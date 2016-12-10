# 回顾
# 作业
    1. 提交哪些参数
        id
        new-password
        manager-password(当前登陆用户)

# 课程
1. 【定时】刷新Highcharts
    setInterval 每个多长时间执行一次
    setTimeout  等待多长时间后执行一次
    都有两个参数，一个返回值
    function() {console.log(new Date())}, time(毫秒)
    var th = setInterval(function() {console.log('interval:' + new Date())}, 1 * 1000)

    clearInterval
    clearTimeout

2.  python常用的库
    hashlib md5
    os
        获取某个文件夹下所有的文件
        调用系统命令
    sys
    time datetime
    exception
    logging/traceback
    paramiko
        command
        upload
        download
    getpass/raw_input
    3点
3. 实战
    告警
        告警检测
        告警存储
        告警展示
        告警发送(邮件&、短信)
        告警处理

4. 上传文件