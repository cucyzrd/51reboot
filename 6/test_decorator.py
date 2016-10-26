# -*- coding: utf-8 -*-
# __author__ = 'zhourudong'
import  time

'''
��¼ÿ��������ִ��ʱ��
'''
def time_wrapper(func):
    def wrapper():
        print '��ʱ��ʼ:%s' % func.__name__
        start = time.time()
        rt = func()
        exec_time = time.time() - start
        print '��ʱ����:%s==>:%s' % (func.__name__,time.time()- start)
        return rt
    return wrapper



def test1():
    print 'test1'
def test2():
    print 'test2'

@time_wrapper
def test3():
    time.sleep(2)
    print 'test3'

@time_wrapper
def test4():
    time.sleep(3)
    print 'test4'
    return 4

'''
�����к���֮ǰִ��һ�����
�����к���֮��ִ��һ�����
'''

def wrapper(func):
    print 'ִ��֮ǰ %s' % func.__name__
    rt = func()
    print 'ִ���Ժ� %s' % func.__name__
    return rt

'''
���õ�λ�ö��ø�
'''
print wrapper(test1)
print wrapper(test2)
print wrapper(test3)
print wrapper(test4)

test3()
test4()