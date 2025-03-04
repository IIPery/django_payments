from rest_framework import serializers
from core import models

class Order(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = '__all__'