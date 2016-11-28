#encoding: utf-8

if __name__ == '__main__':
    print 'start'
    try:
        1/0
    except BaseException as e:
        print e
    print 'end'