from django.conf import settings
from django.conf.urls import patterns, include, url,static

from . import views


urlpatterns = patterns('',
    url(r'^$', views.ready_cats),
    url(r'^kitty/(?P<pk>[0-9]+)/$', views.cat_detail),
    url(r'^kitty/add/$', views.add_cat, name='add_cat'),
    url(r'^kitty/(?P<pk>[0-9]+)/edit/$', views.edit_cat, name='edit_cat'),
) + static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

