from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'

class LocaionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationModel
        fields = '__all__'

class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuoteModel
        fields = '__all__'


