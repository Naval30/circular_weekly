'''This module is for adding models and fields to the form'''
from django.db import models

class Store(models.Model):
    '''
    This model is for the store her we
    have one store with the store name and a logo.
    '''
    store_name = models.CharField(max_length=128) #Field for storename eg.shop
    store_logo = models.CharField(
        max_length=512,
        null=True,
        blank=True
        )
    objects = models.Manager() # pylint: disable=E1120
    # Field to hold the store logo

    def __unicode__(self):
        return self.store_name

class StoreLocation(models.Model):
    '''
    Each store can have multiple location. so we have
    this module to rapresent this locations.
    '''
    store = models.ForeignKey(Store) #1 store--many location
                                        #but 1 location can have 1  store
    street = models.CharField(max_length=255) #loc addr street ex.200 main str
    city = models.CharField(max_length=64) #field for the city ex.Queens
    state = models.CharField(max_length=2) #field for the state ex.NY
    zip_code = models.CharField(max_length=5, null=True, blank=True)
     #zipcode ex.11385

    def __unicode__(self):
        return u'%s\n%s, %s, %s' % (self.street, self.city,
                                    self.state, self.zip_code)

class Product(models.Model):
    '''
    Model for the different products that are on discount.
    One product can be in discount on more the one store
    and at more them one location.
    Will need to cerate relation table for this.
    '''
    store_location = models.ManyToManyField(StoreLocation)
    product_name = models.CharField(max_length=512)
    discount_price = models.CharField(max_length=512)
    start_date = models.DateField("Deal started date:", null=True, blank=True)
    end_date = models.DateField("Deal expier date:")
    notes = models.CharField(max_length=512, null=True, blank=True)
    description = models.CharField(max_length=512, null=True, blank=True)
    product_picture = models.CharField(max_length=512, null=True, blank=True)

    def __unicode__(self):
        return self.product_name
