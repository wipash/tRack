from django.conf.urls import patterns, include, url
from track.views import track_main
from track.trackapp.views import trackapp_main
from django.contrib import admin
admin.autodiscover()



# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    ('^$', trackapp_main),
    ('^admin/', include(admin.site.urls)),
    # Examples:
    # url(r'^$', 'track.views.home', name='home'),
    # url(r'^track/', include('track.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
