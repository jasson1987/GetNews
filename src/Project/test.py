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



for NewsKind in range(1,10):
    for NewsType in range (1,6):
        lot = Lotteryzhcw()
        url = lot.GetAllNews(NewsKind,NewsType)
        print url
        res = GetHeader(url)
        if res == '':
            print 'Time Out!!'
        else :
            soup = bs(res,'html.parser')
            newslist = soup.findAll(attrs={'class':'Nlink'},limit = lmt)
            for listurl in newslist:
                for item in listurl('a'):
                    mainurl = 'http://www.zhcw.com/%s' % item['href']
                    title = item.text.strip()
                    IsExists = Checkurl(mainurl,title)
                    if IsExists == 0:
                        try:
                            lot.InsData(mainurl, NewsKind,NewsType, DD)
                            print 'succ  %d--%d' % (NewsKind,NewsType)
                        except:
                            print 'fail  %d--%d--url:%s' % (NewsKind,NewsType,mainurl)
                        finally:
                            pass
                    else:
                        print 'Exists'
    
    





