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
import requests
import json
import traceback


class Lotteryxinhua():
    def __init__(self):
        pass

    def GetAllNews(self,newskind):
        url = ''
        #    kindtype:  1:彩票要闻,2:福彩动态,3:彩票舆情,4:彩票科普,5:地方动态,6:彩市热点,7:行业数据,8:彩票公益,9:世界彩票
        type = newskind
        if type == 1: #彩票要闻
            url = 'http://www.xinhuanet.com/caipiao/cpyw.htm'
        elif type == 2:#福彩动态
            url = 'http://www.xinhuanet.com/caipiao/fcdt.htm'
        elif type == 3:#彩票舆情
            url = 'http://www.xinhuanet.com/caipiao/cpyq.htm'
        elif type == 4:#彩票科普
            url = 'http://www.xinhuanet.com/caipiao/cpkp.htm'
        elif type == 5:#地方动态
            url = 'http://www.xinhuanet.com/caipiao/dfdt.htm'
        elif type == 6:#彩市热点
            url = 'http://www.xinhuanet.com/caipiao/csrz.htm'
        elif type == 7:#行业数据
            url = 'http://www.xinhuanet.com/caipiao/hysj.htm'
        elif type == 8:#彩票公益
            url = 'http://www.xinhuanet.com/caipiao/cpgy.htm'
        elif type == 9:#世界彩票
            url = 'http://www.xinhuanet.com/caipiao/sjcp.htm'
        else:
            url = ''
        
        return url
    
    def Getjs(self,newskind):
        niddic={1:'1114374',2:'1114811',3:'1114388',4:'1114377',5:'1114382',6:'1114376',7:'1114477',8:'1114381',9:'1114383'}
        url = 'http://qc.wa.news.cn/nodeart/list'
        payload ={
                'nid':niddic[newskind],
                'pgnum':1,
                'cnt':50,
                'tp':1,
                'orderby':1,
                'callback':'jQuery111309723194450204504_1520403793193',
                '_':1520403793194
            }
        try:
            res = requests.get(url,params = payload,timeout = 5)
            json_all = res.content
        except:
            print 'time out'
            json_all = ''
        try :
            json_data = re.findall(r"{.+}",json_all)[0]        
            jsDict=json.loads(json_data)
        except:
            jsDict = 0
        
        return jsDict
    
    
    
    #下载进度
    def Schedule(self,a,b,c):
        per = 100.0 * a * b / c
        if per > 100 :
            per = 100
            print '%.2f%%' % per
    
    def InsData(self,url,newskind,DateDif):
        send_headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Connection':'keep-alive',
            'Referer':'http://www.xinhuanet.com/caipiao/'
        }
           
        req = urllib2.Request(url,headers=send_headers)
        try :
            res = urllib2.urlopen(req,timeout=5)
            soup = bs(res,'html.parser')
        except:
            soup = ''
        if soup <> '':
            title = soup.find(attrs={'class':'h-title'}).text.strip()
            newstime = soup.find(attrs={'class':'h-time'}).text.strip()
            source = soup.find(attrs={'id':'source'})
            
            if source == None:
                source = soup.find(attrs={'class':'h-info'})
                sourcestr = source('span')[1].text.replace('来源：','').strip()
            else:
                sourcestr = source.text.strip()
            
            
            currdate = datetime.datetime.strptime(newstime,'%Y-%m-%d %H:%M:%S')
            now = datetime.datetime.now() - datetime.timedelta(days = DateDif)
            
            
            intro = ''
            picname = ''
            txtpic = ''        
            newstxt = ''
            cont = soup.find(attrs={'id':'p-detail'})
            newscontent = ''
            
            if (now.year == currdate.year and now.month == currdate.month and now.day == currdate.day) or DateDif == -1 :
                
                content = cont('p')
                for c in content:
                    txtpic = txtpic + c.text + '\n'
                    newstxt = newstxt + c.text + '\n'
                    if c('img'):
                        image = c('img')
                        for i in image :
                            if i['src'] <> 'http://www.xinhuanet.com/images/syicon/space.gif':
                            #下载图片
                                downurl = 'http://www.xinhuanet.com/caipiao/%s/%s/' % (newstime[0:7],newstime[8:10])
                                downurlall = downurl + i['src']
                                dir = os.path.dirname(downurlall).replace('http://www.xinhuanet.com','')
                                localpath = 'D:/image/xinhua%s' % dir
                                urlpath = os.path.dirname(dir)
                                if not os.path.exists(localpath):
                                    os.makedirs(localpath)
                                picname = picname + os.path.basename(i['src'])+'|'
                                #下载图片
                                imgres = requests.get(downurlall,headers=send_headers)
                                with open(localpath+'/'+i['src'],'wb') as f:
                                    f.write(imgres.content)
                                txtpic =  '%s[image=%s]' % (txtpic,urlpath) + '\n'
                        picpath = localpath
                        newstxt = newstxt.strip()
                        
                txtpic = txtpic.replace("'","")
                newstxt = newstxt.replace("'","") 
                cmt = 0
                conn = MySQLdb.connect(host='.',port = 3306,user='root',passwd='123456',db ='news_info',charset = 'utf8')
                cur = conn.cursor()  
                 
                txtpic = txtpic.strip()      
                #insert数据
                dictypename = {1:'彩票要闻',2:'福彩动态',3:'彩票舆情',4:'彩票科普',5:'地方动态',6:'彩市热点',7:'行业数据',8:'彩票公益',9:'世界彩票'}
                sql = 'insert into tbl_news_info(title,content,pubtime,newstype,source,typename,webname,newsurl,contenttxt,intro,picpath,picname,txtpic,joincount) select \'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',%d from DUAL where not exists(select 1 from tbl_news_info where title = \'%s\' limit 1) ' % (title,newscontent,newstime,'其它',sourcestr,dictypename[newskind],'新华网',url,newstxt,intro,picpath,picname,txtpic,cmt,title)
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
            