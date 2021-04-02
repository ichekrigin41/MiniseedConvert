
from urllib.parse import urlparse 
import scrapy
import wget

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from scrapy.http import Request





class BlogSpider(scrapy.Spider):
    name = 'test'
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