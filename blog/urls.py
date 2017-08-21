from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^/(?P<id>[0-9]+)', views.article, name='article'),
]