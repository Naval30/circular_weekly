'''
This module will hold all the items that are used by the spiders
'''

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Field
from scrapy.contrib.djangoitem import DjangoItem
from circular.models import Product
from circular.models import Store
from circular.models import StoreLocation

class StopandshopItem(DjangoItem):
    '''
    This item are imported from the django model for the Product
    '''
    django_model = Product
    store_location = Field()
    store_name = Field()

class ShoplocalItem(DjangoItem):
    '''
    This item are imported form django model Store
    '''
    django_model = Store

class StoreLocationItem(DjangoItem):
    '''
    This item are imported form django medol StoreLocation
    '''
    django_model = StoreLocation
