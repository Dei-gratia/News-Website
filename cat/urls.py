from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'panel/category/list/$', views.cat_list, name='cat_list'),
    re_path(r'panel/category/add/$', views.cat_add, name='cat_add'),
]