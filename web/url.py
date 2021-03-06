from django.conf.urls import url
from django.contrib import admin
from web import views
urlpatterns = [
    url(r'^$', views.index, name='list'),
    url(r'^cat/(?P<cat_name>[\w-]+)$', views.category, name = 'category'),
    url(ur'^(?P<title>[\w-]+)$', views.page, name = 'page'),
]
