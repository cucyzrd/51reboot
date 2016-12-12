#encoding: utf-8

# format中如果有{, }需要用转义,{{, }}

port = 5555
server_name = 'cmdb'
access_log = '/tmp/access.log'
root = '/opt/www'
proxy_pass = 'http://0.0.0.0:9999'


## 读取tpl文件
fh = open('nginx.tpl', 'r')
tpl = fh.read()
fh.close()
#关闭


cxt = tpl.format(PORT=port, \
                SERVER_NAME=server_name, \
                ACCESS_LOG=access_log, \
                ROOT=root, \
                PROXY_PASS=proxy_pass)
#打开新文件
fh = open('nginx.conf', 'w')
fh.write(cxt)
fh.close()
#关闭文件