#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Ziyi Cao
# @Time    : 2021/3/25
# @Function:

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('regions', views.region_list, name='region_list'),
    path('region/<int:id>', views.region_detail, name='region_detail'),
    path('fire/<str:region>/<int:year>', views.fire_detail_by_year, name='fire_detail_by_year'),
    path('fire/<str:region>/<str:fire_type>', views.fire_detail_by_type, name='fire_detail_by_type'),

]
