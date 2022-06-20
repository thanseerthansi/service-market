from rest_framework import serializers
from .models import *


class ServiceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceTypeModel 
        fields = '__all__'

class ServiceCitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCitiesModel
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceModel
        fields = '__all__'


