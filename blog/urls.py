from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.listar, name='listar'),
    url(r'postear/(?P<pk>[0-9]+)/$', views.detalle_pub, name='postear'),
    url(r'^nuevo/$', views.nueva_publicacion, name='nueva_publicacion'),
    url(r'^editar/(?P<pk>[0-9]+)/edit/$', views.editar_publicacion, name='editar_publicacion'),
    url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),

]
