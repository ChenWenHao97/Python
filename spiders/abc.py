#!/usr/bin/env python
# coding=utf-8
import requests
root = "/home/cwh/Python/spiders/"
url = 'http://img0.dili360.com/rw9/ga/M00/47/FC/wKgBy1kQGluADPm_ADhv3cl-9zY117.tub.jpg'
path = root + url.split('/')[-1]#加上最后一个斜杠的内容
r = requests.get(url)
print(r.status_code)
with open(path,'wb') as f:
    f.write(r.content)
    f.close()


