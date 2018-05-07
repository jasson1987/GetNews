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





class Lottery500():
    def __init__(self):
        pass



    def GetAllNews(self,newskind):
        #    kindtype:  1:专家推荐
        type = newskind
        if type == 1: #专家推荐
            url = 'http://zx.500.com/ssq/n_zjtj/'
        elif type == 2:#双色球推荐
            url = 'http://zx.500.com/ssq/n_mtkd/'
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
            
            soupinfo = soup.find('div',attrs={'class':'news_title'})
            
            if newskind == 1:
                totstr = soupinfo.text.strip()
                
                totlist = totstr.split('\n')
                
                title = totlist[0]
                
                infolist = totlist[1].split('　 ')
                newstime = infolist[0].strip()
                source = infolist[1].replace('来源：','')
                author = infolist[2].replace('责编：','')
                
            elif newskind == 2:
                totstr = soupinfo.text.strip()
                totlist = []
                totlist1 = totstr.split('\n')
                for i in totlist1 :
                    if i :
                        totlist.append(i)
                
                title = totlist[0]
                author = totlist[1]
                source = totlist[2]
                newstime = totlist[3]
            
            
            cmt = 0
            newstxt = ''
            souptxt = soup.find('div',attrs={'class':'detail'})
            for p in souptxt('p'):
                newstxt = newstxt + p.text.strip()
            
            now = datetime.datetime.now() - datetime.timedelta(days = DateDif)
            currdate = datetime.datetime.strptime(newstime,'%Y-%m-%d %H:%M:%S')
            
            
            if (now.year == currdate.year and now.month == currdate.month and now.day == currdate.day) or DateDif == -1 :
                
                conn = MySQLdb.connect(host='.',port = 3306,user='root',passwd='123456',db ='news_info',charset = 'utf8')
                cur = conn.cursor()  
      
                #insert数据
                dictypename = {1:'专家推荐',2:'双色球推荐'}
                sql = 'insert into tbl_news_info(title,newstype,source,pubtime,typename,webname,newsurl,contenttxt,joincount,author) select \'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',%d,\'%s\' from DUAL where not exists(select 1 from tbl_news_info where title = \'%s\' limit 1) ' % (title,'其它',source,newstime,dictypename[newskind],'500彩票网',url,newstxt,cmt,author,title)
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
        
    
    
 