from django.conf import settings
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView


from . import views
from rest_framework import routers

class HomeView(TemplateView):
    template_name = "finder/ready_cats.html"

router = routers.DefaultRouter()
router.register(r'kitty', views.CatList)
router.register(r'shelters', views.ShelterList)


urlpatterns = patterns('',
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^kitty/(?P<pk>[0-9]+)/$', views.CatDetail),
    url(r'^$', HomeView.as_view()),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'%s(?P<path>.*)' % settings.MEDIA_URL[1:], 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )