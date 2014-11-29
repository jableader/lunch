from django.conf.urls import patterns, include, url
from django.contrib import admin
import lunch

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Lunchbox.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', lunch.views.home),
    url(r'^api/login', lunch.api.auth),
    url(r'^api/canteen/(?P<user_pk>\d+)', lunch.api.canteen),
    url(r'^api/kids/(?P<user_pk>\d+)', lunch.api.kids),
    url(r'^api/make_order', lunch.api.makeOrder),
    url(r'^admin/', include(admin.site.urls)),
)
