# -*- coding:utf-8 -*-
'''
Created on 2018-3-27

@author: jason
'''

from Main_Province import GetProvNews
from Main import GetWebNews
from Func import ImportExcel





#地方新闻

'''    DicProvince={1:'黑龙江',2:'内蒙古',3:'陕西', 4:'杭州', 5:'天津', 6:'北京', 7:'河北', 8:'辽宁', 9:'吉林',10:'江苏',
                    11:'浙江',12:'安徽',13:'福建',14:'江西',15:'河南',16:'深圳',17:'广东',18:'广西',19:'海南',20:'重庆',
                    21:'四川',22:'云南',23:'甘肃',24:'青海',25:'宁夏',26:'湖北',27:'湖南',28:'新疆',29:'贵州'}
'''
#各省份新闻
lotpro = GetProvNews()
try:
    lotpro.GetNewProv([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18])
    print 'Import Province News Successfully'
except:
    print 'Import Province News Fail'
       
    
#门户网站新闻
lot = GetWebNews()
try:
    lot.GetNewWeb(['中彩','新浪','网易','中国福彩','凤凰网','彩客网','新华网','搜狐网','500彩票网'], -1, 20)
    print 'Import Web News Successfully'
except:
    print 'Import Web News Fail'
        
#输出Excel
ImportExcel()


# lotpro = GetProvNews()
# lotpro.GetNewProv([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18])


# lot = GetWebNews()
# lot.GetNewWeb(['中彩','新浪','网易','中国福彩','凤凰网','彩客网','新华网','搜狐网','500彩票网'], -1, 20)
# lot.GetNewWeb(['中彩'], -1, 1)