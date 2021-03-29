import scrapy


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
                