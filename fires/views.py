from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Region, FireTCC


def index(request):
    title = 'Global Fire Emissions'
    return render(request, 'fires/index.html', {'title': title})


def region_list(request):
    regions = Region.objects.all()
    return render(request, 'fires/regions.html', {'regions': regions})


def region_detail(request, id):
    region = get_object_or_404(Region, id=id)
    return render(request, 'fires/region_details.html', {'region': region})


def fire_detail_by_year(request, region, year):
    fires = []
    db_fires = FireTCC.objects.all()
    for i in db_fires:
        db_region = Region.objects.filter(id=i.region)
        if i.year == year and db_region == region:
            fires.append(i)
    return render(request, 'fires/fire.html', {'fires': fires})


def fire_detail_by_type(request, region, fire_type):
    fires = []
    db_fires = FireTCC.objects.all()
    for i in db_fires:
        db_type = Region.objects.filter(type_name=i.type)
        db_region = Region.objects.filter(id=i.region)
        if i.type == db_type and db_region == region:
            fires.append(i)
    return render(request, 'fires/fire.html', {'fires': fires})
