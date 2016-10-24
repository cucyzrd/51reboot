#encoding:utf-8

def loganalysis(logfile, topn=10):

    fhandler = open(logfile, 'r')

    rt_dict = {}
    # 统计
    while True:
        line = fhandler.readline()
        if line == '':
            break

        nodes = line.split()
        ip, url, code = nodes[0], nodes[6], nodes[8]
        key = (ip, url, code)
        if key not in rt_dict:
            rt_dict[key] = 1
        else:
            rt_dict[key] = rt_dict[key] + 1

    fhandler.close()
    #print rt_dict

    # 排序
    rt_list = rt_dict.items()
    # [(key, value), (key, value)]

    for j in range(0, topn):
        for i in range(0, len(rt_list) - 1):
            if rt_list[i][1] > rt_list[i + 1][1]:
                temp = rt_list[i]
                rt_list[i] = rt_list[i + 1]
                rt_list[i + 1] = temp


    page_tpl = '''
    <!DOCTYPE html>
    <html>
        <head>
            <meta charset="utf-8"/>
            <title>{title}</title>
        </head>
        <body>
            <table>
                <thead>
                    <tr>
                       {thead}
                    </tr>
                </thead>
                <tbody>
                    {tbody}
                </tbody>
            </table>
        </body>
    </html>
    '''

    title = 'TOP %s 访问日志' % topn
    thead = '<th>IP</th><th>URL</th><th>Code</th><th>次数</th>'
    tbody = ''

    for node in rt_list[-1:-topn - 1:-1]:
        tbody += '<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>' % \
        (node[1], node[0][0], node[0][1], node[0][2])

    return page_tpl.format(title=title, thead=thead, tbody=tbody)

if __name__ == '__main__':
    logfile = 'www_access_20140823.log'

    print loganalysis(topn=5, logfile=logfile)
    print loganalysis(logfile=logfile)