from django.db import models

# Create your models here.
class Region(models.Model):
    """For example Asia"""
    region=models.CharField(blank=True,max_length=100)
    updated_on=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.region

class Country(models.Model):
    region=models.ForeignKey(Region,on_delete=models.CASCADE)
    country=models.CharField(blank=True,max_length=100)
    capital=models.CharField(blank=True,max_length=100)
    population=models.IntegerField(blank=True)
    currency=models.CharField(blank=True,max_length=100)
    updated_on=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.country