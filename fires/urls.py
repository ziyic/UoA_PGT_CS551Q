#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Ziyi Cao
# @Time    : 2021/3/25
# @Function:

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('regions', views.region_list),
    path('region/<int:id>', views.region_detail),
    path('fire/<str:region>/<int:id>'),
    path('fire/<str:region>/<str:type>'),



    # path('fire/<int:id>')
    # https://fire.heroku.com/region/<int:id>/fire/<int:id>
    # https://fire.heroku.com/fire/<str:region>/<int:year
]
