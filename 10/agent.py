# -*- coding: utf-8 -*-
# __author__ = 'zhourudong'

import time
from datetime import datetime

import psutil
import requests

INTERVAL = 2
URL = 'http://127.0.0.1:10000/monitor/host/create/'
NIC = 'WLAN'
def get_addr():
    addr= '0.0.0.0'
    nics = psutil.net_if_addrs().get(NIC)
    for nic in nics:
        if nic.address.find('.') !=-1:
            addr = nic.address
            break
    return addr

def monitor():
    while True:
        ip_addr = get_addr()
        usage = {}
        usage['ip'] = ip_addr
        usage['disk'] = psutil.disk_usage('/').percent
        usage['cpu'] = psutil.cpu_percent()
        usage['mem'] = psutil.virtual_memory().percent
        usage['m_time'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print usage
        # print psutil.net_if_addrs()
        response = requests.post(URL,data=usage)
        if response.ok:
            print response.json()
        else:
            print 'error'
        time.sleep(INTERVAL)

if __name__ == '__main__':
    monitor()