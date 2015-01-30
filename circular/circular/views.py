'''
  This module displays all the information of deals,
  stores and products of each store
'''
from django.shortcuts import render_to_response
from django.shortcuts import RequestContext
from circular.models import Product
from circular.models import Store
from circular.models import StoreLocation
from circular.utils import make_list

def home(request):
    '''
    This view is to display link to index/ home page.
    '''
    return render_to_response("index.html",
                              locals(),
                              context_instance=RequestContext(request)
                             )
def about(request):
    '''
    This view is to display link to about page.
    '''
    return render_to_response("about.html",
                              locals(),
                              context_instance=RequestContext(request)
                             )
def contact(request):
    '''
    This view is to display link to contact page.
    '''
    return render_to_response("contact.html",
                              locals(),
                              context_instance=RequestContext(request)
                             )
def deals(request):
    '''
    This view will be used in the deals page to display the different stores
    the store location and the products for each store.
    '''
    store = Store.objects.all()#.order_by('store_name')
    stores = make_list(db_object=store, numberc=3)
    #stores_count = stores.count()
    #store_locations = StoreLocation.objects.prefetch_related('store')
    #products = Product.objects.all()
    data = {
        'stores': stores,
        #'locations': store_locations,
        #'products': products,
        #'store_count': stores_count
        }
    return render_to_response("deals_tmp.html",
                              data,
                              context_instance=RequestContext(request)
                             )

def store_locations(request, store_id):
    '''
    This view is to display store locations.
    '''
    store = Store.objects.get(id=store_id)
    location = StoreLocation.objects.filter(store_id=store_id) # pylint: disable=E1101
    locations = make_list(db_object=location, numberc=3)
    data = {
        'store_name': store.store_name,
        'locations': locations,
        }
    return render_to_response("store_location_tmp.html",
                              data,
                              context_instance=RequestContext(request)
                             )

def products(request, store_id, location_id):
    '''
    This view is to display the products.
    '''
    store = Store.objects.get(id=store_id)
    location = StoreLocation.objects.get(id=location_id) # pylint: disable=E1101
    product = Product.objects.filter(store_location=location_id) # pylint: disable=E1101
    products = make_list(db_object=product, numberc=3) # pylint: disable=W0621
    data = {
        'store_name': store.store_name,
        'location': location,
        'products': products,
    }
    return render_to_response("products.html",
                              data,
                              context_instance=RequestContext(request)
                             )
