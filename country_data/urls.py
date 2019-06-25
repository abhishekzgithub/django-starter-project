from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url,include

urlpatterns = [
    # url(r'^region/<name>/',views.region_getter),
    # url(r'^region/<rname>/country/<cname>/', views.country_getter),
    path('region/<slug:region>/',views.region_getter,name="region-name"),
    path('region/<slug:region>/country/<slug:country>/', views.country_getter,name="country-name"),
]