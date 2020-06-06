from django.conf.urls import re_path
from django.urls import path
from . import views

app_name = 'wordcount'
urlpatterns = [
    re_path(r'^$', views.homepage, name='index'),
    # ex: /polls/5
    # re_path(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    path('home/', views.homepage, name='home'),
    path('count/', views.count, name='count'),
    path('about/', views.about, name='about'),
]
