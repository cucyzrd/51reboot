# -*- coding: utf-8 -*-
# __author__ = 'zhourudong'
import  time
from  functools import wraps

# wraps 可以防止修改其他函数名字


"""
记录日志
"""
def log_wrapper(func):
    @wraps(func)
    def wrapper():
        print '日志记录开始:%s' % func.__name__
        rt = func()
        print '日志记录结束:%s' % func.__name__
        return rt
    return wrapper

'''
记录每个函数的执行时间
'''
def time_wrapper(func):
    @wraps(func)
    def wrapper():
        print '计时开始:%s' % func.__name__
        start = time.time()
        rt = func()
        exec_time = time.time() - start
        print '计时结束:%s==>:%s' % (func.__name__,time.time()- start)
        return rt
    return wrapper



@log_wrapper
def test1():
    print 'test1'

@time_wrapper
def test2():
    print 'test2'


def test3():
    time.sleep(2)
    print 'test3'

@log_wrapper
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
# print wrapper(test1)
# print wrapper(test2)
# print wrapper(test3)
# print wrapper(test4)

test1()  # 只记录日志
test2()
test3() # 只记录时间
test4() # 记录时间、日志
