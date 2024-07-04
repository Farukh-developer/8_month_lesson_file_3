from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Area(models.Model):
    name=models.CharField(max_length=100)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return  self.name
    
class Construction_organization(models.Model):
    name=models.CharField(max_length=100)  
    description=models.TextField(max_length=700)
    period_of_construction=models.DateTimeField(auto_now_add=True)
    area=models.ForeignKey(Area, on_delete=models.CASCADE)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return  self.name
    
class Construction_building(models.Model):
    construction_organization=models.ForeignKey(Construction_organization, on_delete=models.CASCADE)
    area=models.ForeignKey(Area, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    field=models.IntegerField()
    floor=models.IntegerField()
    parking=models.IntegerField()
    kinder_garden=models.CharField(max_length=20)
    lift=models.CharField(max_length=20)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
            return  self.name


          