# -*- coding:utf-8 -*-

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
import urllib2
import traceback
import requests


class Province():
    def __init__(self):
        pass
    
    def GetALlNews(self,province,newskind,newstype):
        #省编号对应省名称
        DicProvince={1:'黑龙江',2:'内蒙古',3:'陕西',4:'杭州',5:'天津',6:'北京',7:'河北',8:'辽宁',9:'吉林',10:'江苏',11:'浙江',12:'安徽',13:'福建',14:'江西',15:'河南',16:'深圳',17:'广东',18:'广西',19:'海南',20:'重庆',21:'四川',22:'云南',23:'甘肃',24:'青海',25:'宁夏',26:'湖北',27:'湖南',28:'新疆',29:'贵州'}
        prov = DicProvince[province]
        url = ''
        
        if prov == '黑龙江':
            #彩种新闻
            if newskind == 1 :
                if newstype == 1:
                    url = 'http://www.lottost.cn/html/xinwen/caizhongdongtaixinwen/'
                else :
                    url = ''
            #彩民之家
            elif newskind == 2 :
                if newstype == 1:
                    url = 'http://www.lottost.cn/html/xinwen/caiminzhijia/'
                else :
                    url = ''
            #龙江公益
            elif newskind == 3:
                #1：公益动态
                if newstype == 1:
                    url = 'http://www.lottost.cn/html/fucaigongyi/gongyidongtai/index.html'
                #2：龙江公益
                elif newstype == 2:
                    url = 'http://www.lottost.cn/html/fucaigongyi/longjianggongyi/index.html'
                #3：公益行动
                elif newstype == 3:
                    url = 'http://www.lottost.cn/html/fucaigongyi/gongyixingdong/index.html'
                #4：公益项目
                elif newstype == 4:
                    url = 'http://www.lottost.cn/html/fucaigongyi/gongyixiangmu/index.html'
                #5：公益黄页
                elif newstype == 5:
                    url = 'http://www.lottost.cn/html/fucaigongyi/gongyihuangye/index.html'
                #6：营销管理
                elif newstype == 6:
                    url = 'http://www.lottost.cn/html/fucaigongyi/yingxiaoguanli/index.html'
                else:
                    url = ''
            else :
                url = ''
        elif prov == '内蒙古':
            #新闻
            if newskind == 1:
                #1：玩法新闻
                if newstype == 1:
                    url = 'http://www.nmlottery.com.cn/ssq/ssqxw/index.shtml'
                #2：区外新闻
                elif newstype == 2:
                    url = 'http://www.nmlottery.com.cn/xw/gwxw/index.shtml'
                #3：站主之家
                elif newstype == 3:
                    url = 'http://www.nmlottery.com.cn/zzzj/yxjy/index.shtml'
                #4：区内新闻
                elif newstype == 4:
                    url = 'http://www.nmlottery.com.cn/xw/gnxw/index.shtml'
                #5：彩民之家
                elif newstype == 5:
                    url = 'http://www.nmlottery.com.cn/sx/cmzj/index.shtml'
                else:
                    url =''
            #公益金
            elif newskind == 2:
                #公益金
                if newstype == 1:
                    url = 'http://www.nmlottery.com.cn/gy/gyhd/index.shtml'
                #公益项目
                elif newstype == 2:
                    url = 'http://www.nmlottery.com.cn/gy/gyxm/index.shtml'
                #我区公益新闻
                elif newstype == 3:
                    url = 'http://www.nmlottery.com.cn/gy/nmgyxw/index.shtml'
                #全国公益新闻
                elif newstype == 4:
                    url = 'http://www.nmlottery.com.cn/gy/qggyxw/index.shtml'
                else:
                    url =''
            else:
                url = ''
        
        elif prov == '陕西':
            #新闻
            if newskind == 1:
                #玩法新闻
                if newstype == 1:
                    url = 'http://www.sxfc.gov.cn/xw/wfxw/index.shtml'
                #2：公益新闻
                elif newstype == 2:    
                    url ='http://www.sxfc.gov.cn/xw/gyxw/index.shtml'
                #3：全球彩风
                elif newstype == 3:
                    url = 'http://www.sxfc.gov.cn/xw/qqfc/index.shtml'
                #4：福彩文化
                elif newstype == 4:
                    url ='http://www.sxfc.gov.cn/xw/fcwh/index.shtml'
                #5：大奖统计
                elif newstype == 5:
                    url ='http://www.sxfc.gov.cn/xw/djtj/index.shtml'
                else:
                    url =''
            #福彩公益
            elif newskind == 2:
                #1：省公益新闻
                if newstype == 1:
                    url ='http://www.sxfc.gov.cn/gybd/sgyxw/index.shtml'
                #2：全国公益新闻
                elif newstype == 2:
                    url ='http://www.sxfc.gov.cn/gybd/qggyxw/index.shtml'    
                else:
                    url =''
            else:
                url = ''
        elif prov == '杭州' :
            if newskind == 1:
                #1：杭州公益
                if newstype == 1:
                    url = 'http://www.hzfucai.net/fcgy/hzgy/index.shtml'
                #2：公益行动
                elif newstype == 2:
                    url = 'http://www.hzfucai.net/fcgy/gyhd/index.shtml'
                #3：公益项目
                elif newstype == 3:
                    url = 'http://www.hzfucai.net/fcgy/gyxm/index.shtml'
                else:
                    url = ''
            else:
                url = ''
        
        elif prov == '天津' :
            if newskind == 1:
                #1：网站公告
                if newstype == 1 :
                    url = 'http://www.tjflcpw.com/news/NewsListLower.aspx?typeid=12'
                #2：彩市快讯
                elif newstype == 2 :
                    url = 'http://www.tjflcpw.com/news/NewsListLower.aspx?typeid=9'
                #3：爱心公益
                elif newstype == 3 :
                    url = 'http://www.tjflcpw.com/news/NewsListLower.aspx?typeid=6'
                #4：福彩新闻    
                elif newstype == 4 :
                    url = 'http://www.tjflcpw.com/news/NewsListLower.aspx?typeid=1'
                #5：彩票文化
                elif newstype == 5 :
                    url = 'http://www.tjflcpw.com/news/NewsListLower.aspx?typeid=4'
                else:
                    url = ''
            else:
                url = ''
        elif prov == '北京' :
            if newskind == 1:
                #1：福彩公告
                if newstype == 1:
                    url = 'http://www.bwlc.net/info/index.html'
                #2：福彩新闻
                elif newstype == 2:
                    url = 'http://www.bwlc.net/info/news.html'
                #3：中奖报道
                elif newstype == 3:
                    url = 'http://www.bwlc.net/info/cover.html'
                #4：公益金使用
                elif newstype == 4:
                    url = 'http://www.bwlc.net/info/award.html'
                else :
                    url = ''
            else :
                url = ''
                
        elif prov == '河北' :
            if newskind == 1 :
                #1：通知公告
                if newstype == 1:
                    url = 'http://www.yzfcw.com/lotteryNews/newsList?classficationId=2'
                #2：燕赵新闻
                elif newstype == 2:
                    url = 'http://www.yzfcw.com/lotteryNews/newsList?classficationId=3'
                #3：全国新闻
                elif newstype == 3:
                    url = 'http://www.yzfcw.com/lotteryNews/newsList?classficationId=15'
                #彩民故事
                elif newstype == 4:
                    url = 'http://www.yzfcw.com/lotteryNews/newsList?classficationId=17'
                #中奖播报
                elif newstype == 5:
                    url = 'http://www.yzfcw.com/lotteryNews/newsList?classficationId=18'
                else:
                    url = ''
            
            elif newskind == 2:
                #公益之窗
                if newstype == 1:
                    url = 'http://www.yzfcw.com/commonweal/newsList?classficationId=28'
                else:
                    url = ''
            else:
                url = ''

        
        elif prov == '辽宁':
            if newskind == 1:
                #1：网站公告
                if newstype == 1:
                    url = 'http://www.lnlotto.com/View/NewsList.aspx?TypeId=2&FocousType=0'
                #2：即开票资讯
                elif newstype == 2:
                    url = 'http://www.lnlotto.com/View/NewsList.aspx?TypeId=12&FocousType=0'
                #3：电投资讯
                elif newstype == 3:
                    url = 'http://www.lnlotto.com/View/NewsList.aspx?TypeId=13&FocousType=0'
                #4：中福在线
                elif newstype == 4:
                    url = 'http://www.lnlotto.com/View/NewsList.aspx?TypeId=14&CityID=0'
                #5：地方资讯
                elif newstype == 5:
                    url = 'http://www.lnlotto.com/View/NewsList.aspx?TypeId=47&CityID=1'
                #6：中奖故事
                elif newstype == 6:
                    url = 'http://www.lnlotto.com/View/NewsList.aspx?TypeId=43&FocousType=0'
                #7：福彩文化
                elif newstype == 7:
                    url = 'http://www.lnlotto.com/View/NewsList.aspx?TypeId=42&FocousType=0'
                else:
                    url = ''
            else :
                url = ''
        
        
        
        elif prov == '吉林':
            if newskind == 1:
                #1：地市资讯
                if newstype == 1:
                    url = 'http://www.jlfc.com.cn/View/NewsList.aspx?TypeId=47'
                #2：最新公告
                elif newstype == 2:
                    url = 'http://www.jlfc.com.cn/View/NewsList.aspx?TypeId=2&CityID=0'
                #3：中奖故事
                elif newstype == 3:
                    url = 'http://www.jlfc.com.cn/View/NewsList.aspx?TypeId=54&CityID=0'
                #4：明星站点
                elif newstype == 4:
                    url = 'http://www.jlfc.com.cn/View/NewsList.aspx?TypeId=49&CityID=0'
                #5：即开票资讯
                elif newstype == 5:
                    url = 'http://www.jlfc.com.cn/View/NewsList.aspx?TypeId=12&CityID=0'
                else:
                    url = ''
            elif newskind == 2:
                #1：公益动态
                if newstype == 1:
                    url = 'http://www.jlfc.com.cn/View/NewsList.aspx?TypeId=21&CityID=0'
                else:
                    url = ''
            else:
                url = ''
                
        
        elif prov == '江苏':
            if newskind == 1:
                #1：彩市新闻
                if newstype == 1:
                    url = 'http://www.jslottery.com/News?NewsType=1'        
                else :
                    url = ''
            elif newskind == 2:
                #公益活动
                if newstype == 1:
                    url = 'http://www.jslottery.com/News?NewsType=3'
                else:
                    url = ''
            else:
                url = ''
                
        
        elif prov == '浙江':
            if newskind == 1:
                #1：浙江福彩
                if newstype == 1:
                    url = 'http://www.zjflcp.com/05fc/gyfc/gydt/index.shtml'        
                else :
                    url = ''
            elif newskind == 2:
                #公益福彩
                if newstype == 1:
                    url = 'http://www.zjflcp.com/05fc/gyfc/gydt/index.shtml'
                else:
                    url = ''
            else:
                url = ''
        
        
        elif prov == '安徽':
            if newskind == 1:
                #1：全国新闻
                if newstype == 1:
                    url = 'http://www.ahfc.gov.cn/news/guo.shtml'        
                #2：省内新闻
                elif newstype == 2:
                    url = 'http://www.ahfc.gov.cn/news/sheng.shtml'
                else:
                    url = ''
            elif newskind == 2:
                #1：公益金
                if newstype == 1:
                    url = 'http://www.ahfc.gov.cn/news/gyj.shtml'
                #2：圆梦大学
                elif newstype == 2:
                    url = 'http://www.ahfc.gov.cn/ppgy/fcymdx.shtml'
                #3:图书进校园
                elif newstype == 3:
                    url = 'http://www.ahfc.gov.cn/ppgy/axtsxy.shtml'
                else :
                    url = ''
            elif newskind == 3:
                if newstype == 1:
                #1:决策公开
                    url = 'http://www.ahfc.gov.cn/zwgk/jcgk.shtml'
                #2:部门预决算
                elif newstype == 2:
                    url='http://www.ahfc.gov.cn/zwgk/czyjs.shtml'
                #3:招标采购
                elif newstype == 3:
                    url = 'http://www.ahfc.gov.cn/zwgk/zbcg.shtml'
                #4：廉政信息
                elif newstype == 4:
                    url = 'http://www.ahfc.gov.cn/zwgk/lzxx.shtml'
                else:
                    url = ''
            else:
                url = ''
        
        elif prov == '福建':
            if newskind == 1:
                if newstype == 1:
                    url = 'http://www.fjcp.cn/newsList.aspx?typeID=1'
                else :
                    url = ''
            else :
                url = ''
    
        
        elif prov == '河南':
            if newskind == 1:
                #1：全国新闻
                if newstype == 1:
                    url = 'http://www.henanfucai.com/List.html?id=41'        
                #2：省内新闻
                elif newstype == 2:
                    url = 'http://www.henanfucai.com/List.html?id=40'
                else:
                    url = ''
            elif newskind == 2:
                #1：公益新闻
                if newstype == 1:
                    url = 'http://www.henanfucai.com/List.html?id=55'
                #2：公益行动
                elif newstype == 2:
                    url = 'http://www.henanfucai.com/List.html?id=56'
                else :
                    url = ''
            else:
                url = ''
        
        elif prov == '深圳':
            if newskind == 1:
                #1：深圳福彩
                if newstype == 1:
                    url = 'http://www.szlottery.org/fcw/fcxw/szfc/'        
                #2：通知公告
                elif newstype == 2:
                    url = 'http://www.szlottery.org/fcw/fcxw/tzgg/'
                #3：行业资讯
                elif newstype == 3:
                    url = 'http://www.szlottery.org/fcw/fcxw/hyzx/'
                else:
                    url = ''
            elif newskind == 2:
                #1：促销新闻
                if newstype == 1:
                    url = 'http://www.szlottery.org/fcw/yxhd/cxxw/'
                else :
                    url = ''
            elif newskind == 3:
                #1：政策法规
                if newstype == 1:
                    url = 'http://www.szlottery.org/fcw/sczx/zcfg/'        
                else:
                    url = ''
            elif newskind == 4:
                #1：深圳中奖喜讯
                if newstype == 1:
                    url = 'http://www.szlottery.org/fcw/kjxx/szzjxx/ssq/'        
                #2：中奖故事
                elif newstype == 2:
                    url = 'http://www.szlottery.org/fcw/kjxx/zjgs/ssq/'
                #3：行业资讯
                else:
                    url = ''
            else:
                url = ''
                
        elif prov == '广东':
            if newskind == 1:
                #1：彩市要闻
                if newstype == 1:
                    url = 'http://www.gdfc.org.cn/news_list_91.html'        
                #2：本省新闻
                elif newstype == 2:
                    url = 'http://www.gdfc.org.cn/news_list_13.html'
                #3：国内新闻
                elif newstype == 3:
                    url = 'http://www.gdfc.org.cn/news_list_14.html'
                #4:大奖喜报
                elif newstype == 4:
                    url = 'http://www.gdfc.org.cn/news_list_92.html'
                else:
                    url = ''
            elif newskind == 2:
                #1：福彩公益
                if newstype == 1:
                    url = 'http://www.gdfc.org.cn/jk_list_11.html'
                else :
                    url = ''
            else:
                url = ''
        
        elif prov == '广西':
            if newskind == 1:
                #1：全国彩市
                if newstype == 1:
                    url = 'http://www.gxcaipiao.com.cn/commHtml/pnews.html?smallclassid=204'        
                #2：八桂彩市
                elif newstype == 2:
                    url = 'http://www.gxcaipiao.com.cn/commHtml/new_pnews.html?smallclassid=205'
                #3：中奖报道
                elif newstype == 3:
                    url = 'http://www.gxcaipiao.com.cn/commHtml/new_pnews.html?smallclassid=206'
                #4:彩票娱乐
                elif newstype == 4:
                    url = 'http://www.gxcaipiao.com.cn/commHtml/new_pnews.html?smallclassid=271'
                #5:政策法规
                elif newstype == 5:
                    url = 'http://www.gxcaipiao.com.cn/commHtml/new_pnews.html?smallclassid=208'
                #6:百万榜
                elif newstype == 6:
                    url = 'http://www.gxcaipiao.com.cn/commHtml/new_pnews.html?smallclassid=170'                    
                else:
                    url = ''
            elif newskind == 2:
                #1：福彩公益
                if newstype == 1:
                    url = 'http://www.gxcaipiao.com.cn/commHtml/new_pnews.html?smallclassid=209'
                #2:赈灾公益金
                if newstype == 2:
                    url = 'http://www.gxcaipiao.com.cn/commHtml/new_pnews.html?smallclassid=331'
                #3:重生行动
                if newstype == 3:
                    url = 'http://www.gxcaipiao.com.cn/commHtml/new_pnews.html?smallclassid=291'
                #4：项目掠影
                if newstype == 4:
                    url = 'http://www.gxcaipiao.com.cn/commHtml/new_pnews.html?smallclassid=210'
                #5：明天计划
                if newstype == 5:
                    url = 'http://www.gxcaipiao.com.cn/commHtml/new_pnews.html?smallclassid=211'
                #6：五保村
                if newstype == 6:
                    url = 'http://www.gxcaipiao.com.cn/commHtml/new_pnews.html?smallclassid=212'
                #7：星光计划
                if newstype == 7:
                    url = 'http://www.gxcaipiao.com.cn/commHtml/new_pnews.html?smallclassid=213'
                #8：复明计划
                if newstype == 8:
                    url = 'http://www.gxcaipiao.com.cn/commHtml/new_pnews.html?smallclassid=214'
                else :
                    url = ''
            else:
                url = ''
                
                

        elif prov == '海南':
            if newskind == 1:
                #1:'福彩新闻'
                if newstype == 1:
                    url = 'http://www.hainancp.com/513/list_1.aspx'
                else :
                    url = ''
            elif newskind == 2:
                #2:'福彩公益'
                if newstype == 1:
                    url = 'http://www.hainancp.com/518/list_1.aspx'
                else :
                    url = ''
            elif newskind == 3:
                #3:'网站公告'
                if newstype == 1:
                    url = 'http://www.hainancp.com/512/list_1.aspx'
                else :
                    url = ''
            elif newskind == 4:
                #4:'福彩文化'
                if newstype == 1:
                    url = 'http://www.hainancp.com/519/list_1.aspx'
                else :
                    url = ''
            else:
                url = ''  
                    
      
        elif prov == '四川':
            if newskind == 1:
                #1:'党建工作'
                if newstype == 1:
                    url = 'http://www.scflcp.com/news/lotteryImportantNewsList?classficationId=3'
                #2:福彩动态
                elif newstype == 2:
                    url = 'http://www.scflcp.com/news/lotteryImportantNewsList?classficationId=4'
                #3:市州风采
                elif newstype == 3:
                    url = 'http://www.scflcp.com/news/lotteryImportantNewsList?classficationId=5'
                else :
                    url = ''
            elif newskind == 2:
                #1:中奖播报
                if newstype == 1:
                    url = 'http://www.scflcp.com/news/lotteryBriefNewsList?classficationId=9'
                #2：精彩活动
                elif newstype == 2:
                    url = 'http://www.scflcp.com/news/lotteryBriefNewsList?classficationId=10'
                else :
                    url = ''
            elif newskind == 3:
                #1:公益金信息
                if newstype == 1:
                    url = 'http://www.scflcp.com/news/charitableLotteryList?classficationId=54'
                #2:公益救助
                elif newstype == 2:
                    url = 'http://www.scflcp.com/news/charitableLotteryList?classficationId=55'
                #3:图说公益
                elif newstype == 3:
                    url = 'http://www.scflcp.com/news/charitableLotteryList?classficationId=84'
                else :
                    url = ''
            elif newskind == 4:
                #1:政策法规
                if newstype == 1:
                    url = 'http://www.scflcp.com/news/policiesAndLaws'
                else :
                    url = ''  
            else:
                url = ''  
            
        elif prov == '云南':
            if newskind == 1:
                #1:'网站公告'
                if newstype == 1:
                    url = 'http://www.ynflcp.cn/news/NewsListLower.aspx?typeid=50'
                #2:中奖喜讯
                elif newstype == 2:
                    url = 'http://www.ynflcp.cn/news/NewsListLower.aspx?typeid=87'
                #3:中福在线新闻
                elif newstype == 3:
                    url = 'http://www.ynflcp.cn/news/NewsListLower.aspx?typeid=93'
                #4：地方新闻
                elif newstype == 4:
                    url = 'http://www.ynflcp.cn/news/NewsListLower.aspx?typeid=39'
                #4：彩票文化
                elif newstype == 5:
                    url = 'http://www.ynflcp.cn/news/NewsListLower.aspx?typeid=40'
                else :
                    url = ''
            elif newskind == 2:
                #1:即开彩票
                if newstype == 1:
                    url = 'http://www.ynflcp.cn/news/NewsListLower.aspx?typeid=92'
                else :
                    url = ''
            elif newskind == 3:
                #1:福彩公益
                if newstype == 1:
                    url = 'http://www.ynflcp.cn/news/NewsListLower.aspx?Typeid=7'
                else :
                    url = ''            
            else:
                url = ''   
                    
        elif prov == '甘肃':
            if newskind == 1:
                #1:'福彩要闻'
                if newstype == 1:
                    url = 'http://www.gsflcp.com/newsCenter/newsList?classficationId=8'
                #2:全国新闻
                elif newstype == 2:
                    url = 'http://www.gsflcp.com/newsCenter/newsList?classficationId=11'
                #3:网站公告
                elif newstype == 3:
                    url = 'http://www.gsflcp.com/newsCenter/newsList?classficationId=9'
                #4：市州之窗
                elif newstype == 4:
                    url = 'http://www.gsflcp.com/newsCenter/newsList?classficationId=12'
                #4：中奖播报
                elif newstype == 5:
                    url = 'http://www.gsflcp.com/General/lotteryList?classficationId=13'
                else :
                    url = ''
            elif newskind == 2:
                #1:公益福彩
                if newstype == 1:
                    url = 'http://www.gsflcp.com/news/moreNewsList?classficationId=2'
                else :
                    url = ''
            elif newskind == 3:
                #1:彩票知识
                if newstype == 1:
                    url = 'http://www.gsflcp.com/newsCenter/newsList?classficationId=35'
                #1:玩家说彩
                if newstype == 2:
                    url = 'http://www.gsflcp.com/newsCenter/newsList?classficationId=36'
                else :
                    url = ''  
            else:
                url = ''
        
        elif prov == '青海':              
            if newskind == 1:
                #1:'福彩新闻'
                if newstype == 1:
                    url = 'http://www.qhfc.gov.cn/plus/list.php?tid=10'
                #2:大奖展示
                elif newstype == 2:
                    url = 'http://www.qhfc.gov.cn/plus/list.php?tid=12'
                #3:政策法规
                elif newstype == 3:
                    url = 'http://www.qhfc.gov.cn/plus/list.php?tid=29'
                #4：福彩公告
                elif newstype == 4:
                    url = 'http://www.qhfc.gov.cn/plus/list.php?tid=11'
                #5：彩市动态
                elif newstype == 5:
                    url = 'http://www.qhfc.gov.cn/plus/list.php?tid=14'
                #6：福彩文化
                elif newstype == 6:
                    url = 'http://www.qhfc.gov.cn/plus/list.php?tid=13'
                else:
                    url = ''
            elif newskind == 2:
                #1:扶老救孤
                if newstype == 1:
                    url = 'http://www.qhfc.gov.cn/plus/list.php?tid=22'
                #助残济困
                elif newstype == 2:
                    url = 'http://www.qhfc.gov.cn/plus/list.php?tid=23'
                else :
                    url = ''      
            else:
                url = ''       
        
        elif prov == '宁夏':        
            if newskind == 1:
                #1:'工作动态'
                if newstype == 1:
                    url = 'http://www.nxflcp.com/news/newsList.action?listType=gzdt'
                #2:党建阵地
                elif newstype == 2:
                    url = 'http://www.nxflcp.com/news/newsList.action?listType=djzd'
                #3:学习园地
                elif newstype == 3:
                    url = 'http://www.nxflcp.com/news/newsList.action?listType=xxyd'
                else:
                    url = ''
            elif newskind == 2:
                #1:福彩文化
                if newstype == 1:
                    url = 'http://www.nxflcp.com/news/lotteryculture_work.action?listType=lotteryculture'
                else :
                    url = ''      
            elif newskind == 3:
                #1:国家政策法规
                if newstype == 1:
                    url = 'http://www.nxflcp.com/news/newsList.action?listType=regulations'
                #2、宁夏福彩规则
                if newstype == 2:
                    url = 'http://www.nxflcp.com/news/newsList.action?listType=nxfcregulations'
                else :
                    url = ''      
            else:
                url = ''  
        
        
        elif prov == '湖北':        
            if newskind == 1:
                #1:'彩市要闻'
                if newstype == 1:
                    url = 'http://www.hbfcw.gov.cn/csyw/'
                else:
                    url = ''
            elif newskind == 2:
                #1:通知公告
                if newstype == 1:
                    url = 'http://www.hbfcw.gov.cn/tzgg/'
                else :
                    url = ''      
            elif newskind == 3:
                #1:大奖喜报
                if newstype == 1:
                    url = 'http://www.hbfcw.gov.cn/djxb/'   
                else:
                    url = ''
            else:
                url = ''  
         
        elif prov == '湖南':
            if newskind == 1:
                #1:'福彩要闻'
                if newstype == 1:
                    url = 'http://www.hnflcp.gov.cn/newstypelist.asp?intype=1'
                #2:中奖喜讯
                elif newstype == 2:
                    url = 'http://www.hnflcp.gov.cn/newstypelist.asp?intype=2'
                else:
                    url = ''
            elif newskind == 2:
                #1:公益事业
                if newstype == 1:
                    url = 'http://www.hnflcp.gov.cn/newstypelist.asp?intype=3'
                #2:公益图片
                elif newstype == 2:
                    url = 'http://www.hnflcp.gov.cn/newstypelist.asp?intype=4'
                else :
                    url = ''      
            elif newskind == 3:
                #1:国内彩市
                if newstype == 1:
                    url = 'http://www.hnflcp.gov.cn/newstypelist.asp?intype=49'  
                #2:国际彩市
                elif newstype == 2:
                    url = 'http://www.hnflcp.gov.cn/newstypelist.asp?intype=50'
                else:
                    url = ''
            else:
                url = ''  
        
        elif prov == '新疆':
            if newskind == 1:
                #1:'重要公告'
                if newstype == 1:
                    url = 'http://www.xjflcp.com/newsCenter/newsList?classficationId=7'
                #2:区内新闻
                elif newstype == 2:
                    url = 'http://www.xjflcp.com/newsCenter/newsList?classficationId=8'
                #3:国内新闻
                elif newstype == 3:
                    url = 'http://www.xjflcp.com/newsCenter/newsList?classficationId=9'
                else:
                    url = ''
            elif newskind == 2:
                #1:爱心关注
                if newstype == 1:
                    url = 'http://www.xjflcp.com/newsCenter/newsList?classficationId=10'
                #2:公益救助
                elif newstype == 2:
                    url = 'http://www.xjflcp.com/newsCenter/newsList?classficationId=11'
                #4：图说公益
                elif newstype == 3:
                    url = 'http://www.xjflcp.com/newsCenter/newsList?classficationId=12'
                else :
                    url = ''      
            else:
                url = ''   
                  
        elif prov == '贵州':
            if newskind == 1:
                #1:'省内新闻'
                if newstype == 1:
                    url = 'http://www.gzfucai.cn/news/NewsListTo.aspx?TypeId=5'
                #2:省外新闻
                elif newstype == 2:
                    url = 'http://www.gzfucai.cn/news/NewsListTo.aspx?TypeId=8'
                #3:双色球
                elif newstype == 3:
                    url = 'http://www.gzfucai.cn/news/NewsListTo.aspx?TypeId=27'
                #4:福彩3d
                elif newstype == 4:
                    url = 'http://www.gzfucai.cn/news/NewsListTo.aspx?TypeId=28'
                #5七彩乐
                elif newstype == 5:
                    url = 'http://www.gzfucai.cn/news/NewsListTo.aspx?TypeId=5808'
                #6:快3
                elif newstype == 6:
                    url = 'http://www.gzfucai.cn/news/NewsListTo.aspx?TypeId=5813'
                #7:彩票文化
                elif newstype == 7:
                    url = 'http://www.gzfucai.cn/news/NewsListTo.aspx?TypeId=37'
                #8：中福在线
                elif newstype == 8:
                    url = 'http://www.gzfucai.cn/news/NewsListTo.aspx?TypeId=5812'
                #9：刮刮乐
                elif newstype == 9:
                    url = 'http://www.gzfucai.cn/news/NewsListTo.aspx?TypeId=5811'
                #10：福彩公告
                elif newstype == 10:
                    url = 'http://www.gzfucai.cn/news/NewsListTo.aspx?TypeId=20'                
                else:
                    url = ''
            elif newskind == 2:
                #1:温暖贵州
                if newstype == 1:
                    url = 'http://www.gzfucai.cn/news/NewsListTo.aspx?TypeId=5808'
                #2：省外公益
                elif newstype == 2:
                    url = 'http://www.gzfucai.cn/news/NewsListTo.aspx?TypeId=5806'
                else :
                    url = ''    
            elif newskind == 3:
                #1:大奖喜报
                if newstype == 1:
                    url = 'http://www.gzfucai.cn/news/NewsListTo.aspx?TypeId=21'
                else :
                    url = ''   
            elif newskind == 4:
                #1:投注技巧
                if newstype == 1:
                    url = 'http://www.gzfucai.cn/news/NewsListTo.aspx?TypeId=5801'
                else :
                    url = ''
            elif newskind == 5:
                #1:信息公开
                if newstype == 1:
                    url = 'http://www.gzfucai.cn/news/NewsListTo.aspx?TypeId=23'
                else :
                    url = ''
            elif newskind == 6:
                #1:政策法规
                if newstype == 1:
                    url = 'http://www.gzfucai.cn/news/NewsListTo.aspx?TypeId=4'
                else :
                    url = ''
            elif newskind == 7:
                #1:支部园地
                if newstype == 1:
                    url = 'http://www.gzfucai.cn/news/NewsListTo.aspx?TypeId=5800'
                else :
                    url = ''
            else:
                url = ''   
        
        
         
                        
        return url
    
    def InsData(self,province,newskind,newstype,url,datedif):
###################################################################################黑龙江#################################################################    
        DicProvince={1:'黑龙江',2:'内蒙古',3:'陕西',4:'杭州',5:'天津',6:'北京',7:'河北',8:'辽宁',9:'吉林',10:'江苏',11:'浙江',12:'安徽',13:'福建',14:'江西',15:'河南',16:'深圳',17:'广东',18:'广西',19:'海南',20:'重庆',21:'四川',22:'云南',23:'甘肃',24:'青海',25:'宁夏',26:'湖北',27:'湖南',28:'新疆',29:'贵州'}
        prov = DicProvince[province]
        userhead = {  
                    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'  
                    }
        try:
            rep = requests.get(url,headers=userhead,timeout=5)
            res = rep.content
            soup = bs(res,'html.parser')
        except:
            print 'time out'
            soup = ''
        if soup <> '':
            if prov == '黑龙江':
                
                soupdiv=soup.find(attrs={'class':'leftcenter'})
                
                titlediv = soupdiv.find('h2')
                title = titlediv.text.strip()
                 
                topdiv = soupdiv.find('h3')
                strlist = topdiv('span')
                sourcestr = strlist[1].text
                source = sourcestr.replace('来源:','').strip()
                
                newstime = strlist[0].text.strip()
                newstime = newstime.replace('时间:','').strip()
                newstime = datetime.datetime.strptime(newstime,'%Y-%m-%d %H:%M') 
                
                author = strlist[2].text.strip()
                author = author.replace('作者:','')
                
                sourcediv = soupdiv.find(attrs={'class':'nr'})
                newstxt = sourcediv.text.strip()
    
                cmt = 0
                
                dictypename = {1:'彩市新闻',2:'彩民之家',3:'龙江公益'}
                if newskind in (1,2):
                    newstype = 0
                dicnewstype = {0:'其它',1:'公益动态',2:'龙江公益',3:'公益行动',4:'公益项目',5:'公益黄页',6:'营销管理'}
                
                
            
            
###################################################################################内蒙古#################################################################    
            elif prov == '内蒙古' :
                
                soupdiv=soup.find(attrs={'class':'zhengWen'})
                
                titlediv = soupdiv.find('h3')
                title = titlediv.text.strip()
                
                
                topdiv = soupdiv.find(attrs={'class':'xinxi'})
                toptext = topdiv.text
                strlist = toptext.split(' ')
                 
                
                sourcestr = strlist[2]
                source = sourcestr.replace('来源：','').strip()
                
                
                newstime = strlist[0]+' '+strlist[1]
                newstime = newstime.replace('时间:','').strip()
                newstime = datetime.datetime.strptime(newstime,'%Y-%m-%d %H:%M:%S') 
                
                
                #author = strlist[2].text.strip()
                #author = author.replace('作者:','') 
                
                sourcediv = soupdiv.find(attrs={'id':'news_content'})
                newstxt = sourcediv.text.strip()
                
                alist = re.findall(r"\(.*?\)$", newstxt)
                if len(alist):
                    author = alist[0]
                else:
                    author =''
    
                cmt = 0
                
                dictypename = {1:'新闻',2:'公益速递'}
                if newskind == 1:
                    dicnewstype = {1:'玩法新闻',2:'区外新闻',3:'站主之家',4:'区内新闻',5:'彩民之家'}
                elif newskind == 2:
                    dicnewstype = {1:'公益金',2:'公益项目',3:'我区公益新闻',4:'全国公益新闻'}
            
    
###################################################################################陕西#################################################################        
            elif prov == '陕西' :
                
                soupdiv=soup.find(attrs={'class':'textL'})
                
                titlediv = soupdiv.find('h1')
                title = titlediv.text.strip()
                
                topdiv = soupdiv.find(attrs={'class':'info'})
                toptext = topdiv.text
                strlist = toptext.split(' ')
                 
                sourcestr = strlist[2]
                source = sourcestr.replace('来源：','').strip()
                
                newstime = strlist[0]+' '+strlist[1]
                newstime = newstime.replace('时间:','').strip()
                newstime = datetime.datetime.strptime(newstime,'%Y-%m-%d %H:%M:%S') 
                
                author = '' 
                newstxt = ''
                for content in soupdiv('p'):
                    newstxt = newstxt + '\n' +content.text
                
                newstxt = newstxt.strip()
    
                cmt = 0
                
                dictypename = {1:'新闻',2:'福彩公益'}
                if newskind == 1:
                    dicnewstype = {1:'玩法新闻',2:'公益新闻',3:'全球彩风',4:'福彩文化',5:'大奖统计'}
                elif newskind == 2:
                    dicnewstype = {1:'省公益新闻',2:'全国公益新闻'}                
                
            elif prov == '杭州' :
                            
                soupdiv=soup.find(attrs={'class':'news_content'})
                
                titlediv = soupdiv.find(attrs={'class':'newsTitle'})
                title = titlediv.text.strip()
                
                topdiv = soupdiv.find(attrs={'class':'message'})
                toptext = topdiv.text
                strlist = toptext.split('    ')
                 
                sourcestr = strlist[1]
                source = sourcestr.replace('来源：','').strip()
                
                newstime = strlist[0]
                newstime = newstime.replace('时间:','').strip()
                newstime = datetime.datetime.strptime(newstime,'%Y-%m-%d %H:%M:%S') 
                
                author = '' 
                newstxt = ''
                for content in soupdiv('p'):
                    newstxt = newstxt+content.text.strip()
                newstxt = newstxt.strip()
    
                cmt = 0
                
                dictypename = {1:'福彩公益'}
                dicnewstype = {1:'杭州公益',2:'公益行动',3:'公益项目'}
            
            elif prov == '天津' :
                
                soupdiv=soup.find(attrs={'id':'newsWDiv'})
                
                titlediv = soupdiv.find('b')
                title = titlediv.text.strip()
                
                topdiv = soupdiv.findAll('td')
                source = topdiv[1].text.strip()
                
                newstime = topdiv[3].text.strip()
                newstime = datetime.datetime.strptime(newstime,'%Y-%m-%d')
                
                author = '' 
                newstxt = ''
                for content in soupdiv('p'):
                    newstxt = newstxt+content.text.strip()
                
                newstxt = newstxt.strip()
    
                cmt = 0
                
                dictypename = {1:'新闻资讯'}
                dicnewstype = {1:'网站公告',2:'彩市快讯',3:'爱心公益',4:'福彩新闻',5:'彩票文化'}
            
            elif prov == '北京' :
                
                soupdiv=soup.find(attrs={'class':'infoArticle'})
                
                titlediv = soupdiv.find('h4')
                title = titlediv.text.strip()
                
                newstime = datedif
                newstime = datetime.datetime.strptime(newstime,'%Y-%m-%d %H:%M:%S')
                
                author = '' 
                newstxt = ''
                for content in soupdiv('p'):
                    newstxt = newstxt+content.text.strip()
                newstxt = newstxt.strip()
                
                soulist = re.findall(r"\(.*?\)$",newstxt)
                if soulist:
                    source = soulist[0]
                    source = author.replace('来源：','')
                    source = author.replace('(','')
                    source = author.replace(')','')
                else:
                    source = ''
    
                cmt = 0
                
                dictypename = {1:'福彩资讯'}
                dicnewstype = {1:'福彩公告',2:'福彩新闻',3:'中奖报道',4:'公益金使用'}
                
                #北京特殊处理，datedif传入值为日期
                datedif = -1
    
            elif prov == '河北':
                
                soupdiv=soup.find(attrs={'class':'leftPage'})
                souptop = soupdiv.find(attrs={'class':'tit_con'})
                
                titlediv = soupdiv.find('strong')
                title = titlediv.text.strip()
                
                topdiv = souptop.find(attrs={'class':'fl'})
                restr = topdiv.text
                strlist = restr.split('  ')
                sourcestr = strlist[0]
                sourcelist = sourcestr.split(' ')
                source = sourcelist[0]
                author = sourcelist[1]
                newstime = strlist[1]
                
                cmt = int(souptop.find(attrs={'class':'fr'}).find('em').text)
                
                newstime = datetime.datetime.strptime(newstime,'%Y-%m-%d %H:%M:%S')
                
                newstxt = ''
                consoup = soupdiv.find(attrs={'class':'news_con'})
                
                for content in consoup('span'):
                    newstxt = newstxt+content.text.strip()
                
                newstxt = newstxt.strip()
    
                dictypename = {1:'福彩新闻',2:'公益之窗'}
                if newskind == 1:
                    dicnewstype = {1:'通知公告',2:'燕赵新闻',3:'全国新闻',4:'彩民故事',5:'中奖播报'}
                elif newskind == 2:
                    dicnewstype = {1:'公益之窗'}
            
            
            elif prov == '辽宁':
                
                soupdiv=soup.find(attrs={'class':'newsHaed'})
                
                titlediv = soupdiv.find('h1')
                title = titlediv.text.strip()
                 
                topdiv = soupdiv.findAll('td')
                
                source = topdiv[1].text.strip().replace('来源：','')
                newstime = topdiv[3].text.strip()
                cmt = int(topdiv[5].text.strip().replace('查看人数：',''))
                
                author = ''
                newstime = datetime.datetime.strptime(newstime,'%Y-%m-%d')
                 
                newstxt = ''
                 
                consoup = soup.find(attrs={'class':'newsContent'})
                 
                for content in consoup('p'):
                    newstxt = newstxt+content.text.strip()
                 
                newstxt = newstxt.strip()
    
                dictypename = {1:'福彩资讯'}
                dicnewstype = {1:'网站公告',2:'即开票资讯',3:'电讯资讯',4:'中福在线',5:'地市资讯',6:'中奖故事',7:'福彩文化'}
                
            
            
            
            
            elif prov == '吉林':
                
                soupdiv=soup.find(attrs={'class':'newsHaed'})
                
                titlediv = soupdiv.find('h1')
                title = titlediv.text.strip()
                
                topdiv = soupdiv.findAll('td')
                
                source = topdiv[1].text.strip().replace('来源：','')
                newstime = topdiv[3].text.strip()
                cmt = int(topdiv[5].text.strip().replace('查看人数：',''))
                
                author = ''
                newstime = datetime.datetime.strptime(newstime,'%Y-%m-%d')
                 
                newstxt = ''
                 
                consoup = soup.find(attrs={'class':'newsContent'})
                 
                for content in consoup('p'):
                    newstxt = newstxt+content.text.strip()
                 
                newstxt = newstxt.strip()
    
                dictypename = {1:'新闻资讯',2:'公益活动'}
                if newskind == 1:
                    dicnewstype = {1:'地市资讯',2:'最新公告',3:'中奖故事',4:'明星站点',5:'即开票资讯'}
                elif newskind == 2:
                    dicnewstype = {1:'公益动态'}
            
            
            elif prov == '江苏':
                head = {
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                    'Accept-Encoding': 'gzip, deflate',
                    'Accept-Language': 'zh-CN,zh;q=0.9',
                    'Cache-Control': 'max-age=0',
                    'Connection': 'keep-alive',
                    'Cookie': 'Hm_lvt_bc3cd40b25461d70cfbfdb5517f3f1ef=1522374631; Hm_lpvt_bc3cd40b25461d70cfbfdb5517f3f1ef=1522374631',
                    'Host': 'www.jslottery.com',
                    'Upgrade-Insecure-Requests': '1',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
                        }
                    
                res = requests.get(url,headers = head,timeout=5)
                soup = bs(res.content,'lxml')           
                 
                soupdiv=soup.find(attrs={'class':'news_table'})
                title = ''
                for a in soupdiv.findAll('th'):
                    title = title + a.text.strip().replace("\n", "")
                
                souptop = soupdiv.find(attrs={'align':'center'})
                
                infolist = souptop.findAll('td')
                
                source = infolist[1].text.strip()
                newstime = infolist[3].text.strip()
                cmtstr = infolist[5].text.strip()
                
                source = source.replace('来源：','').strip()
                newstime = datetime.datetime.strptime(newstime,'%Y-%m-%d') 
                cmt = int(cmtstr.replace('浏览次数：',''))
                    
                soupcon = soupdiv.find(attrs={'class':'newscontent'})
                newstxt = soupcon.text.strip()
                
                author = ''
                
                dictypename = {1:'彩市新闻',2:'公益活动'}
                dicnewstype = {1:'其它'}
            
            elif prov == '浙江':
                
                souptitle=soup.find('h1',attrs={'class':'artTitle'})
                if souptitle is None:
                    soupinfo = soup.find('dt',attrs={'class':'neiDt'})
                
                    infolist = soupinfo.text.split('\n')
                    title = infolist[0]
                    
                    infostr = infolist[1].strip().split(' ')
                    
                    newstime = infostr[0]+' ' +infostr[1]
                    newstime = datetime.datetime.strptime(newstime,'%Y年%m月%d日 %H:%M:%S')
                    
                    source = infostr[2]
                    soupcon = soup.find('div',attrs={'id':'zwen'})
                    
                else:    
                    title = souptitle.text.strip()
                    
                    soupinfo = soup.find('div',attrs={'class':'info'})
                    infostr = soupinfo.text.strip()
                    infolist = infostr.split('\n')
                    
                    newstime= infolist[0]
                    newstime = newstime.replace('发布时间：','').strip()
                    newstime = datetime.datetime.strptime(newstime,'%Y-%m-%d %H:%M:%S')
                    source = infolist[1]
                    soupcon = soup.find('div',attrs={'class':'artCon'})
                    
                newstxt = ''
                for t in soupcon('p'):
                    newstxt = newstxt + t.text.strip()
                 
                author = ''
    
                cmt = 0
                
                dictypename = {1:'浙江福彩',2:'公益福彩'}
                dicnewstype = {1:'其它'}
                        
            
            
            elif prov == '安徽' :
                
                souptitle = soup.find('td',attrs={'class':'font26bold'})
                title = souptitle.text.strip()
                
                soupinfo = soup.find('tr',attrs={'class':'gray'})
                infolist = soupinfo.text.strip()
                infostr = infolist.split('　')
                infostr[0].replace('发布时间：','')
                newstime = infostr[0].replace('发布时间：','')
                newstime = datetime.datetime.strptime(newstime,'%Y-%m-%d')
                
                source = ''
                
                soupcon = soup.find('td',attrs={'id':'fontZoom'})
                newstxt = soupcon.text.strip()
                
                alist = re.findall(u'（.*?）$', newstxt)
                if len(alist):
                    author = alist[0]
                else:
                    author =''
                
                if len(author) > 50:
                    author = ''           
    
                cmt = 0
    
                dictypename = {1:'福彩资讯',2:'福彩公益',3:'政务公开'}
                if newskind == 1:
                    dicnewstype = {1:'全国新闻',2:'省内新闻'}
                elif newskind == 2:
                    dicnewstype = {1:'公益金',2:'圆梦大学',3:'图书进校园'}
                elif newskind == 3:
                    dicnewstype = {1:'决策公开',2:'部门预决算',3:'招标采购',4:'廉政信息'}
            
            
            elif prov == '福建':
                
                titlediv = soup.find('div',attrs={'class':'news_h'})
                title = titlediv.text.strip()
                 
                infodiv = soup.find('div',attrs={'align':'center','class':'black'})
                infostr = infodiv.text
                infolist = infostr.split('：')
                newstime = infolist[1].replace('编辑人','').strip()
                author = infolist[2].strip()
                source = 0
                cmt = 0
                newstime = datetime.datetime.strptime(newstime,'%Y-%m-%d %H:%M:%S')
                 
                newstxt = ''
                   
                cont = soup.find('td',attrs={'id':'ShowContent'})
                for cont in cont('p'):
                    newstxt = newstxt + cont.text.strip()
                newstxt = newstxt.replace('\n','')
                  
                dictypename = {1:'新闻中心'}
                dicnewstype = {1:'其它'}
            
            
            elif prov == '河南':
                
                souptitle = soup.find('h1',attrs={'id':'title'})
                title = souptitle.text.strip()
                
                soupinfo = soup.find('div',attrs={'id':'cai'})
                infolist = soupinfo.text.strip().split('\n')
                infolist.remove('\r')
                
                source = infolist[0].strip()
                source = source.replace('编辑：','')
                
                newstime = infolist[2].strip()
                newstime = newstime.replace('录入：','')
                newstime = newstime[0:19]
                newstime = datetime.datetime.strptime(newstime,'%Y-%m-%d %H:%M:%S')
                
                newstxt = ''
                soupcon = soup.find('div',attrs={'id':'content'})
                for a in soupcon('p'):
                    newstxt = newstxt + a.text.strip()            
                
                author = ''
                cmt = 0
    
                dictypename = {1:'福彩新闻',2:'公益'}
                if newskind == 1:
                    dicnewstype = {1:'全国新闻',2:'省内新闻'}
                elif newskind == 2:
                    dicnewstype = {1:'公益新闻',2:'公益行动'}
            
            elif prov == '深圳':
                
                soupdiv = soup.find('div',attrs={'class':'count-box'})
    
                titlediv = soupdiv.find('h3',attrs={'class':'count-title'})
                title = titlediv.text.strip()
                
                soupinfo = soup.find('div',attrs={'class':'count-msg'})
                infolist = soupinfo.text.strip().split('\n')
                
                newstime = infolist[0]
                newstime = newstime.replace('发布时间：','')
                newstime = datetime.datetime.strptime(newstime,'%Y-%m-%d')
    
                cmt = 0
                author = ''
                source = ''
                newstxt = ''
                soupcon = soup.find('div',attrs={'class':'count-text'})
                for a in soupcon('p'):
                    newstxt = newstxt + a.text.strip()
    
                dictypename = {1:'福彩新闻',2:'营销活动',3:'深彩中心',4:'开奖公告'}
                if newskind == 1:
                    dicnewstype = {1:'深圳福彩',2:'通知公告',3:'行业资讯'}
                elif newskind == 2:
                    dicnewstype = {1:'促销新闻'}
                elif newskind == 3:
                    dicnewstype = {1:'政策法规'}
                elif newskind == 4:
                    dicnewstype = {1:'深圳中奖喜讯',2:'中奖故事'}
     
            elif prov == '广东':
                
                soupdiv = soup.find('div',attrs={'class':'contentBox_R_02'})
                
                souptitle = soupdiv.find('div',attrs={'class':'news_content_R_title'})
                title = souptitle.text.strip()
                
                soupinfo = soupdiv.find('div',attrs={'class':'news_content_R_time'})
                infolist = soupinfo.text.strip().split('\n')
                
                newstime = infolist[0].strip().replace('日期：','')
                source = infolist[1].strip().replace('来源：','')
                
                newstime = datetime.datetime.strptime(newstime,'%Y-%m-%d')
                
                cmt = 0
                author = ''
                newstxt = ''
                soupcon = soupdiv.find('div',attrs={'class':'news_content_R_con'})
                newstxt = soupcon.text.strip().replace('\n','')
    
                dictypename = {1:'彩票新闻',2:'福彩公益'}
                if newskind == 1:
                    dicnewstype = {1:'彩市要闻',2:'本省新闻',3:'国内新闻',4:'大奖喜报'}
                elif newskind == 2:
                    dicnewstype = {1:'福彩公益'}
            
            elif prov == '广西':
                 
                soupdiv = soup.find('div',attrs={'class':'textCon'})
                
                souptitle = soupdiv.find('h2',attrs={'class':'fwb'})
                title = souptitle.text.strip()
                
                soupinfo = soupdiv.find('span',attrs={'class':'s-tt'})
                infolist = soupinfo.text.strip().split('】')
                
                author = infolist[0].replace('【','').strip()
                author = author.replace('作者：','')
                newstime = infolist[2].replace('【','').strip()
                
                newstime = datetime.datetime.strptime(newstime,'%Y-%m-%d %H:%M:%S')
                source = ''
                cmt = 0
                newstxt = ''
                for cont in soupdiv.findAll('p'):
                    newstxt = newstxt + cont.text.strip()
    
                dictypename = {1:'彩票新闻',2:'公益福彩'}
                if newskind == 1:
                    dicnewstype = {1:'全国彩市',2:'八桂彩市',3:'中奖报道',4:'彩票娱乐',5:'政策法规',6:'百万榜'}
                elif newskind == 2:
                    dicnewstype = {1:'福彩公益',2:'赈灾公益金',3:'重生行动',4:'项目掠影',5:'明天计划',6:'五保村',7:'星光计划',8:'复明计划'}
            
            elif prov == '海南':
                
                soupdiv = soup.find('div',attrs={'class':'s_body'})
                souptitle = soupdiv.find('h1',attrs={'class':'aTitle'})
                title = souptitle.text.strip()
                
                soupinfo = soupdiv.find('div',attrs={'class':'infos'})
                infolist = soupinfo.text.strip().split('：')
                newstime = infolist[1]
                author = infolist[2]
                cmt = infolist[3]
                
                cmt = cmt.replace(']','')
                if cmt :
                    cmt = int(cmt)
                newstime = newstime.replace('作者','').strip()
                author = author.replace('浏览次数','').strip()
    
                newstime = datetime.datetime.strptime(newstime,'%Y-%m-%d %H:%M')
    
                source = ''
                newstxt = ''
                for cont in soupdiv.findAll('p'):
                    newstxt = newstxt + cont.text.strip()
                
                
                dictypename = {1:'福彩新闻',2:'福彩公益',3:'网站公告',4:'福彩文化'}
                dicnewstype = {1:'其它'}
                
                
    
            elif prov == '四川':
                
                soupdiv = soup.find('div',attrs={'class':'newsPage_left'})
                
                souptitle = soupdiv.find('h3',attrs={'class':'tit_con'})
                title = soupdiv.find('strong').text
                info = soupdiv.find('p').text
                
                infolist = info.split('：')
                source = infolist[1]
                source = source.replace('作者','').strip()
                
                list2 = infolist[2]
                infolist2 = infolist[2].split('  ')
                
                try:
                    cmt = int(infolist[3])
                except:
                    cmt = 0
                
                author = infolist2[0]
                newstime = infolist2[1]
                newstime = newstime.replace('市场二部','').strip()
                newstime = newstime[0:19]
                
                newstime = datetime.datetime.strptime(newstime,'%Y-%m-%d %H:%M:%S')
                
                newstxt = ''
                condiv = soupdiv.find('div',attrs={'class':'news_con'})
                for cont in condiv('p'):
                    newstxt = newstxt + cont.text.strip()
                    
                    
                
                dictypename = {1:'福彩要闻',2:'福彩简讯',3:'公益福彩',4:'政策法规'}
                if newskind == 1 :
                    dicnewstype = {1:'党建工作',2:'福彩动态',3:'市州风采'}
                elif newskind == 2 :
                    dicnewstype = {1:'中奖播报',2:'精彩活动'}
                elif newskind == 3 :
                    dicnewstype = {1:'公益金信息',2:'公益救助',3:'图说公益'}
                elif newskind == 4 :
                    dicnewstype = {1:'其它'}   
                
            elif prov == '云南':
    #             userhead = {  
    #                 'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'  
    #             }  
    #             rep = requests.get(url,headers=userhead,timeout=5)
    #             res = rep.content
    #             soup = bs(res,'html.parser')
                
                soupdiv = soup.find('div',attrs={'id':'newsWDiv'})
                
                souptitle = soupdiv.find('h2',attrs={'style':'margin-top: 30px;'})
                title = soupdiv.find('b').text.strip()
                
                infostr = ''
                
                infodiv = soupdiv.find('tr')
                infostr = infodiv.text
                infostr = re.sub('\s','',infostr)
                
                
                infolist = infostr.split('  ')
                
                source = infolist[0].replace('编辑：','')
                newstime = infolist[1]
                cmtstr = infolist[2].replace('查看人数：','')
                if cmtstr:
                    cmt = int(cmtstr)
                author = ''
                
                newstime = datetime.datetime.strptime(newstime,'%Y-%m-%d')
                
                newstxt = ''
                condiv = soupdiv.find('div',attrs={'class':'div_newsContent'})
                for cont in condiv('p'):
                    newstxt = newstxt + cont.text.strip()
    
    
                dictypename = {1:'新闻资讯',2:'即开彩票',3:'福彩公益'}
                if newskind == 1 :
                    dicnewstype = {1:'网站公告',2:'中奖喜讯',3:'中福在线新闻',4:'地方新闻',5:'彩票文化'}
                elif newskind == 2 :
                    dicnewstype = {1:'其它'}
                elif newskind == 3 :
                    dicnewstype = {1:'其它'}   
                
            elif prov == '甘肃':
                            
                soupdiv = soup.find('div',attrs={'class':'newsDetail'})
                
                souptitle = soupdiv.find('h2',attrs={'class':'tit'})
                title = souptitle.text.strip()
                
                source = soupdiv.find('span',attrs={'class':'fl info01'}).text.strip()
                author = soupdiv.find('span',attrs={'class':'fl info02'}).text.strip()
                newstime = soupdiv.find('span',attrs={'class':'fl info03'}).text.strip()
                cmtstr = soupdiv.find('span',attrs={'class':'fr info04'}).text.strip()
                
                source = source.replace('来源：','')
                author = author.replace('编辑：','')
                cmtstr = cmtstr.replace('阅读次数：','')
                cmt = int(cmtstr)
                
                newstime = datetime.datetime.strptime(newstime,'%Y-%m-%d %H:%M:%S')
                
                newstxt = ''
                for cont in soupdiv('p'):
                    newstxt = newstxt + cont.text.strip()
                
                
                
                dictypename = {1:'福彩新闻',2:'公益福彩',3:'投注指南'}
                if newskind == 1 :
                    dicnewstype = {1:'福彩要闻',2:'全国新闻',3:'网站公告',4:'市州之窗',5:'中奖播报'}
                elif newskind == 2 :
                    dicnewstype = {1:'其它'}
                elif newskind == 3 :
                    dicnewstype = {1:'彩票知识',2:'玩家说彩'}   
            
            
            
            elif prov == '青海':
                            
                soupdiv = soup.find('div',attrs={'class':'lb lf'})
                
                souptitle = soupdiv.find('h1')
                title = souptitle.text.strip()
                 
                infodiv = soup.find('div',attrs={'class':'nrx'})
                infostr = infodiv.text.strip()
                infolist = infostr.split(' ')
                
                newstime = infolist[1]+' '+infolist[2]
                author = infolist[3].replace('作者：','')
                source = infolist[5].replace('来源：','')
                cmt = 0
                
                newstime = datetime.datetime.strptime(newstime,'%Y-%m-%d %H:%M')
                newstxt = ''
                
                for cont in soupdiv('p'):
                    newstxt = newstxt + cont.text.strip()
                    
                newstxt = newstxt.replace('\n','')    
                
                
                dictypename = {1:'新闻',2:'公益'}
                if newskind == 1 :
                    dicnewstype = {1:'福彩新闻',2:'大奖展示',3:'政策法规',4:'福彩公告',5:'彩市动态',6:'福彩文化'}
                elif newskind == 2 :
                    dicnewstype = {1:'扶老救孤',2:'助残济困'}   
                    
                    
            elif prov == '宁夏':
                
                soupdiv = soup.find('div',attrs={'class':'news_a1'})
                 
                souptitle = soupdiv.find('div',attrs={'class':'news_a1_a'})
                title = souptitle.text.strip()
     
                infodiv = soup.find('tr')
                infolist=[]
                for i in infodiv('td'):
                    infolist.append(i.text.strip())
                    
                author = infolist[0].replace('作者：','')
                source = infolist[1].replace('来源：','')
                newstime = '20'+infolist[2].replace('日期：','')
                cmt = 0
                
                
                newstime = datetime.datetime.strptime(newstime,'%Y-%m-%d')
                newstxt = ''
                  
                for cont in soupdiv('p'):
                    newstxt = newstxt + cont.text.strip()
                      
                newstxt = newstxt.replace('\n','')             
                 
                dictypename = {1:'中信工作',2:'福彩文化',3:'政策法规'}
                if newskind == 1 :
                    dicnewstype = {1:'工作动态',2:'党建阵地',3:'学习园地'}
                elif newskind == 2 :
                    dicnewstype = {1:'其它'}
                elif newskind == 3:
                    dicnewstype = {1:'国家政策法规',2:'宁夏福彩规则'} 
             
            elif prov == '湖北':
                
                soupdiv = soup.find('div',attrs={'class':'wzy_box'})
                 
                souptitle = soupdiv.find('div',attrs={'class':'title'})
                title = souptitle.text.strip()
    
                infodiv = soupdiv.find('div',attrs={'class':'sub_title'})
                
                infolist=[]
                for i in infodiv('span'):
                    infolist.append(i.text.strip())
                
                newstime = infolist[0].replace('发布时间：','')
                source = infolist[1].replace('来源：','')
                author = ''
                cmt = 0
                     
                
                newstime = datetime.datetime.strptime(newstime,'%Y-%m-%d %H:%M:%S')
                newstxt = ''
                   
                for cont in soupdiv('p'):
                    newstxt = newstxt + cont.text.strip()
                      
                newstxt = newstxt.replace('\n','')
                 
                dictypename = {1:'福彩要闻',2:'通知公告',3:'大奖喜报'}
                dicnewstype = {1:'其它'}
                
            elif prov == '湖南':
                
                soupdiv = soup.find('table',attrs={'width':'98%'})
                
                ilist = []
                for infodiv in soupdiv.findAll('div',attrs={'align':'center'}):
                    ilist.append(infodiv)
                
                souptitle = ilist[0]
                title = souptitle.text.strip()
                
                infostr = ilist[1].text.strip()
                infolist = infostr.split('    ')
                
                source = infolist[0].replace('来源：','')
                newstime = infolist[1].replace('发布时间：','')
                cmt = 0
                author = ''
                 
                newstime = datetime.datetime.strptime(newstime,'%Y-%m-%d')
                newstxt = ''
                    
                for cont in soup('p'):
                    newstxt = newstxt + cont.text.strip()
                newstxt = newstxt.replace('\n','')
                  
                dictypename = {1:'信息公开',2:'公益事业',3:'八面彩风'}
                if newskind == 1 :
                    dicnewstype = {1:'福彩要闻',2:'中奖喜讯'}
                elif newskind == 2 :
                    dicnewstype = {1:'公益事业',2:'公益图片'}
                elif newskind == 3 :
                    dicnewstype = {1:'国内彩市',2:'国际彩市'}
                
            
            
            elif prov == '新疆':
                
                soupdiv = soup.find('div',attrs={'class':'news_content'})
                
                titlediv = soupdiv.find('h2')
                title = titlediv.text.strip()
                
                infodiv = soupdiv.find('p')
                infostr = infodiv.text
                infolist = infostr.split('：')
                
                source = infolist[1].strip()
                cmtstr = infolist[3].strip()
                
                if cmtstr:
                    cmt = int(cmtstr)
                
                infolist2 = infolist[2].strip().split('  ')
                author = infolist2[0].strip()
                newstime = infolist2[1].strip()
                
                newstime = newstime.replace('阅读次数','').strip()
                source = source.replace('编辑','').strip()
                
                newstime = datetime.datetime.strptime(newstime,'%Y-%m-%d %H:%M:%S')
                newstxt = ''
                
                for cont in soup('p',attrs={'class':['p','MsoNormal']}):
                    newstxt = newstxt + cont.text.strip()
                newstxt = newstxt.replace('\n','')
    
                dictypename = {1:'新闻中心',2:'慈善福彩'}
                if newskind == 1 :
                    dicnewstype = {1:'重要公告',2:'区内新闻',3:'国内新闻'}
                elif newskind == 2 :
                    dicnewstype = {1:'爱信关注',2:'公益救助',3:'图说公益'}  
                    
                    
            elif prov == '贵州':
                
                soupdiv = soup.find('div',attrs={'id':'newsWDiv'})
                
                titlediv = soupdiv.find('b')
                title = titlediv.text.strip()
                
                infodiv = soupdiv.findAll('td')
                infostr = ''
                for a in infodiv:
                    infostr +=  a.text
                infostr = re.sub('\s','',infostr)
                infolist = infostr.split(':')
                
                newstime = re.sub('\D','',infolist[1])
                
                source = infolist[1].split('2')[0]
                
                cmtstr = infolist[2].strip()
                
                if cmtstr:
                    cmt = int(cmtstr)
                    
                author = ''
                 
                newstime = datetime.datetime.strptime(newstime,'%Y%m%d')
                
                newstxt = ''
                cont = soup.find('div',attrs={'class':'div_newsContent'})
                for cont in cont('p'):
                    newstxt = newstxt + cont.text.strip()
                newstxt = newstxt.replace('\n','')
    
                dictypename = {1:'新闻中心',2:'公益',3:'大奖喜报',4:'投注技巧',5:'信息公开',6:'政策法规',7:'支部园地'}
                if newskind == 1 :
                    dicnewstype = {1:'省内新闻',2:'省外新闻',3:'双色球',4:'福彩3D',5:'七彩乐',6:'快3',7:'彩票文化',8:'中福在线',9:'刮刮乐',10:'福彩公告'}
                elif newskind == 2 :
                    dicnewstype = {1:'温暖贵州',2:'省外公益'}
                elif newskind == 3 :
                    dicnewstype = {1:'其它'}
                elif newskind == 4 :
                    dicnewstype = {1:'其它'}
                elif newskind == 5 :
                    dicnewstype = {1:'其它'}
                elif newskind == 6 :
                    dicnewstype = {1:'其它'}            
                elif newskind == 7 :
                    dicnewstype = {1:'其它'}    
    ##########################################################################################################################################################        
            now = datetime.datetime.now() - datetime.timedelta(days = datedif)
            currdate = newstime
            picname = ''
            picpath = ''
            txtpic = ''
            intro = ''
            province = prov
    #########################insert数据########################################################################################################################
            if (now.year == currdate.year and now.month == currdate.month and now.day == currdate.day) or datedif == -1 :    
                
                conn = MySQLdb.connect(host='.',port = 3306,user='root',passwd='123456',db ='news_info',charset = 'utf8')
                cur = conn.cursor()           
                                
                sql = 'insert into tbl_news_info(title,content,pubtime,newstype,source,typename,webname,newsurl,contenttxt,intro,picpath,picname,txtpic,joincount,author,province) select \'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',%d,\'%s\',\'%s\' from DUAL ' % (title,'',newstime,dicnewstype[newstype],source,dictypename[newskind],'地方新闻',url,newstxt,intro,picpath,picname,txtpic,cmt,author,province)
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
