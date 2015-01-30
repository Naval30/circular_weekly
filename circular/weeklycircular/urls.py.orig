'''
This is the main uarls file
'''

from django.conf.urls import patterns, include, url

from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static
admin.autodiscover()

urlpatterns = patterns(  # pylint: disable=C0103
    '',
    url(r'^password_change/$',
        'django.contrib.auth.views.password_change',
        {}, name='password_change'),
    url(r'^password_change_done/$',
        'django.contrib.auth.views.password_change_done',
        {}, name='password_change_done'),
    url(r'^password_reset/$',
        'django.contrib.auth.views.password_reset',
        {}, 'password_reset'),
    url(r'^password_reset_done/$',
        'django.contrib.auth.views.password_reset_done',
        {}, 'password_reset_done'),
    url(r'^password_reset_confirm/(?P<uidb64>.+)/(?P<token>.+)/$',
        'django.contrib.auth.views.password_reset_confirm',
        {}, 'password_reset_confirm'),
    url(r'^password_reset_complete/$',
        'django.contrib.auth.views.password_reset_complete',
        {}, 'password_reset_complete'),
    url(r'^accounts/profile/', include('userprofile.urls')),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'circular.views.home', name='home'),
    url(r'^about/$', 'circular.views.about', name='about'),
    url(r'^contact/$', 'circular.views.contact', name='contact'),
    url(r'^deals/$', 'circular.views.deals', name='deals'),
    url(r'^recipe/$', 'recipe.views.get_recipe', name='recipe'),
    url(r'^deals/(?P<store_id>[0-9]+)/$',
        'circular.views.store_locations',
        name='locations'),
    url(r'^deals/(?P<store_id>[0-9]+)/(?P<location_id>[0-9]+)/$',
        'circular.views.products',
        name='products'),
)

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT)
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)
