'''
Here we will have all the helper function that we use with the scraper tool.
'''
import datetime
import re
import os
import csv
from time import strptime

from circular.models import Product
from circular.models import Store
from circular.models import StoreLocation

def deal_valid(valid):
    '''
    This function take a string and return the date that
    the deal is valid for.
    '''
    year = datetime.date.today().year
    case = ['valid from', 'deal expires today', 'deal expires in']
    valid = valid.lower()
    start_date = None

    if re.match(case[0], valid):
        got = valid.split()
        start_date = datetime.date(year,
                                   strptime(got[2][0:3], '%b').tm_mon,
                                   strptime(got[3], '%d').tm_mday)
        end_date = datetime.date(year,
                                 strptime(got[5][0:3], '%b').tm_mon,
                                 strptime(got[6], '%d').tm_mday)
    elif re.match(case[1], valid):
        end_date = datetime.date.today()
    elif re.match(case[2], valid):
        got = valid.split()
        end_date = datetime.date.today() + datetime.timedelta(int(got[3]))
    try:
        end_date
    except:
        raise TypeError("No expiration date can be found for this deal.")

    return [start_date, end_date]

def check_product_in_db(data_item):
    '''
    This function check if we already have the product in the database.
    If the product is in the database it will return False
    If the product can't be found in the database will return True.
    It takes 1 item type impout.
    '''
    products = None
    on_db = False
    counter = Product.objects.filter(
        product_name=data_item['product_name']
        ).count()
    if counter == 0:
        on_db = True
    else:
        products = Product.objects.get(product_name=data_item['product_name'])
        if (data_item['product_name'] == products.product_name and
                data_item['discount_price'] == products.discount_price and
                data_item['notes'] == products.notes):
            on_db = False
    return [on_db, products]

def check_store_in_db(data_item):
    '''
    This function check if we already have the sotre in the database.
    If the store is in the database it will return False
    If the store can't be found in the database will return True.
    It takes 1 item type impout.
    '''
    counter = Store.objects.filter(store_name=data_item['store_name']).count()
    if counter == 0:
        on_db = True
    else:
        on_db = False
    return on_db

def check_store_location(data_item):
    '''
    This helper function is used to check if a store is in the
    database and if is just return the store. If it is not
    will insert the store location in the database and return
    the store.
    '''
    location = data_item['store_location']
    counter = StoreLocation.objects.filter(
        street=location['street'],
        city=location['city'],
        state=location['state']).count()
    if counter == 0:
        location = StoreLocation(
            store_id=Store.objects.get(store_name=data_item['store_name']).id,
            street=location['street'],
            city=location['city'],
            state=location['state'],
            zip_code=location['zip_code'])
        location.save()
    else:
        location = StoreLocation.objects.get(
            street=location['street'],
            city=location['city'],
            state=location['state'])
    return location

def get_zipcode(data_item):
    '''
    This fuction will check that we are puting the correct zip code in the
    address if the zip code cant be found we will use None.
    '''
    base_path= os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_path,'zips.csv')
    zip_true = False

    data = csv.reader(open(file_path), delimiter=',')
    for row in data:
        if row[3].lower() == data_item['state'].lower():
            if row[1].lower() == data_item['city'].lower():
                zip_true = True
                zip_code = row[0]
            elif re.search(data_item['city'].lower(), str(row[2]).lower()):
                zip_true = True
                zip_code = row[0]
    if zip_true == False:
        zip_code = None
    return zip_code
