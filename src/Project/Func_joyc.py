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



class LotteryJoyc():
    def __init__(self):
        pass


    def GetAllNews(self,newskind,newstype):
        type = newskind
        if type == 1: #新闻中心
            if newstype == 1:#福彩要闻
                url = 'http://www.joycail.com/html/fucaiyaowen/'
            elif newstype == 2:#公告公示
                url = 'http://www.joycail.com/html/gonggaogongshi/'
            elif newstype == 3:#福彩活动
                url = 'http://www.joycail.com/html/fucaihuodong/'
            else:
                url = ''
        elif type == 2:#福彩公益
            if newstype == 1:#公益新闻
                url = 'http://www.joycail.com/html/gongyixinwen/'
            elif newstype == 2:#公益活动
                url = 'http://www.joycail.com/html/gongyihuodong/'
            elif newstype == 3:#政策法规
                url = 'http://www.joycail.com/html/zhengcefagui/'
            elif newstype == 4:#公益掠影:
                url = 'http://www.joycail.com/html/gongyilueying/'
            else:
                url = ''
        elif type == 3:#彩站风采
            if newstype == 1:#福彩动态
                url = 'http://www.joycail.com/html/fucaidongtai/'
            elif newstype == 2:#江城名站
                url = 'http://www.joycail.com/html/jiangchengmingzhan/'
            elif newstype == 3:#站长之星
                url = 'http://www.joycail.com/html/zhanchangzhixing/'
            else:
                url = ''
        elif type == 4:#彩友之家
            if newstype == 1:#江城彩讯
                url = 'http://www.joycail.com/html/jiangchengcaixun/'
            elif newstype == 2:#双色球
                url = 'http://www.joycail.com/html/shuangseqiu/xinwen/'
            elif newstype == 3:#福彩3d
                url = 'http://www.joycail.com/html/fucai3D/xinwen/'
            elif newstype == 4:#七乐彩
                url = 'http://www.joycail.com/html/qilecai/xinwen/'
            elif newstype == 5:#30选5
                url = 'http://www.joycail.com/html/30xuan5/xinwen/'
            elif newstype == 6:#快3
                url = 'http://www.joycail.com/html/fucaikuaisan/xinwen/'
            elif newstype == 7:#刮刮乐
                url = 'http://www.joycail.com/html/guaguale/xinwen/'
            elif newstype == 8:#无纸化
                url = 'http://www.joycail.com/html/wuzhihua/'            
            else:
                url = ''
        else:
            url = ''
        return url
            
    def InsData(self,url,newskind,newstype,DateDif):
        res = Func.GetHeader(url)
        if res == '':
            print 'Time Out!'
        else:
            soup = bs(res,'html.parser')

            soupinfo = soup.find('div',attrs={'class','w700 fl'})
            
            souptitle = soupinfo.find('dt')
            title = souptitle.text.strip()
            
            infolist = soup.find('dd',attrs={'class':'dd_time'})('span')
            timestr = infolist[0].text.replace('发布时间：','')
            source = infolist[1].text.replace('来源：','')
            
            newstime = datetime.datetime.strptime(timestr,'%Y-%m-%d %H:%M')            
            
            soupcon = soup.find('dd',attrs={'class':'dd_content'})
            
            newstxt = ''
            for con in soupcon('p'):
                newstxt = newstxt + con.text.strip()          

            cmt = 0
            author = ''

            
            now = datetime.datetime.now() - datetime.timedelta(days = DateDif)
            currdate = newstime
            
            
            if (now.year == currdate.year and now.month == currdate.month and now.day == currdate.day) or DateDif == -1 :
                
                conn = MySQLdb.connect(host='.',port = 3306,user='root',passwd='123456',db ='news_info',charset = 'utf8')
                cur = conn.cursor()  
      
                #insert数据
                dictypename = {1:'新闻中心', 2:'福彩公益', 3:'彩站风采',4:'彩友之家'}
                if newskind == 1:
                    dicttype ={1:'福彩要闻',2:'公告公示',3:'福彩活动'}
                elif newskind == 2 :
                    dicttype ={1:'公益新闻',2:'公益活动',3:'政策法规',4:'公益掠影'}
                elif newskind == 3 :
                    dicttype ={1:'福彩动态',2:'江城名站',3:'站长之星'}
                elif newskind == 4 :
                    dicttype ={1:'江城彩讯',2:'双色球',3:'福彩3d',4:'七乐彩',5:'30选5',6:'快3',7:'刮刮乐',8:'无纸化'}
                sql = 'insert into tbl_news_info(title,newstype,source,pubtime,typename,webname,newsurl,contenttxt,joincount,author) select \'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',%d,\'%s\' from DUAL' % (title,dicttype[newstype],source,newstime,dictypename[newskind],'快乐福彩',url,newstxt,cmt,author)
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
