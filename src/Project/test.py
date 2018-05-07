# -*- coding:utf-8 -*-
'''
Created on 2018-2-22

@author: jason
'''

from bs4 import BeautifulSoup as bs
import urllib
import datetime
import MySQLdb
import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import os
import MySQLdb
import bs4
import urllib2
import traceback
import requests
from Func import GetHeader,Checkurl
from Func_zhcw import Lotteryzhcw
 
 

newskind = 2
newstype = 1
datedif = -1
lmt = 20


url = 'http://www.joycail.com/html/fucaiyaowen/20180420/7321.html'
rep = requests.get(url, timeout=5)
res = rep.content
soup = bs(res,'html.parser')

soupinfo = soup.find('div',attrs={'class','w700 fl'})
print soupinfo

souptitle = soupinfo.find('dt')
title = souptitle.text.strip()
print title

infolist = soup.find('dd',attrs={'class':'dd_time'})('span')
timestr = infolist[0].text.replace('发布时间：','')
source = infolist[1].text.replace('来源：','')

print source

newstime = datetime.datetime.strptime(timestr,'%Y-%m-%d %H:%M')
print newstime


soupcon = soup.find('dd',attrs={'class':'dd_content'})

newstxt = ''
for con in soupcon('p'):
    newstxt = newstxt + con.text.strip()

print newstxt



cmt = 0
author = ''











