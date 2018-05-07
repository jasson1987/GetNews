# -*-coding:utf-8 -*-

from bs4 import BeautifulSoup as bs
import urllib
import urllib2
import datetime
import MySQLdb
import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import os
import MySQLdb
import bs4
import Func
import traceback
import requests



class Lottery310Win():
    def __init__(self):
        pass
    
    
    
    def GetAllNews(self,newskind):
        #    kindtype:  1:彩通观察,2:国际彩讯,3:国内彩讯,4:中奖新闻
        type = newskind
        url = ''
        if type == 1: #双色球
            url = 'http://www.310win.com/shuangseqiu/info_t1sub1page1.html'
        elif type == 2:#大乐透
            url = 'http://www.310win.com/daletou/info_t1sub1page1.html'
        elif type == 3:#七星彩
            url = 'http://www.310win.com/qixingcai/info_t1sub1page1.html'
        elif type == 4:#福彩3d
            url = 'http://www.310win.com/3d/info_t1sub1page1.html'
        elif type == 5:#排列3排列5
            url = 'http://www.310win.com/p3p5/info_t1sub1page1.html'
        else:
            url = ''

        return url
    
    
    def Schedule(self,a,b,c):
        per = 100.0 * a * b / c
        if per > 100 :
            per = 100
            print '%.2f%%' % per
    
    
    def InsData(self,url,newskind,DateDif):
        try:
            rep = requests.get(url,timeout=5)
        except :
            rep = ''
            print 'time out'
            
        if rep <> '':
            rep = requests.get(url,timeout=10)
            res = rep.content
            soup = bs(res,'html.parser')
             
            soupcontent = soup.find(attrs={'class':'articleContent'})
            
            souptitle = soup.find(attrs={'class':'articleTitle'})
            title = souptitle.text
            
            soupinfo = soup.find(attrs={'class':'aInfo'})
            infolist = soupinfo.text.split('  ')
            while '' in infolist:
                infolist.remove('')
            
            author = infolist[0]
            
            newstime = infolist[1].replace('发表于：','')
            
            localpath = 'D:/image/win310/%s/%s/%s/' % (newstime[0:4],newstime[5:7],newstime[8:10])
            
            source = infolist[2].replace('来源：','')
            
            soupintro = soup.find(attrs={'class':'aBrief'})
            newsintro = soupintro.text.strip()
            
            content = soupcontent
            
            newscon = ''
            
            newstxt = content.text.strip().replace('\n','')
            
            now = datetime.datetime.now() - datetime.timedelta(days = DateDif)
            currdate = datetime.datetime.strptime(newstime,'%Y-%m-%d %H:%M')
            picname = ''
            picpath = ''
            txtpic = ''
            
            if (now.year == currdate.year and now.month == currdate.month and now.day == currdate.day) or DateDif == -1 :
                for con in content('p'):
                    txtpic = txtpic + con.text.strip() + '\n'
                    if con('img'):
                        img = con('img')
                        for i in img:
                            picname = os.path.basename(i['src'])
                            localpathall = localpath + picname
                            
                            urlpath = localpathall.replace('D:/image/win310','')          
                            downurl = i['src']
                            downurl = 'http://www.310win.com'+downurl.replace('http://www.310win.com','')
                            
                            if not os.path.exists(localpath):
                                os.makedirs(localpath)
                            urllib.urlretrieve(downurl, localpathall,self.Schedule)
                        txtpic = '%s[image=%s]' % (txtpic.strip(),urlpath) + '\n'
                    
                cmt = Func.GetComment('310win', newskind, url)
                picpath = localpath 
                conn = MySQLdb.connect(host='.',port = 3306,user='root',passwd='123456',db ='news_info',charset = 'utf8')
                cur = conn.cursor()           
                #insert数据
                
                dictypename = {1:'双色球',2:'大乐透',3:'七星彩',4:'福彩3d',5:'排列3排列5'}
                sql = 'insert into tbl_news_info (title,content,pubtime,newstype,source,typename,webname,newsurl,contenttxt,intro,picpath,picname,txtpic,joincount,author) select \'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',%d,\'%s\' from DUAL where not exists(select 1 from tbl_news_info where title = \'%s\' limit 1)' % (title,newscon,newstime,'',source,dictypename[newskind],'彩客网',url,newstxt,newsintro,picpath,picname,txtpic,cmt,author,title)
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
                  
            
    
    
    