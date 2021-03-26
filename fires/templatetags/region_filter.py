#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Ziyi Cao
# @Time    : 2021/3/26
# @Function:

from django import template

from fires.models import Region

register = template.Library()


@register.filter(is_safe=True)
def region_id_to_name(value):
    region = Region.objects.filter(id=value)
    return region.type_name
