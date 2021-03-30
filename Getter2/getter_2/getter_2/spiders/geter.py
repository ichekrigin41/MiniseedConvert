
from urllib.parse import urlparse 
import scrapy

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from scrapy.http import Request


# start_urls = ["http://seismic.p3volc.keenetic.pro/archive/2021/03/"]





class DownloaderMNSD(CrawlSpider):
    name ='MNSD'
    allowed_domains=['seismic.p3volc.keenetic.pro']
    start_urls = ["http://seismic.p3volc.keenetic.pro/archive/2021/"]

    rules=(
        Rule(LinkExtractor(allow=r'2021/'),callback='parse_item',follow=True),
    )

   

    def file_path(self, request, response=None, info=None):
     file_name: str = request.url.split("/")[-1]
     return file_name


    def parse_item(self,response):
        item={}

        file_url=response.css('a::attr(href)').get()
        file_url = response.urljoin(file_url)
        file_extension = file_url.split('.')[-1]
        if file_extension not in('.miniseed'):
            return
        item = ZipfilesItem()
        item['file_urls'] = [file_url]
        item['original_file_name'] = file_url.split('/')[-1]
        #wget.download(item,'/home/zoohan/Desktop/cnvrt/Getter2/getter_2/getter_2/Downloaded')
        yield item
        print("RESPONSE",response)
      




links=[]



class AllSpider(scrapy.Spider):


    name = 'all'

    start_urls = ['http://seismic.p3volc.keenetic.pro/archive/2021/03/']

    def __init__(self):
        self.links=[]

    def parse(self, response):
        page=response.url.split("/")[-2]
        filename=f'all-{page}.html'
       

        self.links.append(response.url)
        for href in response.css('a::attr(href)'):
            yield response.follow(href, self.parse)
            with open(filename, 'wb') as f:
                f.write(response.body)
                '''