
from urllib.parse import urlparse 
import scrapy
import wget

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from scrapy.http import Request


#scrapy crawl test -o test.csv




class BlogSpider(scrapy.Spider):
    name = 'miniseedGetter'
    start_urls = [
        'http://seismic.p3volc.keenetic.pro/archive/2021/01',
        'http://seismic.p3volc.keenetic.pro/archive/2021/02',
        'http://seismic.p3volc.keenetic.pro/archive/2021/03',
        'http://seismic.p3volc.keenetic.pro/archive/2021/04',
    ]

    def __init__(self):
        self.links=[]

    def parse(self, response):
        self.links.append(response.url)
        for href in response.css('a::attr(href)'):
            yield { '' : href.get()}


#To RUN script Type: #scrapy crawl miniseedGetter -o scraped.csv (in CMD)