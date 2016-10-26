# -*- coding: utf-8 -*-
# __author__ = 'zhourudong'
import  time

'''
记录每个函数的执行时间
'''
def time_wrapper(func):
    def wrapper():
        print '计时开始:%s' % func.__name__
        start = time.time()
        rt = func()
        exec_time = time.time() - start
        print '计时结束:%s==>:%s' % (func.__name__,time.time()- start)
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
在所有函数之前执行一块代码
在所有函数之后执行一块代码
'''

def wrapper(func):
    print '执行之前 %s' % func.__name__
    rt = func()
    print '执行以后 %s' % func.__name__
    return rt

'''
调用的位置都得改
'''
print wrapper(test1)
print wrapper(test2)
print wrapper(test3)
print wrapper(test4)

test3()
test4()