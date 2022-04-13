from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'news/(?P<word>.*)/$', views.news_detail, name='news_detail'),
    re_path(r'panel/news/list/$', views.news_list, name='news_list'),
    re_path(r'panel/news/add/$', views.news_add, name='news_add'),
    re_path(r'panel/news/del/(?P<pk>\d+)/$', views.news_delete, name='news_delete'),
    re_path(r'panel/news/edit/(?P<pk>\d+)/$', views.news_edit, name='news_edit'),
    
]