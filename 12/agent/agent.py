#encoding: utf-8
import os
import sys
import time
from datetime import datetime
import logging

import psutil
import requests

INTERVAL = 10
URL = 'http://%s:%s/monitor/host/create/'

logger = logging.getLogger(__name__)

def get_addr():
    addr = '0.0.0.0'
    nics = psutil.net_if_addrs().get('eth0')
    for nic in nics:
        if nic.address.find('.') != -1:
            addr = nic.address
            break
    return addr

def monitor(server_ip, server_port):
    ip_addr = get_addr()
    url = URL % (server_ip, server_port)
    while True:
        try:
            usage = {}
            usage['ip'] = ip_addr
            usage['disk'] = psutil.disk_usage('/').percent
            usage['cpu'] = psutil.cpu_percent()
            usage['mem'] = psutil.virtual_memory().percent
            usage['m_time'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            logger.debug(usage)
            response = requests.post(url, data=usage)
            if response.ok:
                logger.debug(response.json())
            else:
                logger.error('server error')
        except BaseException as e:
            logger.error(e)
        
        time.sleep(INTERVAL)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print 'usage: python agent.py server_ip server_ip'
        sys.exit(-1)

    logging.basicConfig(level=logging.INFO, filename='agent.log')

    pid = os.getpid()
    logger.info('PID:%s', pid)

    with open('agent.pid', 'wb') as fh:
        fh.write(str(pid))

    monitor(sys.argv[1], sys.argv[2])