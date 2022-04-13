from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'panel/subcategory/list/$', views.subcat_list, name='subcat_list'),
    re_path(r'panel/subcategory/add/$', views.subcat_add, name='subcat_add'),
]