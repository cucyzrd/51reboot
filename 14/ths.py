#encoding: utf-8

import time
import logging
import threading #导入库

logger = logging.getLogger(__name__)

def sleep_func(n):
    logger.info('start function:%s', n)
    time.sleep(n)
    logger.info('end function:%s', n)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    start_time = time.time()

    ths = []

    #分配任务
    for i in range(5):
        th = threading.Thread(target=sleep_func, args=(10-i, )) #创建线程
        ths.append(th)
        th.start() #启动线程
        #sleep_func(10 - i)

    #等待
    for th in ths:
        th.join()
        
    print 'over:%s' % (time.time() - start_time)

    #1.10
    #2.9
    #3.8
    #4.7
    #5.6
    #total: 10 + 9 + 8 + 7 + 6 (40s)