'''
This is the spider that we use to scrape data from www.shoplocal.com.
I will scrape only data for one store and one store location
'''

from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.http import Request
from getdata.items import StopandshopItem
from getdata.items import StoreLocationItem
from getdata.utils import deal_valid
from getdata.utils import get_zipcode

class AldiSpider(CrawlSpider):
    '''
    StopandshopSpider is the CrawlSpider class that is use to scrape data for
    one of the Stopandshop stores.
    '''

    name = 'aldi'
    allowed_domains = ['shoplocal.com']

    def __init__(self, zip_code='', *args, **kwargs):
        super(AldiSpider, self).__init__(*args, **kwargs)
        self.start_urls = ['http://www.shoplocal.com/',
                           'http://www.shoplocal.com/changelocation?citystatezip=%s' % zip_code]

    rules = (
        Rule(SgmlLinkExtractor(allow=r'aldi/weekly-ads-sales/'),
             callback='parse_main_page', follow=True),
    )

    def parse_main_page(self, response):
        '''
        parse_main_page parse the page http://www.shoplocal.com/ and return
        all links that include:
        1. stop-and-shop/weekly-ads-sales/
        2. promotionpagenumbers
        '''
        sel = Selector(response)

        main_data = sel.xpath('//a/@href').extract()
        for link in main_data:
            if 'aldi/weekly-ads-sales/' in link and\
            'promotionpagenumbers' in link:
                link = self.start_urls[0] + link
                yield Request(link, callback=self.parse_deals_links)

    def parse_deals_links(self, response):
        '''
        parse_deals_links parse all links returned by parse_main_page and
        extract likns that under the <div class="sl_deal_tile"> the extracted
        links will be procesed through parse_prduct.
        '''
        sel = Selector(response)

        location = StoreLocationItem()

        hold = sel.xpath('//div[@class="sl_retailer_info fl"]')
        city_state = hold.xpath('//span[@class="sl_retailer_address2"]/text()')\
        .extract()[0].strip().split(',')
        location['street'] = hold.xpath('//span[@class="sl_retailer_address1"]\
                                        /text()').extract()[0].strip()
        location['city'] = city_state[0]
        location['state'] = city_state[1].strip()
        location['zip_code'] = get_zipcode(location) #self.start_urls[1].split('=')[1]

        deal_data = sel.xpath('//div[@class="sl_deal_tile"]//a/@href').extract()
        for link in deal_data:
            link = self.start_urls[0] + link
            request = Request(link, callback=self.parse_product)
            request.meta['store_location'] = location
            yield request

    def parse_product(self, response):
        '''
        Parse_product get the data from the parse_deals_links and extract
        the data that we need.
        '''
        sel = Selector(response)

        data = StopandshopItem()
        data['store_location'] = response.request.meta['store_location']
        data['store_name'] = 'Aldi'
        product = sel.xpath('//article[@class="sl_detail_left clearfix"]')
        data['product_name'] = product.xpath('//h1[@class="sl_detail_title"\
                                             ]/text()').extract()[0].strip()
        data['discount_price'] = product.xpath('//div[@class="sl_detail_dealdesc"]/text()').extract()[0].strip()
        picture = product.xpath('//img[@class="sl_detail_image"]/@src')\
        .extract()
        if len(picture) > 0:
            data['product_picture'] = picture[0].strip()
        else:
            data['product_picture'] = None
        [data['start_date'], data['end_date']] = deal_valid(
            product.xpath('//div[@class="sl_detail_dates"]/text()')\
            .extract()[0].strip())
        description = product.xpath('//div[@class="sl_detail_description"\
                                    ]/text()').extract()
        if len(description) > 0:
            data['description'] = description[0].strip()
        else:
            data['description'] = None
        notes = product.xpath('//div[@class="sl_detail_price_qualifier"]/text()')\
        .extract()
        if len(notes) > 0:
            data['notes'] = notes[0].strip()
        else:
            data['notes'] = None
        return data
    