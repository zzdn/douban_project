#_*_coding:utf-8_*_
from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r"^login",Logins.as_view()),
    url(r"^register$", register),
    url(r"^db_movie$", db_movie),
    # url(r"^index", index),
]