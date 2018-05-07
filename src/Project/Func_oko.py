#-*-coding:utf8 -*_
'''
Created on 2018-5-2

@author: jason
'''


import requests
from bs4 import BeautifulSoup as bs
import datetime
import traceback
import MySQLdb
import sys
import Func
reload(sys)
sys.setdefaultencoding('utf8')



class LotteryOko():
    def __init__(self):
        pass


    def GetAllNews(self,newskind):
        type = newskind
        if type == 1: #双色球
            url = 'http://www.okooo.com/shuangseqiu/news/'
        elif type == 2:#福彩3D
            url = 'http://www.okooo.com/3d/news/'
        elif type == 3:#七彩乐
            url = 'http://www.okooo.com/qilecai/news/'
        else:
            url = ''
        return url
            
    def InsData(self,url,newskind,DateDif):
        res = Func.GetHeader(url)
        if res == '':
            print 'Time Out!'
        else:
            soup = bs(res,'html.parser')
            
            souptitle = soup.find('h2',attrs={'class':'news_title'})
            title = souptitle.text
            
            timesoup = soup.find('span',attrs={'class':'gray9 mgl10'})
            timestr = timesoup.text
            newstime = datetime.datetime.strptime(timestr,'%Y-%m-%d %H:%M')
            
            source = ''
            cmt = 0
            author = ''
            
            txtsoup = soup.find('div',attrs={'class':'newsDetail_txt'})
            newstxt = txtsoup.text.strip()
            
            now = datetime.datetime.now() - datetime.timedelta(days = DateDif)
            currdate = newstime
            
            
            if (now.year == currdate.year and now.month == currdate.month and now.day == currdate.day) or DateDif == -1 :
                
                conn = MySQLdb.connect(host='.',port = 3306,user='root',passwd='123456',db ='news_info',charset = 'utf8')
                cur = conn.cursor()  
      
                #insert数据
                dictypename = {1:'双色球', 2:'福彩3D', 3:"七彩乐"}
                sql = 'insert into tbl_news_info(title,newstype,source,pubtime,typename,webname,newsurl,contenttxt,joincount,author) select \'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',%d,\'%s\' from DUAL' % (title,'其它',source,newstime,dictypename[newskind],'澳客网',url,newstxt,cmt,author)
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
