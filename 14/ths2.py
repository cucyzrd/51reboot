#encoding: utf-8

import time
import logging
import threading #导入库

logger = logging.getLogger(__name__)

def sleep_func(n):
    logger.info('start function:%s', n)
    time.sleep(n)
    logger.info('end function:%s', n)

def cpu():
    logger.info('cpu start')
    while True:
        logger.info('cpu value')
        time.sleep(10)


def mem():
    logger.info('mem start')
    while True:
        logger.info('mem value')
        time.sleep(20)


def disk():
    logger.info('disk start')
    
    while True:
        logger.info('disk value')
        time.sleep(30)
        break


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    start_time = time.time()

    ths = {}
    th = threading.Thread(target=cpu)
    th.setDaemon(True)
    th.start()
    ths['cpu'] = th

    th = threading.Thread(target=mem)
    th.setDaemon(True)
    th.start()
    ths['mem'] = th
    
    th = threading.Thread(target=disk)
    th.setDaemon(True)
    th.start()
    ths['disk'] = th
    
    while True:
        for th in ths:
            print th, ths[th].isAlive() 
            
        time.sleep(10)
   
   
    #1.10
    #2.9
    #3.8
    #4.7
    #5.6
    #total: 10 + 9 + 8 + 7 + 6 (40s)