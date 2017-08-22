from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^(?P<id>[0-9]+)$', views.article, name='article'),
    url(r'^edit/(?P<id>[0-9]+)*$', views.edit, name='edit'),
    url(r'^edit/action/(?P<id>[0-9]+)*$', views.edit_action, name='edit_action'),
]