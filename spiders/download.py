#!/usr/bin/env python
# coding=utf-8
#from urllib import request
from urllib import error
import urllib.request

def download(url,user_agent='wswp',proxy=None,num_retries=2):
    print("downloading:",url)
    headers = {'User-agent':user_agent}
    request = urllib.request.Request(url,headers=headers)

    opener = urllib.build_opener()

    if proxy:
        proxy_params = {urlparse.urlparse(url).scheme:proxy}
        opener.add_handler(urllib.ProxyHandler(proxy_params))
    try:
        html = urllib.request.urlopen(request).read()
    except error.URLError as e:
        print('Download error:'+e.reason)
        html = None
        if num_retries > 0:
            if hasattr(e,'code') and 500 <= e.code <600:
                html =  download(url,uer_agent,proxy,num_retries-1)
    return html


