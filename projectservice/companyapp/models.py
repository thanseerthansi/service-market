from django.db import models

from serviceapp.models import ServiceCitiesModel, ServiceModel

# Create your models here.
class CompanyModel(models.Model):
    company_name = models.CharField(max_length=100)
    no_of_empoyees = models.CharField(max_length=100)
    contact = models.CharField(max_length=12)
    email = models.EmailField(max_length=100)
    website = models.CharField(max_length=100)
    cities = models.ManyToManyField(ServiceCitiesModel)
    services = models.ManyToManyField(ServiceModel)
    description = models.TextField()