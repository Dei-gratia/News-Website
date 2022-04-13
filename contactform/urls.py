from unicodedata import name
from django.urls import re_path
from . import views

urlpatterns = [
    #re_path(r'^about/$', views.about, name='about'),
    re_path(r'^contact/submit/$', views.contact_add, name='contact_add'),
    re_path(r'^panel/contactform/$', views.contact_show, name='contact_show'),
    re_path(r'^panel/contactform/del/(?P<pk>\d+)/$', views.contact_del, name='contact_del'),
    
]