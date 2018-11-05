#_*_coding:utf-8_*_
from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r"^login", login),
    url(r"^register$", register),
]