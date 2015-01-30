'''
This is the spider that we use to scrape data from www.shoplocal.com.
I will scrape only data for one store and one store location
'''

from scrapy.selector import Selector
from scrapy.spider import Spider
from scrapy.http import Request
from getdata.items import ShoplocalItem


class ShoplocalSpider(Spider):
    '''
    ShoplocalSpider is the CrawlSpider class that is use to scrape data for
    one of the Stores names and logs.
    '''

    name = 'shoplocal'
    allowed_domains = ['shoplocal.com']
    start_urls = ['http://www.shoplocal.com/']

    def parse(self, response):
        sel = Selector(response)
        data = sel.xpath('//article[@class="sl_weekly_ads clearfix cb"\
                         ]//a/@href').extract()
        for i in range(len(data)):
            name = sel.xpath('//article[@class="sl_weekly_ads clearfix cb"\
                             ]//div[@class="tile_primary"]/text()').extract()
            link = self.start_urls[0] + data[i]
            request = Request(link, callback=self.parse_store)
            request.meta['store'] = name[i]
            yield request

    def parse_store(self, response):
        '''
        Here is where we do the data exstraction.
        '''
        sel = Selector(response)
        store = ShoplocalItem()
        data_logo = sel.xpath('//div[@class="sl_retailerpage_logo fl"\
                              ]/img/@src').extract()[0]
        store['store_logo'] = data_logo
        store['store_name'] = response.request.meta['store']
        return store
    