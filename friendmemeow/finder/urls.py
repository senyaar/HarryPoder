from django.conf import settings
from django.conf.urls import patterns, include, url,static
from . import views


urlpatterns = patterns('',
    url(r'^$', views.ready_cats),
    url(r'^kitty/(?P<pk>[0-9]+)/$', views.cat_detail),
    url(r'^kitty/add/$', views.cat_form, name='add_cat'),
    url(r'^kitty/(?P<pk>\d+)/edit/$', views.cat_form, name='edit_cat'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
) + static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'%s(?P<path>.*)' % settings.MEDIA_URL[1:], 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )