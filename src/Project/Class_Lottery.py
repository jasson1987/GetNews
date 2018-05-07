# -*- coding:utf-8 -*-
'''
Created on 2018��3��2��

@author: jason
'''
from bs4 import BeautifulSoup as bs
import urllib
import datetime
import MySQLdb
import re
import os
import MySQLdb
import bs4
import sys
reload(sys)
sys.setdefaultencoding('utf8')


class Lottery():
    def __init__(self):
        pass



    def GetNews(self,webname,newskind,newstype):
        url = ''
        #中彩网zhcw
        if webname == 'zhcw':
            if newskind == 1:# '彩种新闻':
                if newstype == 1: #双色球
                    url = 'http://www.zhcw.com/xinwen/caizhongxinwen-ssq/'
                elif newstype == 2:#3D
                    url = 'http://www.zhcw.com/xinwen/caizhongxinwen-3D/'
                elif newstype == 3:#七乐彩
                    url = 'http://www.zhcw.com/xinwen/caizhongxinwenqlc/'
                elif newstype == 4:#其它彩种
                    url = 'http://www.zhcw.com/xinwen/caizhongxinwen-qt/'
                elif newstype == 5:#刮刮乐
                    url = 'http://www.zhcw.com/xinwen/caizhongxinwen-ggl/'
            elif newskind == 2:#机构要闻
                if newstype == 0:#无二级分类
                    url = 'http://www.zhcw.com/xinwen/jigouyaowen/index.shtml?from=xwdh&do=jgyw'
            elif newskind == 3:#地市风采
                if newstype == 0:#无二级分类
                    url = 'http://www.zhcw.com/xinwen/dishifengcai/index.shtml?from=xwdh&do=dsfc'
            elif newskind == 4:#中奖报道
                if newstype == 1:#双色球
                    url = 'http://www.zhcw.com/xinwen/caimingushi/ssq/'
                elif newstype == 2:#3d
                    url = 'http://www.zhcw.com/xinwen/caimingushi/3d/'
                elif newstype == 3:#七乐彩
                    url = 'http://www.zhcw.com/xinwen/caimingushi/qlc/'
            elif newskind == 5:#彩民故事
                if newstype == 0:#无二级分类
                    url = 'http://www.zhcw.com/xinwen/caimingushi/qitacaizhong/'
            elif newskind == 6:#站主之家
                if newstype == 0:#无二级分类
                    url = 'http://www.zhcw.com/xinwen/zhanzhuzhijia/index.shtml'
            elif newskind == 7:#漫趣彩市
                if newstype == 0:#无二级分类
                    url ='http://www.zhcw.com/xinwen/manqucaishi/index.shtml'
            elif newskind == 8:#全球彩风
                if newstype == 0:#无二级分类
                    url = 'http://www.zhcw.com/xinwen/quanqiucaifeng/index.shtml?from=xwdh&do=qqcf'
            elif newskind == 9:#行业数据
                if newstype == 0:#无二级分类
                    url = 'http://www.zhcw.com/xinwen/hangyeshuju/'        
        #新浪sina
        if webname == 'sina':
            if newstype == 1: #彩通观察
                if newstype == 0:#无二级分类
                    url = 'http://roll.sports.sina.com.cn/s_zucai_all/19/index.shtml'
            elif newstype == 2:#国际彩讯
                if newstype == 0:#无二级分类
                    url = 'http://roll.sports.sina.com.cn/s_zucai_all/17/index.shtml'
            elif newstype == 3:#国内彩讯
                if newstype == 0:#无二级分类
                    url = 'http://roll.sports.sina.com.cn/s_zucai_all/7/index.shtml'
            elif newstype == 4:#中奖新闻
                if newstype == 0:#无二级分类
                    url = 'http://roll.sports.sina.com.cn/s_zucai_all/16/index.shtml'    
         
        #网易163
        if webname == '163':
            if newstype == 1: #彩市新闻
                if newstype == 0:#无二级分类
                    url = 'http://cai.163.com/zx/more_news.html'
            elif newstype == 2:#数字大奖
                if newstype == 0:#无二级分类
                    url = 'http://cai.163.com/zx/more_shuZiAward.html'
        
        #中国福彩网cwl
        if webname =='cwl':
            if newskind == 1:# '党建工作':
                if newstype == 1: #党建动态
                    url = 'http://www.cwl.gov.cn/djgz/djdt/'
                if newstype == 2:#理论学习
                    url = 'http://www.cwl.gov.cn/djgz/llxx/'
            elif newskind == 2:#新闻资讯
                if newstype == 1:#新闻动态
                    url = 'http://www.cwl.gov.cn/xwzx/xwdt/'
                if newstype == 2:#派奖促销
                    url = 'http://www.cwl.gov.cn/xwzx/pjcx/'
                if newstype == 3:#大奖速递
                    url = 'http://www.cwl.gov.cn/xwzx/djsd/'
                if newstype == 4:#站主风采
                    url = 'http://www.cwl.gov.cn/xwzx/zzfc/'
                if newstype == 5:#各省资讯
                    url = 'http://www.cwl.gov.cn/xwzx/gszx/'
                if newstype == 6:#媒体声音
                    url = 'http://www.cwl.gov.cn/xwzx/mtsy/'
                if newstype == 7:#环球风采
                    url = 'http://www.cwl.gov.cn/xwzx/hqfc/'        
            elif newskind == 3:#福彩公益
                if newstype == 1:#公益活动
                    url = 'http://www.cwl.gov.cn/fcgy/gyhd/'
                if newstype == 2:#公益金管理
                    url = 'http://www.cwl.gov.cn/fcgy/gyjgl/'
                if newstype == 3:#公益金使用
                    url = 'http://www.cwl.gov.cn/fcgy/gyjsy/'
                if newstype == 4:#公益金筹集
                    url = 'http://www.cwl.gov.cn/fcgy/gyjcj/'
                if newstype == 5:#公益金项目
                    url = 'http://www.cwl.gov.cn/fcgy/gyjxm/'

        return url
    
    
    
    
    
    def GetUrlList(self,webname,url,rerow):
        res = urllib.urlopen(url)
        soup = bs(res,'html.parser')
        if webname == 'zhcw':
            newslist = soup.findAll(attrs={'class':'Nlink'},limit = rerow)
        if webname == 'sina':
            newslist = soup.findAll(attrs={'class':'c_tit'},limit = rerow)
        if webname == '163':
            newslist1 = soup.find(attrs={'class':'zx_list_l'})
            newslist =  newslist1.findAll('li',limit = rerow)
        if webname == 'cwl':
            newslist = soup.findAll(attrs={'class':'list-groupitem'},limit = rerow)
            
        return newslist

            