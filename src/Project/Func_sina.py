# -*- coding:utf-8 -*-
'''
Created on 2018-2-24

@author: jason
'''
from bs4 import BeautifulSoup as bs
import urllib
import requests
import datetime
import MySQLdb
import re
import os
import urllib2
from Func import GetComment,GetHeader
import traceback

class Lotterysina():
    def __init__(self):
        pass

    def GetAllNews(self,newskind):
        #    kindtype:  1:彩通观察,2:国际彩讯,3:国内彩讯,4:中奖新闻
        type = newskind
        if type == 1: #彩通观察
            url = 'http://roll.sports.sina.com.cn/s_zucai_all/19/index.shtml'
        elif type == 2:#国际彩讯
            url = 'http://roll.sports.sina.com.cn/s_zucai_all/17/index.shtml'
        elif type == 3:#国内彩讯
            url = 'http://roll.sports.sina.com.cn/s_zucai_all/7/index.shtml'
        elif type == 4:#中奖新闻
            url = 'http://roll.sports.sina.com.cn/s_zucai_all/16/index.shtml'
        else :
            url = ''
#         try :
#             rep = requests.get(url,timeout=5)
#             res = rep.content
#         except:
#             print 'time out'
#             res = ''
#         return res
        return url
    #下载进度
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
            res = ''
        if res <> '':
            soup = bs(res,'html.parser')
            soupnews = soup.find(attrs={'class':['q-box-news','main-content w1240']})
            newstimediv = soupnews.find(attrs={'class':['news-time','date-source']})
            #时间
            newstime = datetime.datetime.strptime(newstimediv('span')[0].text,'%Y年%m月%d日 %H:%M')
            #来源
            source = '新浪彩票'
            #Title
            if not soupnews.find(attrs={'id':'news_title'}):
                title = soupnews.find(attrs={'class':'main-title'}).text
            else:
                title = soupnews.find(attrs={'id':'news_title'}).text
    
            #获取新闻介绍
            if not soupnews.find(attrs={'class':'news-introduct'}):
                newsintro = ''
            else:
                newsintro = soupnews.find(attrs={'class':'news-introduct'}).text.strip()
            
            #新闻内容
            newscontent = soupnews.find(attrs={'class':['article-txt','article']})
            newscon =''
            newstxt = newscontent.text.strip()
            #存储间隔时间
            now = datetime.datetime.now() - datetime.timedelta(days = DateDif)
            currdate = newstime
            picname = ''
            picpath = ''
            txtpic = ''
            
            
            
    
            #处理图片
            if (now.year == currdate.year and now.month == currdate.month and now.day == currdate.day) or DateDif == -1 :
                for c in newscontent(['div','p']):
                    txtpic = txtpic + c.text
                    if c('img'):
                        image = c('img')
                        for i in image :
                            if os.path.basename(i['src']) <> 'caitong_artical_bottom.jpg':
                                dir = 'D:/image/sina/' + datetime.datetime.strftime(newstime,'%Y%m%d') + '/'
                                imgname= os.path.basename(i['src'])
                                dirall = dir + imgname 
                                urlpath = '/' + datetime.datetime.strftime(newstime,'%Y%m%d') + '/'+imgname
                                if not os.path.exists(dir):
                                    os.makedirs(dir)
                                src = i['src']
                                src = 'http:' + src.replace('http:','')
                                urllib.urlretrieve(src,dirall,self.Schedule)
                                picname = picname + imgname + '|'
                                txtpic = '\n' + '%s[image=%s]' % (txtpic,urlpath)
                                picpath = dir
                        
                txtpic = txtpic.strip()
                #获得评论数
                cmt = Func.GetComment('sina', newskind, url)
                conn = MySQLdb.connect(host='.',port = 3306,user='root',passwd='123456',db ='news_info',charset = 'utf8')
                cur = conn.cursor()           
                #insert数据
                
                dictypename = {1:'彩通观察',2:'国际彩讯',3:'国内彩讯',4:'中奖新闻'}
                sql = 'insert into tbl_news_info (title,content,pubtime,newstype,source,typename,webname,newsurl,contenttxt,intro,picpath,picname,txtpic,joincount) select \'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',%d from DUAL where not exists(select 1 from tbl_news_info where title = \'%s\' limit 1)' % (title,newscon,newstime,'其它',source,dictypename[newskind],'新浪网',url,newstxt,newsintro,picpath,picname,txtpic,cmt,title)
                try:
                    cur.execute(sql)
                    cur.close()
                    conn.commit()
                    conn.close()
                except Exception, e:
                    print sql
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
            
            
    def InsData_Spe(self,url,newskind,DateDif):
        headers = {'User-agent' : 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:22.0) Gecko/20100101 Firefox/22.0'}
        try :
            request = urllib2.Request(url, headers = headers,timeout=2)
            res = urllib2.urlopen(request,timeout=2)
        except:
            print 'time out'
            res = ''
        if res <> '':
            soup = bs(res,'html.parser')
            topsoup = soup.find(attrs={'class':'top-bar-wrap'})
    
            title = topsoup.find(attrs={'class':'second-title'}).text.strip()
            newstimeori = topsoup.find(attrs={'class':'date'}).text.strip()
            source = topsoup.find(attrs={'class':'source ent-source'}).text.strip()
    
            newstime1 = newstimeori.replace('年','-').replace('月','-').replace('日','')
            newstime = datetime.datetime.strptime(newstime1,'%Y-%m-%d %H:%M')
    
            newsintro = ''
            #新闻内容
            soupnews = soup.find(attrs={'class':'article'})
            newscontent = soupnews
            #新闻内容文本
            newstxt = newscontent.text.strip()
            
            newscontent1 = '待解决'
            
            now = datetime.datetime.now() - datetime.timedelta(days = DateDif)
            currdate = newstime
            
            picname = ''
            picpath = ''
            txtpic = ''
    
            #处理图片
            if (now.year == currdate.year and now.month == currdate.month and now.day == currdate.day) or DateDif == -1 :
                for c in newscontent(['div','p']):
                    txtpic = txtpic + c.text
                    image = c('img')
                    for i in image:
                        if os.path.basename(i['src']) <> 'caitong_artical_bottom.jpg':
                            dir = 'D:/image/sina/' + datetime.datetime.strftime(newstime,'%Y%m%d') + '/'
                            imgname= os.path.basename(i['src'])
                            dirall = dir + imgname
                            urlpath = '/' + datetime.datetime.strftime(newstime,'%Y%m%d') + '/'+imgname
                            src = i['src']
                            src = src.replace('http:','')
                            if not os.path.exists(dir):
                                os.makedirs(dir)
                            urllib.urlretrieve('http:%s' % src,dirall,self.Schedule)
                            picname = picname + imgname + '|'
                            txtpic =  '\n' + '%s[image=%s]' % (txtpic,urlpath) 
                            picpath = dir
            
                txtpic = txtpic.strip()
                cmt = Func.GetComment('sina', newskind, url)
                conn = MySQLdb.connect(host='.',port = 3306,user='root',passwd='123456',db ='news_info',charset = 'utf8')
                cur = conn.cursor()           
                #insert数据
                
                dictypename = {1:'彩通观察',2:'国际彩讯',3:'国内彩讯',4:'中奖新闻'}
                sql = 'insert into tbl_news_info (title,content,pubtime,newstype,source,typename,webname,newsurl,contenttxt,intro,picpath,picname,txtpic,joincount) select \'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',%d from DUAL where not exists(select 1 from tbl_news_info where title = \'%s\' limit 1) ' % (title,newscontent1,newstime,'新浪无',source,dictypename[newskind],'新浪网',url,newstxt,newsintro,picpath,picname,txtpic,cmt,title)
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
        