#encoding: utf-8

# format中如果有{, }需要用转义,{{, }}

port = 11000
server_name = 'cmdb'
access_log = '/tmp/kk_access.log'
root = 'www'
proxy_pass = 'http://0.0.0.0:10000'


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