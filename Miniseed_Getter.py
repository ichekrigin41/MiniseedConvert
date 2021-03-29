from datetime import datetime,timedelta,date
import os
import wget
import scrapy

'''
#today.strftime('%Y%m%d')
today=datetime.now()

y=(today.strftime('%Y'))
m=(today.strftime('%m'))
d=(today.strftime('%d'))
H=(today.strftime('%H'))



H1=[f'{str(index):0>2.2}' for index in range(0,24)]

file_URL="http://seismic.p3volc.keenetic.pro/archive/"+y+"/"+m+"/"+"IV.KRMSH_centaur-6_7618_"+y+m+d+"_"+H+"0000.miniseed"
file_NAME="IV.KRMSH_centaur-6_7618_"+y+m+d+"_"+H+"0000.miniseed"

#temp_file_URL="http://seismic.p3volc.keenetic.pro/archive/"+y+"/"+m+"/"+"IV.KRMSH_centaur-6_7618_"+y+m+d+"_"+H1[]+"0000.miniseed"


path="/home/zoohan/Desktop/cnvrt/KRMSH"

os.mkdir(path+y+m+d)
os.chdir(path+y+m+d)

start_date=date(2021,3,1)
end_date=date(2021,3,29)

#delta=timedelta(days=1)
#while start_date <=end_date:
   # wget.download(file_URL,path+y+m+d)

for i, val in enumerate(H1):
    temp_file_URL="http://seismic.p3volc.keenetic.pro/archive/"+y+"/"+m+"/"+"IV.KRMSH_centaur-6_7618_"+y+m+d+"_"+H1[i]+"0000.miniseed"    
    wget.download(temp_file_URL,path+y+m+d)
    i=i+1




#wget.download(file_URL,path+y+m+d)



print(y,m,d,H)
print(file_URL)
print(file_NAME)
'''
'''

class BlogSpider(scrapy.Spider):
    name='blogspider'
     start_urls = ['http://seismic.p3volc.keenetic.pro/archive/2021/']

    def __init__(self):
        self.links[]

    def parse(self, response):
        self.links.append(response.url)
        for href in response.css('a::attr(href)'):
            yield response.follow(href, self.parse)
    
'''

