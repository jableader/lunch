from django.conf.urls import patterns, include, url
from django.contrib import admin
import lunchapp

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Lunchbox.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', lunchapp.views.home),
    url(r'^api/login', lunchapp.api.auth),
    url(r'^api/gettoken/(?P<client_id>\w+)', lunchapp.api.getToken),
    url(r'^api/canteen/(?P<user_pk>\d+)', lunchapp.api.canteen),
    url(r'^api/kids/(?P<user_pk>\d+)', lunchapp.api.kids),
    url(r'^api/make_order', lunchapp.api.makeOrder),
    url(r'^admin/', include(admin.site.urls)),
)