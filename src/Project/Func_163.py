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
import MySQLdb
import bs4
import urllib2
import Func
import traceback
import requests
 
 

class Lottery163():
    def __init__(self):
        pass
    
    def GetAllNews(self,newskind):
        #    kindtype:  1:彩市新闻,2:数字大奖
        type = newskind
        if type == 1: #彩市新闻
            url = 'http://cai.163.com/zx/more_news.html'
        elif type == 2:#数字大奖
            url = 'http://cai.163.com/zx/more_shuZiAward.html'
        else:
            url = ''
        try :
            rep = requests.get(url,timeout=5)
            res = rep.content
        except:
            print 'time out'
            res = ''
        return res
 
    def Schedule(self,a,b,c):
        per = 100.0 * a * b / c
        if per > 100 :
            per = 100
            print '%.2f%%' % per
 
 
    def InsData(self,url,newskind,DateDif):
        try:
            rep = requests.get(url,timeout=5)
            res = rep.content
        except:
            print 'time out'
            res = ''
        if res <> '':
            soup = bs(res,'html.parser')
            soupdiv = soup.find(attrs={'class':['ep-content-main','d_info clearfix']})
            
            titlediv = soupdiv.find(attrs={'id':'h1title'})
            title = titlediv.text.strip()
            
            timediv = soupdiv.find(attrs={'class':'ep-time-soure cDGray'})
            if timediv == None:
                timediv = soupdiv.find(attrs={'style':'float:left;'})
            newstime = timediv.text.strip()
            newstime = newstime[0:19]
            newstime = datetime.datetime.strptime(newstime,'%Y-%m-%d %H:%M:%S') 
            
            sourcediv = soupdiv.find(attrs={'id':'ne_article_source'})
            if sourcediv ==None:
                source = '网易彩票'
            else:
                source = sourcediv.text.strip()    
           
            string = ''
            for i in soupdiv('p'):
                string = string + i.text
            
            newstxt = string
            newscontent1 = '待解决'
            now = datetime.datetime.now() - datetime.timedelta(days = DateDif)
            currdate = newstime
            picname = ''
            picpath = ''
            txtpic = ''
            intro = ''

        #处理图片
            if (now.year == currdate.year and now.month == currdate.month and now.day == currdate.day) or DateDif == -1 :
                for c in soupdiv('p'):
                    txtpic = txtpic + c.text + '\n'
                    if c('img'):
                        for i in c('img'):
                            dir = 'D:/image/163/' + datetime.datetime.strftime(newstime,'%Y%m%d') + '/'
                            #imgname= os.path.basename(i['src'])
                            src = re.findall("(.*.png|.*.jpg|.*.gif|.*.jpeg)",i['src'])
                            imgname= os.path.basename(src[0])
                            dirall = dir + imgname 
                            urlpath = '/' + datetime.datetime.strftime(newstime,'%Y%m%d') + '/'+imgname
                            if not os.path.exists(dir):
                                os.makedirs(dir)
                            urllib.urlretrieve(src[0],dirall,self.Schedule)
                            picname = picname + imgname + '|'
                            txtpic = '\n' + '%s[image=%s]' % (txtpic,urlpath)
                            picpath = dir          
            
                txtpic = txtpic.strip()
                cmt = Func.GetComment('163', newskind, url)
                conn = MySQLdb.connect(host='.',port = 3306,user='root',passwd='123456',db ='news_info',charset = 'utf8')
                cur = conn.cursor()           
                #insert数据
                
                dictypename = {1:'彩市新闻',2:'数字大奖'}
                sql = 'insert into tbl_news_info (title,content,pubtime,newstype,source,typename,webname,newsurl,contenttxt,intro,picpath,picname,txtpic,joincount) select \'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',%d from DUAL where not exists (select 1 from tbl_news_info where title = \'%s\' limit 1)' % (title,newscontent1,newstime,'其它',source,dictypename[newskind],'网易',url,newstxt,intro,picpath,picname,txtpic,cmt,title)
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


