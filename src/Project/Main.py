# -*- coding:utf-8 -*-
'''
Created on 2018年2月22日

@author: jason
'''

from bs4 import BeautifulSoup as bs
import requests
import re
from Func_zhcw import Lotteryzhcw
from Func_sina import Lotterysina
from Func_163 import Lottery163
from Func_cwl import Lotterycwl
from Func_xinhua import Lotteryxinhua
from Func_ifeng import LotteryiFeng
from Func_310win import Lottery310Win
from Func_sohu import LotterySohu
from Func_lot500 import Lottery500
from Func_oko import LotteryOko
from Func_ac import LotteryAc
from Func_joyc import LotteryJoyc
from Func import Checkurl,GetHeader
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class GetWebNews():
    def __init__(self):
        pass
    
    def GetNewWeb(self,weblist,datedif,linklimit):
        DD = datedif
        lmt = linklimit

#综合类新闻网站
        for site in weblist:
        #weblist = ['中彩','新浪','网易','中国福彩','新华网','凤凰网','彩客网']:
        
###中彩网##################################################################################################################################################
            if site == '中彩':
                print 'zhcw'
                for NewsKind in range(1,10):
                    for NewsType in range (1,6):
                        lot = Lotteryzhcw()
                        res = lot.GetAllNews(NewsKind,NewsType)
                        if res <> '':
                            soup = bs(res,'html.parser')
                            newslist = soup.findAll(attrs={'class':'Nlink'},limit = lmt)
                            for listurl in newslist:
                                for item in listurl('a'):
                                    mainurl = 'http://www.zhcw.com/%s' % item['href']
                                    title = item.text.strip()
                                    IsExists = Checkurl(mainurl,title)
                                    if IsExists == 0:
                                        try:
                                            lot.InsData(mainurl, NewsKind,NewsType, DD)
                                            print 'succ  %d--%d' % (NewsKind,NewsType)
                                        except:
                                            print 'fail  %d--%d--url:%s' % (NewsKind,NewsType,mainurl)
                                        finally:
                                            pass
                                    else:
                                        print 'Exists'
                            print 'zhcw-finish %d--%d' % (NewsKind,NewsType)
                    print 'zhcw-finish %d' % NewsKind
          
##新浪网#####################################################################################################################################################
            elif site == '新浪':  
                print 'sina'
                for NewsKind in range(1,5):
                    lot = Lotterysina()
                    res = lot.GetAllNews(NewsKind)
                    soup = bs(res,'html.parser')
                    newslist = soup.findAll(attrs={'class':'c_tit'},limit=lmt)
                    for listurl in newslist:
                        for item in listurl('a'):
                            mainurl = item['href']
                            title = item.text.strip()
                            IsExists = Checkurl(mainurl,title)
                            if IsExists == 0:
                                try:
                                    if NewsKind == 4:
                                        lot.InsData_Spe(mainurl, NewsKind, DD)
                                    else:
                                        lot.InsData(mainurl,NewsKind,DD)
                                    print 'succ %d' % NewsKind
                                except:
                                    print 'fail %d--url:%s' % (NewsKind,mainurl)
                                finally:
                                    pass
                            else:
                                print 'Exists'
                    print 'sina-finish %d' % NewsKind
                 
##网易#####################################################################################################################################################
            elif site == '网易':    
                print '163'
                for NewsKind in range(1,3):
                    lot = Lottery163()
                    res = lot.GetAllNews(NewsKind)
                    soup = bs(res,'html.parser')
                    newslist = soup.find(attrs={'class':'zx_list_l'})
                    for listurl in newslist.findAll('li',limit=lmt):
                        for item in listurl('a'):
                            mainurl = item['href']
                            title = item.text.strip()
                            IsExists = Checkurl(mainurl,title)
                            if IsExists == 0:
                                try:
                                    lot.InsData(mainurl,NewsKind,DD)
                                    print 'succ %d' % NewsKind
                                except:
                                    print 'fail %d--url:%s' % (NewsKind,mainurl)
                                finally:
                                    pass
                            else:
                                print 'Exists'
                    print '163-finish %d' % NewsKind
                  
##中国福彩网#####################################################################################################################################################
            elif site == '中国福彩':    
                print 'cwl'
                for NewsKind in range(1,4):
                    for NewsType in range(1,8):
                        lot = Lotterycwl()
                        res = lot.GetAllNews(NewsKind, NewsType)
                        if res <> '':
                            soup = bs(res,'html.parser')
                            newslist = soup.find(attrs={'class':'list-group'})
                            for listurl in newslist.findAll('li',limit=lmt):
                                for item in listurl('a'):
                                    mainurl = 'http://www.cwl.gov.cn'+item['href']
                                    title = item.text.strip()
                                    title = title.replace('• ','')
                                    IsExists = Checkurl(mainurl,title)
                                    if IsExists == 0:
                                        try:
                                            lot.InsData(mainurl, NewsKind, NewsType, DD)
                                            print 'succ %d--%d' % (NewsKind,NewsType)
                                        except:
                                            print 'fail %d--%d--url:%s' % (NewsKind,NewsType,mainurl)
                                        finally:
                                            pass
                                    else:
                                        print 'Exists'
                        print 'cwl-finish %d--%d' % (NewsKind,NewsType)
                  
###新华网##################################################################################################################################################
            elif site == '新华网':
                print 'xinhua'
                for NewsKind in range(1,10):
                    lot = Lotteryxinhua()
                    jd = lot.Getjs(NewsKind)
                    for i in range(0,lmt):
                        mainurl = jd['data']['list'][i]['LinkUrl']
                        title = jd['data']['list'][i]['Title']
                        IsExists = Checkurl(mainurl,title)
                        if IsExists == 0:
                            try:
                                lot.InsData(mainurl, NewsKind, DD)
                                print 'succ %d' % NewsKind
                            except:
                                print 'fail %d--url:%s' % (NewsKind,mainurl)
                            finally:
                                pass
                        else:
                            print 'Exists'
                    print 'xinhua-finish %d' % (NewsKind)
                print 'xinhua-finish'
         
###凤凰网##################################################################################################################################################
            elif site == '凤凰网':
                print 'ifeng'
                for NewsKind in range(1,4):
                    lot = LotteryiFeng()
                    res = lot.GetAllNews(NewsKind)
                    if res <> '':
                        soup = bs(res,'html.parser')
                        newslist = soup.find(attrs={'class':'e_i_list_DLHall'})
                        for listurl1 in newslist.findAll('li',limit=lmt):
                            for listurl in listurl1.findAll(attrs={'class':'b'}):
                                for item in listurl('a'):
                                    mainurl = item['href'].replace('..','http://zx.cp.ifeng.com')
                                    title = item.text.strip()
                                    IsExists = Checkurl(mainurl,title)
                                    if IsExists == 0:
                                        try:
                                            lot.InsData(mainurl, NewsKind, DD)
                                            print 'succ %d' % (NewsKind)
                                        except:
                                            print 'fail %d--url:%s' % (NewsKind,mainurl)
                                        finally:
                                            pass
                                    else:
                                        print 'Exists'
                        print 'ifeng-finish %d' % (NewsKind)
                         
         
###彩客网#####################################################################################################################################################
            elif site == '彩客网':    
                print '310win'
                lot = Lottery310Win()
                for NewsKind in range(1,6):
                    url = lot.GetAllNews(NewsKind)
                    try:
                        rep = requests.get(url,timeout=5)
                    except:
                        rep = '' 
                        print 'timeout'
                       
                    if rep <>'':
                        res = rep.content
                        soup = bs(res,'html.parser')
                        newslist = soup.find(attrs={'class':'td_div3'})
                        for i in newslist.findAll('td',attrs={'class':''}):
                            for a in i('a'):
                                if len(a.text)>10:
                                    href = a['href']
                                    title = a.text.strip()
                                    mainurl = 'http://www.310win.com%s' % href.replace('http://www.310win.com','')
                                    IsExists = Checkurl(mainurl,title)
                                    if IsExists == 0:
                                        try:
                                            lot.InsData(mainurl,NewsKind,DD)
                                            print 'succ %d' % NewsKind
                                        except:
                                            print 'fail %d--url:%s' % (NewsKind,mainurl)
                                        finally:
                                            pass
                                    else:
                                        print 'Exists'
                    print '310win-finish %d' % NewsKind
                    
                    
###搜狐网#####################################################################################################################################################
                                
            elif site == '搜狐网':    
                print 'soho'
                lot = LotterySohu()
                for NewsKind in range(1,2):
                    url = lot.GetAllNews(NewsKind)
                    try:
                        rep = requests.get(url,timeout=5)
                        res = rep.content
                        soup = bs(res,'html.parser')
                    except:
                        soup = ''
                    if soup <> '':
                        newslist = soup.find('div',attrs={'class':'f14list'})
                        for li in newslist.findAll('li',limit=lmt):
                            for a in li('a'):
                                    href = a['href']
                                    title = a.text.strip()
                                    mainurl = href
                                    IsExists = Checkurl(mainurl,title)
                                    if IsExists == 0:
                                        try:
                                            lot.InsData(mainurl,NewsKind,DD)
                                            print 'succ %d' % NewsKind
                                        except:
                                            print 'fail %d--url:%s' % (NewsKind,mainurl)
                                        finally:
                                            pass
                                    else:
                                        print 'Exists'
                    print 'sohu-finish %d' % NewsKind

##500彩票网#####################################################################################################################################################
                                
            elif site == '500彩票网':    
                print 'lot500'
                lot = Lottery500()
                for NewsKind in range(1,3):
                    url = lot.GetAllNews(NewsKind)
                    try :
                        rep = requests.get(url,timeout=5)
                        res = rep.content
                        soup = bs(res,'html.parser')
                    except:
                        print 'time out'
                        soup = ''
                    if soup <> '':
                        souplist = soup.find('div',attrs={'class':'news_list'})
                        for li in souplist('li',limit=lmt):
                            for a in li('a'):
                                href = a['href']
                                title = a.text.strip()
                                mainurl = href
                                IsExists = Checkurl(mainurl,title)
                                if IsExists == 0:
                                    try:
                                        lot.InsData(mainurl,NewsKind,DD)
                                        print 'succ %d' % NewsKind
                                    except:
                                        print 'fail %d--url:%s' % (NewsKind,mainurl)
                                    finally:
                                        pass
                                else:
                                    print 'Exists'
                    print 'lot500-finish %d' % NewsKind
        
        
            elif site == '澳客':    
                print 'Oko'
                lot = LotteryOko()
                for NewsKind in range(1,4):
                    url = lot.GetAllNews(NewsKind)
                    res = GetHeader(url)
                    if res == '':
                        soup = ''
                        print 'Time Out!'
                    else:
                        soup = bs(res,'html.parser')
                    if soup <> '':
                        souplist = soup.find('div',attrs={'class':'news_list'})
                        for h in souplist('h2',attrs={'class':'news_title'},limit=lmt):
                            for a in h('a'):
                                href = a['href']
                                title = a.text.strip()
                                mainurl = 'http://www.okooo.com%s' % href.replace('http://www.okooo.com','')
                                IsExists = Checkurl(mainurl,title)
                                if IsExists == 0:
                                    try:
                                        lot.InsData(mainurl,NewsKind,DD)
                                        print 'succ %d' % NewsKind
                                    except:
                                        print 'fail %d--url:%s' % (NewsKind,mainurl)
                                    finally:
                                        pass
                                else:
                                    print 'Exists'
                    print 'Oko-finish %d' % NewsKind
                    
            elif site == '爱彩':    
                print 'Ac'
                lot = LotteryAc()
                for NewsKind in range(1,3):
                    url = lot.GetAllNews(NewsKind)
                    res = GetHeader(url)
                    if res == '':
                        print 'Time Out!'
                        soup = ''
                    else:    
                        soup = bs(res,'html.parser')
                    if soup <> '':
                        souplist = soup.find('div',attrs={'class':'newsjjcList'})
                        for li in souplist('li',limit=lmt):
                            i = li.find('div',attrs={'class':'newsJTitle'})
                            for a in i('a',attrs={'target':'_blank'}):
                                href = a['href']
                                title = a.text.strip()
                                mainurl = 'https://zx.aicai.com%s' % href.replace('https://zx.aicai.com','')
                                IsExists = Checkurl(mainurl,title)
                                if IsExists == 0:
                                    try:
                                        lot.InsData(mainurl,NewsKind,DD)
                                        print 'succ %d' % NewsKind
                                    except:
                                        print 'fail %d--url:%s' % (NewsKind,mainurl)
                                    finally:
                                        pass
                                else:
                                    print 'Exists'
                    print 'Ac-finish %d' % NewsKind
                    
            elif site == '快乐福彩':    
                print 'joyc'
                lot = LotteryJoyc()
                for NewsKind in range(1,5):
                    for NewsType in range(1,9):
                        url = lot.GetAllNews(NewsKind,NewsType)
                        res = GetHeader(url)
                        if res == '':
                            print 'Time Out!'
                            soup = ''
                        else:    
                            soup = bs(res,'html.parser')
                        if soup <> '':
                            souplist = soup.find('div',attrs={'class':'main clearfix'})
                            for li in souplist('li',limit=lmt):
                                for a in li('a',attrs={'target':'_blank'}):
                                    href = a['href']
                                    title = a.text.strip()
                                    mainurl = 'http://www.joycail.com%s' % href.replace('http://www.joycail.com','')
                                    IsExists = Checkurl(mainurl,title)
                                    if IsExists == 0:
                                        try:
                                            lot.InsData(mainurl,NewsKind,NewsType,DD)
                                            print 'succ %d--%d' % (NewsKind,NewsType)
                                        except:
                                            print 'fail %d--%d--url:%s' % (NewsKind,NewsType,mainurl)
                                        finally:
                                            pass
                                    else:
                                        print 'Exists'
                    print 'Ac-Joyc %d' % NewsKind

# lot = Lottery()
# for web in range(1,5):
#     if web == 1:
#         webname = 'zhcw'
#     elif web == 2:
#         webname = 'sina'
#     elif web == 3:
#         webname = '163'
#     elif web == 4:
#         webname ='cwl'
#     for NewsKind in range(1,10):
#         for NewsType in range (0,6):
#             url = lot.GetNews(webname, NewsKind, NewsType)
#             if url <> '':
#                 newslist = lot.GetUrlList(webname, url, 1)
#                 for listurl in newslist:
#                     for item in listurl('a'):
#                         if webname == 'zhcw':
#                             mainurl = 'http://www.zhcw.com/%s' % item['href']
#                         elif webname == 'cwl':
#                             mainurl = 'http://www.cwl.gov.cn%s' % item['href']
#                         else:
#                             mainurl = item['href']
#                 print mainurl

#中彩网政策数据
# url= 'http://www.zhcw.com/zhengce/'
# res = urllib.urlopen(url)
# lot = Lotteryzhcw()
# soup = bs(res,'html.parser')
# soupdiv = soup('tbody')
# 
# for tdlist in soupdiv:
#     item = tdlist.findAll(attrs={'valign':'top'})
#     for list in item:
#         lista = list('a')
#         for i in lista:
#             mainurl = 'http://www.zhcw.com%s' % i['href'].replace('http://www.zhcw.com','')
#             IsExists = Checkurl(mainurl)
#             if IsExists == 0:
#                 try:
#                     lot.InsDate(mainurl, 10,0, DD)
#                     print 'succ--url:%s' % mainurl
#                 except:
#                     print 'fail--url:%s' % mainurl
#                 finally:
#                     pass

#####################################################################################################################################################
#####################################################################################################################################################
#####################################################################################################################################################
