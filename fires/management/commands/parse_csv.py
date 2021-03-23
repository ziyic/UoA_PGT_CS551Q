#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Ziyi Cao
# @Time    : 2021/3/23
# @Function:

from django.db import models
from django.core.management.base import BaseCommand, CommandError
from fires.models import Region, FileType, FileTCC
from pathlib import Path
import pandas as pd
import os


class Command(BaseCommand):
    help = 'Load data from csv files'

    def handle(self, *args, **options):
        Region.objects.all().delete()
        FireType.objects.all().delete()
        base_dir = Path(__file__).resolve().parents[4]
        fire_list = os.listdir(base_dir + '/fires/Files_data/')
        print('reset database')

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

        fire_types = []
        for i in fire_list:
            fire.types.append(i.split('.')[0])
        for type in fire_types:
            fire_type = FileType.objects.create(
                name=type)

            fire_type.save()

        regions = list(Region.objects.all())
        types = list(FireType.objects.all())
        for i in fire_list:
            data = pd.read_csv(i)
            for row in data:
                for region in regions:
                    if region.name == row['COUNTRY']:
                        for years in range(1997, 2015, 1):
                            f_type = i.split('.')[0]
                            for t in types:
                                if f_type == t.type_name:
                                    if f_type == 'Total_Area_Burned':
                                        Fire_TCC.objects.create(
                                            region=region.id,
                                            years=years,
                                            type=t.id,
                                            amount=row[f'Y{years}burned_ha']
                                        )
                                    else:
                                        Fire_TCC.objects.create(
                                            region=region.id,
                                            years=years,
                                            type=t.id,
                                            amount=row[f'Y{years}TCC']
                                        )

        return