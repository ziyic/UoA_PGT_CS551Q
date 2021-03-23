#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Ziyi Cao
# @Time    : 2021/3/23
# @Function:

from django.db import models
from django.core.management.base import BaseCommand, CommandError
from fires.models import Region
from pathlib import Path
import pandas as pd


class Command(BaseCommand):
    help = 'Load data from csv files'

    def handle(self, *args, **options):
        Region.objects.all().delete()
        print('reset database')

        base_dir = Path(__file__).resolve().parents[4]
        regions_data = pd.read_csv(base_dir + '/fires/Files_data/Total_Area_Burned.csv')
        for row in regions_data:
            region = Region.objects.create(
                name=row['COUNTRY'],
                ISOCODE=row['ISOCODE'],
                UNSDCODE=row['UNSDCODE'],
                CIESINCODE=row['UNSDCODE'],
                # Population=row['Population'],
                Area_sqkm=row['Area_sqkm'],
            )
            region.save()

        return
