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
import traceback
import requests





class LotteryiFeng():
    def __init__(self):
        pass

    def GetAllNews(self,newskind):
        #    kindtype:  1:大奖资讯,2:彩市报道,3:彩票公益
        type = newskind
        if type == 1: #大奖资讯
            url = 'http://zx.cp.ifeng.com/winning/index.htm'
        elif type == 2:#彩市报道
            url = 'http://zx.cp.ifeng.com/anecdote/index.htm'
        elif type == 3:#彩票公益
            url = 'http://zx.cp.ifeng.com/charity/index.htm'
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
        try :
            rep = requests.get(url,timeout=5)
            res = rep.content
        except:
            print 'time out'
            res = ''
        if res <> '':
            soup = bs(res,'html.parser')
        
            souptop = soup.find(attrs={'class':'e_i_deta_LXT'})
            
            newscontent = souptop
            
            soupdiv = souptop.find('p')
            titlesoup = souptop('h1')
            divstr = soupdiv.text.strip().split('|')
            title = titlesoup[0].text
            title = title.strip()
            
            newstime = divstr[0]
            newstime = newstime.strip()
            
            source = divstr[1]
            source = source.replace('来源：','')
            source = source.strip()
            
            author = divstr[2]
            author = author.strip()
            
            cont = soup.find(attrs={'class':'e_i_deta_LXD'})
            
            newstxt = cont.text
            newstxt = newstxt.strip()
            newstxt = newstxt.replace("'","\\\'")
            
            
            now = datetime.datetime.now() - datetime.timedelta(days = DateDif)
            currdate = datetime.datetime.strptime(newstime,'%Y-%m-%d %H:%M:%S')
            
            
            localpath = 'D:/image/ifeng/%s/%s/%s/' % (newstime[0:4] ,newstime[5:7],newstime[8:10]) 
            
            txtpic = ''
            picname = ''
            intro = ''
            
            if (now.year == currdate.year and now.month == currdate.month and now.day == currdate.day) or DateDif == -1 :
                content = cont('p')
                for c in content:
                    txtpic = txtpic + c.text + '\n'
                    if c('img'):
                        image = c('img')
                        for i in image:
                            #下载图片
                            #http://zx.cp.ifeng.com/upload/images/news/0825001.png
                            #下载地址
                            downurlall = i['src']
                            #相对地址
                            urlpath = localpath.replace('D:/image/ifeng','')
                            #本地存储地址
                            imgname = os.path.basename(i['src'])
                            if os.path.splitext(imgname)[1] == '':
                                imgname = imgname+'.jpg'
                            localpathall = localpath + imgname
                            if not os.path.exists(localpath):
                                os.makedirs(localpath)
                            picname = picname + imgname + '|'
                            #下载图片
                            urllib.urlretrieve(downurlall,localpathall,self.Schedule)
                            txtpic =  '%s\n[image=%s]' % (txtpic.strip(),urlpath) + '\n'
                            
                picpath = localpath            
                
                txtpic = txtpic.replace("'","\\\'")     
                cmt = 0
                conn = MySQLdb.connect(host='.',port = 3306,user='root',passwd='123456',db ='news_info',charset = 'utf8')
                cur = conn.cursor()  
                 
                txtpic = txtpic.strip()      
                #insert数据
                dictypename = {1:'大奖资讯',2:'彩市报道',3:'彩票公益'}
                sql = 'insert into tbl_news_info(title,content,pubtime,newstype,source,typename,webname,newsurl,contenttxt,intro,picpath,picname,txtpic,joincount,author) select \'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',%d,\'%s\' from DUAL where not exists(select 1 from tbl_news_info where title = \'%s\' limit 1) ' % (title,newscontent,newstime,'其它',source,dictypename[newskind],'凤凰网',url,newstxt,intro,picpath,picname,txtpic,cmt,author,title)
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
        
    
    
 