# -*-coding:utf8 -*-
'''
Created on 2018-5-3

@author: jason
'''
import requests
import datetime
from bs4 import BeautifulSoup as bs
import MySQLdb
from Func import GetHeader
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import traceback




class LotteryAc():
    def __init__(self):
        pass


    def GetAllNews(self,newskind):
        type = newskind
        if type == 1: #双色球
            url = 'https://zx.aicai.com/zx/ssq/list'
        elif type == 2:#大乐透
            url = 'https://zx.aicai.com/zx/dlt/list'
        else:
            url = ''
        return url
            
    def InsData(self,url,newskind,DateDif):
        res = GetHeader(url)
        
        if res == '':
            print 'time out'
        else:
            soup = bs(res,'html.parser')
            
            titlesoup = soup.find('h1')
            title = titlesoup.text.strip()
            
            infosoup = soup.find('div',attrs={'class':'newHeadS'})
            infolist = infosoup('span')
            timestr = infolist[0].text
            source = infolist[1].text
            source = source.replace('来源：','')
            newstime = datetime.datetime.strptime(timestr,'%Y-%m-%d %H:%M:%S')
            
            cmt = 0
            author = ''
            
            txtsoup = soup.find('div',attrs={'class':'newsCenterA'})
            newstxt = txtsoup.text.strip()

            now = datetime.datetime.now() - datetime.timedelta(days = DateDif)
            currdate = newstime
            
            
            if (now.year == currdate.year and now.month == currdate.month and now.day == currdate.day) or DateDif == -1 :
                
                conn = MySQLdb.connect(host='.',port = 3306,user='root',passwd='123456',db ='news_info',charset = 'utf8')
                cur = conn.cursor()  
      
                #insert数据
                dictypename = {1:'双色球', 2:'大乐透',}
                sql = 'insert into tbl_news_info(title,newstype,source,pubtime,typename,webname,newsurl,contenttxt,joincount,author) select \'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',%d,\'%s\' from DUAL' % (title,'其它',source,newstime,dictypename[newskind],'爱彩网',url,newstxt,cmt,author)
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