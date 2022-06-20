from rest_framework import serializers
from .models import *


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyModel 
        fields = ["company_name","no_of_empoyees","contact","email","website","description"]
       
class GetCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyModel 
        fields = '__all__'
       

# class ServiceCitiesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ServiceCitiesModel
#         fields = '__all__'

# class ServiceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ServiceModel
#         fields = '__all__'


