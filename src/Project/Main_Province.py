# -*- coding:utf-8 -*-
'''
Created on 2018��2��22��

@author: jason
'''

from bs4 import BeautifulSoup as bs
import urllib
import re
from Func import Checkurl
from Func import CheckurlProv
from Func import GetHeader
from Func import GetNewsList
from Func import GetXmlList
from Province_Func import Province
import requests
import sys
reload(sys)
sys.setdefaultencoding('utf8')




DD = -1
lmt = 10

class GetProvNews():
    def __init__(self):
        pass
    
    def GetNewProv(self,plist):
        p = Province()
        for prov in plist:
            for NewsKind in range(1,8):
                for NewsType in range(1,11):
                    url = p.GetALlNews(prov, NewsKind,NewsType)
                    if url:
                        if prov == 22:
                            userhead = {  
                                        'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'  
                                    }
                            try:
                                rep = requests.get(url,headers=userhead,timeout=5)
                                res = rep.content
                                soup = bs(res,'html.parser')
                            except:
                                soup = ''
                                print 'time out'
                        else:
                            try:
                                rep = requests.get(url,timeout=5)
                                res = rep.content
                                soup = bs(res,'html.parser')
                                souplx = bs(res,'lxml')
                            except:
                                soup = ''
                                souplx = ''
                                print 'time out'
                        print 'ProvinceCode:%s' % prov
                        
                        #黑龙江
                        if soup <> '':
                            if prov == 1:
                                souplist = soup.find(attrs={'class':'mapculture'})
                                for li in souplist('li'):
                                    for a in li.findAll('a'):
                                        title = a.text.strip()
                                        href = a['href']
                                        mainurl ='http://www.lottost.cn%s' % href.replace('http://www.lottost.cn','')
                                        IsExists = CheckurlProv(mainurl,title)
                                        if IsExists == 0 :
                                            try:
                                                p.InsData(prov,NewsKind,NewsType,mainurl,DD)
                                                print 'succ %d--%d' % (NewsKind,NewsType)
                                            except:
                                                print 'fail %d--%d--url:%s' % (NewsKind,NewsType,mainurl)
                                            finally:
                                                pass
                                        else:
                                            print 'Exists'
                                print 'finish--heilongjiang'
                            #内蒙古
                            elif prov == 2:         
                                souplist = soup.find(attrs={'class':'left3'})
                                for li in souplist('li'):
                                    for a in li('a'):
                                        title = a.text.strip()
                                        href = a['href']
                                        href = href.replace('http://www.nmlottery.com.cn','')
                                        mainurl = 'http://www.nmlottery.com.cn%s' % href.replace('../..','')         
                                        IsExists = CheckurlProv(mainurl,title)
                                        if IsExists == 0 :
                                            try:
                                                p.InsData(prov,NewsKind,NewsType,mainurl,DD)
                                                print 'succ %d--%d' % (NewsKind,NewsType)
                                            except:
                                                print 'fail %d--%d--url:%s' % (NewsKind,NewsType,mainurl)
                                            finally:
                                                pass
                                        else:
                                            print 'Exists'
                                print 'finish--neimenggu'
                            #陕西
                            elif prov == 3:  
                                for soupdiv in soup('ul'):
                                    for li in soupdiv('li'):
                                        for a in li('a'):
                                            title = a.text.strip()
                                            href = a['href']
                                            href = href.replace('http://www.szfc.gov.cn','')
                                            mainurl = 'http://www.sxfc.gov.cn%s' % href.replace('../..','')
                                            IsExists = CheckurlProv(mainurl,title)
                                            if IsExists == 0 :
                                                try:
                                                    p.InsData(prov,NewsKind,NewsType,mainurl,DD)
                                                    print 'succ %d--%d' % (NewsKind,NewsType)
                                                except:
                                                    print 'fail %d--%d--url:%s' % (NewsKind,NewsType,mainurl)
                                                finally:
                                                    pass
                                            else:
                                                print 'Exists'
                        
                                print 'finish--shanxi'
                            #杭州
                            elif prov == 4:  
                                soupdiv = soup.find(attrs={'class':'Nlistul'})
                                for li in soupdiv.findAll(attrs={'class':'Nlink'}):
                                    for a in li('a'):
                                        title = a.text.strip()
                                        href = a['href']
                                        href = href.replace('http://www.hzfucai.net','')
                                        mainurl = 'http://www.hzfucai.net%s' % href.replace('../..','')
                                        IsExists = CheckurlProv(mainurl,title)
                                        if IsExists == 0 :
                                            try:
                                                p.InsData(prov,NewsKind,NewsType,mainurl,DD)
                                                print 'succ %d--%d' % (NewsKind,NewsType)
                                            except:
                                                print 'fail %d--%d--url:%s' % (NewsKind,NewsType,mainurl)
                                            finally:
                                                pass
                                        else:
                                            print 'Exists'
                                print 'finish--hangzhou'
                            #天津
                            elif prov == 5:  
                                soupdiv = soup.find(attrs={'class':'news_loca_list_title'})
                                for li in soupdiv.findAll('li'):
                                    for a in li('a'):
                                        title = a.text.strip()
                                        href = a['href']
                                        href = href.replace('http://www.tjflcpw.com/news/','')
                                        mainurl = 'http://www.tjflcpw.com/news/%s' % href
                                        IsExists = CheckurlProv(mainurl,title)
                                        if IsExists == 0 :
                                            try:
                                                p.InsData(prov,NewsKind,NewsType,mainurl,DD)
                                                print 'succ %d--%d' % (NewsKind,NewsType)
                                            except:
                                                print 'fail %d--%d--url:%s' % (NewsKind,NewsType,mainurl)
                                            finally:
                                                pass
                                        else:
                                            print 'Exists'
                                print 'finish--tianjin'
                            #北京
                            elif prov == 6:   
                                soupdiv = soup.find(attrs={'class':'news_col'})
                                for li in soupdiv.findAll('li'):
                                    for a in li('a'):
                                        for s in li('span'):
                                            newstime = s.text
                                            title = a.text.strip()
                                            href = a['href']
                                            href = href.replace('http://www.bwlc.net','')
                                            mainurl = 'http://www.bwlc.net%s' % href
                                            IsExists = CheckurlProv(mainurl,title)
                                            if IsExists == 0 :
                                                try:
                                                    #北京特殊处理。出入时间间隔为新闻发布时间
                                                    p.InsData(prov,NewsKind,NewsType,mainurl,newstime)
                                                    print 'succ %d--%d' % (NewsKind,NewsType)
                                                except:
                                                    print 'fail %d--%d--url:%s' % (NewsKind,NewsType,mainurl)
                                                finally:
                                                    pass
                                            else:
                                                print 'Exists'
                                print 'finish--beijing'
                            #河北
                            elif prov == 7:   
                                soupdiv = soup.find(attrs={'class':'leftPage'})
                                for ul in soupdiv.findAll('ul',attrs={'class':'newslist'}):
                                    for li in ul('li'):
                                        for a in li('a'):
                                            title = a.text.strip()
                                            href = a['href']
                                            href = href.replace('http://www.yzfcw.com','')
                                            mainurl = 'http://www.yzfcw.com%s' % href
                                            IsExists = CheckurlProv(mainurl,title)
                                            if IsExists == 0 :
                                                try:
                                                    p.InsData(prov,NewsKind,NewsType,mainurl,DD)
                                                    print 'succ %d--%d' % (NewsKind,NewsType)
                                                except:
                                                    print 'fail %d--%d--url:%s' % (NewsKind,NewsType,mainurl)
                                                finally:
                                                    pass
                                            else:
                                                print 'Exists'
                                print 'finish--hebei'
                            #辽宁
                            elif prov == 8 :   
                                soupdiv = soup.find(attrs={'class':'news_list_10'})
                                for li in soupdiv.findAll('li'):
                                    for con in li('div',attrs={'class':'txt'}):
                                        for a in con('a'):
                                            title = a.text.strip()
                                            href = a['href']
                                            href = href.replace('http://www.lnlotto.com/View/','')
                                            mainurl = 'http://www.lnlotto.com/View/%s' % href
                                            IsExists = CheckurlProv(mainurl,title)
                                            if IsExists == 0 :
                                                try:
                                                    p.InsData(prov,NewsKind,NewsType,mainurl,DD)
                                                    print 'succ %d--%d' % (NewsKind,NewsType)
                                                except:
                                                    print 'fail %d--%d--url:%s' % (NewsKind,NewsType,mainurl)
                                                finally:
                                                    pass
                                            else:
                                                print 'Exists'
                                print 'finish--liaoning'
                            #吉林
                            elif prov == 9: 
                                soupdiv = soup.find(attrs={'class':'news_list_10'})
                                for li in soupdiv.findAll('li'):
                                    for con in li('div',attrs={'class':'txt'}):
                                        for a in con('a'):
                                            title = a.text.strip()
                                            href = a['href']
                                            href = href.replace('http://www.jlfc.com.cn/View/','')
                                            mainurl = 'http://www.jlfc.com.cn/View/%s' % href
                                            IsExists = CheckurlProv(mainurl,title)
                                            if IsExists == 0 :
                                                try:
                                                    p.InsData(prov,NewsKind,NewsType,mainurl,DD)
                                                    print 'succ %d--%d' % (NewsKind,NewsType)
                                                except:
                                                    print 'fail %d--%d--url:%s' % (NewsKind,NewsType,mainurl)
                                                finally:
                                                    pass
                                            else:
                                                print 'Exists'
                                print 'finish--jilin'
                            
                            #江苏
                            elif prov == 10:
                                NewsList = GetNewsList(NewsKind)
                                for i in range(0,20):
                                    id = NewsList[i]
                                    title = NewsList[20+i]
                                    mainurl = 'http://www.jslottery.com/News/NewsDetails?ID=%s' % id
                                    IsExists = CheckurlProv(mainurl,title)
                                    if IsExists == 0 :
                                        try:
                                            p.InsData(prov,NewsKind,NewsType,mainurl,DD)
                                            print 'succ %d--%d' % (NewsKind,NewsType)
                                        except:
                                            print 'fail %d--%d--url:%s' % (NewsKind,NewsType,mainurl)
                                        finally:
                                            pass
                                    else:
                                        print 'Exists'
                                print 'finish--jiangsu'
                            #浙江
                            elif prov == 11:
                                soupdiv = soup.find('ul',attrs={'class':'zlistUl'})
                                for li in soupdiv.findAll('li'):
                                    for a in li('a'):
                                        title = a.text.strip()
                                        href = a['href']
                                        href = href.replace('http://www.zjflcp.com','')
                                        mainurl = 'http://www.zjflcp.com%s' % href
                                        IsExists = CheckurlProv(mainurl,title)
                                        if IsExists == 0 :
                                            try:
                                                p.InsData(prov,NewsKind,NewsType,mainurl,DD)
                                                print 'succ %d--%d' % (NewsKind,NewsType)
                                            except:
                                                print 'fail %d--%d--url:%s' % (NewsKind,NewsType,mainurl)
                                            finally:
                                                pass
                                        else:
                                            print 'Exists'
                                print 'finish--zhejiang'
                            
                            #安徽
                            elif prov == 12:
                                soupdiv = soup.findAll('td',attrs={'class':'list2'})
                                for td in soupdiv:
                                    for a in td('a'):
                                        title = a.text.strip()
                                        href = a['href']
                                        href = href.replace('http://www.ahfc.gov.cn','')
                                        mainurl = 'http://www.ahfc.gov.cn%s' % href
                                        IsExists = CheckurlProv(mainurl,title)
                                        if IsExists == 0 :
                                            try:
                                                p.InsData(prov,NewsKind,NewsType,mainurl,DD)
                                                print 'succ %d--%d' % (NewsKind,NewsType)
                                            except:
                                                print 'fail %d--%d--url:%s' % (NewsKind,NewsType,mainurl)
                                            finally:
                                                pass
                                        else:
                                            print 'Exists'
                                print 'finish--anhui'
                            #福建
                            elif prov == 13:
                                soupdiv = soup.find('table',attrs={'width':'95%','align':'center'})
                                if soupdiv:
                                    for td in soupdiv('div',attrs={'align':'left'}):
                                        for a in td('a'):
                                            title = a.text.strip()
                                            href = a['href']
                                            href = href.replace('http://www.fjcp.cn/','')
                                            mainurl = 'http://www.fjcp.cn/%s' % href
                                            IsExists = CheckurlProv(mainurl,title)
                                            if IsExists == 0 :
                                                try:
                                                    p.InsData(prov,NewsKind,NewsType,mainurl,DD)
                                                    print 'succ %d--%d' % (NewsKind,NewsType)
                                                except:
                                                    print 'fail %d--%d--url:%s' % (NewsKind,NewsType,mainurl)
                                                finally:
                                                    pass
                                            else:
                                                print 'Exists'
                                print 'finish--fujian'
                            #河南
                            elif prov == 15:
                                soupdiv = soup.find('table',attrs={'class':'tableBorder'})
                                for tr in soupdiv('tr'):
                                    for td in tr('td'):
                                        for a in td('a'):
                                            title = a.text.strip()
                                            href = a['href']
                                            href = href.replace('http://www.henanfucai.com','')
                                            mainurl = 'http://www.henanfucai.com%s' % href
                                            IsExists = CheckurlProv(mainurl,title)
                                            if IsExists == 0 :
                                                try:
                                                    p.InsData(prov,NewsKind,NewsType,mainurl,DD)
                                                    print 'succ %d--%d' % (NewsKind,NewsType)
                                                except:
                                                    print 'fail %d--%d--url:%s' % (NewsKind,NewsType,mainurl)
                                                finally:
                                                    pass
                                            else:
                                                print 'Exists'
                                print 'finish--henan'
                            #深圳
                            elif prov == 16:
                                soupdiv = soup.find('ul',attrs={'class':'news-list'})
                                if soupdiv is not None:
                                    for li in soupdiv('li'):
                                        for a in li('a'):
                                            title = a.text.strip()
                                            href = a['href']
                                            href = href.replace('./','')
                                            mainurl = '%s%s' % (url,href)
                                            IsExists = CheckurlProv(mainurl,title)
                                            if IsExists == 0 :
                                                try:
                                                    p.InsData(prov,NewsKind,NewsType,mainurl,DD)
                                                    print 'succ %d--%d' % (NewsKind,NewsType)
                                                except:
                                                    print 'fail %d--%d--url:%s' % (NewsKind,NewsType,mainurl)
                                                finally:
                                                    pass
                                            else:
                                                print 'Exists'
                                else:
                                    soupdiv = soup.find('ul',attrs={'class':'news2-list'})
                                    for li in soupdiv('li'):
                                        for a in li('a'):
                                            href = a['href']
                                            href = href.replace('./','')
                                            mainurl = '%s%s' % (url,href)
                                            titlediv = a.find('h3',attrs={'class':'news2-title'})
                                            title = titlediv.text.strip()
                                            IsExists = CheckurlProv(mainurl,title)
                                            if IsExists == 0 :
                                                try:
                                                    p.InsData(prov,NewsKind,NewsType,mainurl,DD)
                                                    print 'succ %d--%d' % (NewsKind,NewsType)
                                                except:
                                                    print 'fail %d--%d--url:%s' % (NewsKind,NewsType,mainurl)
                                                finally:
                                                    pass
                                            else:
                                                print 'Exists'
                                print 'finish--shenzhen'
                            #广东
                            elif prov == 17:   
                                soupdiv = soup.find('div',attrs={'class':'contentBox_R_02'})
                                for tr in soupdiv('ul'):
                                    for td in tr('li'):
                                        for a in td('a'):
                                            title = a.text.strip()
                                            href = a['href']
                                            href = href.replace('http://www.gdfc.org.cn','')
                                            mainurl = 'http://www.gdfc.org.cn%s' % href
                                            IsExists = CheckurlProv(mainurl,title)
                                            if IsExists == 0 :
                                                try:
                                                    p.InsData(prov,NewsKind,NewsType,mainurl,DD)
                                                    print 'succ %d--%d' % (NewsKind,NewsType)
                                                except:
                                                    print 'fail %d--%d--url:%s' % (NewsKind,NewsType,mainurl)
                                                finally:
                                                    pass
                                            else:
                                                print 'Exists'
                                print 'finish--guangdong'
                            #广西
                            elif prov == 18:   
                                lid = re.findall(r'\d{3}$',url)[0]
                                list = GetXmlList(lid)
                                length=len(list)
                                for i in range(0,length/2):
                                    newsid = list[i]
                                    title = list[i+length/2]
                                    mainurl = 'http://www.gxcaipiao.com.cn/news.d.html?_id=%s' % newsid
                                    IsExists = CheckurlProv(mainurl,title)
                                    if IsExists == 0 :
                                        try:
                                            p.InsData(prov,NewsKind,NewsType,mainurl,DD)
                                            print 'succ %d--%d' % (NewsKind,NewsType)
                                        except:
                                            print 'fail %d--%d--url:%s' % (NewsKind,NewsType,mainurl)
                                        finally:
                                            pass
                                    else:
                                        print 'Exists'
                                print 'finish--guangxi'
                            
                             #海南
                            elif prov == 19:   
                                soupdiv = soup.find('ul',attrs={'class':'u_list2 f14px'})
                                for li in soupdiv('li'):
                                    for a in li('a'):
                                        title = a.text.strip()
                                        href = a['href']
                                        href = href.replace('http://www.hainancp.com','')
                                        mainurl = 'http://www.hainancp.com%s' % href
                                        IsExists = CheckurlProv(mainurl,title)
                                        if IsExists == 0 :
                                            try:
                                                p.InsData(prov,NewsKind,NewsType,mainurl,DD)
                                                print 'succ %d--%d' % (NewsKind,NewsType)
                                            except:
                                                print 'fail %d--%d--url:%s' % (NewsKind,NewsType,mainurl)
                                            finally:
                                                pass
                                        else:
                                            print 'Exists'
                                print 'finish--hainan'
                            
                            
                            
                             #四川
                            elif prov == 21:   
                                soupdiv = soup.find('div',attrs={'class':'newsPage_left'})
                                for li in soupdiv('li'):
                                    for a in li('a'):
                                        title = a.text.strip()
                                        id = a['id']
                                        if NewsKind == 4:
                                            itemurl  ='http://www.scflcp.com/policiesAndLaws/newsContent?classficationId=72'
                                        else:
                                            itemurl = url
                                            itemurl = itemurl.replace('List','Content')
                                        href = '%s&&newsId=%s' % (itemurl,id) 
                                        mainurl = href
                                        IsExists = CheckurlProv(mainurl,title)
                                        if IsExists == 0 :
                                            try:
                                                p.InsData(prov,NewsKind,NewsType,mainurl,DD)
                                                print 'succ %d--%d' % (NewsKind,NewsType)
                                            except:
                                                print 'fail %d--%d--url:%s' % (NewsKind,NewsType,mainurl)
                                            finally:
                                                pass
                                        else:
                                            print 'Exists'
                                print 'finish--sichuan'
                                
                            #云南
                            elif prov == 22:   
                                soupdiv = soup.findAll('td',attrs={'class':'newslist_title_table'})
                                for td in soupdiv:
                                    for a in td('a'):
                                        title = a['title']
                                        href = a['href']
                                        href = href.replace('http://www.ynflcp.cn','')
                                        href = href.replace('..','http://www.ynflcp.cn')
                                        mainurl = href
                                        IsExists = CheckurlProv(mainurl,title)
                                        if IsExists == 0 :
                                            try:
                                                p.InsData(prov,NewsKind,NewsType,mainurl,DD)
                                                print 'succ %d--%d' % (NewsKind,NewsType)
                                            except:
                                                print 'fail %d--%d--url:%s' % (NewsKind,NewsType,mainurl)
                                            finally:
                                                pass
                                        else:
                                            print 'Exists'
                                print 'finish--yunnan'
                            
                            #甘肃
                            elif prov == 23:   
                                soupdiv = soup.find('ul',attrs={'class':'newsList'})
                                for td in soupdiv('li'):
                                    for a in td('a'):
                                        title=a.find('p',attrs={'class':'fl'}).text
                                        href = a['href']
                                        href = href.replace('http://www.gsflcp.com','')
                                        mainurl = 'http://www.gsflcp.com%s' % href
                                        IsExists = CheckurlProv(mainurl,title)
                                        if IsExists == 0 :
                                            try:
                                                p.InsData(prov,NewsKind,NewsType,mainurl,DD)
                                                print 'succ %d--%d' % (NewsKind,NewsType)
                                            except:
                                                print 'fail %d--%d--url:%s' % (NewsKind,NewsType,mainurl)
                                            finally:
                                                pass
                                        else:
                                            print 'Exists'
                                print 'finish--gansu'
                                
                                
                            #青海
                            elif prov == 24:   
                                soupdiv = soup.find('div',attrs={'class':'lb lf'})
                                td = soupdiv.findAll('div',attrs={'class':'wzlb1'})
                                for li in td: 
                                    for a in li('a'):
                                        title= a.text
                                        href = a['href']
                                        mainurl = href
                                        IsExists = CheckurlProv(mainurl,title)
                                        if IsExists == 0 :
                                            try:
                                                p.InsData(prov,NewsKind,NewsType,mainurl,DD)
                                                print 'succ %d--%d' % (NewsKind,NewsType)
                                            except:
                                                print 'fail %d--%d--url:%s' % (NewsKind,NewsType,mainurl)
                                            finally:
                                                pass
                                        else:
                                            print 'Exists'
                                print 'finish--qinghai'
                            #宁夏
                            elif prov == 25:   
                                soupdiv = soup.find('div',attrs={'class':'news_a1'})
                                td = soupdiv.findAll('li')
                                for li in td: 
                                    for a in li('a'):
                                        title= a.text
                                        href = a['href']
                                        href = href.replace('http://www.nxflcp.com','')
                                        mainurl = 'http://www.nxflcp.com%s' % href
                                        IsExists = CheckurlProv(mainurl,title)
                                        if IsExists == 0 :
                                            try:
                                                p.InsData(prov,NewsKind,NewsType,mainurl,DD)
                                                print 'succ %d--%d' % (NewsKind,NewsType)
                                            except:
                                                print 'fail %d--%d--url:%s' % (NewsKind,NewsType,mainurl)
                                            finally:
                                                pass
                                        else:
                                            print 'Exists'
                                print 'finish--ningxia'                           
                            
                            #湖北
                            elif prov == 26:   
                                #当日头条
                                urllist = []
                                titlist = []
                                NewsDic = {1:'csyw',2:'tzgg',3:'djxb'}
                                if NewsKind == 1:
                                    soupdiv = soup.find('div',attrs={'class':'fc_hot_news w396'})
                                    soupdt = soupdiv.find('dt')
                                    for a in soupdt('a'):
                                        title = a.text
                                        mainurl = a['href']
                                        mainurl = mainurl.replace('./','http://www.hbfcw.gov.cn/%s/' % NewsDic[NewsKind])
                                        titlist.append(title)
                                        urllist.append(mainurl)
                                    #imagebox
                                    soupdiv = soup.findAll('div',attrs={'class':'csyw_img_box'})
                                    listdet=[]
                                    for lista in soupdiv:
                                        for a in lista('a'):
                                            listdet.append(a)
                                    for wi in (listdet[1],listdet[5]):
                                        titlist.append(wi['title'])
                                        urldet = wi['href']
                                        urldet = urldet.replace('../','http://www.hbfcw.gov.cn/')
                                        urldet = urldet.replace('./','http://www.hbfcw.gov.cn/%s/' % NewsDic[NewsKind])
                                        urllist.append(urldet)
                                    #list
                                    soupdiv = soup.findAll('ul',attrs={'class':'list_erect djxb_list_ul'})
                                    for div1 in soupdiv:
                                        for li in div1.findAll('li'):
                                            for a in li('a',attrs={'class':'title'}):
                                                titlist.append(a['title'])
                                                urldet = a['href']
                                                urldet = urldet.replace('../','http://www.hbfcw.gov.cn/')
                                                urldet = urldet.replace('./','http://www.hbfcw.gov.cn/%s/' % NewsDic[NewsKind])
                                                urllist.append(urldet)
                                    print len(titlist)
                                    for i in range(0,len(titlist)):                           
                                        IsExists = CheckurlProv(urllist[i],titlist[i])
                                        if IsExists == 0 :
                                            try:
                                                mainurl = urllist[i]
                                                title = titlist[i]
                                                p.InsData(prov,NewsKind,NewsType,mainurl,DD)
                                                print 'succ %d--%d' % (NewsKind,NewsType)
                                            except:
                                                print 'fail %d--%d--url:%s' % (NewsKind,NewsType,mainurl)
                                            finally:
                                                pass
                                        else:
                                            print 'Exists'
                              
                                else:
                                    soupdiv = soup.findAll('ul',attrs={'class':'list_erect djxb_list_ul'})
                                    for ul in soupdiv:
                                        for li in ul('li'):
                                            for a in li('a'):
                                                title = a['title']
                                                urldet = a['href']
                                                urldet = urldet.replace('../','http://www.hbfcw.gov.cn/')
                                                urldet = urldet.replace('./','http://www.hbfcw.gov.cn/%s/' % NewsDic[NewsKind])
                                                mainurl = urldet
                                                IsExists = CheckurlProv(mainurl,title)
                                                if IsExists == 0 :
                                                    try:
                                                        p.InsData(prov,NewsKind,NewsType,mainurl,DD)
                                                        print 'succ %d--%d' % (NewsKind,NewsType)
                                                    except:
                                                        print 'fail %d--%d--url:%s' % (NewsKind,NewsType,mainurl)
                                                    finally:
                                                        pass
                                                else:
                                                    print 'Exists'
                                print 'finish--hubei'     
                                
                            #湖南
                            elif prov == 27:   
                                soupdiv = soup.findAll('a',attrs={'class':'d1','target':'_blank'})
                                for a in soupdiv:
                                    title= a.text
                                    href = a['href']
                                    href = href.replace('http://www.hnflcp.gov.cn','')
                                    mainurl = 'http://www.hnflcp.gov.cn%s' % href
                                    IsExists = CheckurlProv(mainurl,title)
                                    if IsExists == 0 :
                                        try:
                                            p.InsData(prov,NewsKind,NewsType,mainurl,DD)
                                            print 'succ %d--%d' % (NewsKind,NewsType)
                                        except:
                                            print 'fail %d--%d--url:%s' % (NewsKind,NewsType,mainurl)
                                        finally:
                                            pass
                                    else:
                                        print 'Exists'
                                print 'finish--hunan'        
                            #新疆
                            elif prov == 28:   
                                soupdiv = soup.findAll('div',attrs={'class':'honour_list'})
                                for ul in soupdiv:
                                    for li in ul('li'):
                                        for a in li('a'):
                                            title= a.text
                                            href = a['href']
                                            href = href.replace('http://www.xjflcp.com','')
                                            mainurl = 'http://www.xjflcp.com%s' % href
                                            IsExists = CheckurlProv(mainurl,title)
                                            if IsExists == 0 :
                                                try:
                                                    p.InsData(prov,NewsKind,NewsType,mainurl,DD)
                                                    print 'succ %d--%d' % (NewsKind,NewsType)
                                                except:
                                                    print 'fail %d--%d--url:%s' % (NewsKind,NewsType,mainurl)
                                                finally:
                                                    pass
                                            else:
                                                print 'Exists'
                                print 'finish--xinjiang'       
                            #贵州
                            elif prov == 29:   
                                soupdiv = soup.find('ul',attrs={'class':'ul_newslist2'})
                                for li in soupdiv('li'):
                                    for a in li('a'):
                                        title= a['title']
                                        href = a['href']
                                        href = href.replace('http://www.gzfucai.cn/news/','')
                                        mainurl = 'http://www.gzfucai.cn/news/%s' % href
                                        IsExists = CheckurlProv(mainurl,title)
                                        if IsExists == 0 :
                                            try:
                                                p.InsData(prov,NewsKind,NewsType,mainurl,DD)
                                                print 'succ %d--%d' % (NewsKind,NewsType)
                                            except:
                                                print 'fail %d--%d--url:%s' % (NewsKind,NewsType,mainurl)
                                            finally:
                                                pass
                                        else:
                                            print 'Exists'
                                print 'finish--guizhou'                                     