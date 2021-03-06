#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Ziyi Cao
# @Time    : 2021/3/23
# @Function:

# from django.db import models
import types

from django.core.management.base import BaseCommand, CommandError
from fires.models import Region, FireType, FireTCC
from pathlib import Path
import pandas as pd
import os


class Command(BaseCommand):
    help = 'Load data from csv files'

    def handle(self, *args, **options):
        Region.objects.all().delete()
        FireType.objects.all().delete()
        base_dir = Path(__file__).resolve().parents[3]
        fire_list = os.listdir(str(base_dir) + '/fires/Fires_data/')
        print('reset database')

        regions_data = pd.read_csv(str(base_dir) + '/fires/Fires_data/Total_Area_Burned.csv')
        for i in range(0, len(regions_data)):
            region = Region.objects.create(
                name=regions_data.iloc[i]['COUNTRY'],
                ISOCODE=regions_data.iloc[i]['ISOCODE'],
                UNSDCODE=regions_data.iloc[i]['UNSDCODE'],
                CIESINCODE=regions_data.iloc[i]['UNSDCODE'],
                Area_sqkm=float(regions_data.iloc[i]['Area_sqkm'].replace(',', '')))
        print("region table parsed")

        region_population_data = pd.read_csv(str(base_dir) + '/fires/Fires_data/TCC_All_fires.csv')
        for i in range(0, len(region_population_data)):
            pop = region_population_data.iloc[i]['country_pop'].replace(',', '')
            Region.objects.filter(name=region_population_data.iloc[i]['COUNTRY']).update(Population=int(pop))
        print("region table updated")

        fire_types = []
        for i in fire_list:
            fire_types.append(i.split('.')[0])
        for t in fire_types:
            fire_type = FireType.objects.create(type_name=t)
        print("fire type table parsed")

        regions = list(Region.objects.all())
        f_types = list(FireType.objects.all())
        for i in fire_list:
            data = pd.read_csv(str(base_dir) + '/fires/Fires_data/' + i)
            f_type = types.SimpleNamespace()
            for t in f_types:
                if i.split('.')[0] == t.type_name:
                    f_type.id = t.id
                    f_type.type_name = t.type_name
                    for r in range(0, len(data)):
                        for region in regions:
                            if region.name == data.iloc[r]['COUNTRY']:
                                fire_region = region
                                for years in range(1997, 2015+1, 1):
                                    if f_type.type_name == 'Total_Area_Burned':
                                        amount = data.iloc[r][f'Y{years}burned_ha']
                                        t = FireType(id=f_type.id, type_name=f_type.type_name)
                                        fire = FireTCC.objects.create(
                                            region=fire_region,
                                            year=years,
                                            type=t,
                                            amount=float(amount.replace(',', '') if str(amount) != 'nan' else 0))
                                    else:
                                        amount = data.iloc[r][f'Y{years}TCC']
                                        t = FireType(id=f_type.id, type_name=f_type.type_name)
                                        fire = FireTCC.objects.create(
                                            region=fire_region,
                                            year=years,
                                            type=t,
                                            amount=float(amount.replace(',', '') if str(amount) != 'nan' else 0))
        print('fire table parsed')
        print('reset database finished')
        return
