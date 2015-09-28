import scrapy
from newalbums_scraper.items import NewalbumsItem

class newalbums_spider(scrapy.Spider):
    name = "newalbums"
    allowed_domains = ["newalbumreleases.net"]
    start_urls = [
        "http://newalbumreleases.net/category/electronic/"
    ]

    # Objective:
    # Crawl X pages to obtain Y albums of Style = ""

    # parse(): 
    # 1. parse response data
    # 2. extract scraped data (as scraped items) and more URLs to follow.
    def parse(self, response):
        for sel in response.xpath("//div[@class='single']/div[@class='cover']/div[@class='entry']/p[@align='center']"):
            item = NewalbumsItem()
            desc = sel.xpath('font//text()').extract() 
            # item['artist'] = 
            # item['album_name']= 
            # item['style']= 
            # yield item
        #NOTE: Only 1 artist info printed. Index out of range @ [15]
        print desc
        # p = 0
        #NOTE: Only 1 artist info printed. Index out of range @ [15]
        # for i in desc:
        #     print '%d: %s' % (p, i)
        #     p+=1
        #Create a local .html file with returned HTML response. 
        # filename = response.url.split("/")[-2] + '.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)