from django.db import models


# Create your models here.
class ServiceTypeModel(models.Model):
    service = models.CharField(max_length=100)
    description = models.TextField()
    created_date =  models.DateTimeField(auto_now_add=True,null=True)
    updated_date = models.DateTimeField(auto_now=True,null=True)

class ServiceCitiesModel(models.Model):
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    description = models.TextField()
    
class ServiceModel(models.Model):#auto add while adding companies
    service_type = models.ForeignKey(ServiceTypeModel,on_delete=models.CASCADE)
    service_name = models.CharField(max_length=100)
    city = models.ManyToManyField(ServiceCitiesModel)