#!/usr/bin/python3
#coding: utf-8

import time
import requests

def get_timestamp():
    return int(time.time() * 1000)

def req(host, business, runtype):
    url = f'http://{host}/statusRun/?business={business}&runtype={runtype}&_={get_timestamp()}'
    print(url)
    res = requests.get(url)
    return res

host='172.22.77.11'
business='ss'
runtype='stop'

print(req(host, 'ss', 'stop').status_code)
time.sleep(3)

print(req(host, 'ss', 'start'))

