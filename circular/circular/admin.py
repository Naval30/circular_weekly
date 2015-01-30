'''This module is for registering models'''
from django.contrib import admin
#from circular.models import Profile
from circular.models import Store
from circular.models import StoreLocation
from circular.models import Product

class StoreLocationInLine(admin.TabularInline): # pylint: disable=R0901
    '''This class is to register StoreLocationInLine'''
    model = StoreLocation
    extra = 0

class StoreAdminInLine(admin.TabularInline): # pylint: disable=R0901
    '''This class is to register StoreAdminInLine'''
    model = Store
    extra = 0

class StoreLocationAdmin(admin.ModelAdmin): # pylint: disable=R0904
    '''This class is to register StoreLocationAdmin'''
    fieldsets = [
        (None, {'fields': ['store']}),
        ('Store Locations:', {'fields': ['street', 'city',
                                         'state', 'zip_code']}),
    ]
    list_filter = ['store']

class StoreAdmin(admin.ModelAdmin): # pylint: disable=R0904
    '''This class is to register StoreAdmin'''
    fieldsets = [
        ('Store information', {'fields': ['store_name', 'store_logo'],}),
    ]
    list_display = ['store_name', 'store_logo',]
    inlines = [StoreLocationInLine]

class ProductAdmin(admin.ModelAdmin): # pylint: disable=R0904
    '''This class is to register ProductAdmin'''
    #filter_vertical = ('store_location',)
    filter_horizontal = ('store_location',)

# Register your models here.
#admin.site.register(Profile)
admin.site.register(Store, StoreAdmin)
admin.site.register(StoreLocation, StoreLocationAdmin)
admin.site.register(Product, ProductAdmin)
