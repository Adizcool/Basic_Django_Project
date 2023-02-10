from rest_framework import serializers
from .models import *

class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = ['side_id', 'site_name', 'address', 'state', 'country', 'zipcode']

class IAPSerializer(serializers.ModelSerializer):
    class Meta:
        model = IAP
        fields = '__all__'

class SwitchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Switch
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'    