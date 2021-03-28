from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Region, FireTCC


def index(request):
    title = 'Global Fire Emissions'
    return render(request, 'fires/index.html', {'title': title})


def region_list(request):
    regions = Region.objects.all()
    paginator = Paginator(regions, 25)

    page_num = request.GET.get('page')
    page = paginator.get_page(page_num)
    return render(request, 'fires/regions.html', {'page_obj': page})


def region_detail(request, id):
    region = get_object_or_404(Region, id=id)
    types = FireTCC.objects.all()
    return render(request, 'fires/region_details.html', {'region': region,
                                                         'types': types,
                                                         'year_range': range(1997, 2015+1, 1)})


def fire_detail_by_year(request, region, year):
    fires = []
    db_fires = FireTCC.objects.all()
    for i in db_fires:
        db_region = Region.objects.filter(id=i.region.id)
        if i.year == year and db_region == region:
            fires.append(i)
    return render(request, 'fires/fire_year.html', {'fires': fires, 'region': region.id, 'year': year})


def fire_detail_by_type(request, region, fire_type):
    fires = []
    db_fires = FireTCC.objects.all()
    for i in db_fires:
        db_type = Region.objects.filter(type_name=i.type)
        db_region = Region.objects.filter(id=i.region)
        if db_type.type_name == fire_type and db_region == region:
            fires.append(i)
    return render(request, 'fires/fire_year.html', {'fires': fires, 'region': region, 'type': db_type})
