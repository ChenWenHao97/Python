#!/usr/bin/env python
# coding=utf-8
import urllib.robotparser

rp = urllib.robotparser.RobotFileParser()
rp.set_url('http://example.webscraping.com/robots.txt')
rp.read()
url = 'http://example.webscraping.com'
user_agent = 'GoodCrawler'
print(rp.can_fetch(user_agent,url))


