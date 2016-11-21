#encoding: utf-8


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


if __name__ == '__main__':
    access_file_path = "/home/share/www_access_20140823.log"
    result = get_topn(access_file_path)
    tbody = ''
    for line in result:
        tbody += '''<tr>
            <td>{ip}</td>
            <td>{url}</td>
            <td>{code}</td>
            <td>{count}</td>
        </tr>'''.format(ip=line[0][0], url=line[0][0], code=line[0][2], count=line[1])

    html = '''<!DOCTYPE html>
                <html>
                    <head>
                        <!-- 我是一个注释 -->
                        <!-- 给浏览器说明编码方式、title等信息-->
                        <meta charset="utf-8" />
                        <title>我是一个HTML页面</title>
                    </head>
                    <body>
                        <!-- 给用户看的信息 -->
                        我是kk
                        <table border="1">
                            <thead>
                                <tr>
                                    <th>IP</th>
                                    <th>URL</th>
                                    <th>状态码</th>
                                    <th>次数</th>
                                </tr>
                            </thead>
                            <tbody>
                                {tbody}
                            </tbody>
                        </table>
                    </body>
                </html>
    '''.format(tbody=tbody)

    fh = open("topn.html", "w")
    fh.write(html)
    fh.close()