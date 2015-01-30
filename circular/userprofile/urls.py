'''
Local file for the links to the user profile.
This is called int he main urls file of the project.
'''
from django.conf.urls import patterns, url

from userprofile import views

urlpatterns = patterns(  # pylint: disable=C0103
    '',
    url(r'^edit/$',
        views.update_profile,
        name='userprofile_edit_profile'),
    url(r'^$',
        views.ditail_profile,
        name='userprofile_ditail_profile'),
)
