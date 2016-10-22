from rest_framework import serializers
from api.models import Address, Location
from django.conf import settings
from django.contrib.auth.models import User
#from django_logging import log
import requests, json

class AddressSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    #address = serializers.CharField(required=True)
    
    class Meta:
        model = Address
        fields = ('pk', 'owner', 'address')
        
class LocationSerializer(serializers.Serializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Location
        fields = ('pk', 'owner','entity_id', 'entity_type')


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'pk', 'username')
