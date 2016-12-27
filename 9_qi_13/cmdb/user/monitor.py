#encoding: utf-8
import logging
import datetime

from models import Asset

from dbutils import MySQLConnection
from mailutils import sendemail
from gconf import ALARM_RECIVERS

logger = logging.getLogger(__name__)

CNT = 3
CPU_PERCENT = 2
RAM_PERCENT = 4

def has_alarm(ip):
    _sql = 'select cpu,ram from performs where ip = %s and time >= %s order by time desc limit %s'
    _time = datetime.datetime.now() + datetime.timedelta(minutes=-5)
    _args = (ip, _time.strftime('%Y-%m-%d %H:%M:%S'), CNT)
    _rt_cnt, _rt_list = MySQLConnection.execute_sql(_sql, _args)

    if _rt_cnt < CNT:
        return False, False

    _cpu_alarm = True
    _ram_alarm = True
    for _cpu, _ram in _rt_list:
        if _cpu < CPU_PERCENT:
            _cpu_alarm = False

        if _ram < RAM_PERCENT:
            _ram_alarm = False

    return _cpu_alarm, _ram_alarm


def monitor():
    _asset_list = Asset.get_list()
    _title = u'CPU&内存告警'
    for _asset in _asset_list:
        _ip = _asset['ip']
        _cpu_alarm, _ram_alarm = has_alarm(_ip)
        _content_list = [u'主机{ip}告警'.format(ip=_ip)]
        if _cpu_alarm:
            _content_list.append(u'CPU连续 {cnt} 次超过 {persent}%'.format(cnt=CNT, persent=CPU_PERCENT))
        if _ram_alarm:
            _content_list.append(u'内存连续 {cnt} 次超过 {persent}%'.format(cnt=CNT, persent=RAM_PERCENT))
        
        if len(_content_list) >= 2:
            sendemail(ALARM_RECIVERS, _title, ','.join(_content_list))
            logger.info('send mail to:%s, title:%s, msg:%s', ALARM_RECIVERS, _title, ','.join(_content_list))

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s %(name)s [%(lineno)d] %(levelname)s:%(message)s",
                    filename="monitor.log")
    #cron
    #

    monitor()