#!/usr/bin/env python
# coding=utf-8
from download import download
from urllib.parse import urljoin
from urllib import error
import urllib
import re

def link_crawler(seed_url,link_regex,max_depth=2):
    max_depth = 2;
    depth= [seed_url]
    #见过的建立集合，防止重复
    #seen = set(crawl_queue)
    #防止动态的网站，造成爬虫陷阱，用字典好一点
    seen = {}

    while crawl_queue:
        url = crawl_queue.pop()
        html = download(url).decode('utf-8')
        #python3需要转码！！
        print(html)
        for link in get_links(html):
            if re.match(link_regex,link):
                link = urljoin(seed_url,link)
                #检测是否已经载过
                if link not in seen:
                    seen.add(link)
                    crawl_queue.append(link)

def get_links(html):
    webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    return webpage_regex.findall(html)

link_crawler('http://example.webscraping.com','/(index|view)')

