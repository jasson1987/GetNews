# -*- coding:utf-8 -*-
'''
Created on 2018��2��28��

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
import traceback
import requests

class Lotterycwl():
    def __init__(self):
        pass
    
    def GetAllNews(self,newskind,newstype):
        #    newskind:  1:党建工作,2:新闻资讯,3:福彩公益
        url =''
        type = newstype
        if newskind == 1:# '党建工作':
            if type == 1: #党建动态
                url = 'http://www.cwl.gov.cn/djgz/djdt/'
            elif type == 2:#理论学习
                url = 'http://www.cwl.gov.cn/djgz/llxx/'
            else:
                url = ''
        elif newskind == 2:#新闻资讯
            if type == 1:#新闻动态
                url = 'http://www.cwl.gov.cn/xwzx/xwdt/'
            elif type == 2:#派奖促销
                url = 'http://www.cwl.gov.cn/xwzx/pjcx/'
            elif type == 3:#大奖速递
                url = 'http://www.cwl.gov.cn/xwzx/djsd/'
            elif type == 4:#站主风采
                url = 'http://www.cwl.gov.cn/xwzx/zzfc/'
            elif type == 5:#各省资讯
                url = 'http://www.cwl.gov.cn/xwzx/gszx/'
            elif type == 6:#媒体声音
                url = 'http://www.cwl.gov.cn/xwzx/mtsy/'
            elif type == 7:#环球风采
                url = 'http://www.cwl.gov.cn/xwzx/hqfc/'
            else:
                url = ''        
        elif newskind == 3:#福彩公益
            if type == 1:#公益活动
                url = 'http://www.cwl.gov.cn/fcgy/gyhd/'
            elif type == 2:#公益金管理
                url = 'http://www.cwl.gov.cn/fcgy/gyjgl/'
            elif type == 3:#公益金使用
                url = 'http://www.cwl.gov.cn/fcgy/gyjsy/'
            elif type == 4:#公益金筹集
                url = 'http://www.cwl.gov.cn/fcgy/gyjcj/'
            elif type == 5:#公益金项目
                url = 'http://www.cwl.gov.cn/fcgy/gyjxm/'
            else:
                url = ''
        else:
            url = ''
        if url =='':
            res = ''
        else:
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
            
    def InsData(self,url,newskind,newstype,DateDif):
        try:
            rep = requests.get(url,timeout=5)
            res = rep.content
        except:
            res = ''
        if res <> '':
            soup = bs(res,'html.parser')
            soupdiv=soup.find(attrs={'class':'col-lg-8 col-md-8 col-sm-8 col-xs-12 text_content'})
    
            titlediv = soupdiv.find('h4')
            title = titlediv.text.strip()
            intro = ''
            
            topdiv = soupdiv('small')
            sourcestr = topdiv[0].text
            source = sourcestr.replace('来源：','').strip()
    
            newstime = topdiv[1].text.strip()
            newstime = newstime[0:19]
            newstime = datetime.datetime.strptime(newstime,'%Y-%m-%d %H:%M') 
    
            sourcediv = soupdiv.find(attrs={'class':'article col-lg-12 col-md-12 col-sm-12 col-xs-12'})
            newstxt = sourcediv.text.strip()
            newscontent = sourcediv
            newscontent1 ='待解决'
            now = datetime.datetime.now() - datetime.timedelta(days = DateDif)
            currdate = newstime
            picname = ''
            picpath = ''
            txtpic = ''
            intro = ''
            for c in soupdiv('p'):
                txtpic = txtpic + c.text + '\n'
                if c('img'):
                    for i in c('img'):
                        dir = 'D:/image/cwl/' + datetime.datetime.strftime(newstime,'%Y%m%d') + '/' 
                        imgname= os.path.basename(i['src'])
                        dirall = dir + imgname 
                        urlpath = os.path.dirname(i['src'])
                        if not os.path.exists(dir):
                            os.makedirs(dir)
                        src =  i['src']
                        if src[0:7] <> 'http://':
                            src = 'http://www.cwl.gov.cn%s' % src
                        urllib.urlretrieve(src,dirall,self.Schedule)
                        #if newskind == 1 and newstype == 2:
                         #   urllib.urlretrieve(i['src'],dirall,self.Schedule())
                        #else:
                            
                        #    if src[0:7] = 'http://':
                        #        urllib.urlretrieve('http://www.cwl.gov.cn%s' % i['src'],dirall,self.Schedule())
                        #    else:
                        #        urllib.urlretrieve(i['src'],dirall,self.Schedule())
                                
                        picname = picname + imgname + '|'
                        txtpic = '\n' + '%s[image=%s]' % (txtpic,urlpath) + '\n'
                        picpath = dir
    
            txtpic = txtpic.strip()
            cmt = 0
            conn = MySQLdb.connect(host='.',port = 3306,user='root',passwd='123456',db ='news_info',charset = 'utf8')
            cur = conn.cursor()           
            #insert数据
            
            dicnewskind = {1:'党建工作',2:'新闻动态',3:'福彩公益'}
            if newskind == 1:
                dicnewstype = {1:'党建动态',2:'理论学习'}
            if newskind == 2:
                dicnewstype = {1:'新闻动态',2:'派奖促销',3:'大奖速递',4:'站主风采',5:'各省资讯',6:'媒体声音',7:'环球风采'}
            if newskind == 3:
                dicnewstype = {1:'公益活动',2:'公益金管理',3:'公益金使用',4:'公益金筹集',5:'公益金项目'}
            sql = 'insert into tbl_news_info (title,content,pubtime,newstype,source,typename,webname,newsurl,contenttxt,intro,picpath,picname,txtpic,joincount) select \'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',%d from DUAL where not exists (select 1 from tbl_news_info where title = \'%s\' limit 1)' % (title,newscontent1,newstime,dicnewstype[newstype],source,dicnewskind[newskind],'中国福彩网',url,newstxt,intro,picpath,picname,txtpic,cmt,title)
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
            
            
    


