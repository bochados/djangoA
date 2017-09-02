from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.listar),
    url(r'postear/(?P<pk>[0-9]+)/$', views.detalle_pub, name='postear'),
]
