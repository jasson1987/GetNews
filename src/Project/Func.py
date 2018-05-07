# -*-coding:utf-8 -*-
'''
Created on 2018-3-1

@author: jason
'''

import MySQLdb
import json
import requests
import re
import urllib2
import urllib
import time
import xlwt
import datetime
from bs4 import BeautifulSoup as bs
import bs4
import traceback
import os
import random
import sys
reload(sys)
sys.setdefaultencoding('utf8')




def Checkurl(url,title):
    exist = 0
    
    sql = 'select 1 from tbl_news_info where newsurl = \'%s\' or title = \'%s\' ' % (url,title)

    conn = MySQLdb.connect(host='.',port = 3306,user='root',passwd='123456',db ='news_info',charset = 'utf8')
    cur = conn.cursor()  

    try:
        exist = cur.execute(sql)
        cur.close()
        conn.commit()
        conn.close()
    except:
        exist = 0
    return exist

def CheckurlProv(url,title):
    exist = 0
    
    sql = 'select 1 from tbl_news_info where newsurl = \'%s\' or title = \'%s\' ' % (url,title)

    conn = MySQLdb.connect(host='.',port = 3306,user='root',passwd='123456',db ='news_info',charset = 'utf8')
    cur = conn.cursor()  

    try:
        exist = cur.execute(sql)
        cur.close()
        conn.commit()
        conn.close()
    except:
        exist = 0
    return exist

def GetHeader(url):    
    print url
    res = ''
    agent_list = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
        ]
    UA = random.choice(agent_list)
    user_headers = {
            'User-Agent':UA,
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Connection':'keep-alive'
                    }
    try:
        req = requests.get(url, headers=user_headers, timeout=10)
        res = req.content
    except requests.exceptions.ReadTimeout:
        print("timeout")
    except requests.exceptions.ConnectionError:
        print("connection Error")
    except requests.exceptions.RequestException:
        print("error")
    return res
    
    





def GetComment(webname,newskind,url):
    comcount = 0
    if  webname == 'sina':
        newsid = re.findall(r"doc.+\.",url)[0]
        newsid = newsid.replace('.','')
        newsid = newsid.replace('doc-i','comos-')
          
        payload = {
            'version':1,
            'format':'json',
            'channel':'ty',
            'newsid':newsid,
            'group':'undefined',
            'compress':0,
            'ie':'utf-8',
            'oe':'utf-8',
            'page':1,
            'page_size':3,
            't_size':3,
            'h_size':3,
            'thread':1,
            'callback':'jsonp_1520235839038',
            '_':'1520235839038'
            }
        res = requests.get('http://comment5.news.sina.com.cn/page/info' ,params = payload)
        json_all = res.content
        json_data = re.findall(r"{.+}",json_all)[0]
          
        jsDict=json.loads(json_data)
        
        try:
            comcount = jsDict['result']['count']['total']
        except:
            payload = {
                'version' : 1,
                'format' : 'js',
                'channel' : 'caitong' ,
                'newsid' : newsid,
                #'newsid' : 'comos-fyitapp2864583',
                'group' : '',
                'compress' : 1 ,
                'ie' : 'utf-8',
                'oe' : 'utf-8',
                'page' : 1,
                'show_reply' : 1,
                'page_size' : 20,
                'jsvar' : 'loader_1521513776198_73002544'
                }
            res = requests.get('http://comment5.news.sina.com.cn/page/info' ,params = payload)
            json_all = res.content
            json_data = re.findall(r"{.+}",json_all)[0]
              
            jsDict=json.loads(json_data)
            comcount = jsDict['result']['count']['total']
            
        

##########################################################################################
#         if newskind == 4:
#             newsid = re.findall(r"doc.+\.",url)[0]
#             newsid = newsid.replace('.','')
#             newsid = newsid.replace('doc-i','comos-')
#              
#             payload = {
#                 'version':1,
#                 'format':'json',
#                 'channel':'ty',
#                 'newsid':newsid,
#                 'group':'undefined',
#                 'compress':0,
#                 'ie':'utf-8',
#                 'oe':'utf-8',
#                 'page':1,
#                 'page_size':3,
#                 't_size':3,
#                 'h_size':3,
#                 'thread':1,
#                 'callback':'jsonp_1520235839038',
#                 '_':'1520235839038'
#             }
#              
#             res = requests.get('http://comment5.news.sina.com.cn/page/info' ,params = payload)
#              
#             json_all = res.content
#             json_data = re.findall(r"{.+}",json_all)[0]
#              
#             jsDict=json.loads(json_data)
#             comcount = jsDict['result']['count']['total']
#              
#              
#              
#         else:
#             newsid = re.findall(r"doc.+\.",url)[0]
#             newsid = newsid.replace('.','')
#             newsid = newsid.replace('doc-i','comos-')
#              
#             payload = {
#                 'version' : 1,
#                 'format' : 'js',
#                 'channel' : 'caitong' ,
#                 'newsid' : newsid,
#                 #'newsid' : 'comos-fyitapp2864583',
#                 'group' : '',
#                 'compress' : 1 ,
#                 'ie' : 'utf-8',
#                 'oe' : 'utf-8',
#                 'page' : 1,
#                 'show_reply' : 1,
#                 'page_size' : 20,
#                 'jsvar' : 'loader_1521513776198_73002544'}
#          
#             res = requests.get('http://comment5.news.sina.com.cn/page/info' ,params = payload)
#              
#             json_all = res.content
#             json_data = re.findall(r"{.+}",json_all)[0]
#              
#             jsDict=json.loads(json_data)
#             comcount = jsDict['result']['count']['total']
         
    if webname =='163':
        newsid = re.findall(r"[^/]+$",url)[0]
        newsid = newsid.replace('.html','')     
        newsurl = 'http://sdk.comment.163.com/api/v1/products/a2869674571f77b5a0867c3d71db5856/threads/%s' % newsid         
        
        payload = {
          'ibc':'jssdk',
          'callback':'tool1004959407081285372_1520240676539',
          '_':1520240676540
          }
        
        res = requests.get(newsurl ,params = payload)
        json_all = res.content
        
        json_data = re.findall(r"{.+}",json_all)[0]
        
        jsDict=json.loads(json_data)
        
        comcount = jsDict['cmtVote'] + jsDict['rcount']           

    if webname == '310win':
        newsid = re.findall(r"\d\d\d\d+",url)[0]
        
        murl = 'http://www.310win.com/Info/Information/Ajax.aspx'
        payload = {
            'HandleType':'click',
            'ArticleID':newsid,
            'randomT-_-':'0.36421787502242964'
            }
        res = requests.get(murl ,params = payload, timeout=5)

        json_all = res.content
        comcount = int(json_all)
        
        
    return comcount









def ImportExcel():
    path = 'E:/Doc/Doc_News/'
    fname = '%s.xls' % datetime.datetime.now().strftime('%Y-%m-%d-%H')
    
    conn = MySQLdb.connect(host='.',port = 3306,user='root',passwd='123456',db ='news_info',charset = 'utf8')
    cur = conn.cursor() 
     
    cur.callproc('proc_getnews')
     
    #重置游标位置  
    cur.scroll(0,mode='absolute')  
    #搜取所有结果  
    results = cur.fetchall()  
    #测试代码，print results  
    #获取MYSQL里的数据字段  
    fields = cur.description  
    #将字段写入到EXCEL新表的第一行  
    wbk = xlwt.Workbook()  
    sheet = wbk.add_sheet('sheet1',cell_overwrite_ok=True)  
     
    titlelist = [u'标题',u'网站名称',u'来源',u'一级分类',u'二级分类',u'发布时间',u'链接',u'参与人次',u'时间批次',u'网站类别'] #直接定义结果集的各字段名

    for i in range(0,len(titlelist)):   #写入字段信息
        sheet.write(0,i,titlelist[i])
     
    for row in range(1,len(results)+1):
        for col in range(0,len(fields)):
            if col in (5,8):
                style = xlwt.XFStyle()
                style.num_format_str = 'M/D/YY  h:mm:ss' # Other options: D-MMM-YY, D-MMM, MMM-YY, h:mm, h:mm:ss, h:mm, h:mm:ss, M/D/YY h:mm, mm:ss, [h]:mm:ss, mm:ss.0
                sheet.write(row, col, results[row-1][col], style)
#             sheet.col(5).width
            elif col == 6:
                sheet.write(row, col, xlwt.Formula('HYPERLINK("%s")' % results[row-1][col]))
                #sheet.col(6).wodth = 3333 * 5
            else:
                sheet.write(row,col,results[row-1][col]) 
            #设置宽度
    sheet.col(0).width = int(3000 * 3.5)
    sheet.col(1).width = 3000
    sheet.col(2).width = 3000
    sheet.col(3).width = 3000
    sheet.col(4).width = 3000
    sheet.col(5).width = int(3000 * 1.5)
    sheet.col(6).width = 3000 * 4
    sheet.col(7).width = 3000
    sheet.col(8).width = int(3000 * 1.2) 
    sheet.col(9).width = 3000
    
    cur.close()
    conn.close()
    try:
        wbk.save('%s%s' % (path,fname))
        print 'Excel Import Succesfully'  
    except:
        print 'Excel Import Fail'




def GetNewsList(type):
    url = 'http://www.jslottery.com/News/NewsList'
    payload ={
        'newsType': 1,
        'currentPage': 1,
        'pageSize': 20
        }
    
    plencode = urllib.urlencode(payload)
    req=urllib2.Request(url=url,data = plencode)
    res_data = urllib2.urlopen(req)
    res = res_data.read()
    
    jsDict=json.loads(res)
    Newslist=[]
    for i in range(0,20):
        Newslist.append(jsDict['NewsList'][i]['ID'])
    for j in range(0,20):
        Newslist.append(jsDict['NewsList'][j]['NewsTitle'])
    return Newslist


def GetXmlList(listid):
    heads={
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length': '0',
        'Content-Type':'charset:utf8',
        'Cookie': 'JSESSIONID=1CAC971916E0078912340134C4D409A9; UM_distinctid=1628e78a9463ac-06189e3917cb21-3f3c5501-144000-1628e78a94819d; CNZZDATA1000130400=498410719-1522806702-http%253A%252F%252Fwww.gxcaipiao.com.cn%252F%7C1522806702; jiathis_rdc=%7B%22http%3A//www.gxcaipiao.com.cn/news/39195_1.html%22%3A-1904630611%2C%22http%3A//www.gxcaipiao.com.cn/news/38918_1.html%22%3A-1904213197%2C%22http%3A//www.gxcaipiao.com.cn/news/24491_1.html%22%3A-1904208020%2C%22http%3A//www.gxcaipiao.com.cn/news/40512_1.html%22%3A-1904204808%2C%22http%3A//www.gxcaipiao.com.cn/news/39921_1.html%22%3A-1904196561%2C%22http%3A//www.gxcaipiao.com.cn/news/38916_1.html%22%3A0%7C1522809198015%2C%22http%3A//www.gxcaipiao.com.cn/news/21615_1.html%22%3A%222%7C1522809208942%22%7D',
        'Host': 'www.gxcaipiao.com.cn',
        'Origin': 'http://www.gxcaipiao.com.cn',
        'Referer': 'http://www.gxcaipiao.com.cn/commHtml/pnews.html?smallclassid=209',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
        }


    stamp = int(round(time.time() * 1000))
    url = 'http://www.gxcaipiao.com.cn/xml/newslist/newslist_%s.xml?timestamp=%s' % (listid,stamp)

    news=[]
    req = urllib2.Request(url, headers = heads)
    res = urllib2.urlopen(req)

    soup = bs(res.read(),'html.parser')
    for a in soup('list'):
        news.append(a['newsid'])
    for i in soup('list'):
        news.append(i['newstitle'])
        
    return news

    