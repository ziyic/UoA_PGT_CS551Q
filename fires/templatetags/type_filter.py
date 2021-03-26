#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Ziyi Cao
# @Time    : 2021/3/26
# @Function:

from django import template

from fires.models import FireType

register = template.Library()


@register.filter(is_safe=True)
def fire_type(value):
    f_type = FireType.objects.filter(id=value)
    return f_type.type_name
