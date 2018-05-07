# -*- coding:utf-8 -*-
'''
Created on 2018��2��22��

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
import bs4
import urllib2
import traceback
import requests





class LotterySohu():
    def __init__(self):
        pass



    def GetAllNews(self,newskind):
        #    kindtype:  1:福彩新闻
        type = newskind
        if type == 1: #福彩新闻
            url = 'http://caipiao.sohu.com/lotto/fc/'
        else:
            url = ''
        return url
    
#     def Schedule(self,a,b,c):
#         per = 100.0 * a * b / c
#         if per > 100 :
#             per = 100
#             print '%.2f%%' % per
            
    def InsData(self,url,newskind,DateDif):
        try:
            rep = requests.get(url,timeout=5)
            res = rep.content
        except:
            print 'time out'
            res = ''
        if res <> '':
            soup = bs(res,'html.parser')
            
            souptitle = soup.find('h1',attrs={'itemprop':'headline'})
            title = souptitle.text.strip()
            
            newstime = soup.find('div',attrs={'class':'time'}).text.strip()
            newstime = datetime.datetime.strptime(newstime,'%Y-%m-%d %H:%M:%S')
            
            source = soup.find('span',attrs={'id':'media_span'}).text.strip()
            
            authorstr = soup.find('span',attrs={'class':'editer','id':'editor_baidu'})
            if authorstr:
                author = authorstr.text.strip().replace('(责任编辑：','').replace(')','')
    
            cmt = 0
            
            souptxt = soup.find('div',attrs={'itemprop':'articleBody'})
            newstxt = souptxt.text.strip()
            
            now = datetime.datetime.now() - datetime.timedelta(days = DateDif)
            currdate = newstime
            
            if (now.year == currdate.year and now.month == currdate.month and now.day == currdate.day) or DateDif == -1 :
                
                conn = MySQLdb.connect(host='.',port = 3306,user='root',passwd='123456',db ='news_info',charset = 'utf8')
                cur = conn.cursor()  
      
                #insert数据
                dictypename = {1:'福彩新闻'}
                sql = 'insert into tbl_news_info(title,newstype,source,pubtime,typename,webname,newsurl,contenttxt,joincount,author) select \'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',%d,\'%s\' from DUAL where not exists(select 1 from tbl_news_info where title = \'%s\' limit 1) ' % (title,'其它',source,newstime,dictypename[newskind],'搜狐网',url,newstxt,cmt,author,title)
                try:
                    cur.execute(sql)
                    cur.close()
                    conn.commit()
                    conn.close()
                except Exception, e:
                    print 'str(Exception):\t', str(Exception)
                    print 'str(e):\t\t', str(e)
                    print 'repr(e):\t', repr(e)
                    print 'e.message:\t', e.message
                    print 'traceback.print_exc():'; traceback.print_exc()
                    print 'traceback.format_exc():\n%s' % traceback.format_exc()
                    print 'url:%s' % url
                    print '########################################################'
                finally:
                    pass
            else:
                print 'exists-inside'
        
    
    
 