'''
# Define your data pipelines here
#
# Don't forget to add your pipeline to the DATA_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/data-pipeline.html
'''
from getdata.utils import check_product_in_db
from getdata.utils import check_store_in_db
from getdata.utils import check_store_location
from scrapy.exceptions import DropItem

class GetdataProductPipeline(object):
    '''
    Module that will pipeline the items form the spiders
    from the diffrent stores.
    '''
    def process_item(self, item, spider):
        '''
        This is where the item get processed
        '''
        if spider.name in ['stopandshop', 'aldi']:
            location = check_store_location(item)
            if check_product_in_db(item)[0] == False:
                check_product_in_db(item)[1].store_location.add(location)
                raise DropItem("Product  %s is already in the\
                               database. Skipping" % item)
            else:
                try:
                    item.save(commit=False)
                except:
                    raise DropItem
                finally:
                    product = item.save()
                    product.store_location.add(location)
        return item

class GetdataStorePipeline(object):
    '''
    Module that will pipeline the items for the store names
    and the store logos
    '''
    def process_item(self, item, spider):
        '''
        This is where the items from the shoplocal spider get
        processed.
        '''
        if spider.name == "shoplocal":
            if check_store_in_db(item) == False:
                raise DropItem("Store  %s is already in\
                               the database. Skipping" % item)
            else:
                try:
                    item.save(commit=False)
                except:
                    raise DropItem
                finally:
                    item.save()
        return item
