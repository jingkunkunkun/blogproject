#!_*_coding:utf-8_*_
# Author:Jingkun
from django.urls import path

from . import views

app_name = 'comments'
urlpatterns = [
    path('comment/<int:post_pk>', views.comment, name='comment'),
]
