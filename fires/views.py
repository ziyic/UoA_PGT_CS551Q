from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Region, FireTCC, FireType


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
    print(region, type(region))
    types = FireType.objects.all()
    year_range = range(1997, 2015 + 1, 1)
    return render(request, 'fires/region_details.html', {'region': region,
                                                         'types': types,
                                                         'year_range': year_range})


def fire_detail_by_year(request, region, year):
    fire_region = get_object_or_404(Region, name=region)
    fires = FireTCC.objects.filter(region=Region(fire_region).id, year=year)
    return render(request, 'fires/fire_year.html', {'fires': fires, 'region': fire_region.name, 'year': year})


def fire_detail_by_type(request, region, fire_type):
    fire_region = get_object_or_404(Region, name=region)
    f_type = FireType.objects.filter(type_name=fire_type)
    print(f_type,type(f_type))
    print(f_type[0], type(f_type[0]))
    fires = FireTCC.objects.filter(region=Region(fire_region).id, type=f_type[0].id)
    return render(request, 'fires/fire_type.html', {'fires': fires, 'region': region, 'fire_type': f_type[0].type_name})
