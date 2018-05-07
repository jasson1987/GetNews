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
import os
from Func import GetHeader
import traceback
import requests



class Lotteryzhcw():
    def __init__(self):
        pass


    def GetAllNews(self,newskind,newstype):
        #    newskind:  1:彩种新闻,2:机构要闻,3:地市风采,4:中奖报道,5:彩民故事,6:站主之家,7:漫趣彩市,8:全球彩风,9:行业数据,10政策
        #    newstype:  1:双色球,2:3D,3:七乐彩,4:其它,5;刮刮乐
        url = ''
        type = newstype
        if newskind == 1:# '彩种新闻':
            if type == 1: #双色球
                url = 'http://www.zhcw.com/xinwen/caizhongxinwen-ssq/'
            elif type == 2:#3D
                url = 'http://www.zhcw.com/xinwen/caizhongxinwen-3D/'
            elif type == 3:#七乐彩
                url = 'http://www.zhcw.com/xinwen/caizhongxinwenqlc/'
            elif type == 4:#其它彩种
                url = 'http://www.zhcw.com/xinwen/caizhongxinwen-qt/'
            elif type == 5:#刮刮乐
                url = 'http://www.zhcw.com/xinwen/caizhongxinwen-ggl/'
            else :
                url = ''
        elif newskind == 2 :#机构要闻
            if type == 1:
                url = 'http://www.zhcw.com/xinwen/jigouyaowen/index.shtml?from=xwdh&do=jgyw'
            else :
                url = ''
        elif newskind == 3 :#地市风采
            if type == 1:
                url = 'http://www.zhcw.com/xinwen/dishifengcai/index.shtml?from=xwdh&do=dsfc'
            else:
                url = ''
        elif newskind == 4 :#中奖报道
            if type == 1:#双色球
                url = 'http://www.zhcw.com/xinwen/caimingushi/ssq/'
            elif type == 2:#3d
                url = 'http://www.zhcw.com/xinwen/caimingushi/3d/'
            elif type == 3:#七乐彩
                url = 'http://www.zhcw.com/xinwen/caimingushi/qlc/'
            else :
                url = ''
        elif newskind == 5 :#彩民故事
            if type == 1:
                url = 'http://www.zhcw.com/xinwen/caimingushi/qitacaizhong/'
            else :
                url = ''
        elif newskind == 6 :#站主之家
            if type == 1:
                url = 'http://www.zhcw.com/xinwen/zhanzhuzhijia/index.shtml'
            else:
                url = ''
        elif newskind == 7 :#漫趣彩市
            if type == 1:
                url ='http://www.zhcw.com/xinwen/manqucaishi/index.shtml'
            else:
                url = ''
        elif newskind == 8 :#全球彩风
            if type == 1:
                url = 'http://www.zhcw.com/xinwen/quanqiucaifeng/index.shtml?from=xwdh&do=qqcf'
            else:
                url = '' 
        elif newskind == 9:#行业数据
            if type == 1:
                url = 'http://www.zhcw.com/xinwen/hangyeshuju/'
            else:
                url = ''
        elif newskind == 10 :#政策
            if type == 1:
                url = 'http://www.zhcw.com/zhengce/'
            else:
                url = ''
        try:
            res = GetHeader(url)
        except:
            res = ''
        return res
    
    def Schedule(self,a,b,c):
        per = 100.0 * a * b / c
        if per > 100 :
            per = 100
            print '%.2f%%' % per
            
            
    def InsData(self,url,newskind,newstype,DateDif):
        res = GetHeader(url)
        if res == '':
            print 'Time Out!'
        else:
            soupnews = bs(res,'html.parser')
            message = soupnews.find(attrs={'class':'message'})
            newstime = message.text[0:19]
            parent = re.compile(u'[\u4e00-\u9fa5]+')
            source = parent.findall(message.text)[1]
            #titlestr = soupnews.title.text.replace('_中彩网','')
            titlestr = soupnews.title.text
            if titlestr.index('_'):
                titlelist = titlestr.split('_')
                title = titlelist[0]
            else:
                title = titlestr
            newscontent = soupnews.find(attrs={'id':'news_content'})
            newscontent1 = ''
            newstxt = newscontent.text
            currdate = datetime.datetime.strptime(newstime,'%Y-%m-%d %H:%M:%S')
            now = datetime.datetime.now() - datetime.timedelta(days = DateDif)
            picname = ''
            picpath = ''
            txtpic = ''
            intro = ''
    #获取新闻内容
            if (now.year == currdate.year and now.month == currdate.month and now.day == currdate.day) or DateDif == -1 :
                cont = soupnews.find(attrs={'id':'news_content'})
                content = cont('p')
                for c in content:
                    txtpic = txtpic + c.text + '\n'
                    if c('img'):
                        image = c('img')
                        for i in image :
                            #下载图片
                            dirall = 'D:/image/zhcw' + i['src']
                            dir = os.path.dirname(dirall)
                            urlpath = os.path.dirname(i['src'])
                            if not os.path.exists(dir):
                                os.makedirs(dir)
                            urllib.urlretrieve('http://www.zhcw.com'+i['src'],dirall,self.Schedule)
                            picname = picname + os.path.basename(i['src'])+'|'
                            txtpic =  '%s[image=%s]' % (txtpic,urlpath) + '\n'
                        picpath = dir
    
    #数据录入数据库
                cmt = 0
                conn = MySQLdb.connect(host='.',port = 3306,user='root',passwd='123456',db ='news_info',charset = 'utf8')
                cur = conn.cursor()  
                
                txtpic = txtpic.strip()      
    #insert数据
                dictypename = {1:'彩种新闻',2:'机构要闻',3:'地市风采',4:'中奖报道',5:'彩民故事',6:'站主之家',7:'漫趣彩市',8:'全球彩风',9:'行业数据',10:'政策'}
                dicnewstype = {0:'其它',1:'双色球',2:'3D',3:'七彩乐',4:'其它',5:'刮刮乐'}
                sql = 'insert into tbl_news_info(title,content,pubtime,newstype,source,typename,webname,newsurl,contenttxt,intro,picpath,picname,txtpic,joincount) select \'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',%d from DUAL where not exists(select 1 from tbl_news_info where title = \'%s\' limit 1) ' % (title,newscontent1,newstime,dicnewstype[newstype],source,dictypename[newskind],'中彩网',url,newstxt,intro,picpath,picname,txtpic,cmt,title)
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
                print 'exists'