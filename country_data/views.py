from django.shortcuts import render
# Create your views here.
from .models import Country, Region
import json
import pdb
def region_getter(request,region):
    print("region_getter")
    region_obj=Region.objects.filter(region__iexact=region)
    region_id=list(region_obj.values('id'))
    country_obj=list(Country.objects.filter(region_id__exact=region_id[0]['id']).values())
    no_countries=len(country_obj)
    population=sum([int(i['population']) for i in country_obj])
    result=[region,no_countries,population]
    context={
        "result":result
    }
    return render(request,'result.html',context)

def country_getter(request,region,country):
    print("country_getter")
    obj=list(Country.objects.filter(country__iexact=country).values())
    capital=obj[0]["capital"]
    region_id=obj[0]["region_id"]
    region=list(Region.objects.filter(id__exact=region_id).values())[0]['region']
    population=obj[0]["population"]
    currencies=obj[0]["currency"]
    result=[country,capital,region,population,currencies]
    context={
        "result":result
    }
    return render(request,'result.html',context)

