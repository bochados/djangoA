from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.listar),
    url(r'postear/(?P<pk>[0-9]+)/$', views.detalle_pub, name='postear'),
    url(r'^nuevo/$', views.nueva_publicacion, name='nueva_publicacion'),
    url(r'^editar/(?P<pk>[0-9]+)/edit/$', views.editar_publicacion, name='editar_publicacion'),
]
