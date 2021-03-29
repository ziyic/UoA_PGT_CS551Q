#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Ziyi Cao
# @Time    : 2021/3/26
# @Function:

from django import template
from django.shortcuts import get_object_or_404

from fires.models import FireType

register = template.Library()


@register.filter(is_safe=True)
def fire_type(value):
    f_type = get_object_or_404(FireType, id=value.id)
    return f_type.type_name
